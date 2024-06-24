#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_instance
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance

short_description: Configure IBM Cloud 'ibm_is_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_instance' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    keys:
        description:
            - SSH key Ids for the instance
        required: False
        type: list
        elements: str
    primary_network_attachment:
        description:
            - The primary network attachment for this virtual server instance.
        required: False
        type: list
        elements: dict
    zone:
        description:
            - Zone name
        required: False
        type: str
    network_interfaces:
        description:
            - None
        required: False
        type: list
        elements: dict
    metadata_service:
        description:
            - The metadata service configuration
        required: False
        type: list
        elements: dict
    availability_policy_host_failure:
        description:
            - The availability policy to use for this virtual server instance
        required: False
        type: str
    default_trusted_profile_target:
        description:
            - The unique identifier or CRN of the default IAM trusted profile to use for this virtual server instance.
        required: False
        type: str
    dedicated_host:
        description:
            - Unique Identifier of the Dedicated Host where the instance will be placed
        required: False
        type: str
    wait_before_delete:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: bool
        default: True
    network_attachments:
        description:
            - The network attachments for this virtual server instance, including the primary network attachment.
        required: False
        type: list
        elements: dict
    vpc:
        description:
            - VPC id
        required: False
        type: str
    instance_template:
        description:
            - Id of the instance template
        required: False
        type: str
    dedicated_host_group:
        description:
            - Unique Identifier of the Dedicated Host Group where the instance will be placed
        required: False
        type: str
    resource_group:
        description:
            - Instance resource group
        required: False
        type: str
    force_action:
        description:
            - If set to true, the action will be forced immediately, and all queued actions deleted. Ignored for the start action.
        required: False
        type: bool
        default: False
    default_trusted_profile_auto_link:
        description:
            - If set to `true`, the system will create a link to the specified `target` trusted profile during instance creation. Regardless of whether a link is created by the system or manually using the IAM Identity service, it will be automatically deleted when the instance is deleted.
        required: False
        type: bool
    primary_network_interface:
        description:
            - Primary Network interface info
        required: False
        type: list
        elements: dict
    boot_volume:
        description:
            - None
        required: False
        type: list
        elements: dict
    auto_delete_volume:
        description:
            - Auto delete volume along with instance
        required: False
        type: bool
    force_recovery_time:
        description:
            - Define timeout to force the instances to start/stop in minutes.
        required: False
        type: int
    name:
        description:
            - (Required for new resource) Instance name
        required: True
        type: str
    profile:
        description:
            - Profile info
        required: False
        type: str
    volumes:
        description:
            - List of volumes
        required: False
        type: list
        elements: str
    image:
        description:
            - image id
        required: False
        type: str
    total_volume_bandwidth:
        description:
            - The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes
        required: False
        type: int
    tags:
        description:
            - list of tags for the instance
        required: False
        type: list
        elements: str
    access_tags:
        description:
            - list of access tags for the instance
        required: False
        type: list
        elements: str
    catalog_offering:
        description:
            - The catalog offering or offering version to use when provisioning this virtual server instance. If an offering is specified, the latest version of that offering will be used. The specified offering or offering version may be in a different account in the same enterprise, subject to IAM policies.
        required: False
        type: list
        elements: dict
    placement_group:
        description:
            - Unique Identifier of the Placement Group for restricting the placement of the instance
        required: False
        type: str
    user_data:
        description:
            - User data given for the instance
        required: False
        type: str
    reservation_affinity:
        description:
            - None
        required: False
        type: list
        elements: dict
    action:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'keys',
    'primary_network_attachment',
    'zone',
    'network_interfaces',
    'metadata_service',
    'availability_policy_host_failure',
    'default_trusted_profile_target',
    'dedicated_host',
    'wait_before_delete',
    'network_attachments',
    'vpc',
    'instance_template',
    'dedicated_host_group',
    'resource_group',
    'force_action',
    'default_trusted_profile_auto_link',
    'primary_network_interface',
    'boot_volume',
    'auto_delete_volume',
    'force_recovery_time',
    'name',
    'profile',
    'volumes',
    'image',
    'total_volume_bandwidth',
    'tags',
    'access_tags',
    'catalog_offering',
    'placement_group',
    'user_data',
    'reservation_affinity',
    'action',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'passphrase',
    'private_key',
]

TL_CONFLICTS_MAP = {
    'primary_network_attachment': ['primary_network_interface', 'network_interfaces'],
    'network_interfaces': ['primary_network_attachment', 'network_attachments'],
    'metadata_service': ['metadata_service_enabled'],
    'dedicated_host': ['dedicated_host_group', 'placement_group'],
    'network_attachments': ['primary_network_interface', 'network_interfaces'],
    'instance_template': ['boot_volume.0.snapshot', 'boot_volume.0.volume_id'],
    'dedicated_host_group': ['dedicated_host', 'placement_group'],
    'primary_network_interface': ['primary_network_attachment', 'network_attachments'],
    'image': ['boot_volume.0.snapshot', 'catalog_offering.0.offering_crn', 'catalog_offering.0.version_crn', 'boot_volume.0.volume_id'],
    'placement_group': ['dedicated_host', 'dedicated_host_group'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    keys=dict(
        required=False,
        elements='',
        type='list'),
    primary_network_attachment=dict(
        required=False,
        elements='',
        type='list'),
    zone=dict(
        required=False,
        type='str'),
    network_interfaces=dict(
        required=False,
        elements='',
        type='list'),
    metadata_service=dict(
        required=False,
        elements='',
        type='list'),
    availability_policy_host_failure=dict(
        required=False,
        type='str'),
    default_trusted_profile_target=dict(
        required=False,
        type='str'),
    dedicated_host=dict(
        required=False,
        type='str'),
    wait_before_delete=dict(
        required=False,
        type='bool'),
    network_attachments=dict(
        required=False,
        elements='',
        type='list'),
    vpc=dict(
        required=False,
        type='str'),
    instance_template=dict(
        required=False,
        type='str'),
    dedicated_host_group=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    force_action=dict(
        required=False,
        type='bool'),
    default_trusted_profile_auto_link=dict(
        required=False,
        type='bool'),
    primary_network_interface=dict(
        required=False,
        elements='',
        type='list'),
    boot_volume=dict(
        required=False,
        elements='',
        type='list'),
    auto_delete_volume=dict(
        required=False,
        type='bool'),
    force_recovery_time=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    profile=dict(
        required=False,
        type='str'),
    volumes=dict(
        required=False,
        elements='',
        type='list'),
    image=dict(
        required=False,
        type='str'),
    total_volume_bandwidth=dict(
        required=False,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
    catalog_offering=dict(
        required=False,
        elements='',
        type='list'),
    placement_group=dict(
        required=False,
        type='str'),
    user_data=dict(
        required=False,
        type='str'),
    reservation_affinity=dict(
        required=False,
        elements='',
        type='list'),
    action=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.66.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
