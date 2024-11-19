#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_private_certificate_configuration_template
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_private_certificate_configuration_template

short_description: Configure IBM Cloud 'ibm_sm_private_certificate_configuration_template' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_sm_private_certificate_configuration_template' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    not_before_duration:
        description:
            - The duration in seconds by which to backdate the `not_before` property of an issued private certificate.The value can be supplied as a string representation of a duration, such as `30s`. In the API response, this value is returned in seconds (integer).
        required: False
        type: str
    region:
        description:
            - The region of the Secrets Manager instance.
        required: False
        type: str
    locality:
        description:
            - The Locality (L) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    allow_bare_domains:
        description:
            - Determines whether to allow clients to request private certificates that match the value of the actual domains on the final certificate.For example, if you specify `example.com` in the `allowed_domains` field, you grant clients the ability to request a certificate that contains the name `example.com` as one of the DNS values on the final certificate.**Important:** In some scenarios, allowing bare domains can be considered a security risk.
        required: False
        type: bool
    allow_any_name:
        description:
            - Determines whether to allow clients to request a private certificate that matches any common name.
        required: False
        type: bool
    allow_wildcard_certificates:
        description:
            - Determines whether the issuance of certificates with RFC 6125 wildcards in the CN field.When set to false, this field prevents wildcards from being issued even if they can be allowed by an option `allow_glob_domains`.
        required: False
        type: bool
    policy_identifiers:
        description:
            - A list of policy Object Identifiers (OIDs).
        required: False
        type: list
        elements: str
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    allowed_domains_template:
        description:
            - Determines whether to allow the domains that are supplied in the `allowed_domains` field to contain access control list (ACL) templates.
        required: False
        type: bool
    allowed_other_sans:
        description:
            - The custom Object Identifier (OID) or UTF8-string Subject Alternative Names (SANs) to allow for private certificates.The format for each element in the list is the same as OpenSSL: `<oid>:<type>:<value>` where the current valid type is `UTF8`. To allow any value for an OID, use `*` as its value. Alternatively, specify a single `*` to allow any `other_sans` input.
        required: False
        type: list
        elements: str
    ext_key_usage:
        description:
            - The allowed extended key usage constraint on private certificates.You can find valid values in the [Go x509 package documentation](https://golang.org/pkg/crypto/x509/#ExtKeyUsage). Omit the `ExtKeyUsage` part of the value. Values are not case-sensitive. To specify no key usage constraints, set this field to an empty list.
        required: False
        type: list
        elements: str
    require_cn:
        description:
            - Determines whether to require a common name to create a private certificate.By default, a common name is required to generate a certificate. To make the `common_name` field optional, set the `require_cn` option to `false`.
        required: False
        type: bool
    max_ttl:
        description:
            - The maximum time-to-live (TTL) for certificates that are created by this CA.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).Minimum value is one hour (`1h`). Maximum value is 100 years (`876000h`).
        required: False
        type: str
    country:
        description:
            - The Country (C) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    basic_constraints_valid_for_non_ca:
        description:
            - Determines whether to mark the Basic Constraints extension of an issued private certificate as valid for non-CA certificates.
        required: False
        type: bool
    allowed_uri_sans:
        description:
            - The URI Subject Alternative Names to allow for private certificates.Values can contain glob patterns, for example `spiffe://hostname/_*`.
        required: False
        type: list
        elements: str
    use_csr_sans:
        description:
            - When used with the `private_cert_configuration_action_sign_csr` action, this field determines whether to use the Subject Alternative Names(SANs) from a certificate signing request (CSR) instead of the SANs that are included in the data of the certificate.Does not include the common name in the CSR. To use the common name, include the `use_csr_common_name` property.
        required: False
        type: bool
    ttl:
        description:
            - The requested time-to-live (TTL) for certificates that are created by this CA. This field's value cannot be longer than the `max_ttl` limit.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).
        required: False
        type: str
    organization:
        description:
            - The Organization (O) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    province:
        description:
            - The Province (ST) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    use_csr_common_name:
        description:
            - When used with the `private_cert_configuration_action_sign_csr` action, this field determines whether to use the common name (CN) from a certificate signing request (CSR) instead of the CN that's included in the data of the certificate.Does not include any requested Subject Alternative Names (SANs) in the CSR. To use the alternative names, include the `use_csr_sans` property.
        required: False
        type: bool
    name:
        description:
            - (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.
        required: True
        type: str
    key_bits:
        description:
            - The number of bits to use to generate the private key.Allowable values for RSA keys are: `2048` and `4096`. Allowable values for EC keys are: `224`, `256`, `384`, and `521`. The default for RSA keys is `2048`. The default for EC keys is `256`.
        required: False
        type: int
    allowed_domains:
        description:
            - The domains to define for the certificate template. This property is used along with the `allow_bare_domains` and `allow_subdomains` options.
        required: False
        type: list
        elements: str
    code_signing_flag:
        description:
            - Determines whether private certificates are flagged for code signing use.
        required: False
        type: bool
    instance_id:
        description:
            - (Required for new resource) The ID of the Secrets Manager instance.
        required: True
        type: str
    allowed_secret_groups:
        description:
            - Scopes the creation of private certificates to only the secret groups that you specify.This field can be supplied as a comma-delimited list of secret group IDs.
        required: False
        type: str
    allow_subdomains:
        description:
            - Determines whether to allow clients to request private certificates with common names (CN) that are subdomains of the CNs that are allowed by the other certificate template options. This includes wildcard subdomains.For example, if `allowed_domains` has a value of `example.com` and `allow_subdomains`is set to `true`, then the following subdomains are allowed: `foo.example.com`, `bar.example.com`, `*.example.com`.**Note:** This field is redundant if you use the `allow_any_name` option.
        required: False
        type: bool
    allow_ip_sans:
        description:
            - Determines whether to allow clients to request a private certificate with IP Subject Alternative Names.
        required: False
        type: bool
    certificate_authority:
        description:
            - (Required for new resource) The name of the intermediate certificate authority.
        required: True
        type: str
    enforce_hostnames:
        description:
            - Determines whether to enforce only valid host names for common names, DNS Subject Alternative Names, and the host section of email addresses.
        required: False
        type: bool
    server_flag:
        description:
            - Determines whether private certificates are flagged for server use.
        required: False
        type: bool
    client_flag:
        description:
            - Determines whether private certificates are flagged for client use.
        required: False
        type: bool
    email_protection_flag:
        description:
            - Determines whether private certificates are flagged for email protection use.
        required: False
        type: bool
    ou:
        description:
            - The Organizational Unit (OU) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    street_address:
        description:
            - The street address values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    postal_code:
        description:
            - The postal code values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    ext_key_usage_oids:
        description:
            - A list of extended key usage Object Identifiers (OIDs).
        required: False
        type: list
        elements: str
    key_usage:
        description:
            - The allowed key usage constraint to define for private certificates.You can find valid values in the [Go x509 package documentation](https://pkg.go.dev/crypto/x509#KeyUsage). Omit the `KeyUsage` part of the value. Values are not case-sensitive. To specify no key usage constraints, set this field to an empty list.
        required: False
        type: list
        elements: str
    key_type:
        description:
            - The type of private key to generate.
        required: False
        type: str
    allow_localhost:
        description:
            - Determines whether to allow `localhost` to be included as one of the requested common names.
        required: False
        type: bool
    allow_glob_domains:
        description:
            - Determines whether to allow glob patterns, for example, `ftp*.example.com`, in the names that are specified in the `allowed_domains` field.If set to `true`, clients are allowed to request private certificates with names that match the glob patterns.
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
    ('certificate_authority', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'not_before_duration',
    'region',
    'locality',
    'allow_bare_domains',
    'allow_any_name',
    'allow_wildcard_certificates',
    'policy_identifiers',
    'endpoint_type',
    'allowed_domains_template',
    'allowed_other_sans',
    'ext_key_usage',
    'require_cn',
    'max_ttl',
    'country',
    'basic_constraints_valid_for_non_ca',
    'allowed_uri_sans',
    'use_csr_sans',
    'ttl',
    'organization',
    'province',
    'use_csr_common_name',
    'name',
    'key_bits',
    'allowed_domains',
    'code_signing_flag',
    'instance_id',
    'allowed_secret_groups',
    'allow_subdomains',
    'allow_ip_sans',
    'certificate_authority',
    'enforce_hostnames',
    'server_flag',
    'client_flag',
    'email_protection_flag',
    'ou',
    'street_address',
    'postal_code',
    'ext_key_usage_oids',
    'key_usage',
    'key_type',
    'allow_localhost',
    'allow_glob_domains',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
    ('instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'instance_id',
    'region',
    'endpoint_type',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    not_before_duration=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    locality=dict(
        required=False,
        elements='',
        type='list'),
    allow_bare_domains=dict(
        required=False,
        type='bool'),
    allow_any_name=dict(
        required=False,
        type='bool'),
    allow_wildcard_certificates=dict(
        required=False,
        type='bool'),
    policy_identifiers=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
        required=False,
        type='str'),
    allowed_domains_template=dict(
        required=False,
        type='bool'),
    allowed_other_sans=dict(
        required=False,
        elements='',
        type='list'),
    ext_key_usage=dict(
        required=False,
        elements='',
        type='list'),
    require_cn=dict(
        required=False,
        type='bool'),
    max_ttl=dict(
        required=False,
        type='str'),
    country=dict(
        required=False,
        elements='',
        type='list'),
    basic_constraints_valid_for_non_ca=dict(
        required=False,
        type='bool'),
    allowed_uri_sans=dict(
        required=False,
        elements='',
        type='list'),
    use_csr_sans=dict(
        required=False,
        type='bool'),
    ttl=dict(
        required=False,
        type='str'),
    organization=dict(
        required=False,
        elements='',
        type='list'),
    province=dict(
        required=False,
        elements='',
        type='list'),
    use_csr_common_name=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    key_bits=dict(
        required=False,
        type='int'),
    allowed_domains=dict(
        required=False,
        elements='',
        type='list'),
    code_signing_flag=dict(
        required=False,
        type='bool'),
    instance_id=dict(
        required=False,
        type='str'),
    allowed_secret_groups=dict(
        required=False,
        type='str'),
    allow_subdomains=dict(
        required=False,
        type='bool'),
    allow_ip_sans=dict(
        required=False,
        type='bool'),
    certificate_authority=dict(
        required=False,
        type='str'),
    enforce_hostnames=dict(
        required=False,
        type='bool'),
    server_flag=dict(
        required=False,
        type='bool'),
    client_flag=dict(
        required=False,
        type='bool'),
    email_protection_flag=dict(
        required=False,
        type='bool'),
    ou=dict(
        required=False,
        elements='',
        type='list'),
    street_address=dict(
        required=False,
        elements='',
        type='list'),
    postal_code=dict(
        required=False,
        elements='',
        type='list'),
    ext_key_usage_oids=dict(
        required=False,
        elements='',
        type='list'),
    key_usage=dict(
        required=False,
        elements='',
        type='list'),
    key_type=dict(
        required=False,
        type='str'),
    allow_localhost=dict(
        required=False,
        type='bool'),
    allow_glob_domains=dict(
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
        resource_type='ibm_sm_private_certificate_configuration_template',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_sm_private_certificate_configuration_template',
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
