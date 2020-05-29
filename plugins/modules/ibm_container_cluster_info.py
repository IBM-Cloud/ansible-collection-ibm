#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster_info
short_description: Retrieve IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_container_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.7.0
    - Terraform v0.12.20

options:
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    server_url:
        description:
            - None
        required: False
        type: str
    cluster_name_id:
        description:
            - Name or id of the cluster
        required: True
        type: str
    is_trusted:
        description:
            - None
        required: False
        type: bool
    bounded_services:
        description:
            - None
        required: False
        type: list
        elements: dict
    vlans:
        description:
            - None
        required: False
        type: list
        elements: dict
    ingress_secret:
        description:
            - None
        required: False
        type: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    region:
        description:
            - The cluster region
        required: False
        type: str
    workers:
        description:
            - None
        required: False
        type: list
        elements: str
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    worker_count:
        description:
            - Number of workers
        required: False
        type: int
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    alb_type:
        description:
            - None
        required: False
        type: str
        default: all
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    public_service_endpoint_url:
        description:
            - None
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
    ('cluster_name_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_service_endpoint_url',
    'org_guid',
    'resource_group_id',
    'public_service_endpoint',
    'private_service_endpoint',
    'server_url',
    'cluster_name_id',
    'is_trusted',
    'bounded_services',
    'vlans',
    'ingress_secret',
    'space_guid',
    'region',
    'workers',
    'worker_pools',
    'ingress_hostname',
    'resource_status',
    'account_guid',
    'worker_count',
    'albs',
    'crn',
    'resource_crn',
    'alb_type',
    'resource_controller_url',
    'resource_name',
    'resource_group_name',
    'public_service_endpoint_url',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    org_guid=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    server_url=dict(
        required=False,
        type='str'),
    cluster_name_id=dict(
        required=True,
        type='str'),
    is_trusted=dict(
        required=False,
        type='bool'),
    bounded_services=dict(
        required=False,
        elements='',
        type='list'),
    vlans=dict(
        required=False,
        elements='',
        type='list'),
    ingress_secret=dict(
        required=False,
        type='str'),
    space_guid=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    workers=dict(
        required=False,
        elements='',
        type='list'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    account_guid=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    crn=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    alb_type=dict(
        default='all',
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.7.0',
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
