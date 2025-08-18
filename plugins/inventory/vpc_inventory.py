#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
name: vpc_inventory
author:
    - Michael Cohoon (@mtcohoon)
    - Torin Reilly (@torinreilly)
version_added: "1.49.0"
requirements:
    - Python >= 3
short_description: Inventory source for IBM Cloud Virtual Private Cloud virtual server instances
description:
    - This plugin utilizes the ibmcloud_terraform modules to build a dynamic inventory
      of defined virtual server instances (VSIs). Inventory sources must be structured as *.vpc.yml
      or *.vpc.yaml.
    - Valid VSI properties that can be used for groups, keyed groups, filters, and composite variables can be found in the
      IBM Cloud (instances documentation, https://cloud.ibm.com/apidocs/vpc/latest#get-instance-template).
    - It is expected that the IC_API_KEY environment variable is set. More information about this API key can be found in
      the IBM Cloud (API keys documentation, https://cloud.ibm.com/docs/account?topic=account-classic_keys).
extends_documentation_fragment:
    - inventory_cache
options:
    regions:
        description: List of IBM Cloud regions to query.
        default: []
    filters:
        description:
            - A key value pair for filtering by various VSI attributes.
              Only results matching the filter will be included in the inventory.
        default: {}
    groups:
        description: Add VSI hosts to group based on Jinja2 conditionals.
        type: dict
        default: {}
    compose:
        description: Create variables based on VSI attributes.
        type: dict
        default: {}
    exclude_ip:
        description: A list of VSI IP addresses to exclude from the inventory.
        type: list
        elements: str
    exclude_name:
        description: A list of VSI names to exclude from the inventory.
        type: list
        elements: str
    exclude_id:
        description: A list of VSI IDs to exclude from the inventory.
        type: list
        elements: str
    exclude_tag:
        description: A list of VSI tags to exclude from the inventory.
        type: list
        elements: str
    keyed_groups:
        description: Add VSI hosts to group based on the values of a variable.
        type: list
        elements: str
    use_floating_ips:
        description:
            - Indicates whether or not to use Floating IP addresses instead of the private IP addresses
              for a VSI. If this value is True, all instances that do not have a Floating IP address will
              be filtered out when building the inventory.
            - Since the correlation between Floating IP and VSI belongs to the Floating IP, additional queries need
              to be done which may increase the time to generate the inventory.
        type: bool
        default: False
    fail_on_duplicate:
        description:
            - If True, the vpc_inventory plugin will fail if it finds duplicate host names or IP addresses. This can
              occur when targetting different VPCs and regions.
        type: bool
        default: True
    ansible_display_name:
        description: By default, the VSI's name will be used as the name displayed by Ansible in the output.
          Instead of the VSI's name, its IP address or ID may also be used.
        type: str
        choices: [name, ip, id]
        default: "name"
    ansible_host_type:
        description: Determines if the IP Address or the VSI name will be used as the "ansible_host" variable
          in playbooks.
        type: str
        choices: [name, ip]
        default: "ip"
'''

EXAMPLES = '''
# The most minimal example, targeting only a single region
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south

# Target multiple regions and only add running VSIs to the inventory
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south
  - br-sao
filters:
  status: 'running'

# Generate an inventory of all running VSIs, using floating IP addresses and adding extra host variables.
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south
  - br-sao
filters:
  status: 'running'
compose:
  memory: memory
  image: image
  profile: profile
  vpc: vpc
use_floating_ips: True

# Generate an inventory of running VSIs that were tagged with both 'database' and 'application.'
# Additionally, create a db2 group for any VSI that has 'db2' as part of its name.
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south
  - br-sao
filters:
  status: 'running'
  tags:
    - database
    - application
groups:
  db2: "'db2' in name"
compose:
  vpc: vpc
  tags: tags

# Generate an inventory of running systems that excludes VSI by IP, name, and ID.
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south
filters:
  status: 'running'
exclude_ip:
  - 10.x.x.x
  - 11.x.x.x
exclude_name:
  - example-name-1
  - example-name-2
exclude_id:
  - abc_example_id_xyz

# Generate an inventory of running VSIs, grouped by their memory value. The groups will be prefixed with 'custom.'
plugin: ibm.cloudcollection.vpc_inventory
regions:
  - us-south
  - br-sao
filters:
  status: 'running'
keyed_groups:
  - prefix: custom
    key: memory
compose:
  memory: memory
'''

from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.module_utils.six import string_types, viewitems
from ansible.errors import AnsibleParserError
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import ibmcloud_terraform
from ansible.config.manager import ensure_type
from ansible.template import Templar

from ansible.utils.display import Display
display = Display()

# Generic setting for log initializing and log rotation
import logging
LOG_FILENAME = "/tmp/ansible_vpc.log"
logger = logging.getLogger(__name__)

TL_REQUIRED_PARAMETERS = [
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'vpc_name',
    'vpc_crn',
    'dedicated_host_name',
    'instance_group',
    'instance_group_name',
    'vpc',
    'resource_group',
    'dedicated_host',
    'placement_group_name',
    'placement_group',
]


def init_logger():
    logging.basicConfig(
        filename=LOG_FILENAME,
        format='[%(asctime)s] %(levelname)s: [%(funcName)s] %(message)s',
        level=logging.DEBUG)


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):

    NAME = 'ibm.cloudcollection.vpc_inventory'
    _cache = None

    def __init__(self):
        super().__init__()

        self.group_prefix = 'vpc_'
        self.template_handle = None
        init_logger()

    def verify_file(self, path):
        """
        Verify inventory source is valid
        """
        if super().verify_file(path):
            logger.debug("Path: %s", path)
            if path.endswith(('.vpc.yml', '.vpc.yaml')):
                return True
            raise AnsibleParserError("Path is not valid. All IBM Cloud inventory sources must have a suffix of .vpc.yml or .vpc.yaml.")

    def parse(self, inventory, loader, path, cache=True):
        """
        Parse inventory source
        """
        super(InventoryModule, self).parse(inventory, loader, path)

        self.load_cache_plugin()

        # Read the inventory YAML file
        self._configure(path)
        cache_key = self.get_cache_key(path)

        # cache may be True or False at this point to indicate if the inventory is being refreshed
        # get the user's cache option too to see if we should save the cache if it is changing
        user_cache_setting = self.get_option('cache')

        # read if the user has caching enabled and the cache isn't being refreshed
        attempt_to_read_cache = user_cache_setting and cache

        # update if the user has caching enabled and the cache is being refreshed;
        # update this value to True if the cache has expired below
        cache_needs_update = user_cache_setting and not cache

        # attempt to read the cache if inventory isn't being refreshed and the user has caching enabled
        if attempt_to_read_cache:
            try:
                vsis = self._cache[cache_key]
            except KeyError:
                # This occurs if the cache_key is not in the cache or if the cache_key expired,
                # so the cache needs to be updated
                logger.debug("Cache needs to be updated: %s", cache_key)
                cache_needs_update = True

        if not attempt_to_read_cache or cache_needs_update:
            # parse the provided inventory source
            # submit the parsed data to the inventory object (add_host, set_variable, etc)
            self.template_handle = Templar(loader=loader)
            vsis = self.get_virtual_server_instances()

        if cache_needs_update:
            self._cache[cache_key] = vsis

        self._populate_from_vsis(vsis)

    def _populate_from_vsis(self, vsis):
        # Ensure that at least one VSI was discovered
        if not vsis:
            raise Exception("There are no VSIs defined to any valid region or no valid connections were established.")
        
        # Check to see if the list of VSIs contains duplicates of the ansible display name or IP address.
        if self.fail_on_duplicate and len(vsis) != len(set([v.get(self.ansible_display_name) for v in vsis])):
            raise Exception(f"The fail_on_duplicate option is set and multiple hosts with the same {self.ansible_display_name} were found.")
        elif self.fail_on_duplicate and len(vsis) != len(set([self.get_vsi_ip(v) for v in vsis])):
            raise Exception("The fail_on_duplicate option is set and multiple hosts with the same IP address were found.")

        for vsi in vsis:
            if self.vsi_should_be_included(vsi):
                # Lookup the IP address for the VSI
                vsi_ip = self.get_vsi_ip(vsi)
                vsi_name = self.get_vsi_name(vsi)
                vsi_id = self.get_vsi_id(vsi)

                if self.ansible_host_type == "name":
                    hostname = vsi_name
                else:
                    hostname = vsi_ip

                if self.ansible_display_name == "name":
                    entry_name = vsi_name
                elif self.ansible_display_name == "ip":
                    entry_name = vsi_ip
                else:
                    entry_name = vsi_id

                self.inventory.add_host(entry_name)

                # Only add an ansible_host variable if it differs from the displayname in the inventory
                if hostname != entry_name:
                    self.inventory.set_variable(entry_name, "ansible_host", hostname)
                try:
                    self._set_composite_vars(self.compose, vsi, entry_name, strict=True)
                    self._add_host_to_composed_groups(self.groups, vsi, entry_name, strict=True)
                    self._add_host_to_keyed_groups(self.keyed_groups, vsi, entry_name, strict=True)
                except Exception:
                    logger.debug("Attribute not found in the VSI")
                    continue

    def get_virtual_server_instances(self):
        vsis = []
        for region in self.regions:
            result = ibmcloud_terraform(
                resource_type='ibm_is_instances',
                tf_type='data',
                parameters={"region": region},
                ibm_provider_version='1.71.2',
                tl_required_params=TL_REQUIRED_PARAMETERS,
                tl_all_params=TL_ALL_PARAMETERS
            )

            if result['rc'] > 0:
                logging.error(result['stderr'])
                instances = {}
            else:
                instances = result.get("resource").get("instances")
                for i in instances:
                    # Add the region to the VSI dictionary to be filtered on
                    i['region'] = region

                vsis.extend(instances)

            if instances and self.use_floating_ips:
                result = ibmcloud_terraform(
                    resource_type='ibm_is_floating_ips',
                    tf_type='data',
                    parameters={"region": region},
                    ibm_provider_version='1.71.2',
                    tl_required_params=TL_REQUIRED_PARAMETERS,
                    tl_all_params=TL_ALL_PARAMETERS
                )

                if result['rc'] > 0:
                    logging.error(result['stderr'])

                fips = result.get("resource").get("floating_ips")
                bound_fips = [f for f in fips if len(f.get("target")) > 0]
                for fip in bound_fips:
                    # Assumption #1: Floating IPs can only target one virtual network interface.
                    fip_addr = fip.get("address")
                    if len(fip.get("target")) != 1:
                        raise Exception(f"Did not expect more than one target for floating IP {fip_addr}")
                    if fip.get("target")[0].get("resource_type") != "virtual_network_interface":
                        raise Exception(f"Floating IP {fip_addr} does not target a virtual network interface (target is {fip.get("target")})")

                    vni_target_id = fip.get("target")[0].get("id")

                    for instance in instances:
                        # Assumption #2: VSIs may only have one Floating IP
                        instance_vni_ids = []

                        instance_nas = instance.get("network_attachments")
                        for instance_na in instance_nas:
                            instance_vnis = instance_na.get("virtual_network_interface")
                            instance_vni_ids = [instance_vnis.get("id") for instance_vnis in instance_vnis]
                        
                        if vni_target_id in instance_vni_ids:
                            instance['floating_ip'] = fip_addr

        # If using Floating IPs, remove VSIs that don't have one
        if self.use_floating_ips:
            vsis = [v for v in vsis if "floating_ip" in v]

        return vsis

    def _configure(self, path):
        config = self._read_config_data(path)

        args = dict(
            regions=dict(type="list", value=config.get("regions", []), required=True),
            filters=dict(type="dict", value=config.get("filters", {})),
            groups=dict(type="dict", value=config.get("groups", {})),
            keyed_groups=dict(type="list", value=config.get("keyed_groups", [])),
            compose=dict(type="dict", value=config.get("compose", {})),
            exclude_ip=dict(type="list", value=config.get("exclude_ip", [])),
            exclude_name=dict(type="list", value=config.get("exclude_name", [])),
            exclude_id=dict(type="list", value=config.get("exclude_id", [])),
            exclude_tag=dict(type="list", value=config.get("exclude_tag", [])),
            use_floating_ips=dict(type="bool", value=config.get("use_floating_ips", False)),
            fail_on_duplicate=dict(type="bool", value=config.get("fail_on_duplicate", True)),
            ansible_display_name=dict(type="str", choices=["name", "ip", "id"], value=config.get("ansible_display_name", "name")),
            ansible_host_type=dict(type="str", choices=["name", "ip"], value=config.get("ansible_host_type", "ip")),
        )

        self.validate_and_set_args(args)

    def validate_and_set_args(self, args):
        for arg in args:
            if args[arg].get("required") and args[arg].get("value") is None:
                raise AnsibleParserError("%s is required value." % (arg))
            
            # Check type
            if args[arg]["type"] == 'str':
                type_checked_arg = ensure_type(
                    args[arg].get("value"), 'string')
                if type_checked_arg is not None and not isinstance(type_checked_arg, string_types):
                    raise AnsibleParserError("%s is expected to be a string, but got %s instead" % (
                        arg, type(type_checked_arg)))
                # Check for choices
                if "choices" in args[arg]:
                    if type_checked_arg not in args[arg]["choices"]:
                        raise AnsibleParserError("%s is not a valid option for %s. The following are valid options: %s" % (
                            type_checked_arg, arg, str(args[arg]["choices"])))
                setattr(self, arg, type_checked_arg)
            elif args[arg]["type"] == 'bool':
                if isinstance(args[arg].get("value"), bool):
                    setattr(self, arg, args[arg].get("value"))
                else:
                    raise AnsibleParserError("%s must be a boolean value. Current value is: %s" % (arg, args[arg].get("value")))
            elif args[arg]["type"] == 'list':
                if not isinstance(args[arg].get("value"), list):
                    raise AnsibleParserError("%s is currently %s and needs to be defined as a %s." % (arg, args[arg].get("value"), 'list'))
                setattr(self, arg, args[arg].get("value"))
            elif args[arg]["type"] == 'dict':
                if not isinstance(args[arg].get("value"), dict):
                    raise AnsibleParserError("%s is currently %s and needs to be defined as a %s." % (arg, args[arg].get("value"), 'dict'))
                setattr(self, arg, args[arg].get("value"))
            else:
                raise AnsibleParserError("%s is an unhandled type! This shoulddn't happen." % (args[arg]["type"]))

            # Do not allow inventory generation to continue if an argument is set to None,
            # but also do not override a more type specific message that may have been raised.
            if args[arg].get("value") is None:
                raise AnsibleParserError("%s is an optional value, but cannot be None. Please specify a value or remove it from your inventory source." % (arg))

    def get_vsi_ip(self, vsi):
        if self.use_floating_ips:
            if "floating_ip" in vsi:
                return vsi.get("floating_ip")
            raise Exception("VSI has no value for 'floating_ip'")
        else:
            if ("primary_network_interface" in vsi
                and len(vsi.get("primary_network_interface")) > 0
                and "primary_ip" in vsi.get("primary_network_interface")[0]
                and len(vsi.get("primary_network_interface")[0].get("primary_ip")) > 0
                and "address" in vsi.get("primary_network_interface")[0].get("primary_ip")[0]
            ):
                return vsi.get("primary_network_interface")[0].get("primary_ip")[0].get("address")
            raise Exception("VSI has no value for 'primary_ip'")

    def get_vsi_name(self, vsi):
        if "name" in vsi and vsi.get("name") is not None:
            return vsi.get("name")
        raise Exception("VSI has no value for 'name'")

    def get_vsi_id(self, vsi):
        if "id" in vsi and vsi.get("id") is not None:
            return vsi.get("id")
        raise Exception("VSI has no value for 'id'")
    
    def get_vsi_tags(self, vsi):
        if "tags" in vsi and vsi.get("tags") is not None:
            return vsi.get("tags")
        raise Exception("VSI has no value for 'tags'")

    def is_vsi_excluded(self, vsi):
        # VSI excluded due to IP address
        try:
            vsi_ip = self.get_vsi_ip(vsi)
            if vsi_ip in self.exclude_ip:
                return True
        except Exception:
            pass

        # VSI excluded due to name
        try:
            vsi_name = self.get_vsi_name(vsi)
            if vsi_name in self.exclude_name:
                return True
        except Exception:
            pass

        # VSI excluded due to ID
        try:
            vsi_id = self.get_vsi_id(vsi)
            if vsi_id in self.exclude_id:
                return True
        except Exception:
            pass

        # VSI excluded due to a tag
        try:
            vsi_tags = self.get_vsi_tags(vsi)
            if any(t in vsi_tags for t in self.exclude_tag):
                return True
        except Exception:
            pass
        
        return False

    def matches_filters(self, vsi):
        # Our filter should be a subset of our VSI if the VSI matches the filter items
        non_list_filters = {k: v for k, v in self.filters.items() if not isinstance(v, list)}
        list_filters = {k: v for k, v in self.filters.items() if isinstance(v, list)}

        if viewitems(non_list_filters) <= viewitems(vsi):
            # For filters that are lists, check to see if each item in the filter
            # is present in the VSI's properties.
            for k, v in list_filters.items():
                if not set(v).issubset(vsi.get(k)):
                    return False
            return True

        return False

    def vsi_should_be_included(self, vsi):
        if self.matches_filters(vsi) and not self.is_vsi_excluded(vsi):
            return True
        return False
