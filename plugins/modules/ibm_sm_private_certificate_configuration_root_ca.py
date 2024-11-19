#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_private_certificate_configuration_root_ca
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_private_certificate_configuration_root_ca

short_description: Configure IBM Cloud 'ibm_sm_private_certificate_configuration_root_ca' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_sm_private_certificate_configuration_root_ca' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    key_bits:
        description:
            - The number of bits to use to generate the private key.Allowable values for RSA keys are: `2048` and `4096`. Allowable values for EC keys are: `224`, `256`, `384`, and `521`. The default for RSA keys is `2048`. The default for EC keys is `256`.
        required: False
        type: int
    region:
        description:
            - The region of the Secrets Manager instance.
        required: False
        type: str
    max_ttl:
        description:
            - (Required for new resource) The maximum time-to-live (TTL) for certificates that are created by this CA.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).Minimum value is one hour (`1h`). Maximum value is 100 years (`876000h`).
        required: True
        type: str
    crl_expiry:
        description:
            - The time until the certificate revocation list (CRL) expires.The value can be supplied as a string representation of a duration in hours, such as `48h`. The default is 72 hours. In the API response, this value is returned in seconds (integer).**Note:** The CRL is rotated automatically before it expires.
        required: False
        type: str
    issuing_certificates_urls_encoded:
        description:
            - Determines whether to encode the URL of the issuing certificate in the certificates that are issued by this certificate authority.
        required: False
        type: bool
        default: False
    alt_names:
        description:
            - With the Subject Alternative Name field, you can specify additional host names to be protected by a single SSL certificate.
        required: False
        type: list
        elements: str
    ou:
        description:
            - The Organizational Unit (OU) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    instance_id:
        description:
            - (Required for new resource) The ID of the Secrets Manager instance.
        required: True
        type: str
    crl_disable:
        description:
            - Disables or enables certificate revocation list (CRL) building.If CRL building is disabled, a signed but zero-length CRL is returned when downloading the CRL. If CRL building is enabled, it will rebuild the CRL.
        required: False
        type: bool
        default: False
    ttl:
        description:
            - The requested time-to-live (TTL) for certificates that are created by this CA. This field's value cannot be longer than the `max_ttl` limit.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).
        required: False
        type: str
    key_type:
        description:
            - The type of private key to generate.
        required: False
        type: str
    max_path_length:
        description:
            - The maximum path length to encode in the generated certificate. `-1` means no limit.If the signing certificate has a maximum path length set, the path length is set to one less than that of the signing certificate. A limit of `0` means a literal path length of zero.
        required: False
        type: int
    uri_sans:
        description:
            - The URI Subject Alternative Names to define for the CA certificate, in a comma-delimited list.
        required: False
        type: str
    exclude_cn_from_sans:
        description:
            - Controls whether the common name is excluded from Subject Alternative Names (SANs).If the common name set to `true`, it is not included in DNS or Email SANs if they apply. This field can be useful if the common name is a human-readable identifier, instead of a hostname or an email address.
        required: False
        type: bool
        default: False
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
    format:
        description:
            - The format of the returned data.
        required: False
        type: str
    permitted_dns_domains:
        description:
            - The allowed DNS domains or subdomains for the certificates that are to be signed and issued by this CA certificate.
        required: False
        type: list
        elements: str
    province:
        description:
            - The Province (ST) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    postal_code:
        description:
            - The postal code values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    organization:
        description:
            - The Organization (O) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    country:
        description:
            - The Country (C) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    street_address:
        description:
            - The street address values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    crypto_key:
        description:
            - The data that is associated with a cryptographic key.
        required: False
        type: list
        elements: dict
    crl_distribution_points_encoded:
        description:
            - Determines whether to encode the certificate revocation list (CRL) distribution points in the certificates that are issued by this certificate authority.
        required: False
        type: bool
        default: False
    common_name:
        description:
            - (Required for new resource) The Common Name (AKA CN) represents the server name that is protected by the SSL certificate.
        required: True
        type: str
    private_key_format:
        description:
            - The format of the generated private key.
        required: False
        type: str
        default: der
    name:
        description:
            - (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.
        required: True
        type: str
    locality:
        description:
            - The Locality (L) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    endpoint_type:
        description:
            - public or private.
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
    ('max_ttl', 'str'),
    ('instance_id', 'str'),
    ('common_name', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'key_bits',
    'region',
    'max_ttl',
    'crl_expiry',
    'issuing_certificates_urls_encoded',
    'alt_names',
    'ou',
    'instance_id',
    'crl_disable',
    'ttl',
    'key_type',
    'max_path_length',
    'uri_sans',
    'exclude_cn_from_sans',
    'ip_sans',
    'other_sans',
    'format',
    'permitted_dns_domains',
    'province',
    'postal_code',
    'organization',
    'country',
    'street_address',
    'crypto_key',
    'crl_distribution_points_encoded',
    'common_name',
    'private_key_format',
    'name',
    'locality',
    'endpoint_type',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
    ('instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'region',
    'instance_id',
    'endpoint_type',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    key_bits=dict(
        required=False,
        type='int'),
    region=dict(
        required=False,
        type='str'),
    max_ttl=dict(
        required=False,
        type='str'),
    crl_expiry=dict(
        required=False,
        type='str'),
    issuing_certificates_urls_encoded=dict(
        required=False,
        type='bool'),
    alt_names=dict(
        required=False,
        elements='',
        type='list'),
    ou=dict(
        required=False,
        elements='',
        type='list'),
    instance_id=dict(
        required=False,
        type='str'),
    crl_disable=dict(
        required=False,
        type='bool'),
    ttl=dict(
        required=False,
        type='str'),
    key_type=dict(
        required=False,
        type='str'),
    max_path_length=dict(
        required=False,
        type='int'),
    uri_sans=dict(
        required=False,
        type='str'),
    exclude_cn_from_sans=dict(
        required=False,
        type='bool'),
    ip_sans=dict(
        required=False,
        type='str'),
    other_sans=dict(
        required=False,
        elements='',
        type='list'),
    format=dict(
        required=False,
        type='str'),
    permitted_dns_domains=dict(
        required=False,
        elements='',
        type='list'),
    province=dict(
        required=False,
        elements='',
        type='list'),
    postal_code=dict(
        required=False,
        elements='',
        type='list'),
    organization=dict(
        required=False,
        elements='',
        type='list'),
    country=dict(
        required=False,
        elements='',
        type='list'),
    street_address=dict(
        required=False,
        elements='',
        type='list'),
    crypto_key=dict(
        required=False,
        elements='',
        type='list'),
    crl_distribution_points_encoded=dict(
        required=False,
        type='bool'),
    common_name=dict(
        required=False,
        type='str'),
    private_key_format=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    locality=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
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
        resource_type='ibm_sm_private_certificate_configuration_root_ca',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_sm_private_certificate_configuration_root_ca',
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
