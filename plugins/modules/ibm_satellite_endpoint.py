#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_satellite_endpoint
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_endpoint

short_description: Configure IBM Cloud 'ibm_satellite_endpoint' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_satellite_endpoint' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    certs:
        description:
            - The certs.
        required: False
        type: list
        elements: dict
    location:
        description:
            - (Required for new resource) The Location ID.
        required: True
        type: str
    connection_type:
        description:
            - (Required for new resource) The type of the endpoint.
        required: True
        type: str
    server_host:
        description:
            - (Required for new resource) The host name or IP address of the server endpoint. For 'http-tunnel' protocol, server_host can start with '*.' , which means a wildcard to it's sub domains. Such as '*.example.com' can accept request to 'api.example.com' and 'www.example.com'.
        required: True
        type: str
    server_port:
        description:
            - (Required for new resource) The port number of the server endpoint. For 'http-tunnel' protocol, server_port can be 0, which means any port. Such as 0 is good for 80 (http) and 443 (https).
        required: True
        type: int
    timeout:
        description:
            - The inactivity timeout in the Endpoint side.
        required: False
        type: int
    sni:
        description:
            - The server name indicator (SNI) which used to connect to the server endpoint. Only useful if server side requires SNI.
        required: False
        type: str
    client_mutual_auth:
        description:
            - Whether enable mutual auth in the client application side, when client_protocol is 'tls' or 'https', this field is required.
        required: False
        type: bool
        default: False
    server_mutual_auth:
        description:
            - Whether enable mutual auth in the server application side, when client_protocol is 'tls', this field is required.
        required: False
        type: bool
        default: False
    display_name:
        description:
            - (Required for new resource) The display name of the endpoint. Endpoint names must start with a letter and end with an alphanumeric character, can contain letters, numbers, and hyphen (-), and must be 63 characters or fewer.
        required: True
        type: str
    client_protocol:
        description:
            - (Required for new resource) The protocol in the client application side.
        required: True
        type: str
    created_by:
        description:
            - The service or person who created the endpoint. Must be 1000 characters or fewer.
        required: False
        type: str
    server_protocol:
        description:
            - The protocol in the server application side. This parameter will change to default value if it is omitted even when using PATCH API. If client_protocol is 'udp', server_protocol must be 'udp'. If client_protocol is 'tcp'/'http', server_protocol could be 'tcp'/'tls' and default to 'tcp'. If client_protocol is 'tls'/'https', server_protocol could be 'tcp'/'tls' and default to 'tls'. If client_protocol is 'http-tunnel', server_protocol must be 'tcp'.
        required: False
        type: str
    reject_unauth:
        description:
            - Whether reject any connection to the server application which is not authorized with the list of supplied CAs in the fields certs.server_cert.
        required: False
        type: bool
        default: False
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
    ('location', 'str'),
    ('connection_type', 'str'),
    ('server_host', 'str'),
    ('server_port', 'int'),
    ('display_name', 'str'),
    ('client_protocol', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'certs',
    'location',
    'connection_type',
    'server_host',
    'server_port',
    'timeout',
    'sni',
    'client_mutual_auth',
    'server_mutual_auth',
    'display_name',
    'client_protocol',
    'created_by',
    'server_protocol',
    'reject_unauth',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('location', 'str'),
    ('endpoint_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'location',
    'endpoint_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    certs=dict(
        required=False,
        elements='',
        type='list'),
    location=dict(
        required=False,
        type='str'),
    connection_type=dict(
        required=False,
        type='str'),
    server_host=dict(
        required=False,
        type='str'),
    server_port=dict(
        required=False,
        type='int'),
    timeout=dict(
        required=False,
        type='int'),
    sni=dict(
        required=False,
        type='str'),
    client_mutual_auth=dict(
        required=False,
        type='bool'),
    server_mutual_auth=dict(
        required=False,
        type='bool'),
    display_name=dict(
        required=False,
        type='str'),
    client_protocol=dict(
        required=False,
        type='str'),
    created_by=dict(
        required=False,
        type='str'),
    server_protocol=dict(
        required=False,
        type='str'),
    reject_unauth=dict(
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
        resource_type='ibm_satellite_endpoint',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_satellite_endpoint',
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
