#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_instance
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_instance

short_description: Configure IBM Cloud 'ibm_pi_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_instance' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.35.0
    - Terraform v0.12.20

options:
    pi_replication_scheme:
        description:
            - Replication scheme
        required: False
        type: str
        default: suffix
    pi_image_id:
        description:
            - (Required for new resource) PI instance image name
        required: True
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) This is the Power Instance id that is assigned to the account
        required: True
        type: str
    pi_migratable:
        description:
            - set to true to enable migration of the PI instance
        required: False
        type: bool
    pi_volume_ids:
        description:
            - List of PI volumes
        required: False
        type: list
        elements: str
    pi_storage_connection:
        description:
            - Storage Connectivity Group for server deployment
        required: False
        type: str
    pi_storage_type:
        description:
            - Storage type for server deployment
        required: False
        type: str
    pi_replicants:
        description:
            - PI Instance replicas count
        required: False
        type: float
        default: 1
    pi_replication_policy:
        description:
            - Replication policy for the PI Instance
        required: False
        type: str
        default: none
    pi_processors:
        description:
            - (Required for new resource) Processors count
        required: True
        type: float
    pi_virtual_cores_assigned:
        description:
            - Virtual Cores Assigned to the PVMInstance
        required: False
        type: int
    pi_network:
        description:
            - List of one or more networks to attach to the instance
        required: False
        type: list
        elements: dict
    pi_key_pair_name:
        description:
            - (Required for new resource) SSH key name
        required: True
        type: str
    pi_health_status:
        description:
            - Allow the user to set the status of the lpar so that they can connect to it faster
        required: False
        type: str
        default: OK
    pi_user_data:
        description:
            - Base64 encoded data to be passed in for invoking a cloud init script
        required: False
        type: str
    pi_pin_policy:
        description:
            - Pin Policy of the instance
        required: False
        type: str
        default: none
    pi_proc_type:
        description:
            - (Required for new resource) Instance processor type
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
    pi_instance_name:
        description:
            - (Required for new resource) PI Instance name
        required: True
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
    ('pi_image_id', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_processors', 'float'),
    ('pi_key_pair_name', 'str'),
    ('pi_proc_type', 'str'),
    ('pi_memory', 'float'),
    ('pi_sys_type', 'str'),
    ('pi_instance_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_replication_scheme',
    'pi_image_id',
    'pi_cloud_instance_id',
    'pi_migratable',
    'pi_volume_ids',
    'pi_storage_connection',
    'pi_storage_type',
    'pi_replicants',
    'pi_replication_policy',
    'pi_processors',
    'pi_virtual_cores_assigned',
    'pi_network',
    'pi_key_pair_name',
    'pi_health_status',
    'pi_user_data',
    'pi_pin_policy',
    'pi_proc_type',
    'pi_memory',
    'pi_sys_type',
    'pi_instance_name',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('pi_instance_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'pi_instance_name',
    'pi_cloud_instance_id',
]

TL_CONFLICTS_MAP = {
    'pi_network': ['pi_network_ids'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_replication_scheme=dict(
        required=False,
        type='str'),
    pi_image_id=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_migratable=dict(
        required=False,
        type='bool'),
    pi_volume_ids=dict(
        required=False,
        elements='',
        type='list'),
    pi_storage_connection=dict(
        required=False,
        type='str'),
    pi_storage_type=dict(
        required=False,
        type='str'),
    pi_replicants=dict(
        required=False,
        type='float'),
    pi_replication_policy=dict(
        required=False,
        type='str'),
    pi_processors=dict(
        required=False,
        type='float'),
    pi_virtual_cores_assigned=dict(
        required=False,
        type='int'),
    pi_network=dict(
        required=False,
        elements='',
        type='list'),
    pi_key_pair_name=dict(
        required=False,
        type='str'),
    pi_health_status=dict(
        required=False,
        type='str'),
    pi_user_data=dict(
        required=False,
        type='str'),
    pi_pin_policy=dict(
        required=False,
        type='str'),
    pi_proc_type=dict(
        required=False,
        type='str'),
    pi_memory=dict(
        required=False,
        type='float'),
    pi_sys_type=dict(
        required=False,
        type='str'),
    pi_instance_name=dict(
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
        resource_type='ibm_pi_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.35.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.35.0',
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
