#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_image_info
short_description: Retrieve IBM Cloud 'ibm_pi_image' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_image' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    architecture:
        description:
            - None
        required: False
        type: str
    operatingsystem:
        description:
            - None
        required: False
        type: str
    hypervisor:
        description:
            - None
        required: False
        type: str
    pi_image_name:
        description:
            - Imagename Name to be used for pvminstances
        required: True
        type: str
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    state:
        description:
            - None
        required: False
        type: str
    size:
        description:
            - None
        required: False
        type: int
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
    ('pi_image_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'architecture',
    'operatingsystem',
    'hypervisor',
    'pi_image_name',
    'pi_cloud_instance_id',
    'state',
    'size',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    architecture=dict(
        required=False,
        type='str'),
    operatingsystem=dict(
        required=False,
        type='str'),
    hypervisor=dict(
        required=False,
        type='str'),
    pi_image_name=dict(
        required=True,
        type='str'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    state=dict(
        required=False,
        type='str'),
    size=dict(
        required=False,
        type='int'),
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
        resource_type='ibm_pi_image',
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
