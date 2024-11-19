#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_instance_volume_attachment
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_volume_attachment

short_description: Configure IBM Cloud 'ibm_is_instance_volume_attachment' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_instance_volume_attachment' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    tags:
        description:
            - UserTags for the volume instance
        required: False
        type: list
        elements: str
    snapshot_crn:
        description:
            - The snapshot crn of the volume to be attached
        required: False
        type: str
    delete_volume_on_instance_delete:
        description:
            - If set to true, when deleting the instance the volume will also be deleted.
        required: False
        type: bool
    volume:
        description:
            - Instance id
        required: False
        type: str
    encryption_key:
        description:
            - The CRN of the [Key Protect Root Key](https://cloud.ibm.com/docs/key-protect?topic=key-protect-getting-started-tutorial) or [Hyper Protect Crypto Service Root Key](https://cloud.ibm.com/docs/hs-crypto?topic=hs-crypto-get-started) for this resource.
        required: False
        type: str
    instance:
        description:
            - (Required for new resource) Instance id
        required: True
        type: str
    delete_volume_on_attachment_delete:
        description:
            - If set to true, when deleting the attachment, the volume will also be deleted. Default value for this true.
        required: False
        type: bool
        default: True
    profile:
        description:
            - The  globally unique name for the volume profile to use for this volume.
        required: False
        type: str
    snapshot:
        description:
            - The snapshot ID of the volume to be attached
        required: False
        type: str
    name:
        description:
            - The user-defined name for this volume attachment.
        required: False
        type: str
    iops:
        description:
            - The maximum I/O operations per second (IOPS) for the volume.
        required: False
        type: int
    volume_name:
        description:
            - The unique user-defined name for this volume
        required: False
        type: str
    capacity:
        description:
            - The capacity of the volume in gigabytes. The specified minimum and maximum capacity values for creating or updating volumes may expand in the future.
        required: False
        type: int
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
    ('instance', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tags',
    'snapshot_crn',
    'delete_volume_on_instance_delete',
    'volume',
    'encryption_key',
    'instance',
    'delete_volume_on_attachment_delete',
    'profile',
    'snapshot',
    'name',
    'iops',
    'volume_name',
    'capacity',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance', 'str'),
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'instance',
    'name',
]

TL_CONFLICTS_MAP = {
    'tags': ['volume'],
    'snapshot_crn': ['volume', 'snapshot'],
    'volume': ['iops', 'volume_name', 'profile', 'capacity', 'snapshot', 'tags'],
    'profile': ['volume'],
    'snapshot': ['volume', 'snapshot_crn'],
    'iops': ['volume'],
    'capacity': ['volume'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tags=dict(
        required=False,
        elements='',
        type='list'),
    snapshot_crn=dict(
        required=False,
        type='str'),
    delete_volume_on_instance_delete=dict(
        required=False,
        type='bool'),
    volume=dict(
        required=False,
        type='str'),
    encryption_key=dict(
        required=False,
        type='str'),
    instance=dict(
        required=False,
        type='str'),
    delete_volume_on_attachment_delete=dict(
        required=False,
        type='bool'),
    profile=dict(
        required=False,
        type='str'),
    snapshot=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    iops=dict(
        required=False,
        type='int'),
    volume_name=dict(
        required=False,
        type='str'),
    capacity=dict(
        required=False,
        type='int'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
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

    if 'generation' in module.params:
        # VPC required arguments checks
        if module.params['generation'] == 1:
            missing_args = []
            if module.params['iaas_classic_username'] is None:
                missing_args.append('iaas_classic_username')
            if module.params['iaas_classic_api_key'] is None:
                missing_args.append('iaas_classic_api_key')
            if missing_args:
                module.fail_json(msg=(
                    "VPC generation=1 missing required arguments: " +
                    ", ".join(missing_args)))
        elif module.params['generation'] == 2:
            if module.params['ibmcloud_api_key'] is None:
                module.fail_json(
                    msg=("VPC generation=2 missing required argument: "
                         "ibmcloud_api_key"))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_instance_volume_attachment',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_instance_volume_attachment',
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
