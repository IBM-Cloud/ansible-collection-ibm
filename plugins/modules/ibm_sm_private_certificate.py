#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_private_certificate
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_private_certificate

short_description: Configure IBM Cloud 'ibm_sm_private_certificate' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_sm_private_certificate' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    description:
        description:
            - An extended description of your secret.To protect your privacy, do not use personal data, such as your name or location, as a description for your secret group.
        required: False
        type: str
    uri_sans:
        description:
            - The URI Subject Alternative Names to define for the CA certificate, in a comma-delimited list.
        required: False
        type: str
    format:
        description:
            - The format of the returned data.
        required: False
        type: str
    region:
        description:
            - The region of the Secrets Manager instance.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) A human-readable name to assign to your secret.To protect your privacy, do not use personal data, such as your name or location, as a name for your secret.
        required: True
        type: str
    ttl:
        description:
            - The time-to-live (TTL) or lease duration to assign to generated credentials.For `iam_credentials` secrets, the TTL defines for how long each generated API key remains valid. The value can be either an integer that specifies the number of seconds, or the string representation of a duration, such as `120m` or `24h`.Minimum duration is 1 minute. Maximum is 90 days.
        required: False
        type: str
    instance_id:
        description:
            - (Required for new resource) The ID of the Secrets Manager instance.
        required: True
        type: str
    certificate_template:
        description:
            - (Required for new resource) The name of the certificate template.
        required: True
        type: str
    secret_group_id:
        description:
            - A v4 UUID identifier, or `default` secret group.
        required: False
        type: str
    labels:
        description:
            - Labels that you can use to search for secrets in your instance.Up to 30 labels can be created.
        required: False
        type: list
        elements: str
    common_name:
        description:
            - (Required for new resource) The Common Name (AKA CN) represents the server name that is protected by the SSL certificate.
        required: True
        type: str
    ip_sans:
        description:
            - The IP Subject Alternative Names to define for the CA certificate, in a comma-delimited list.
        required: False
        type: str
    other_sans:
        description:
            - The custom Object Identifier (OID) or UTF8-string Subject Alternative Names to define for the CA certificate.The alternative names must match the values that are specified in the `allowed_other_sans` field in the associated certificate template. The format is the same as OpenSSL: `<oid>:<type>:<value>` where the current valid type is `UTF8`.
        required: False
        type: list
        elements: str
    private_key_format:
        description:
            - The format of the generated private key.
        required: False
        type: str
        default: der
    rotation:
        description:
            - Determines whether Secrets Manager rotates your secrets automatically.
        required: False
        type: list
        elements: dict
    custom_metadata:
        description:
            - The secret metadata that a user can customize.
        required: False
        type: dict
        elements: str
    version_custom_metadata:
        description:
            - The secret version metadata that a user can customize.
        required: False
        type: dict
        elements: str
    alt_names:
        description:
            - With the Subject Alternative Name field, you can specify additional host names to be protected by a single SSL certificate.
        required: False
        type: list
        elements: str
    csr:
        description:
            - The certificate signing request.
        required: False
        type: str
    exclude_cn_from_sans:
        description:
            - Controls whether the common name is excluded from Subject Alternative Names (SANs).If the common name set to `true`, it is not included in DNS or Email SANs if they apply. This field can be useful if the common name is a human-readable identifier, instead of a hostname or an email address.
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
    ('name', 'str'),
    ('instance_id', 'str'),
    ('certificate_template', 'str'),
    ('common_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'endpoint_type',
    'description',
    'uri_sans',
    'format',
    'region',
    'name',
    'ttl',
    'instance_id',
    'certificate_template',
    'secret_group_id',
    'labels',
    'common_name',
    'ip_sans',
    'other_sans',
    'private_key_format',
    'rotation',
    'custom_metadata',
    'version_custom_metadata',
    'alt_names',
    'csr',
    'exclude_cn_from_sans',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'instance_id',
    'secret_id',
    'region',
    'endpoint_type',
    'name',
    'secret_group_name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    endpoint_type=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    uri_sans=dict(
        required=False,
        type='str'),
    format=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    ttl=dict(
        required=False,
        type='str'),
    instance_id=dict(
        required=False,
        type='str'),
    certificate_template=dict(
        required=False,
        type='str'),
    secret_group_id=dict(
        required=False,
        type='str'),
    labels=dict(
        required=False,
        elements='',
        type='list'),
    common_name=dict(
        required=False,
        type='str'),
    ip_sans=dict(
        required=False,
        type='str'),
    other_sans=dict(
        required=False,
        elements='',
        type='list'),
    private_key_format=dict(
        required=False,
        type='str'),
    rotation=dict(
        required=False,
        elements='',
        type='list'),
    custom_metadata=dict(
        required=False,
        elements='',
        type='dict'),
    version_custom_metadata=dict(
        required=False,
        elements='',
        type='dict'),
    alt_names=dict(
        required=False,
        elements='',
        type='list'),
    csr=dict(
        required=False,
        type='str'),
    exclude_cn_from_sans=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_sm_private_certificate',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_sm_private_certificate',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.71.2',
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
