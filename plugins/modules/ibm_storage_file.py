#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_storage_file
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/storage_file

short_description: Configure IBM Cloud 'ibm_storage_file' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_storage_file' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    capacity:
        description:
            - (Required for new resource) Storage capacity
        required: True
        type: int
    allowed_ip_addresses:
        description:
            - Allowed range of IP addresses
        required: False
        type: list
        elements: str
    snapshot_schedule:
        description:
            - None
        required: False
        type: list
        elements: dict
    type:
        description:
            - (Required for new resource) Storage type
        required: True
        type: str
    datacenter:
        description:
            - (Required for new resource) Datacenter name
        required: True
        type: str
    allowed_virtual_guest_ids:
        description:
            - Virtual guest ID
        required: False
        type: list
        elements: int
    allowed_hardware_ids:
        description:
            - Hardaware ID
        required: False
        type: list
        elements: int
    notes:
        description:
            - Notes
        required: False
        type: str
    iops:
        description:
            - (Required for new resource) iops rate
        required: True
        type: float
    snapshot_capacity:
        description:
            - Snapshot capacity
        required: False
        type: int
    allowed_subnets:
        description:
            - Allowed network subnets
        required: False
        type: list
        elements: str
    tags:
        description:
            - Tags set for the storage volume
        required: False
        type: list
        elements: str
    hourly_billing:
        description:
            - Hourly based billing type
        required: False
        type: bool
        default: False
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
    iaas_classic_username:
        description:
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
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
    ('capacity', 'int'),
    ('type', 'str'),
    ('datacenter', 'str'),
    ('iops', 'float'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'capacity',
    'allowed_ip_addresses',
    'snapshot_schedule',
    'type',
    'datacenter',
    'allowed_virtual_guest_ids',
    'allowed_hardware_ids',
    'notes',
    'iops',
    'snapshot_capacity',
    'allowed_subnets',
    'tags',
    'hourly_billing',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    capacity=dict(
        required=False,
        type='int'),
    allowed_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    snapshot_schedule=dict(
        required=False,
        elements='',
        type='list'),
    type=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    allowed_virtual_guest_ids=dict(
        required=False,
        elements='',
        type='list'),
    allowed_hardware_ids=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    iops=dict(
        required=False,
        type='float'),
    snapshot_capacity=dict(
        required=False,
        type='int'),
    allowed_subnets=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
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
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
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

    result = ibmcloud_terraform(
        resource_type='ibm_storage_file',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
