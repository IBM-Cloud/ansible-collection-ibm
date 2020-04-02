#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance_info
short_description: Retrieve IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_compute_vm_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    public_interface_id:
        description:
            - None
        required: False
        type: int
    private_interface_id:
        description:
            - None
        required: False
        type: int
    public_subnet_id:
        description:
            - None
        required: False
        type: int
    ip_address_id:
        description:
            - None
        required: False
        type: int
    ip_address_id_private:
        description:
            - None
        required: False
        type: int
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    domain:
        description:
            - The domain of the virtual guest
        required: True
        type: str
    datacenter:
        description:
            - Datacenter in which the virtual guest is deployed
        required: False
        type: str
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    public_ipv6_subnet:
        description:
            - None
        required: False
        type: str
    public_ipv6_subnet_id:
        description:
            - None
        required: False
        type: str
    ipv4_address_private:
        description:
            - None
        required: False
        type: str
    ipv6_address:
        description:
            - None
        required: False
        type: str
    most_recent:
        description:
            - If true and multiple entries are found, the most recently created virtual guest is used. If false, an error is returned
        required: False
        type: bool
        default: False
    private_subnet_id:
        description:
            - None
        required: False
        type: int
    status:
        description:
            - The VSI status
        required: False
        type: str
    power_state:
        description:
            - The current power state of a virtual guest.
        required: False
        type: str
    hostname:
        description:
            - The hostname of the virtual guest
        required: True
        type: str
    cores:
        description:
            - Number of cpu cores
        required: False
        type: int
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    last_known_power_state:
        description:
            - The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.
        required: False
        type: str
    ipv4_address:
        description:
            - None
        required: False
        type: str
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
    ('domain', 'str'),
    ('hostname', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'public_interface_id',
    'private_interface_id',
    'public_subnet_id',
    'ip_address_id',
    'ip_address_id_private',
    'ipv6_address_id',
    'domain',
    'datacenter',
    'secondary_ip_addresses',
    'public_ipv6_subnet',
    'public_ipv6_subnet_id',
    'ipv4_address_private',
    'ipv6_address',
    'most_recent',
    'private_subnet_id',
    'status',
    'power_state',
    'hostname',
    'cores',
    'secondary_ip_count',
    'last_known_power_state',
    'ipv4_address',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_interface_id=dict(
        required=False,
        type='int'),
    private_interface_id=dict(
        required=False,
        type='int'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    ip_address_id=dict(
        required=False,
        type='int'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    domain=dict(
        required=True,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    ipv6_address=dict(
        required=False,
        type='str'),
    most_recent=dict(
        default=False,
        type='bool'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    status=dict(
        required=False,
        type='str'),
    power_state=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=True,
        type='str'),
    cores=dict(
        required=False,
        type='int'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    last_known_power_state=dict(
        required=False,
        type='str'),
    ipv4_address=dict(
        required=False,
        type='str'),
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
        resource_type='ibm_compute_vm_instance',
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
