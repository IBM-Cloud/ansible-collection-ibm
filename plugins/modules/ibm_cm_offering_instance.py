#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cm_offering_instance
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_offering_instance

short_description: Configure IBM Cloud 'ibm_cm_offering_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cm_offering_instance' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    label:
        description:
            - (Required for new resource) the label for this instance.
        required: True
        type: str
    cluster_namespaces:
        description:
            - (Required for new resource) List of target namespaces to install into.
        required: True
        type: list
        elements: str
    cluster_all_namespaces:
        description:
            - (Required for new resource) designate to install into all namespaces.
        required: True
        type: bool
    channel:
        description:
            - channel to target for the operator subscription. Required for operator bundles
        required: False
        type: str
    parent_crn:
        description:
            - CRN of parent instance
        required: False
        type: str
    wait_until_successful:
        description:
            - Whether to wait until the offering instance successfully provisions, or to return when accepted
        required: False
        type: bool
        default: True
    kind_format:
        description:
            - (Required for new resource) the format this instance has (helm, operator, ova...).
        required: True
        type: str
    version:
        description:
            - (Required for new resource) The version this instance was installed from (not version id).
        required: True
        type: str
    cluster_region:
        description:
            - (Required for new resource) Cluster region (e.g., us-south).
        required: True
        type: str
    plan_id:
        description:
            - id of the plan
        required: False
        type: str
    catalog_id:
        description:
            - (Required for new resource) Catalog ID this instance was created from.
        required: True
        type: str
    resource_group_id:
        description:
            - id of the resource group
        required: False
        type: str
    offering_id:
        description:
            - (Required for new resource) Offering ID this instance was created from.
        required: True
        type: str
    cluster_id:
        description:
            - (Required for new resource) Cluster ID.
        required: True
        type: str
    install_plan:
        description:
            - install plan for the subscription of the operator- can be either automatic or manual. Required for operator bundles
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
    iaas_classic_username:
        description:
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
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
    ('label', 'str'),
    ('cluster_namespaces', 'list'),
    ('cluster_all_namespaces', 'bool'),
    ('kind_format', 'str'),
    ('version', 'str'),
    ('cluster_region', 'str'),
    ('catalog_id', 'str'),
    ('offering_id', 'str'),
    ('cluster_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'label',
    'cluster_namespaces',
    'cluster_all_namespaces',
    'channel',
    'parent_crn',
    'wait_until_successful',
    'kind_format',
    'version',
    'cluster_region',
    'plan_id',
    'catalog_id',
    'resource_group_id',
    'offering_id',
    'cluster_id',
    'install_plan',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_identifier', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'instance_identifier',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    label=dict(
        required=False,
        type='str'),
    cluster_namespaces=dict(
        required=False,
        elements='',
        type='list'),
    cluster_all_namespaces=dict(
        required=False,
        type='bool'),
    channel=dict(
        required=False,
        type='str'),
    parent_crn=dict(
        required=False,
        type='str'),
    wait_until_successful=dict(
        required=False,
        type='bool'),
    kind_format=dict(
        required=False,
        type='str'),
    version=dict(
        required=False,
        type='str'),
    cluster_region=dict(
        required=False,
        type='str'),
    plan_id=dict(
        required=False,
        type='str'),
    catalog_id=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    offering_id=dict(
        required=False,
        type='str'),
    cluster_id=dict(
        required=False,
        type='str'),
    install_plan=dict(
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
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
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
        resource_type='ibm_cm_offering_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cm_offering_instance',
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
