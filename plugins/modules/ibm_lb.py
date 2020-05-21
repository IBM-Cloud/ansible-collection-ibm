#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_lb
short_description: Configure IBM Cloud 'ibm_lb' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_lb' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    security_certificate_id:
        description:
            - Security certificate ID
        required: False
        type: int
    ip_address:
        description:
            - None
        required: False
        type: str
    dedicated:
        description:
            - Boolena value true if Load balncer is dedicated type
        required: False
        type: bool
        default: False
    ssl_offload:
        description:
            - boolean value true if SSL offload is enabled
        required: False
        type: bool
        default: False
    tags:
        description:
            - Tags associated with resource
        required: False
        type: list
        elements: str
    hostname:
        description:
            - None
        required: False
        type: str
    connections:
        description:
            - (Required for new resource) Connections value
        required: False
        type: int
    datacenter:
        description:
            - (Required for new resource) Datacenter name info
        required: False
        type: str
    ha_enabled:
        description:
            - true if High availability is enabled
        required: False
        type: bool
        default: False
    subnet_id:
        description:
            - None
        required: False
        type: int
    ssl_enabled:
        description:
            - None
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
    ('connections', 'int'),
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'security_certificate_id',
    'ip_address',
    'dedicated',
    'ssl_offload',
    'tags',
    'hostname',
    'connections',
    'datacenter',
    'ha_enabled',
    'subnet_id',
    'ssl_enabled',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    security_certificate_id=dict(
        required=False,
        type='int'),
    ip_address=dict(
        required=False,
        type='str'),
    dedicated=dict(
        default=False,
        type='bool'),
    ssl_offload=dict(
        default=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    hostname=dict(
        required=False,
        type='str'),
    connections=dict(
        required=False,
        type='int'),
    datacenter=dict(
        required=False,
        type='str'),
    ha_enabled=dict(
        default=False,
        type='bool'),
    subnet_id=dict(
        required=False,
        type='int'),
    ssl_enabled=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_lb',
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
