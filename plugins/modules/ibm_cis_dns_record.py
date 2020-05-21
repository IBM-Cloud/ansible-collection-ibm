#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_dns_record
short_description: Configure IBM Cloud 'ibm_cis_dns_record' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_dns_record' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    ttl:
        description:
            - TTL value
        required: False
        type: int
        default: 1
    created_on:
        description:
            - None
        required: False
        type: str
    cis_id:
        description:
            - (Required for new resource) CIS object id
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: False
        type: str
    name:
        description:
            - DNS record name
        required: False
        type: str
    type:
        description:
            - (Required for new resource) Record type
        required: False
        type: str
    priority:
        description:
            - Priority Value
        required: False
        type: int
    proxied:
        description:
            - Boolean value true if proxied else flase
        required: False
        type: bool
        default: False
    proxiable:
        description:
            - None
        required: False
        type: bool
    content:
        description:
            - DNS record content
        required: False
        type: str
    data:
        description:
            - None
        required: False
        type: dict
        elements: dict
    modified_on:
        description:
            - None
        required: False
        type: str
    record_id:
        description:
            - None
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
    ('cis_id', 'str'),
    ('domain_id', 'str'),
    ('type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ttl',
    'created_on',
    'cis_id',
    'domain_id',
    'name',
    'type',
    'priority',
    'proxied',
    'proxiable',
    'content',
    'data',
    'modified_on',
    'record_id',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ttl=dict(
        default=1,
        type='int'),
    created_on=dict(
        required=False,
        type='str'),
    cis_id=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    priority=dict(
        required=False,
        type='int'),
    proxied=dict(
        default=False,
        type='bool'),
    proxiable=dict(
        required=False,
        type='bool'),
    content=dict(
        required=False,
        type='str'),
    data=dict(
        required=False,
        elements='',
        type='dict'),
    modified_on=dict(
        required=False,
        type='str'),
    record_id=dict(
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
        resource_type='ibm_cis_dns_record',
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
