#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_image
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_image

short_description: Configure IBM Cloud 'ibm_pi_image' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_image' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_affinity_policy:
        description:
            - Affinity policy for image; ignored if pi_image_storage_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified
        required: False
        type: str
    pi_affinity_volume:
        description:
            - Volume (ID or Name) to base storage affinity policy against; required if requesting affinity and pi_affinity_instance is not provided
        required: False
        type: str
    pi_anti_affinity_volumes:
        description:
            - List of volumes to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided
        required: False
        type: list
        elements: str
    pi_user_tags:
        description:
            - The user tags attached to this resource.
        required: False
        type: list
        elements: str
    pi_image_secret_key:
        description:
            - Cloud Object Storage secret key; required for buckets with private access
        required: False
        type: str
    pi_image_bucket_region:
        description:
            - Cloud Object Storage region
        required: False
        type: str
    pi_image_storage_pool:
        description:
            - Storage pool where the image will be loaded, if provided then pi_affinity_policy will be ignored
        required: False
        type: str
    pi_affinity_instance:
        description:
            - PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and pi_affinity_volume is not provided
        required: False
        type: str
    pi_image_storage_type:
        description:
            - Type of storage; If not specified, default is tier3
        required: False
        type: str
    pi_image_name:
        description:
            - (Required for new resource) Image name
        required: True
        type: str
    pi_image_id:
        description:
            - Instance image id
        required: False
        type: str
    pi_image_access_key:
        description:
            - Cloud Object Storage access key; required for buckets with private access
        required: False
        type: str
    pi_image_bucket_file_name:
        description:
            - Cloud Object Storage image filename
        required: False
        type: str
    pi_anti_affinity_instances:
        description:
            - List of pvmInstances to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided
        required: False
        type: list
        elements: str
    pi_image_import_details:
        description:
            - None
        required: False
        type: list
        elements: dict
    pi_cloud_instance_id:
        description:
            - (Required for new resource) PI cloud instance ID
        required: True
        type: str
    pi_image_bucket_name:
        description:
            - Cloud Object Storage bucket name; bucket-name[/optional/folder]
        required: False
        type: str
    pi_image_bucket_access:
        description:
            - Indicates if the bucket has public or private access
        required: False
        type: str
        default: public
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
    ('pi_image_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_affinity_policy',
    'pi_affinity_volume',
    'pi_anti_affinity_volumes',
    'pi_user_tags',
    'pi_image_secret_key',
    'pi_image_bucket_region',
    'pi_image_storage_pool',
    'pi_affinity_instance',
    'pi_image_storage_type',
    'pi_image_name',
    'pi_image_id',
    'pi_image_access_key',
    'pi_image_bucket_file_name',
    'pi_anti_affinity_instances',
    'pi_image_import_details',
    'pi_cloud_instance_id',
    'pi_image_bucket_name',
    'pi_image_bucket_access',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('pi_cloud_instance_id', 'str'),
    ('pi_image_name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'pi_cloud_instance_id',
    'pi_image_name',
]

TL_CONFLICTS_MAP = {
    'pi_affinity_volume': ['pi_affinity_instance'],
    'pi_anti_affinity_volumes': ['pi_anti_affinity_instances'],
    'pi_image_bucket_region': ['pi_image_id'],
    'pi_affinity_instance': ['pi_affinity_volume'],
    'pi_image_id': ['pi_image_bucket_name'],
    'pi_image_bucket_file_name': ['pi_image_id'],
    'pi_anti_affinity_instances': ['pi_anti_affinity_volumes'],
    'pi_image_bucket_name': ['pi_image_id'],
    'pi_image_bucket_access': ['pi_image_id'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_affinity_policy=dict(
        required=False,
        type='str'),
    pi_affinity_volume=dict(
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
    pi_image_secret_key=dict(
        required=False,
        type='str'),
    pi_image_bucket_region=dict(
        required=False,
        type='str'),
    pi_image_storage_pool=dict(
        required=False,
        type='str'),
    pi_affinity_instance=dict(
        required=False,
        type='str'),
    pi_image_storage_type=dict(
        required=False,
        type='str'),
    pi_image_name=dict(
        required=False,
        type='str'),
    pi_image_id=dict(
        required=False,
        type='str'),
    pi_image_access_key=dict(
        required=False,
        type='str'),
    pi_image_bucket_file_name=dict(
        required=False,
        type='str'),
    pi_anti_affinity_instances=dict(
        required=False,
        elements='',
        type='list'),
    pi_image_import_details=dict(
        required=False,
        elements='',
        type='list'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_image_bucket_name=dict(
        required=False,
        type='str'),
    pi_image_bucket_access=dict(
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
        resource_type='ibm_pi_image',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_image',
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
