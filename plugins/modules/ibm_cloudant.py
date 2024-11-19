#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cloudant
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cloudant

short_description: Configure IBM Cloud 'ibm_cloudant' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cloudant' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    name:
        description:
            - (Required for new resource) A name for the resource instance
        required: True
        type: str
    plan:
        description:
            - (Required for new resource) The plan type of the service
        required: True
        type: str
    legacy_credentials:
        description:
            - Use both legacy credentials and IAM for authentication
        required: False
        type: bool
        default: False
    capacity:
        description:
            - A number of blocks of throughput units. A block consists of 100 reads/sec, 50 writes/sec, and 5 global queries/sec of provisioned throughput capacity.
        required: False
        type: int
        default: 1
    resource_group_id:
        description:
            - The resource group id
        required: False
        type: str
    parameters_json:
        description:
            - Arbitrary parameters to pass in Json string format
        required: False
        type: str
    service_endpoints:
        description:
            - Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.
        required: False
        type: str
    include_data_events:
        description:
            - Include data event types in events sent to IBM Cloud Activity Tracker with LogDNA for the IBM Cloudant instance. By default only emitted events are of "management" type.
        required: False
        type: bool
        default: False
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    cors_config:
        description:
            - Configuration for CORS.
        required: False
        type: list
        elements: dict
    enable_cors:
        description:
            - Boolean value to turn CORS on and off.
        required: False
        type: bool
        default: True
    environment_crn:
        description:
            - CRN of the IBM Cloudant Dedicated Hardware plan instance
        required: False
        type: str
    location:
        description:
            - (Required for new resource) The location where the instance available
        required: True
        type: str
    parameters:
        description:
            - Arbitrary parameters to pass. Must be a JSON object
        required: False
        type: dict
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
    ('name', 'str'),
    ('plan', 'str'),
    ('location', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'plan',
    'legacy_credentials',
    'capacity',
    'resource_group_id',
    'parameters_json',
    'service_endpoints',
    'include_data_events',
    'tags',
    'cors_config',
    'enable_cors',
    'environment_crn',
    'location',
    'parameters',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'resource_group_id',
    'location',
    'identifier',
]

TL_CONFLICTS_MAP = {
    'parameters_json': ['parameters'],
    'parameters': ['parameters_json'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    name=dict(
        required=False,
        type='str'),
    plan=dict(
        required=False,
        type='str'),
    legacy_credentials=dict(
        required=False,
        type='bool'),
    capacity=dict(
        required=False,
        type='int'),
    resource_group_id=dict(
        required=False,
        type='str'),
    parameters_json=dict(
        required=False,
        type='str'),
    service_endpoints=dict(
        required=False,
        type='str'),
    include_data_events=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    cors_config=dict(
        required=False,
        elements='',
        type='list'),
    enable_cors=dict(
        required=False,
        type='bool'),
    environment_crn=dict(
        required=False,
        type='str'),
    location=dict(
        required=False,
        type='str'),
    parameters=dict(
        required=False,
        type='dict'),
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
        resource_type='ibm_cloudant',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cloudant',
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
