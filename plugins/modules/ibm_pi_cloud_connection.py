#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_cloud_connection
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_cloud_connection

short_description: Configure IBM Cloud 'ibm_pi_cloud_connection' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_cloud_connection' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_cloud_connection_gre_destination_address:
        description:
            - GRE destination IP address
        required: False
        type: str
    pi_cloud_connection_vpc_crns:
        description:
            - Set of VPCs to attach to this cloud connection
        required: False
        type: list
        elements: str
    pi_cloud_connection_transit_enabled:
        description:
            - Enable transit gateway for this cloud connection
        required: False
        type: bool
        default: False
    pi_cloud_instance_id:
        description:
            - (Required for new resource) PI cloud instance ID
        required: True
        type: str
    pi_cloud_connection_global_routing:
        description:
            - Enable global routing for this cloud connection
        required: False
        type: bool
        default: False
    pi_cloud_connection_networks:
        description:
            - Set of Networks to attach to this cloud connection
        required: False
        type: list
        elements: str
    pi_cloud_connection_classic_enabled:
        description:
            - Enable classic endpoint destination
        required: False
        type: bool
        default: False
    pi_cloud_connection_vpc_enabled:
        description:
            - Enable VPC for this cloud connection
        required: False
        type: bool
        default: False
    pi_cloud_connection_name:
        description:
            - (Required for new resource) Name of the cloud connection
        required: True
        type: str
    pi_cloud_connection_speed:
        description:
            - (Required for new resource) Speed of the cloud connection (speed in megabits per second)
        required: True
        type: int
    pi_cloud_connection_gre_cidr:
        description:
            - GRE network in CIDR notation
        required: False
        type: str
    pi_cloud_connection_metered:
        description:
            - Enable metered for this cloud connection
        required: False
        type: bool
        default: False
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
    ('pi_cloud_instance_id', 'str'),
    ('pi_cloud_connection_name', 'str'),
    ('pi_cloud_connection_speed', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_cloud_connection_gre_destination_address',
    'pi_cloud_connection_vpc_crns',
    'pi_cloud_connection_transit_enabled',
    'pi_cloud_instance_id',
    'pi_cloud_connection_global_routing',
    'pi_cloud_connection_networks',
    'pi_cloud_connection_classic_enabled',
    'pi_cloud_connection_vpc_enabled',
    'pi_cloud_connection_name',
    'pi_cloud_connection_speed',
    'pi_cloud_connection_gre_cidr',
    'pi_cloud_connection_metered',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('pi_cloud_connection_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'pi_cloud_connection_name',
    'pi_cloud_instance_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_cloud_connection_gre_destination_address=dict(
        required=False,
        type='str'),
    pi_cloud_connection_vpc_crns=dict(
        required=False,
        elements='',
        type='list'),
    pi_cloud_connection_transit_enabled=dict(
        required=False,
        type='bool'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_cloud_connection_global_routing=dict(
        required=False,
        type='bool'),
    pi_cloud_connection_networks=dict(
        required=False,
        elements='',
        type='list'),
    pi_cloud_connection_classic_enabled=dict(
        required=False,
        type='bool'),
    pi_cloud_connection_vpc_enabled=dict(
        required=False,
        type='bool'),
    pi_cloud_connection_name=dict(
        required=False,
        type='str'),
    pi_cloud_connection_speed=dict(
        required=False,
        type='int'),
    pi_cloud_connection_gre_cidr=dict(
        required=False,
        type='str'),
    pi_cloud_connection_metered=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_pi_cloud_connection',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_cloud_connection',
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
