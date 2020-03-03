#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_dns_record
short_description: Configure IBM Cloud 'ibm_dns_record' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_dns_record' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    retry:
        description:
            - None
        required: False
        type: int
    service:
        description:
            - None
        required: False
        type: str
    expire:
        description:
            - None
        required: False
        type: int
    mx_priority:
        description:
            - None
        required: False
        type: int
        default: 0
    responsible_person:
        description:
            - None
        required: False
        type: str
    protocol:
        description:
            - None
        required: False
        type: str
    port:
        description:
            - None
        required: False
        type: int
    type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    priority:
        description:
            - None
        required: False
        type: int
        default: 0
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    data:
        description:
            - (Required for new resource) 
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) 
        required: False
        type: int
    refresh:
        description:
            - None
        required: False
        type: int
    weight:
        description:
            - None
        required: False
        type: int
        default: 0
    host:
        description:
            - (Required for new resource) 
        required: False
        type: str
    minimum_ttl:
        description:
            - None
        required: False
        type: int
    ttl:
        description:
            - (Required for new resource) 
        required: False
        type: int
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
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('type', 'str'),
    ('data', 'str'),
    ('domain_id', 'int'),
    ('host', 'str'),
    ('ttl', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'retry',
    'service',
    'expire',
    'mx_priority',
    'responsible_person',
    'protocol',
    'port',
    'type',
    'priority',
    'tags',
    'data',
    'domain_id',
    'refresh',
    'weight',
    'host',
    'minimum_ttl',
    'ttl',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    retry=dict(
        required=False,
        type='int'),
    service=dict(
        required=False,
        type='str'),
    expire=dict(
        required=False,
        type='int'),
    mx_priority=dict(
        default=0,
        type='int'),
    responsible_person=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='int'),
    type=dict(
        required=False,
        type='str'),
    priority=dict(
        default=0,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    data=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='int'),
    refresh=dict(
        required=False,
        type='int'),
    weight=dict(
        default=0,
        type='int'),
    host=dict(
        required=False,
        type='str'),
    minimum_ttl=dict(
        required=False,
        type='int'),
    ttl=dict(
        required=False,
        type='int'),
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
        default='us-south')
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
        resource_type='ibm_dns_record',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.3',
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
