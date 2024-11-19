#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_network_interface
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_network_interface

short_description: Configure IBM Cloud 'ibm_pi_network_interface' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_network_interface' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    pi_cloud_instance_id:
        description:
            - (Required for new resource) The GUID of the service instance associated with an account.
        required: True
        type: str
    pi_network_id:
        description:
            - (Required for new resource) Network ID.
        required: True
        type: str
    instance:
        description:
            - The attached instance to this Network Interface.
        required: False
        type: list
        elements: dict
    pi_ip_address:
        description:
            - The requested IP address of this Network Interface.
        required: False
        type: str
    pi_name:
        description:
            - Name of the Network Interface.
        required: False
        type: str
    pi_user_tags:
        description:
            - The user tags attached to this resource.
        required: False
        type: list
        elements: str
    pi_instance_id:
        description:
            - If supplied populated it attaches to the InstanceID, if empty detaches from InstanceID.
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
    ('pi_network_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_cloud_instance_id',
    'pi_network_id',
    'instance',
    'pi_ip_address',
    'pi_name',
    'pi_user_tags',
    'pi_instance_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('pi_cloud_instance_id', 'str'),
    ('pi_network_interface_id', 'str'),
    ('pi_network_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'pi_cloud_instance_id',
    'pi_network_interface_id',
    'pi_network_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_network_id=dict(
        required=False,
        type='str'),
    instance=dict(
        required=False,
        elements='',
        type='list'),
    pi_ip_address=dict(
        required=False,
        type='str'),
    pi_name=dict(
        required=False,
        type='str'),
    pi_user_tags=dict(
        required=False,
        elements='',
        type='list'),
    pi_instance_id=dict(
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
        resource_type='ibm_pi_network_interface',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_pi_network_interface',
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
