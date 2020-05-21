#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_network
short_description: Configure IBM Cloud 'ibm_pi_network' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_network' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    pi_network_name:
        description:
            - (Required for new resource) PI network name
        required: False
        type: str
    pi_dns:
        description:
            - List of PI network DNS name
        required: False
        type: list
        elements: str
    pi_cidr:
        description:
            - PI network CIDR
        required: False
        type: str
    pi_gateway:
        description:
            - PI network gateway
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) PI cloud instance ID
        required: False
        type: str
    network_id:
        description:
            - PI network ID
        required: False
        type: str
    vlan_id:
        description:
            - VLAN Id value
        required: False
        type: float
    pi_network_type:
        description:
            - (Required for new resource) PI network type
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
    zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environment
              variable 'IC_ZONE'.
        required: False
        type: str
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
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
    ('pi_network_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_network_type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_network_name',
    'pi_dns',
    'pi_cidr',
    'pi_gateway',
    'pi_cloud_instance_id',
    'network_id',
    'vlan_id',
    'pi_network_type',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_network_name=dict(
        required=False,
        type='str'),
    pi_dns=dict(
        required=False,
        elements='',
        type='list'),
    pi_cidr=dict(
        required=False,
        type='str'),
    pi_gateway=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    network_id=dict(
        required=False,
        type='str'),
    vlan_id=dict(
        required=False,
        type='float'),
    pi_network_type=dict(
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
    zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE'])),
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
        resource_type='ibm_pi_network',
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
