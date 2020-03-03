#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_ssh_key_info
short_description: Retrieve IBM Cloud 'ibm_compute_ssh_key' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_compute_ssh_key' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    most_recent:
        description:
            - If true and multiple entries are found, the most recently created key is used. If false, an error is returned
        required: False
        type: bool
        default: False
    label:
        description:
            - The label associated with the ssh key
        required: True
        type: str
    public_key:
        description:
            - The public ssh key
        required: False
        type: str
    fingerprint:
        description:
            - A sequence of bytes to authenticate or lookup a longer ssh key
        required: False
        type: str
    notes:
        description:
            - A small note about a ssh key to use at your discretion
        required: False
        type: str
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
    ('label', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'most_recent',
    'label',
    'public_key',
    'fingerprint',
    'notes',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    most_recent=dict(
        default=False,
        type='bool'),
    label=dict(
        required=True,
        type='str'),
    public_key=dict(
        required=False,
        type='str'),
    fingerprint=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
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
        resource_type='ibm_compute_ssh_key',
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
