#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_instance_info
short_description: Retrieve IBM Cloud 'ibm_pi_instance' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.6
    - Terraform v0.12.20

options:
    status:
        description:
            - None
        required: False
        type: str
    minproc:
        description:
            - None
        required: False
        type: int
    maxproc:
        description:
            - None
        required: False
        type: int
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    volumes:
        description:
            - None
        required: False
        type: list
        elements: str
    state:
        description:
            - None
        required: False
        type: str
    processors:
        description:
            - None
        required: False
        type: int
    proctype:
        description:
            - None
        required: False
        type: str
    maxmem:
        description:
            - None
        required: False
        type: int
    pi_instance_name:
        description:
            - Server Name to be used for pvminstances
        required: True
        type: str
    health_status:
        description:
            - None
        required: False
        type: str
    addresses:
        description:
            - None
        required: False
        type: list
        elements: dict
    minmem:
        description:
            - None
        required: False
        type: int
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('pi_cloud_instance_id', 'str'),
    ('pi_instance_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'status',
    'minproc',
    'maxproc',
    'pi_cloud_instance_id',
    'volumes',
    'state',
    'processors',
    'proctype',
    'maxmem',
    'pi_instance_name',
    'health_status',
    'addresses',
    'minmem',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    status=dict(
        required=False,
        type='str'),
    minproc=dict(
        required=False,
        type='int'),
    maxproc=dict(
        required=False,
        type='int'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    volumes=dict(
        required=False,
        elements='',
        type='list'),
    state=dict(
        required=False,
        type='str'),
    processors=dict(
        required=False,
        type='int'),
    proctype=dict(
        required=False,
        type='str'),
    maxmem=dict(
        required=False,
        type='int'),
    pi_instance_name=dict(
        required=True,
        type='str'),
    health_status=dict(
        required=False,
        type='str'),
    addresses=dict(
        required=False,
        elements='',
        type='list'),
    minmem=dict(
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
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_pi_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.6',
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
