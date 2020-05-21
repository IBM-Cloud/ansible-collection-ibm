#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster
short_description: Configure IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    kube_version:
        description:
            - Kubernetes version
        required: False
        type: str
    service_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for services
        required: False
        type: str
    pod_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for pods
        required: False
        type: str
    worker_count:
        description:
            - Number of worker nodes in the cluster
        required: False
        type: int
        default: 1
    master_status:
        description:
            - None
        required: False
        type: str
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    ingress_secret:
        description:
            - None
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: False
        type: str
    disable_public_service_endpoint:
        description:
            - Boolean value true if Public service endpoint to be disabled
        required: False
        type: bool
        default: False
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    master_url:
        description:
            - None
        required: False
        type: str
    albs:
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
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    flavor:
        description:
            - (Required for new resource) Cluster nodes flavour
        required: False
        type: str
    vpc_id:
        description:
            - (Required for new resource) The vpc id where the cluster is
        required: False
        type: str
    zones:
        description:
            - (Required for new resource) Zone info
        required: False
        type: list
        elements: dict
    tags:
        description:
            - List of tags for the resources
        required: False
        type: list
        elements: str
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready or Ingress Ready
        required: False
        type: str
        default: IngressReady
    state_:
        description:
            - None
        required: False
        type: str
    public_service_endpoint_url:
        description:
            - None
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
    ('flavor', 'str'),
    ('vpc_id', 'str'),
    ('zones', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_crn',
    'kube_version',
    'service_subnet',
    'pod_subnet',
    'worker_count',
    'master_status',
    'private_service_endpoint_url',
    'crn',
    'resource_group_id',
    'ingress_secret',
    'resource_group_name',
    'name',
    'disable_public_service_endpoint',
    'resource_controller_url',
    'master_url',
    'albs',
    'ingress_hostname',
    'resource_name',
    'resource_status',
    'flavor',
    'vpc_id',
    'zones',
    'tags',
    'wait_till',
    'state_',
    'public_service_endpoint_url',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_crn=dict(
        required=False,
        type='str'),
    kube_version=dict(
        required=False,
        type='str'),
    service_subnet=dict(
        required=False,
        type='str'),
    pod_subnet=dict(
        required=False,
        type='str'),
    worker_count=dict(
        default=1,
        type='int'),
    master_status=dict(
        required=False,
        type='str'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    crn=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    ingress_secret=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    disable_public_service_endpoint=dict(
        default=False,
        type='bool'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    master_url=dict(
        required=False,
        type='str'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    flavor=dict(
        required=False,
        type='str'),
    vpc_id=dict(
        required=False,
        type='str'),
    zones=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    wait_till=dict(
        default='IngressReady',
        type='str'),
    state_=dict(
        required=False,
        type='str'),
    public_service_endpoint_url=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_vpc_cluster',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.6.0',
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
