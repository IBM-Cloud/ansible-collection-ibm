#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_instance_template
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_template

short_description: Configure IBM Cloud 'ibm_is_instance_template' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_instance_template' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    name:
        description:
            - Instance Template name
        required: False
        type: str
    profile:
        description:
            - (Required for new resource) Profile info
        required: True
        type: str
    primary_network_interface:
        description:
            - Primary Network interface info
        required: False
        type: list
        elements: dict
    keys:
        description:
            - (Required for new resource) SSH key Ids for the instance template
        required: True
        type: list
        elements: str
    network_attachments:
        description:
            - The network attachments for this virtual server instance, including the primary network attachment.
        required: False
        type: list
        elements: dict
    boot_volume:
        description:
            - None
        required: False
        type: list
        elements: dict
    zone:
        description:
            - (Required for new resource) Zone name
        required: True
        type: str
    enable_secure_boot:
        description:
            - Indicates whether secure boot is enabled for this virtual server instance.If unspecified, the default secure boot mode from the profile will be used.
        required: False
        type: bool
    default_trusted_profile_auto_link:
        description:
            - If set to `true`, the system will create a link to the specified `target` trusted profile during instance creation. Regardless of whether a link is created by the system or manually using the IAM Identity service, it will be automatically deleted when the instance is deleted.
        required: False
        type: bool
    default_trusted_profile_target:
        description:
            - The unique identifier or CRN of the default IAM trusted profile to use for this virtual server instance.
        required: False
        type: str
    total_volume_bandwidth:
        description:
            - The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes
        required: False
        type: int
    dedicated_host_group:
        description:
            - Unique Identifier of the Dedicated Host Group where the instance will be placed
        required: False
        type: str
    primary_network_attachment:
        description:
            - The primary network attachment for this virtual server instance.
        required: False
        type: list
        elements: dict
    image:
        description:
            - image name
        required: False
        type: str
    volume_attachments:
        description:
            - None
        required: False
        type: list
        elements: dict
    network_interfaces:
        description:
            - None
        required: False
        type: list
        elements: dict
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
    confidential_compute_mode:
        description:
            - The confidential compute mode to use for this virtual server instance.If unspecified, the default confidential compute mode from the profile will be used.
        required: False
        type: str
    metadata_service:
        description:
            - The metadata service configuration
        required: False
        type: list
        elements: dict
    vpc:
        description:
            - (Required for new resource) VPC id
        required: True
        type: str
    placement_group:
        description:
            - Unique Identifier of the Placement Group for restricting the placement of the instance
        required: False
        type: str
    resource_group:
        description:
            - Instance template resource group
        required: False
        type: str
    availability_policy_host_failure:
        description:
            - The availability policy to use for this virtual server instance
        required: False
        type: str
    dedicated_host:
        description:
            - Unique Identifier of the Dedicated Host where the instance will be placed
        required: False
        type: str
    catalog_offering:
        description:
            - The catalog offering or offering version to use when provisioning this virtual server instance template. If an offering is specified, the latest version of that offering will be used. The specified offering or offering version may be in a different account in the same enterprise, subject to IAM policies.
        required: False
        type: list
        elements: dict
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
    ('profile', 'str'),
    ('keys', 'list'),
    ('zone', 'str'),
    ('vpc', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'profile',
    'primary_network_interface',
    'keys',
    'network_attachments',
    'boot_volume',
    'zone',
    'enable_secure_boot',
    'default_trusted_profile_auto_link',
    'default_trusted_profile_target',
    'total_volume_bandwidth',
    'dedicated_host_group',
    'primary_network_attachment',
    'image',
    'volume_attachments',
    'network_interfaces',
    'user_data',
    'reservation_affinity',
    'confidential_compute_mode',
    'metadata_service',
    'vpc',
    'placement_group',
    'resource_group',
    'availability_policy_host_failure',
    'dedicated_host',
    'catalog_offering',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'identifier',
    'name',
]

TL_CONFLICTS_MAP = {
    'primary_network_interface': ['primary_network_attachment', 'network_attachments'],
    'network_attachments': ['primary_network_interface', 'network_interfaces'],
    'dedicated_host_group': ['dedicated_host', 'placement_group'],
    'primary_network_attachment': ['primary_network_interface', 'network_interfaces'],
    'network_interfaces': ['primary_network_attachment', 'network_attachments'],
    'metadata_service': ['metadata_service_enabled'],
    'placement_group': ['dedicated_host', 'dedicated_host_group'],
    'dedicated_host': ['dedicated_host_group', 'placement_group'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    name=dict(
        required=False,
        type='str'),
    profile=dict(
        required=False,
        type='str'),
    primary_network_interface=dict(
        required=False,
        elements='',
        type='list'),
    keys=dict(
        required=False,
        elements='',
        type='list'),
    network_attachments=dict(
        required=False,
        elements='',
        type='list'),
    boot_volume=dict(
        required=False,
        elements='',
        type='list'),
    zone=dict(
        required=False,
        type='str'),
    enable_secure_boot=dict(
        required=False,
        type='bool'),
    default_trusted_profile_auto_link=dict(
        required=False,
        type='bool'),
    default_trusted_profile_target=dict(
        required=False,
        type='str'),
    total_volume_bandwidth=dict(
        required=False,
        type='int'),
    dedicated_host_group=dict(
        required=False,
        type='str'),
    primary_network_attachment=dict(
        required=False,
        elements='',
        type='list'),
    image=dict(
        required=False,
        type='str'),
    volume_attachments=dict(
        required=False,
        elements='',
        type='list'),
    network_interfaces=dict(
        required=False,
        elements='',
        type='list'),
    user_data=dict(
        required=False,
        type='str'),
    reservation_affinity=dict(
        required=False,
        elements='',
        type='list'),
    confidential_compute_mode=dict(
        required=False,
        type='str'),
    metadata_service=dict(
        required=False,
        elements='',
        type='list'),
    vpc=dict(
        required=False,
        type='str'),
    placement_group=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    availability_policy_host_failure=dict(
        required=False,
        type='str'),
    dedicated_host=dict(
        required=False,
        type='str'),
    catalog_offering=dict(
        required=False,
        elements='',
        type='list'),
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

    if 'generation' in module.params:
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
        resource_type='ibm_is_instance_template',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_instance_template',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.71.2',
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
