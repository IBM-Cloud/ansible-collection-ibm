#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_range_app
short_description: Configure IBM Cloud 'ibm_cis_range_app' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_range_app' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.19.0
    - Terraform v0.12.20

options:
    ip_firewall:
        description:
            - Enables the IP Firewall for this application. Only available for TCP applications.
        required: False
        type: bool
    edge_ips_type:
        description:
            - The type of edge IP configuration.
        required: False
        type: str
        default: dynamic
    cis_id:
        description:
            - (Required for new resource) CIS Intance CRN
        required: True
        type: str
    protocol:
        description:
            - (Required for new resource) Defines the protocol and port for this application
        required: True
        type: str
    dns_type:
        description:
            - (Required for new resource) Type of the DNS record for this application
        required: True
        type: str
    origin_port:
        description:
            - Port at the origin that listens to traffic
        required: False
        type: int
    domain_id:
        description:
            - (Required for new resource) CIS Domain ID
        required: True
        type: str
    traffic_type:
        description:
            - Configure how traffic is handled at the edge.
        required: False
        type: str
        default: direct
    dns:
        description:
            - (Required for new resource) Name of the DNS record for this application
        required: True
        type: str
    tls:
        description:
            - Configure if and how TLS connections are terminated at the edge.
        required: False
        type: str
        default: off
    origin_direct:
        description:
            - IP address and port of the origin for this Range application.
        required: False
        type: list
        elements: str
    origin_dns:
        description:
            - DNS record pointing to the origin for this Range application.
        required: False
        type: str
    proxy_protocol:
        description:
            - Allows for the true client IP to be passed to the service.
        required: False
        type: str
    edge_ips_connectivity:
        description:
            - Specifies the IP version.
        required: False
        type: str
        default: all
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
    ('protocol', 'str'),
    ('dns_type', 'str'),
    ('domain_id', 'str'),
    ('dns', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ip_firewall',
    'edge_ips_type',
    'cis_id',
    'protocol',
    'dns_type',
    'origin_port',
    'domain_id',
    'traffic_type',
    'dns',
    'tls',
    'origin_direct',
    'origin_dns',
    'proxy_protocol',
    'edge_ips_connectivity',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'origin_port': ['origin_direct'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ip_firewall=dict(
        required=False,
        type='bool'),
    edge_ips_type=dict(
        required=False,
        type='str'),
    cis_id=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    dns_type=dict(
        required=False,
        type='str'),
    origin_port=dict(
        required=False,
        type='int'),
    domain_id=dict(
        required=False,
        type='str'),
    traffic_type=dict(
        required=False,
        type='str'),
    dns=dict(
        required=False,
        type='str'),
    tls=dict(
        required=False,
        type='str'),
    origin_direct=dict(
        required=False,
        elements='',
        type='list'),
    origin_dns=dict(
        required=False,
        type='str'),
    proxy_protocol=dict(
        required=False,
        type='str'),
    edge_ips_connectivity=dict(
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
        resource_type='ibm_cis_range_app',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.19.0',
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
