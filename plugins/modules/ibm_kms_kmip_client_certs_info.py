#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_kms_kmip_client_certs_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/kms_kmip_client_certs

short_description: Retrieve IBM Cloud 'ibm_kms_kmip_client_certs' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_kms_kmip_client_certs' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    instance_id:
        description:
            - Key protect Instance GUID
        required: True
        type: str
    adapter_name:
        description:
            - The name of the KMIP adapter that contains the cert
        required: False
        type: str
    offset:
        description:
            - Offset of adapters to be fetched
        required: False
        type: int
    endpoint_type:
        description:
            - public or private
        required: False
        type: str
    adapter_id:
        description:
            - The id of the KMIP adapter that contains the cert
        required: False
        type: str
    limit:
        description:
            - Limit of how many adapters to be fetched
        required: False
        type: int
    show_total_count:
        description:
            - Flag to return the count of how many adapters there are in total
        required: False
        type: bool
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
    ('instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'instance_id',
    'adapter_name',
    'offset',
    'endpoint_type',
    'adapter_id',
    'limit',
    'show_total_count',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    instance_id=dict(
        required=True,
        type='str'),
    adapter_name=dict(
        required=False,
        type='str'),
    offset=dict(
        required=False,
        type='int'),
    endpoint_type=dict(
        required=False,
        type='str'),
    adapter_id=dict(
        required=False,
        type='str'),
    limit=dict(
        required=False,
        type='int'),
    show_total_count=dict(
        required=False,
        type='bool'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_kms_kmip_client_certs',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
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
