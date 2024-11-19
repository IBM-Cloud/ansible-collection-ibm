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
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_proc_type:
        description:
            - Instance processor type
        required: False
        type: str
    pi_storage_pool_affinity:
        description:
            - Indicates if all volumes attached to the server must reside in the same storage pool
        required: False
        type: bool
        default: True
    pi_pin_policy:
        description:
            - Pin Policy of the instance
        required: False
        type: str
        default: none
    pi_image_id:
        description:
            - (Required for new resource) PI instance image id
        required: True
        type: str
    pi_replication_scheme:
        description:
            - Replication scheme
        required: False
        type: str
        default: suffix
    pi_virtual_optical_device:
        description:
            - Virtual Machine's Cloud Initialization Virtual Optical Device
        required: False
        type: str
    pi_anti_affinity_volumes:
        description:
            - List of volumes to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided
        required: False
        type: list
        elements: str
    pi_sap_profile_id:
        description:
            - SAP Profile ID for the amount of cores and memory
        required: False
        type: str
    pi_storage_pool:
        description:
            - Storage Pool for server deployment; if provided then pi_storage_pool_affinity will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage pool for a custom image (an imported image or an image that is created from a VM capture) defaults to the storage pool the image was created in
        required: False
        type: str
    pi_placement_group_id:
        description:
            - Placement group ID
        required: False
        type: str
    pi_deployment_type:
        description:
            - Custom Deployment Type Information
        required: False
        type: str
    pi_shared_processor_pool:
        description:
            - Shared Processor Pool the instance is deployed on
        required: False
        type: str
    pi_key_pair_name:
        description:
            - SSH key name
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) This is the Power Instance id that is assigned to the account
        required: True
        type: str
    pi_health_status:
        description:
            - Allow the user to set the status of the lpar so that they can connect to it faster
        required: False
        type: str
        default: OK
    pi_ibmi_css:
        description:
            - IBM i Cloud Storage Solution
        required: False
        type: bool
    pi_ibmi_pha:
        description:
            - IBM i Power High Availability
        required: False
        type: bool
    pi_replicants:
        description:
            - PI Instance replicas count
        required: False
        type: int
        default: 1
    pi_boot_volume_replication_enabled:
        description:
            - Indicates if the boot volume should be replication enabled or not.
        required: False
        type: bool
    pi_memory:
        description:
            - Memory size
        required: False
        type: float
    pi_processors:
        description:
            - Processors count
        required: False
        type: float
    pi_replication_sites:
        description:
            - Indicates the replication sites of the boot volume.
        required: False
        type: list
        elements: str
    pi_virtual_cores_assigned:
        description:
            - Virtual Cores Assigned to the PVMInstance
        required: False
        type: int
    pi_affinity_policy:
        description:
            - Affinity policy for pvm instance being created; ignored if pi_storage_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified
        required: False
        type: str
    pi_deployment_target:
        description:
            - The deployment of a dedicated host.
        required: False
        type: list
        elements: dict
    pi_network:
        description:
            - (Required for new resource) List of one or more networks to attach to the instance
        required: True
        type: list
        elements: dict
    pi_sys_type:
        description:
            - PI Instance system type
        required: False
        type: str
    pi_volume_ids:
        description:
            - List of PI volumes
        required: False
        type: list
        elements: str
    pi_anti_affinity_instances:
        description:
            - List of pvmInstances to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided
        required: False
        type: list
        elements: str
    pi_replication_policy:
        description:
            - Replication policy for the PI Instance
        required: False
        type: str
        default: none
    pi_user_tags:
        description:
            - The user tags attached to this resource.
        required: False
        type: list
        elements: str
    pi_user_data:
        description:
            - Base64 encoded data to be passed in for invoking a cloud init script
        required: False
        type: str
    pi_sap_deployment_type:
        description:
            - Custom SAP Deployment Type Information
        required: False
        type: str
    pi_storage_type:
        description:
            - Storage type for server deployment; if pi_storage_type is not provided the storage type will default to tier3
        required: False
        type: str
    pi_storage_connection:
        description:
            - Storage Connectivity Group for server deployment
        required: False
        type: str
    pi_affinity_volume:
        description:
            - Volume (ID or Name) to base storage affinity policy against; required if requesting affinity and pi_affinity_instance is not provided
        required: False
        type: str
    pi_ibmi_rds_users:
        description:
            - IBM i Rational Dev Studio Number of User Licenses
        required: False
        type: int
    pi_instance_name:
        description:
            - (Required for new resource) PI Instance name
        required: True
        type: str
    pi_affinity_instance:
        description:
            - PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and pi_affinity_volume is not provided
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
    ('pi_image_id', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_network', 'list'),
    ('pi_instance_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_proc_type',
    'pi_storage_pool_affinity',
    'pi_pin_policy',
    'pi_image_id',
    'pi_replication_scheme',
    'pi_virtual_optical_device',
    'pi_anti_affinity_volumes',
    'pi_sap_profile_id',
    'pi_storage_pool',
    'pi_placement_group_id',
    'pi_deployment_type',
    'pi_shared_processor_pool',
    'pi_key_pair_name',
    'pi_cloud_instance_id',
    'pi_health_status',
    'pi_ibmi_css',
    'pi_ibmi_pha',
    'pi_replicants',
    'pi_boot_volume_replication_enabled',
    'pi_memory',
    'pi_processors',
    'pi_replication_sites',
    'pi_virtual_cores_assigned',
    'pi_affinity_policy',
    'pi_deployment_target',
    'pi_network',
    'pi_sys_type',
    'pi_volume_ids',
    'pi_anti_affinity_instances',
    'pi_replication_policy',
    'pi_user_tags',
    'pi_user_data',
    'pi_sap_deployment_type',
    'pi_storage_type',
    'pi_storage_connection',
    'pi_affinity_volume',
    'pi_ibmi_rds_users',
    'pi_instance_name',
    'pi_affinity_instance',
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
    'pi_proc_type': ['pi_sap_profile_id'],
    'pi_anti_affinity_volumes': ['pi_anti_affinity_instances'],
    'pi_sap_profile_id': ['pi_processors', 'pi_memory', 'pi_proc_type'],
    'pi_shared_processor_pool': ['pi_sap_profile_id'],
    'pi_memory': ['pi_sap_profile_id'],
    'pi_processors': ['pi_sap_profile_id'],
    'pi_anti_affinity_instances': ['pi_anti_affinity_volumes'],
    'pi_affinity_volume': ['pi_affinity_instance'],
    'pi_affinity_instance': ['pi_affinity_volume'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_proc_type=dict(
        required=False,
        type='str'),
    pi_storage_pool_affinity=dict(
        required=False,
        type='bool'),
    pi_pin_policy=dict(
        required=False,
        type='str'),
    pi_image_id=dict(
        required=False,
        type='str'),
    pi_replication_scheme=dict(
        required=False,
        type='str'),
    pi_virtual_optical_device=dict(
        required=False,
        type='str'),
    pi_anti_affinity_volumes=dict(
        required=False,
        elements='',
        type='list'),
    pi_sap_profile_id=dict(
        required=False,
        type='str'),
    pi_storage_pool=dict(
        required=False,
        type='str'),
    pi_placement_group_id=dict(
        required=False,
        type='str'),
    pi_deployment_type=dict(
        required=False,
        type='str'),
    pi_shared_processor_pool=dict(
        required=False,
        type='str'),
    pi_key_pair_name=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_health_status=dict(
        required=False,
        type='str'),
    pi_ibmi_css=dict(
        required=False,
        type='bool'),
    pi_ibmi_pha=dict(
        required=False,
        type='bool'),
    pi_replicants=dict(
        required=False,
        type='int'),
    pi_boot_volume_replication_enabled=dict(
        required=False,
        type='bool'),
    pi_memory=dict(
        required=False,
        type='float'),
    pi_processors=dict(
        required=False,
        type='float'),
    pi_replication_sites=dict(
        required=False,
        elements='',
        type='list'),
    pi_virtual_cores_assigned=dict(
        required=False,
        type='int'),
    pi_affinity_policy=dict(
        required=False,
        type='str'),
    pi_deployment_target=dict(
        required=False,
        elements='',
        type='list'),
    pi_network=dict(
        required=False,
        elements='',
        type='list'),
    pi_sys_type=dict(
        required=False,
        type='str'),
    pi_volume_ids=dict(
        required=False,
        elements='',
        type='list'),
    pi_anti_affinity_instances=dict(
        required=False,
        elements='',
        type='list'),
    pi_replication_policy=dict(
        required=False,
        type='str'),
    pi_user_tags=dict(
        required=False,
        elements='',
        type='list'),
    pi_user_data=dict(
        required=False,
        type='str'),
    pi_sap_deployment_type=dict(
        required=False,
        type='str'),
    pi_storage_type=dict(
        required=False,
        type='str'),
    pi_storage_connection=dict(
        required=False,
        type='str'),
    pi_affinity_volume=dict(
        required=False,
        type='str'),
    pi_ibmi_rds_users=dict(
        required=False,
        type='int'),
    pi_instance_name=dict(
        required=False,
        type='str'),
    pi_affinity_instance=dict(
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
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_instance',
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
