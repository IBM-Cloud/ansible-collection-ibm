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
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    protocol:
        description:
            - protocol info
        required: False
        type: str
    data:
        description:
            - (Required for new resource) DNS record data
        required: False
        type: str
    minimum_ttl:
        description:
            - Minimun TTL configuration
        required: False
        type: int
    service:
        description:
            - service info
        required: False
        type: str
    priority:
        description:
            - priority info
        required: False
        type: int
        default: 0
    weight:
        description:
            - weight info
        required: False
        type: int
        default: 0
    tags:
        description:
            - tags set for the resource
        required: False
        type: list
        elements: str
    mx_priority:
        description:
            - Maximum priority
        required: False
        type: int
        default: 0
    retry:
        description:
            - Retry count
        required: False
        type: int
    ttl:
        description:
            - (Required for new resource) TTL configuration
        required: False
        type: int
    responsible_person:
        description:
            - Responsible person for DNS record
        required: False
        type: str
    port:
        description:
            - port number
        required: False
        type: int
    refresh:
        description:
            - refresh rate
        required: False
        type: int
    type:
        description:
            - (Required for new resource) DNS record type
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) Domain ID of dns record instance
        required: False
        type: int
    expire:
        description:
            - DNS record expiry info
        required: False
        type: int
    host:
        description:
            - (Required for new resource) Hostname
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
    ('data', 'str'),
    ('ttl', 'int'),
    ('type', 'str'),
    ('domain_id', 'int'),
    ('host', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'protocol',
    'data',
    'minimum_ttl',
    'service',
    'priority',
    'weight',
    'tags',
    'mx_priority',
    'retry',
    'ttl',
    'responsible_person',
    'port',
    'refresh',
    'type',
    'domain_id',
    'expire',
    'host',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    protocol=dict(
        required=False,
        type='str'),
    data=dict(
        required=False,
        type='str'),
    minimum_ttl=dict(
        required=False,
        type='int'),
    service=dict(
        required=False,
        type='str'),
    priority=dict(
        default=0,
        type='int'),
    weight=dict(
        default=0,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    mx_priority=dict(
        default=0,
        type='int'),
    retry=dict(
        required=False,
        type='int'),
    ttl=dict(
        required=False,
        type='int'),
    responsible_person=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='int'),
    refresh=dict(
        required=False,
        type='int'),
    type=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='int'),
    expire=dict(
        required=False,
        type='int'),
    host=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_dns_record',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.6.0',
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
