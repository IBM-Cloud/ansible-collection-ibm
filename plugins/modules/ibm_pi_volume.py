#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_volume
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_volume

short_description: Configure IBM Cloud 'ibm_pi_volume' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_volume' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_affinity_volume:
        description:
            - Volume (ID or Name) to base volume affinity policy against; required if requesting 'affinity' and 'pi_affinity_instance' is not provided.
        required: False
        type: str
    pi_anti_affinity_instances:
        description:
            - List of pvmInstances to base volume anti-affinity policy against; required if requesting 'anti-affinity' and 'pi_anti_affinity_volumes' is not provided.
        required: False
        type: list
        elements: str
    pi_volume_pool:
        description:
            - Volume pool where the volume will be created; if provided then 'pi_affinity_policy' values will be ignored.
        required: False
        type: str
    pi_volume_type:
        description:
            - Type of disk, if diskType is not provided the disk type will default to 'tier3'
        required: False
        type: str
    pi_replication_sites:
        description:
            - List of replication sites for volume replication.
        required: False
        type: list
        elements: str
    pi_volume_name:
        description:
            - (Required for new resource) The name of the volume.
        required: True
        type: str
    pi_volume_shareable:
        description:
            - If set to true, the volume can be shared across Power Systems Virtual Server instances. If set to false, you can attach it only to one instance.
        required: False
        type: bool
    pi_cloud_instance_id:
        description:
            - (Required for new resource) The GUID of the service instance associated with an account.
        required: True
        type: str
    pi_replication_enabled:
        description:
            - Indicates if the volume should be replication enabled or not.
        required: False
        type: bool
    pi_affinity_policy:
        description:
            - Affinity policy for data volume being created; ignored if 'pi_volume_pool' provided; for policy 'affinity' requires one of 'pi_affinity_instance' or 'pi_affinity_volume' to be specified; for policy 'anti-affinity' requires one of 'pi_anti_affinity_instances' or 'pi_anti_affinity_volumes' to be specified; Allowable values: 'affinity', 'anti-affinity'.
        required: False
        type: str
    pi_anti_affinity_volumes:
        description:
            - List of volumes to base volume anti-affinity policy against; required if requesting 'anti-affinity' and 'pi_anti_affinity_instances' is not provided.
        required: False
        type: list
        elements: str
    pi_user_tags:
        description:
            - The user tags attached to this resource.
        required: False
        type: list
        elements: str
    pi_volume_size:
        description:
            - (Required for new resource) The size of the volume in GB.
        required: True
        type: float
    pi_affinity_instance:
        description:
            - PVM Instance (ID or Name) to base volume affinity policy against; required if requesting 'affinity' and 'pi_affinity_volume' is not provided.
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
    ('pi_volume_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_volume_size', 'float'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_affinity_volume',
    'pi_anti_affinity_instances',
    'pi_volume_pool',
    'pi_volume_type',
    'pi_replication_sites',
    'pi_volume_name',
    'pi_volume_shareable',
    'pi_cloud_instance_id',
    'pi_replication_enabled',
    'pi_affinity_policy',
    'pi_anti_affinity_volumes',
    'pi_user_tags',
    'pi_volume_size',
    'pi_affinity_instance',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('pi_cloud_instance_id', 'str'),
    ('pi_volume_name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'pi_cloud_instance_id',
    'pi_volume_name',
]

TL_CONFLICTS_MAP = {
    'pi_affinity_volume': ['pi_affinity_instance'],
    'pi_anti_affinity_instances': ['pi_anti_affinity_volumes'],
    'pi_anti_affinity_volumes': ['pi_anti_affinity_instances'],
    'pi_affinity_instance': ['pi_affinity_volume'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_affinity_volume=dict(
        required=False,
        type='str'),
    pi_anti_affinity_instances=dict(
        required=False,
        elements='',
        type='list'),
    pi_volume_pool=dict(
        required=False,
        type='str'),
    pi_volume_type=dict(
        required=False,
        type='str'),
    pi_replication_sites=dict(
        required=False,
        elements='',
        type='list'),
    pi_volume_name=dict(
        required=False,
        type='str'),
    pi_volume_shareable=dict(
        required=False,
        type='bool'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_replication_enabled=dict(
        required=False,
        type='bool'),
    pi_affinity_policy=dict(
        required=False,
        type='str'),
    pi_anti_affinity_volumes=dict(
        required=False,
        elements='',
        type='list'),
    pi_user_tags=dict(
        required=False,
        elements='',
        type='list'),
    pi_volume_size=dict(
        required=False,
        type='float'),
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
        resource_type='ibm_pi_volume',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_volume',
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
