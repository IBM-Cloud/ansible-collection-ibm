#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_iam_credentials_secret
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_iam_credentials_secret

short_description: Configure IBM Cloud 'ibm_sm_iam_credentials_secret' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_sm_iam_credentials_secret' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    service_id:
        description:
            - The service ID under which the API key (see the `api_key` field) is created.If you omit this parameter, Secrets Manager generates a new service ID for your secret at its creation and adds it to the access groups that you assign.Optionally, you can use this field to provide your own service ID if you prefer to manage its access directly or retain the service ID after your secret expires, is rotated, or deleted. If you provide a service ID, do not include the `access_groups` parameter.
        required: False
        type: str
    reuse_api_key:
        description:
            - Determines whether to use the same service ID and API key for future read operations on an`iam_credentials` secret. Must be set to `true` for IAM credentials secrets managed with Terraform.
        required: False
        type: bool
        default: True
    version_custom_metadata:
        description:
            - The secret version metadata that a user can customize.
        required: False
        type: dict
        elements: str
    labels:
        description:
            - Labels that you can use to search for secrets in your instance.Up to 30 labels can be created.
        required: False
        type: list
        elements: str
    instance_id:
        description:
            - (Required for new resource) The ID of the Secrets Manager instance.
        required: True
        type: str
    name:
        description:
            - (Required for new resource) A human-readable name to assign to your secret.To protect your privacy, do not use personal data, such as your name or location, as a name for your secret.
        required: True
        type: str
    description:
        description:
            - An extended description of your secret.To protect your privacy, do not use personal data, such as your name or location, as a description for your secret group.
        required: False
        type: str
    custom_metadata:
        description:
            - The secret metadata that a user can customize.
        required: False
        type: dict
        elements: str
    rotation:
        description:
            - Determines whether Secrets Manager rotates your secrets automatically.
        required: False
        type: list
        elements: dict
    secret_group_id:
        description:
            - A v4 UUID identifier, or `default` secret group.
        required: False
        type: str
    ttl:
        description:
            - (Required for new resource) The time-to-live (TTL) or lease duration to assign to generated credentials.For `iam_credentials` secrets, the TTL defines for how long each generated API key remains valid. The value is an integer that specifies the number of seconds .Minimum duration is 1 minute. Maximum is 90 days.
        required: True
        type: str
    access_groups:
        description:
            - Access Groups that you can use for an `iam_credentials` secret.Up to 10 Access Groups can be used for each secret.
        required: False
        type: list
        elements: str
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    region:
        description:
            - The region of the Secrets Manager instance.
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
    ('name', 'str'),
    ('ttl', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'service_id',
    'reuse_api_key',
    'version_custom_metadata',
    'labels',
    'instance_id',
    'name',
    'description',
    'custom_metadata',
    'rotation',
    'secret_group_id',
    'ttl',
    'access_groups',
    'endpoint_type',
    'region',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'endpoint_type',
    'secret_group_name',
    'instance_id',
    'secret_id',
    'region',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    service_id=dict(
        required=False,
        type='str'),
    reuse_api_key=dict(
        required=False,
        type='bool'),
    version_custom_metadata=dict(
        required=False,
        elements='',
        type='dict'),
    labels=dict(
        required=False,
        elements='',
        type='list'),
    instance_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    custom_metadata=dict(
        required=False,
        elements='',
        type='dict'),
    rotation=dict(
        required=False,
        elements='',
        type='list'),
    secret_group_id=dict(
        required=False,
        type='str'),
    ttl=dict(
        required=False,
        type='str'),
    access_groups=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
        required=False,
        type='str'),
    region=dict(
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
        resource_type='ibm_sm_iam_credentials_secret',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_sm_iam_credentials_secret',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.66.0',
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
