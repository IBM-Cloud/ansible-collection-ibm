#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_instance
short_description: Configure IBM Cloud 'ibm_pi_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    pi_user_data:
        description:
            - Base64 encoded data to be passed in for invoking a cloud init script
        required: False
        type: str
    pi_image_id:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_processors:
        description:
            - (Required for new resource) 
        required: False
        type: float
    pi_key_pair_name:
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
    health_status:
        description:
            - None
        required: False
        type: str
    instance_id:
        description:
            - None
        required: False
        type: str
    pi_memory:
        description:
            - (Required for new resource) 
        required: False
        type: float
    pi_replicants:
        description:
            - None
        required: False
        type: float
        default: 1
    pi_replication_policy:
        description:
            - None
        required: False
        type: str
        default: none
    pi_proc_type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) This is the Power Instance id that is assigned to the account
        required: False
        type: str
    status:
        description:
            - None
        required: False
        type: str
    migratable:
        description:
            - None
        required: False
        type: bool
    min_processors:
        description:
            - None
        required: False
        type: float
    pi_network_ids:
        description:
            - (Required for new resource) Set of Networks that have been configured for the account
        required: False
        type: list
        elements: str
    pi_volume_ids:
        description:
            - None
        required: False
        type: list
        elements: str
    pi_instance_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_sys_type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    pi_replication_scheme:
        description:
            - None
        required: False
        type: str
        default: suffix
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
    ('pi_image_id', 'str'),
    ('pi_processors', 'float'),
    ('pi_key_pair_name', 'str'),
    ('pi_memory', 'float'),
    ('pi_proc_type', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_network_ids', 'list'),
    ('pi_instance_name', 'str'),
    ('pi_sys_type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_user_data',
    'pi_image_id',
    'pi_processors',
    'pi_key_pair_name',
    'addresses',
    'health_status',
    'instance_id',
    'pi_memory',
    'pi_replicants',
    'pi_replication_policy',
    'pi_proc_type',
    'pi_cloud_instance_id',
    'status',
    'migratable',
    'min_processors',
    'pi_network_ids',
    'pi_volume_ids',
    'pi_instance_name',
    'pi_sys_type',
    'pi_replication_scheme',
    'pi_progress',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_user_data=dict(
        required=False,
        type='str'),
    pi_image_id=dict(
        required=False,
        type='str'),
    pi_processors=dict(
        required=False,
        type='float'),
    pi_key_pair_name=dict(
        required=False,
        type='str'),
    addresses=dict(
        required=False,
        elements='',
        type='list'),
    health_status=dict(
        required=False,
        type='str'),
    instance_id=dict(
        required=False,
        type='str'),
    pi_memory=dict(
        required=False,
        type='float'),
    pi_replicants=dict(
        default=1,
        type='float'),
    pi_replication_policy=dict(
        default='none',
        type='str'),
    pi_proc_type=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    migratable=dict(
        required=False,
        type='bool'),
    min_processors=dict(
        required=False,
        type='float'),
    pi_network_ids=dict(
        required=False,
        elements='',
        type='list'),
    pi_volume_ids=dict(
        required=False,
        elements='',
        type='list'),
    pi_instance_name=dict(
        required=False,
        type='str'),
    pi_sys_type=dict(
        required=False,
        type='str'),
    pi_replication_scheme=dict(
        default='suffix',
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
        resource_type='ibm_pi_instance',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.4',
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
