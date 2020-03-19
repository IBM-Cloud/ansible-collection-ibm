#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_operations
short_description: Configure IBM Cloud 'ibm_pi_operations' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_operations' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.5
    - Terraform v0.12.20

options:
    pi_cloud_instance_id:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_status:
        description:
            - None
        required: False
        type: str
    pi_instance_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    addresses:
        description:
            - None
        required: False
        type: list
        elements: dict
    pi_health_status:
        description:
            - None
        required: False
        type: str
    pi_operation:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_progress:
        description:
            - Progress of the operation
        required: False
        type: float
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
    ('pi_operation', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_cloud_instance_id',
    'pi_status',
    'pi_instance_name',
    'addresses',
    'pi_health_status',
    'pi_operation',
    'pi_progress',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_status=dict(
        required=False,
        type='str'),
    pi_instance_name=dict(
        required=False,
        type='str'),
    addresses=dict(
        required=False,
        elements='',
        type='list'),
    pi_health_status=dict(
        required=False,
        type='str'),
    pi_operation=dict(
        required=False,
        type='str'),
    pi_progress=dict(
        required=False,
        type='float'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_pi_operations',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.5',
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
