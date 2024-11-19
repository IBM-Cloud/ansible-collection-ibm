#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_network_security_group_rule
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_network_security_group_rule

short_description: Configure IBM Cloud 'ibm_pi_network_security_group_rule' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_network_security_group_rule' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_destination_ports:
        description:
            - Destination port ranges.
        required: False
        type: list
        elements: dict
    pi_network_security_group_rule_id:
        description:
            - The network security group rule id to remove.
        required: False
        type: str
    pi_network_security_group_id:
        description:
            - (Required for new resource) The unique identifier of the network security group.
        required: True
        type: str
    pi_remote:
        description:
            - The protocol of the network traffic.
        required: False
        type: list
        elements: dict
    pi_source_ports:
        description:
            - Source port ranges.
        required: False
        type: list
        elements: dict
    pi_action:
        description:
            - The action to take if the rule matches network traffic.
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) The GUID of the service instance associated with an account.
        required: True
        type: str
    pi_protocol:
        description:
            - The protocol of the network traffic.
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
    ('pi_network_security_group_id', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_destination_ports',
    'pi_network_security_group_rule_id',
    'pi_network_security_group_id',
    'pi_remote',
    'pi_source_ports',
    'pi_action',
    'pi_cloud_instance_id',
    'pi_protocol',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'pi_destination_ports': ['pi_network_security_group_rule_id'],
    'pi_network_security_group_rule_id': ['pi_action', 'pi_destination_ports', 'pi_protocol', 'pi_remote', 'pi_source_ports'],
    'pi_remote': ['pi_network_security_group_rule_id'],
    'pi_source_ports': ['pi_network_security_group_rule_id'],
    'pi_action': ['pi_network_security_group_rule_id'],
    'pi_protocol': ['pi_network_security_group_rule_id'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_destination_ports=dict(
        required=False,
        elements='',
        type='list'),
    pi_network_security_group_rule_id=dict(
        required=False,
        type='str'),
    pi_network_security_group_id=dict(
        required=False,
        type='str'),
    pi_remote=dict(
        required=False,
        elements='',
        type='list'),
    pi_source_ports=dict(
        required=False,
        elements='',
        type='list'),
    pi_action=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_protocol=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_pi_network_security_group_rule',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.71.2',
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
