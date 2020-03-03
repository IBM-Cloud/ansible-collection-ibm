#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_network_info
short_description: Retrieve IBM Cloud 'ibm_pi_network' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_network' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    pi_network_name:
        description:
            - Network Name to be used for pvminstances
        required: True
        type: str
    cidr:
        description:
            - None
        required: False
        type: str
    vlan_id:
        description:
            - None
        required: False
        type: int
    gateway:
        description:
            - None
        required: False
        type: str
    available_ip_count:
        description:
            - None
        required: False
        type: float
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    type:
        description:
            - None
        required: False
        type: str
    used_ip_count:
        description:
            - None
        required: False
        type: float
    used_ip_percent:
        description:
            - None
        required: False
        type: float
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('pi_network_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_network_name',
    'cidr',
    'vlan_id',
    'gateway',
    'available_ip_count',
    'pi_cloud_instance_id',
    'type',
    'used_ip_count',
    'used_ip_percent',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_network_name=dict(
        required=True,
        type='str'),
    cidr=dict(
        required=False,
        type='str'),
    vlan_id=dict(
        required=False,
        type='int'),
    gateway=dict(
        required=False,
        type='str'),
    available_ip_count=dict(
        required=False,
        type='float'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    used_ip_count=dict(
        required=False,
        type='float'),
    used_ip_percent=dict(
        required=False,
        type='float'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_pi_network',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.3',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
