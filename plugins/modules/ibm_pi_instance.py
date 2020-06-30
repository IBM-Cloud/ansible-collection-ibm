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
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    pi_replication_policy:
        description:
            - Replication policy for the PI INstance
        required: False
        type: str
        default: none
    pi_instance_name:
        description:
            - (Required for new resource) PI Instance name
        required: True
        type: str
    pi_memory:
        description:
            - (Required for new resource) Memory size
        required: True
        type: float
    pi_sys_type:
        description:
            - (Required for new resource) PI Instance system type
        required: True
        type: str
    status:
        description:
            - PI instance status
        required: False
        type: str
    min_memory:
        description:
            - Minimum memory
        required: False
        type: float
    max_memory:
        description:
            - Maximum memory size
        required: False
        type: float
    pi_processors:
        description:
            - (Required for new resource) Processors count
        required: True
        type: float
    pi_user_data:
        description:
            - Base64 encoded data to be passed in for invoking a cloud init script
        required: False
        type: str
    instance_id:
        description:
            - Instance ID
        required: False
        type: str
    pin_policy:
        description:
            - PIN Policy of the Instance
        required: False
        type: str
    health_status:
        description:
            - PI Instance health status
        required: False
        type: str
    migratable:
        description:
            - set to true to enable migration of the PI instance
        required: False
        type: bool
    min_processors:
        description:
            - Minimum number of the CPUs
        required: False
        type: float
    pi_image_id:
        description:
            - (Required for new resource) PI instance image name
        required: True
        type: str
    pi_replicants:
        description:
            - PI Instance repicas count
        required: False
        type: float
        default: 1
    pi_network_ids:
        description:
            - (Required for new resource) Set of Networks that have been configured for the account
        required: True
        type: list
        elements: str
    pi_volume_ids:
        description:
            - List of PI volumes
        required: False
        type: list
        elements: str
    pi_pin_policy:
        description:
            - Pin Policy of the instance
        required: False
        type: str
        default: none
    reboot_for_resource_change:
        description:
            - Flag to be passed for CPU/Memory changes that require a reboot to take effect
        required: False
        type: str
    pi_key_pair_name:
        description:
            - (Required for new resource) SSH key name
        required: True
        type: str
    pi_progress:
        description:
            - Progress of the operation
        required: False
        type: float
    pi_cloud_instance_id:
        description:
            - (Required for new resource) This is the Power Instance id that is assigned to the account
        required: True
        type: str
    pi_proc_type:
        description:
            - (Required for new resource) Instance processor type
        required: True
        type: str
    pi_replication_scheme:
        description:
            - Replication scheme
        required: False
        type: str
        default: suffix
    max_processors:
        description:
            - Maximum number of processors
        required: False
        type: float
    addresses:
        description:
            - None
        required: False
        type: list
        elements: dict
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
    ('pi_instance_name', 'str'),
    ('pi_memory', 'float'),
    ('pi_sys_type', 'str'),
    ('pi_processors', 'float'),
    ('pi_image_id', 'str'),
    ('pi_network_ids', 'list'),
    ('pi_key_pair_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_proc_type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_replication_policy',
    'pi_instance_name',
    'pi_memory',
    'pi_sys_type',
    'status',
    'min_memory',
    'max_memory',
    'pi_processors',
    'pi_user_data',
    'instance_id',
    'pin_policy',
    'health_status',
    'migratable',
    'min_processors',
    'pi_image_id',
    'pi_replicants',
    'pi_network_ids',
    'pi_volume_ids',
    'pi_pin_policy',
    'reboot_for_resource_change',
    'pi_key_pair_name',
    'pi_progress',
    'pi_cloud_instance_id',
    'pi_proc_type',
    'pi_replication_scheme',
    'max_processors',
    'addresses',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_replication_policy=dict(
        default='none',
        type='str'),
    pi_instance_name=dict(
        required='True',
        type='str'),
    pi_memory=dict(
        required='True',
        type='float'),
    pi_sys_type=dict(
        required='True',
        type='str'),
    status=dict(
        required='False',
        type='str'),
    min_memory=dict(
        required='False',
        type='float'),
    max_memory=dict(
        required='False',
        type='float'),
    pi_processors=dict(
        required='True',
        type='float'),
    pi_user_data=dict(
        required='False',
        type='str'),
    instance_id=dict(
        required='False',
        type='str'),
    pin_policy=dict(
        required='False',
        type='str'),
    health_status=dict(
        required='False',
        type='str'),
    migratable=dict(
        required='False',
        type='bool'),
    min_processors=dict(
        required='False',
        type='float'),
    pi_image_id=dict(
        required='True',
        type='str'),
    pi_replicants=dict(
        default=1,
        type='float'),
    pi_network_ids=dict(
        required='True',
        elements='',
        type='list'),
    pi_volume_ids=dict(
        required='False',
        elements='',
        type='list'),
    pi_pin_policy=dict(
        default='none',
        type='str'),
    reboot_for_resource_change=dict(
        required='False',
        type='str'),
    pi_key_pair_name=dict(
        required='True',
        type='str'),
    pi_progress=dict(
        required='False',
        type='float'),
    pi_cloud_instance_id=dict(
        required='True',
        type='str'),
    pi_proc_type=dict(
        required='True',
        type='str'),
    pi_replication_scheme=dict(
        default='suffix',
        type='str'),
    max_processors=dict(
        required='False',
        type='float'),
    addresses=dict(
        required='False',
        elements='',
        type='list'),
    id=dict(
        required='False',
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
        resource_type='ibm_pi_instance',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.8.1',
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
