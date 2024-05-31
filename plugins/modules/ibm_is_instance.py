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
    - IBM-Cloud terraform-provider-ibm v1.65.1
    - Terraform v1.5.5

options:
    access_tags:
        description:
            - list of access tags for the instance
        required: False
        type: list
        elements: str
    wait_before_delete:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: bool
        default: True
    user_data:
        description:
            - User data given for the instance
        required: False
        type: str
    image:
        description:
            - image id
        required: False
        type: str
    vpc:
        description:
            - VPC id
        required: False
        type: str
    network_attachments:
        description:
            - The network attachments for this virtual server instance, including the primary network attachment.
        required: False
        type: list
        elements: dict
    resource_group:
        description:
            - Instance resource group
        required: False
        type: str
    default_trusted_profile_auto_link:
        description:
            - If set to `true`, the system will create a link to the specified `target` trusted profile during instance creation. Regardless of whether a link is created by the system or manually using the IAM Identity service, it will be automatically deleted when the instance is deleted.
        required: False
        type: bool
    name:
        description:
            - (Required for new resource) Instance name
        required: True
        type: str
    action:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: str
    network_interfaces:
        description:
            - None
        required: False
        type: list
        elements: dict
    catalog_offering:
        description:
            - The catalog offering or offering version to use when provisioning this virtual server instance. If an offering is specified, the latest version of that offering will be used. The specified offering or offering version may be in a different account in the same enterprise, subject to IAM policies.
        required: False
        type: list
        elements: dict
    profile:
        description:
            - Profile info
        required: False
        type: str
    keys:
        description:
            - SSH key Ids for the instance
        required: False
        type: list
        elements: str
    instance_template:
        description:
            - Id of the instance template
        required: False
        type: str
    placement_group:
        description:
            - Unique Identifier of the Placement Group for restricting the placement of the instance
        required: False
        type: str
    reservation_affinity:
        description:
            - None
        required: False
        type: list
        elements: dict
    dedicated_host:
        description:
            - Unique Identifier of the Dedicated Host where the instance will be placed
        required: False
        type: str
    total_volume_bandwidth:
        description:
            - The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes
        required: False
        type: int
    metadata_service:
        description:
            - The metadata service configuration
        required: False
        type: list
        elements: dict
    boot_volume:
        description:
            - None
        required: False
        type: list
        elements: dict
    availability_policy_host_failure:
        description:
            - The availability policy to use for this virtual server instance
        required: False
        type: str
    tags:
        description:
            - list of tags for the instance
        required: False
        type: list
        elements: str
    zone:
        description:
            - Zone name
        required: False
        type: str
    primary_network_attachment:
        description:
            - The primary network attachment for this virtual server instance.
        required: False
        type: list
        elements: dict
    volumes:
        description:
            - List of volumes
        required: False
        type: list
        elements: str
    force_recovery_time:
        description:
            - Define timeout to force the instances to start/stop in minutes.
        required: False
        type: int
    default_trusted_profile_target:
        description:
            - The unique identifier or CRN of the default IAM trusted profile to use for this virtual server instance.
        required: False
        type: str
    dedicated_host_group:
        description:
            - Unique Identifier of the Dedicated Host Group where the instance will be placed
        required: False
        type: str
    force_action:
        description:
            - If set to true, the action will be forced immediately, and all queued actions deleted. Ignored for the start action.
        required: False
        type: bool
        default: False
    primary_network_interface:
        description:
            - Primary Network interface info
        required: False
        type: list
        elements: dict
    auto_delete_volume:
        description:
            - Auto delete volume along with instance
        required: False
        type: bool
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
    generation:
        description:
            - The generation of Virtual Private Cloud infrastructure
              that you want to use. Supported values are 1 for VPC
              generation 1, and 2 for VPC generation 2 infrastructure.
              If this value is not specified, 2 is used by default. This
              can also be provided via the environment variable
              'IC_GENERATION'.
        default: 2
        required: False
        type: int
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
    'access_tags',
    'wait_before_delete',
    'user_data',
    'image',
    'vpc',
    'network_attachments',
    'resource_group',
    'default_trusted_profile_auto_link',
    'name',
    'action',
    'network_interfaces',
    'catalog_offering',
    'profile',
    'keys',
    'instance_template',
    'placement_group',
    'reservation_affinity',
    'dedicated_host',
    'total_volume_bandwidth',
    'metadata_service',
    'boot_volume',
    'availability_policy_host_failure',
    'tags',
    'zone',
    'primary_network_attachment',
    'volumes',
    'force_recovery_time',
    'default_trusted_profile_target',
    'dedicated_host_group',
    'force_action',
    'primary_network_interface',
    'auto_delete_volume',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'private_key',
    'passphrase',
]

TL_CONFLICTS_MAP = {
    'image': ['boot_volume.0.snapshot', 'catalog_offering.0.offering_crn', 'catalog_offering.0.version_crn', 'boot_volume.0.volume_id'],
    'network_attachments': ['primary_network_interface', 'network_interfaces'],
    'network_interfaces': ['primary_network_attachment', 'network_attachments'],
    'instance_template': ['boot_volume.0.snapshot', 'boot_volume.0.volume_id'],
    'placement_group': ['dedicated_host', 'dedicated_host_group'],
    'dedicated_host': ['dedicated_host_group', 'placement_group'],
    'metadata_service': ['metadata_service_enabled'],
    'primary_network_attachment': ['primary_network_interface', 'network_interfaces'],
    'dedicated_host_group': ['dedicated_host', 'placement_group'],
    'primary_network_interface': ['primary_network_attachment', 'network_attachments'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
    wait_before_delete=dict(
        required=False,
        type='bool'),
    user_data=dict(
        required=False,
        type='str'),
    image=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    network_attachments=dict(
        required=False,
        elements='',
        type='list'),
    resource_group=dict(
        required=False,
        type='str'),
    default_trusted_profile_auto_link=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    action=dict(
        required=False,
        type='str'),
    network_interfaces=dict(
        required=False,
        elements='',
        type='list'),
    catalog_offering=dict(
        required=False,
        elements='',
        type='list'),
    profile=dict(
        required=False,
        type='str'),
    keys=dict(
        required=False,
        elements='',
        type='list'),
    instance_template=dict(
        required=False,
        type='str'),
    placement_group=dict(
        required=False,
        type='str'),
    reservation_affinity=dict(
        required=False,
        elements='',
        type='list'),
    dedicated_host=dict(
        required=False,
        type='str'),
    total_volume_bandwidth=dict(
        required=False,
        type='int'),
    metadata_service=dict(
        required=False,
        elements='',
        type='list'),
    boot_volume=dict(
        required=False,
        elements='',
        type='list'),
    availability_policy_host_failure=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    zone=dict(
        required=False,
        type='str'),
    primary_network_attachment=dict(
        required=False,
        elements='',
        type='list'),
    volumes=dict(
        required=False,
        elements='',
        type='list'),
    force_recovery_time=dict(
        required=False,
        type='int'),
    default_trusted_profile_target=dict(
        required=False,
        type='str'),
    dedicated_host_group=dict(
        required=False,
        type='str'),
    force_action=dict(
        required=False,
        type='bool'),
    primary_network_interface=dict(
        required=False,
        elements='',
        type='list'),
    auto_delete_volume=dict(
        required=False,
        type='bool'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
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
        ibm_provider_version='1.65.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.65.1',
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
