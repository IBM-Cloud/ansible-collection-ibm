#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_hpcs_keystore
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/hpcs_keystore

short_description: Configure IBM Cloud 'ibm_hpcs_keystore' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_hpcs_keystore' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.46.0
    - Terraform v0.12.20

options:
    aws_access_key_id:
        description:
            - The access key id used for connecting to this instance of AWS KMS.
        required: False
        type: str
    azure_service_name:
        description:
            - Service name of the key vault instance from the Azure portal.
        required: False
        type: str
    azure_resource_group:
        description:
            - Resource group in Azure.
        required: False
        type: str
    ibm_api_endpoint:
        description:
            - API endpoint of the IBM Cloud keystore.
        required: False
        type: str
    ibm_key_ring:
        description:
            - The key ring of an IBM Cloud KMS Keystore.
        required: False
        type: str
    vault:
        description:
            - (Required for new resource) Reference to a vault.
        required: True
        type: list
        elements: dict
    aws_region:
        description:
            - AWS Region.
        required: False
        type: str
    ibm_api_key:
        description:
            - The IBM Cloud API key to be used for connecting to this IBM Cloud keystore.
        required: False
        type: str
    groups:
        description:
            - List of groups that this keystore belongs to.
        required: False
        type: list
        elements: str
    azure_service_principal_password:
        description:
            - Azure service principal password.
        required: False
        type: str
    azure_environment:
        description:
            - Azure environment, usually 'Azure'.
        required: False
        type: str
    instance_id:
        description:
            - (Required for new resource) The ID of the UKO instance this resource exists in.
        required: True
        type: str
    region:
        description:
            - (Required for new resource) The region of the UKO instance this resource exists in.
        required: True
        type: str
    ibm_iam_endpoint:
        description:
            - Endpoint of the IAM service for this IBM Cloud keystore.
        required: False
        type: str
    description:
        description:
            - Description of the keystore.
        required: False
        type: str
    azure_service_principal_client_id:
        description:
            - Azure service principal client ID.
        required: False
        type: str
    azure_subscription_id:
        description:
            - Subscription ID in Azure.
        required: False
        type: str
    name:
        description:
            - Name of the target keystore. It can be changed in the future.
        required: False
        type: str
    type:
        description:
            - (Required for new resource) Type of keystore.
        required: True
        type: str
    uko_vault:
        description:
            - (Required for new resource) The UUID of the Vault in which the update is to take place.
        required: True
        type: str
    aws_secret_access_key:
        description:
            - The secret access key used for connecting to this instance of AWS KMS.
        required: False
        type: str
    azure_location:
        description:
            - Location of the Azure Key Vault.
        required: False
        type: str
    ibm_variant:
        description:
            - Possible IBM Cloud KMS variants.
        required: False
        type: str
    ibm_instance_id:
        description:
            - The instance ID of the IBM Cloud keystore.
        required: False
        type: str
    azure_tenant:
        description:
            - Azure tenant that the Key Vault is associated with,.
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
    ('vault', 'list'),
    ('instance_id', 'str'),
    ('region', 'str'),
    ('type', 'str'),
    ('uko_vault', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'aws_access_key_id',
    'azure_service_name',
    'azure_resource_group',
    'ibm_api_endpoint',
    'ibm_key_ring',
    'vault',
    'aws_region',
    'ibm_api_key',
    'groups',
    'azure_service_principal_password',
    'azure_environment',
    'instance_id',
    'region',
    'ibm_iam_endpoint',
    'description',
    'azure_service_principal_client_id',
    'azure_subscription_id',
    'name',
    'type',
    'uko_vault',
    'aws_secret_access_key',
    'azure_location',
    'ibm_variant',
    'ibm_instance_id',
    'azure_tenant',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('region', 'str'),
    ('instance_id', 'str'),
    ('uko_vault', 'str'),
    ('keystore_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'region',
    'instance_id',
    'uko_vault',
    'keystore_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    aws_access_key_id=dict(
        required=False,
        type='str'),
    azure_service_name=dict(
        required=False,
        type='str'),
    azure_resource_group=dict(
        required=False,
        type='str'),
    ibm_api_endpoint=dict(
        required=False,
        type='str'),
    ibm_key_ring=dict(
        required=False,
        type='str'),
    vault=dict(
        required=False,
        elements='',
        type='list'),
    aws_region=dict(
        required=False,
        type='str'),
    ibm_api_key=dict(
        required=False,
        type='str'),
    groups=dict(
        required=False,
        elements='',
        type='list'),
    azure_service_principal_password=dict(
        required=False,
        type='str'),
    azure_environment=dict(
        required=False,
        type='str'),
    instance_id=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    ibm_iam_endpoint=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    azure_service_principal_client_id=dict(
        required=False,
        type='str'),
    azure_subscription_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    uko_vault=dict(
        required=False,
        type='str'),
    aws_secret_access_key=dict(
        required=False,
        type='str'),
    azure_location=dict(
        required=False,
        type='str'),
    ibm_variant=dict(
        required=False,
        type='str'),
    ibm_instance_id=dict(
        required=False,
        type='str'),
    azure_tenant=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_hpcs_keystore',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.46.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_hpcs_keystore',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.46.0',
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
