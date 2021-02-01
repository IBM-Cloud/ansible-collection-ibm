#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_domain_settings
short_description: Configure IBM Cloud 'ibm_cis_domain_settings' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_domain_settings' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.20.0
    - Terraform v0.12.20

options:
    always_use_https:
        description:
            - always_use_https setting
        required: False
        type: str
    websockets:
        description:
            - websockets setting
        required: False
        type: str
    minify:
        description:
            - Minify setting
        required: False
        type: list
        elements: dict
    ssl:
        description:
            - SSL/TLS setting
        required: False
        type: str
    image_load_optimization:
        description:
            - image_load_optimization setting
        required: False
        type: str
    image_size_optimization:
        description:
            - image_size_optimization setting
        required: False
        type: str
    ip_geolocation:
        description:
            - ip_geolocation setting
        required: False
        type: str
    origin_error_page_pass_thru:
        description:
            - origin_error_page_pass_thru setting
        required: False
        type: str
    server_side_exclude:
        description:
            - server_side_exclude setting
        required: False
        type: str
    tls_client_auth:
        description:
            - tls_client_auth setting
        required: False
        type: str
    security_header:
        description:
            - Security Header Setting
        required: False
        type: list
        elements: dict
    browser_check:
        description:
            - browser_check setting
        required: False
        type: str
    mobile_redirect:
        description:
            - None
        required: False
        type: list
        elements: dict
    cname_flattening:
        description:
            - cname_flattening setting
        required: False
        type: str
    waf:
        description:
            - WAF setting
        required: False
        type: str
    ipv6:
        description:
            - ipv6 setting
        required: False
        type: str
    true_client_ip_header:
        description:
            - true_client_ip_header setting
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: True
        type: str
    brotli:
        description:
            - brotli setting
        required: False
        type: str
    script_load_optimization:
        description:
            - script_load_optimization setting
        required: False
        type: str
    challenge_ttl:
        description:
            - Challenge TTL setting
        required: False
        type: int
    dnssec:
        description:
            - DNS Sec setting
        required: False
        type: str
    hotlink_protection:
        description:
            - hotlink_protection setting
        required: False
        type: str
    response_buffering:
        description:
            - response_buffering setting
        required: False
        type: str
    min_tls_version:
        description:
            - Minimum version of TLS required
        required: False
        type: str
        default: 1.1
    opportunistic_encryption:
        description:
            - opportunistic_encryption setting
        required: False
        type: str
    prefetch_preload:
        description:
            - prefetch_preload setting
        required: False
        type: str
    automatic_https_rewrites:
        description:
            - automatic_https_rewrites setting
        required: False
        type: str
    http2:
        description:
            - http2 setting
        required: False
        type: str
    pseudo_ipv4:
        description:
            - pseudo_ipv4 setting
        required: False
        type: str
    max_upload:
        description:
            - Maximum upload
        required: False
        type: int
    cipher:
        description:
            - Cipher settings
        required: False
        type: list
        elements: str
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: True
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
    ('domain_id', 'str'),
    ('cis_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'always_use_https',
    'websockets',
    'minify',
    'ssl',
    'image_load_optimization',
    'image_size_optimization',
    'ip_geolocation',
    'origin_error_page_pass_thru',
    'server_side_exclude',
    'tls_client_auth',
    'security_header',
    'browser_check',
    'mobile_redirect',
    'cname_flattening',
    'waf',
    'ipv6',
    'true_client_ip_header',
    'domain_id',
    'brotli',
    'script_load_optimization',
    'challenge_ttl',
    'dnssec',
    'hotlink_protection',
    'response_buffering',
    'min_tls_version',
    'opportunistic_encryption',
    'prefetch_preload',
    'automatic_https_rewrites',
    'http2',
    'pseudo_ipv4',
    'max_upload',
    'cipher',
    'cis_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    always_use_https=dict(
        required=False,
        type='str'),
    websockets=dict(
        required=False,
        type='str'),
    minify=dict(
        required=False,
        elements='',
        type='list'),
    ssl=dict(
        required=False,
        type='str'),
    image_load_optimization=dict(
        required=False,
        type='str'),
    image_size_optimization=dict(
        required=False,
        type='str'),
    ip_geolocation=dict(
        required=False,
        type='str'),
    origin_error_page_pass_thru=dict(
        required=False,
        type='str'),
    server_side_exclude=dict(
        required=False,
        type='str'),
    tls_client_auth=dict(
        required=False,
        type='str'),
    security_header=dict(
        required=False,
        elements='',
        type='list'),
    browser_check=dict(
        required=False,
        type='str'),
    mobile_redirect=dict(
        required=False,
        elements='',
        type='list'),
    cname_flattening=dict(
        required=False,
        type='str'),
    waf=dict(
        required=False,
        type='str'),
    ipv6=dict(
        required=False,
        type='str'),
    true_client_ip_header=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    brotli=dict(
        required=False,
        type='str'),
    script_load_optimization=dict(
        required=False,
        type='str'),
    challenge_ttl=dict(
        required=False,
        type='int'),
    dnssec=dict(
        required=False,
        type='str'),
    hotlink_protection=dict(
        required=False,
        type='str'),
    response_buffering=dict(
        required=False,
        type='str'),
    min_tls_version=dict(
        required=False,
        type='str'),
    opportunistic_encryption=dict(
        required=False,
        type='str'),
    prefetch_preload=dict(
        required=False,
        type='str'),
    automatic_https_rewrites=dict(
        required=False,
        type='str'),
    http2=dict(
        required=False,
        type='str'),
    pseudo_ipv4=dict(
        required=False,
        type='str'),
    max_upload=dict(
        required=False,
        type='int'),
    cipher=dict(
        required=False,
        elements='',
        type='list'),
    cis_id=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_cis_domain_settings',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.20.0',
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
