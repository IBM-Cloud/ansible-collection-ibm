#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_share
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_share

short_description: Configure IBM Cloud 'ibm_is_share' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_share' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    resource_group:
        description:
            - The unique identifier of the resource group to use. If unspecified, the account's [default resourcegroup](https://cloud.ibm.com/apidocs/resource-manager#introduction) is used.
        required: False
        type: str
    replica_share:
        description:
            - Configuration for a replica file share to create and associate with this file share. Ifunspecified, a replica may be subsequently added by creating a new file share with a`source_share` referencing this file share.
        required: False
        type: list
        elements: dict
    access_tags:
        description:
            - List of access management tags
        required: False
        type: list
        elements: str
    allowed_transit_encryption_modes:
        description:
            - Allowed transit encryption modes
        required: False
        type: list
        elements: str
    replication_cron_spec:
        description:
            - The cron specification for the file share replication schedule.Replication of a share can be scheduled to occur at most once per hour.
        required: False
        type: str
    tags:
        description:
            - User Tags for the file share
        required: False
        type: list
        elements: str
    zone:
        description:
            - The globally unique name of the zone this file share will reside in.
        required: False
        type: str
    encryption_key:
        description:
            - The CRN of the key to use for encrypting this file share.If no encryption key is provided, the share will not be encrypted.
        required: False
        type: str
    profile:
        description:
            - The globally unique name for this share profile.
        required: False
        type: str
    source_share:
        description:
            - The ID of the source file share for this replica file share. The specified file share must not already have a replica, and must not be a replica.
        required: False
        type: str
    size:
        description:
            - The size of the file share rounded up to the next gigabyte.
        required: False
        type: int
    source_share_crn:
        description:
            - The CRN of the source file share for this replica file share. The specified file share must not already have a replica, and must not be a replica.
        required: False
        type: str
    initial_owner:
        description:
            - The owner assigned to the file share at creation.
        required: False
        type: list
        elements: dict
    access_control_mode:
        description:
            - The access control mode for the share:
        required: False
        type: str
    iops:
        description:
            - The maximum input/output operation performance bandwidth per second for the file share.
        required: False
        type: int
    name:
        description:
            - (Required for new resource) The unique user-defined name for this file share. If unspecified, the name will be a hyphenated list of randomly-selected words.
        required: True
        type: str
    mount_targets:
        description:
            - The share targets for this file share.Share targets mounted from a replica must be mounted read-only.
        required: False
        type: list
        elements: dict
    origin_share:
        description:
            - The origin share this accessor share is referring to.This property will be present when the `accessor_binding_role` is `accessor`.
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
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_group',
    'replica_share',
    'access_tags',
    'allowed_transit_encryption_modes',
    'replication_cron_spec',
    'tags',
    'zone',
    'encryption_key',
    'profile',
    'source_share',
    'size',
    'source_share_crn',
    'initial_owner',
    'access_control_mode',
    'iops',
    'name',
    'mount_targets',
    'origin_share',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'share',
]

TL_CONFLICTS_MAP = {
    'replica_share': ['source_share', 'origin_share.0.id', 'origin_share.0.crn'],
    'replication_cron_spec': ['replica_share', 'size', 'origin_share.0.id', 'origin_share.0.crn'],
    'source_share': ['replica_share', 'size', 'source_share_crn', 'origin_share.0.id', 'origin_share.0.crn'],
    'size': ['replication_cron_spec', 'source_share', 'source_share_crn', 'origin_share.0.id', 'origin_share.0.crn'],
    'source_share_crn': ['replica_share', 'size', 'source_share', 'origin_share.0.id', 'origin_share.0.crn'],
    'origin_share': ['replica_share', 'size', 'source_share', 'source_share_crn'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_group=dict(
        required=False,
        type='str'),
    replica_share=dict(
        required=False,
        elements='',
        type='list'),
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
    allowed_transit_encryption_modes=dict(
        required=False,
        elements='',
        type='list'),
    replication_cron_spec=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    zone=dict(
        required=False,
        type='str'),
    encryption_key=dict(
        required=False,
        type='str'),
    profile=dict(
        required=False,
        type='str'),
    source_share=dict(
        required=False,
        type='str'),
    size=dict(
        required=False,
        type='int'),
    source_share_crn=dict(
        required=False,
        type='str'),
    initial_owner=dict(
        required=False,
        elements='',
        type='list'),
    access_control_mode=dict(
        required=False,
        type='str'),
    iops=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    mount_targets=dict(
        required=False,
        elements='',
        type='list'),
    origin_share=dict(
        required=False,
        elements='',
        type='list'),
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
        resource_type='ibm_is_share',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_share',
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
