#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_storage_file
short_description: Configure IBM Cloud 'ibm_storage_file' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_storage_file' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.6
    - Terraform v0.12.20

options:
    volumename:
        description:
            - None
        required: False
        type: str
    hostname:
        description:
            - None
        required: False
        type: str
    allowed_subnets:
        description:
            - None
        required: False
        type: list
        elements: str
    notes:
        description:
            - None
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    iops:
        description:
            - (Required for new resource) 
        required: False
        type: float
    allowed_virtual_guest_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    allowed_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    snapshot_schedule:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    allowed_hardware_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: False
    datacenter:
        description:
            - (Required for new resource) 
        required: False
        type: str
    capacity:
        description:
            - (Required for new resource) 
        required: False
        type: int
    snapshot_capacity:
        description:
            - None
        required: False
        type: int
    mountpoint:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    resource_name:
        description:
            - The name of the resource
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
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('iops', 'float'),
    ('type', 'str'),
    ('datacenter', 'str'),
    ('capacity', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'volumename',
    'hostname',
    'allowed_subnets',
    'notes',
    'resource_controller_url',
    'iops',
    'allowed_virtual_guest_ids',
    'allowed_ip_addresses',
    'snapshot_schedule',
    'resource_status',
    'type',
    'allowed_hardware_ids',
    'hourly_billing',
    'datacenter',
    'capacity',
    'snapshot_capacity',
    'mountpoint',
    'tags',
    'resource_name',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    volumename=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=False,
        type='str'),
    allowed_subnets=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    iops=dict(
        required=False,
        type='float'),
    allowed_virtual_guest_ids=dict(
        required=False,
        elements='',
        type='list'),
    allowed_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    snapshot_schedule=dict(
        required=False,
        elements='',
        type='list'),
    resource_status=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    allowed_hardware_ids=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        default=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    capacity=dict(
        required=False,
        type='int'),
    snapshot_capacity=dict(
        required=False,
        type='int'),
    mountpoint=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    resource_name=dict(
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
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_storage_file',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.6',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
