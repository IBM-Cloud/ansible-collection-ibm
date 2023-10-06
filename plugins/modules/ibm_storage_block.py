#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_storage_block
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/storage_block

short_description: Configure IBM Cloud 'ibm_storage_block' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_storage_block' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    capacity:
        description:
            - (Required for new resource) Storage block size
        required: True
        type: int
    iops:
        description:
            - (Required for new resource) IOPS value required
        required: True
        type: float
    allowed_virtual_guest_ids:
        description:
            - List of allowed virtual guest IDs
        required: False
        type: list
        elements: int
    allowed_hardware_ids:
        description:
            - List of allowe hardware IDs
        required: False
        type: list
        elements: int
    type:
        description:
            - (Required for new resource) Storage block type
        required: True
        type: str
    os_format_type:
        description:
            - (Required for new resource) OS formatr type
        required: True
        type: str
    notes:
        description:
            - Additional note info
        required: False
        type: str
    tags:
        description:
            - List of tags associated with the resource
        required: False
        type: list
        elements: str
    hourly_billing:
        description:
            - Billing done hourly, if set to true
        required: False
        type: bool
        default: False
    datacenter:
        description:
            - (Required for new resource) Datacenter name
        required: True
        type: str
    snapshot_capacity:
        description:
            - Snapshot capacity in GB
        required: False
        type: int
    allowed_ip_addresses:
        description:
            - Allowed IP addresses
        required: False
        type: list
        elements: str
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
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('iops', 'float'),
    ('type', 'str'),
    ('os_format_type', 'str'),
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'capacity',
    'iops',
    'allowed_virtual_guest_ids',
    'allowed_hardware_ids',
    'type',
    'os_format_type',
    'notes',
    'tags',
    'hourly_billing',
    'datacenter',
    'snapshot_capacity',
    'allowed_ip_addresses',
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
    iops=dict(
        required=False,
        type='float'),
    allowed_virtual_guest_ids=dict(
        required=False,
        elements='',
        type='list'),
    allowed_hardware_ids=dict(
        required=False,
        elements='',
        type='list'),
    type=dict(
        required=False,
        type='str'),
    os_format_type=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    snapshot_capacity=dict(
        required=False,
        type='int'),
    allowed_ip_addresses=dict(
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
        resource_type='ibm_storage_block',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.51.0',
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
