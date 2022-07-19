#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_satellite_cluster
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_cluster

short_description: Configure IBM Cloud 'ibm_satellite_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_satellite_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.41.1
    - Terraform v0.12.20

options:
    wait_for_worker_update:
        description:
            - Wait for worker node to update during kube version update.
        required: False
        type: bool
        default: True
    crn_token:
        description:
            - The IBM Cloud Identity and Access Management (IAM) service CRN token for the service that creates the cluster.
        required: False
        type: str
    tags:
        description:
            - List of tags for the resources
        required: False
        type: list
        elements: str
    kube_version:
        description:
            - The OpenShift Container Platform version
        required: False
        type: str
    patch_version:
        description:
            - Kubernetes patch version
        required: False
        type: str
    worker_count:
        description:
            - The number of worker nodes per zone in the default worker pool. Required when '--host-label' is specified. (default: 0)
        required: False
        type: int
    service_subnet:
        description:
            - User provided value for service subnet
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    default_worker_pool_labels:
        description:
            - Labels on the default worker pool
        required: False
        type: dict
        elements: str
    zones:
        description:
            - Zone info for worker pool
        required: False
        type: list
        elements: dict
    pull_secret:
        description:
            - The RedHat pull secret to create the OpenShift cluster
        required: False
        type: str
    pod_subnet:
        description:
            - User provided value for the pod subnet
        required: False
        type: str
    enable_config_admin:
        description:
            - Grant cluster admin access to Satellite Config to manage Kubernetes resources.
        required: False
        type: bool
    name:
        description:
            - (Required for new resource) The unique name for the new IBM Cloud Satellite cluster
        required: True
        type: str
    disable_public_service_endpoint:
        description:
            - Boolean value true if Public service endpoint to be disabled
        required: False
        type: bool
        default: False
    location:
        description:
            - (Required for new resource) The name or ID of the Satellite location
        required: True
        type: str
    retry_patch_version:
        description:
            - Argument which helps to retry the patch version updates on worker nodes. Increment the value to retry the patch updates if the previous apply fails
        required: False
        type: int
    host_labels:
        description:
            - Labels that describe a Satellite host for default workerpool
        required: False
        type: list
        elements: str
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
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('location', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'wait_for_worker_update',
    'crn_token',
    'tags',
    'kube_version',
    'patch_version',
    'worker_count',
    'service_subnet',
    'resource_group_id',
    'default_worker_pool_labels',
    'zones',
    'pull_secret',
    'pod_subnet',
    'enable_config_admin',
    'name',
    'disable_public_service_endpoint',
    'location',
    'retry_patch_version',
    'host_labels',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'resource_group_id',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    wait_for_worker_update=dict(
        required=False,
        type='bool'),
    crn_token=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    kube_version=dict(
        required=False,
        type='str'),
    patch_version=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    service_subnet=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    default_worker_pool_labels=dict(
        required=False,
        elements='',
        type='dict'),
    zones=dict(
        required=False,
        elements='',
        type='list'),
    pull_secret=dict(
        required=False,
        type='str'),
    pod_subnet=dict(
        required=False,
        type='str'),
    enable_config_admin=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    disable_public_service_endpoint=dict(
        required=False,
        type='bool'),
    location=dict(
        required=False,
        type='str'),
    retry_patch_version=dict(
        required=False,
        type='int'),
    host_labels=dict(
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
        resource_type='ibm_satellite_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.41.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_satellite_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.41.1',
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
