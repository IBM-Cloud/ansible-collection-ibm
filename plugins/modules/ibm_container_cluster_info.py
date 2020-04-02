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
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    server_url:
        description:
            - None
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    workers:
        description:
            - None
        required: False
        type: list
        elements: str
    vlans:
        description:
            - None
        required: False
        type: list
        elements: dict
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    alb_type:
        description:
            - None
        required: False
        type: str
        default: all
    ingress_secret:
        description:
            - None
        required: False
        type: str
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    cluster_name_id:
        description:
            - Name or id of the cluster
        required: True
        type: str
    bounded_services:
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
    is_trusted:
        description:
            - None
        required: False
        type: bool
    region:
        description:
            - The cluster region
        required: False
        type: str
    public_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    worker_count:
        description:
            - Number of workers
        required: False
        type: int
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('cluster_name_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'server_url',
    'resource_controller_url',
    'workers',
    'vlans',
    'space_guid',
    'resource_group_id',
    'alb_type',
    'ingress_secret',
    'account_guid',
    'private_service_endpoint',
    'resource_status',
    'cluster_name_id',
    'bounded_services',
    'crn',
    'resource_name',
    'resource_group_name',
    'is_trusted',
    'region',
    'public_service_endpoint_url',
    'resource_crn',
    'worker_count',
    'org_guid',
    'private_service_endpoint_url',
    'ingress_hostname',
    'worker_pools',
    'albs',
    'public_service_endpoint',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    server_url=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    workers=dict(
        required=False,
        elements='',
        type='list'),
    vlans=dict(
        required=False,
        elements='',
        type='list'),
    space_guid=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    alb_type=dict(
        default='all',
        type='str'),
    ingress_secret=dict(
        required=False,
        type='str'),
    account_guid=dict(
        required=False,
        type='str'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    resource_status=dict(
        required=False,
        type='str'),
    cluster_name_id=dict(
        required=True,
        type='str'),
    bounded_services=dict(
        required=False,
        elements='',
        type='list'),
    crn=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    is_trusted=dict(
        required=False,
        type='bool'),
    region=dict(
        required=False,
        type='str'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    org_guid=dict(
        required=False,
        type='str'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.3.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
