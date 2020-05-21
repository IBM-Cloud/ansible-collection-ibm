#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_volume
short_description: Configure IBM Cloud 'ibm_pi_volume' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_volume' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    volume_id:
        description:
            - Volume ID
        required: False
        type: str
    pi_volume_name:
        description:
            - (Required for new resource) Volume Name to create
        required: False
        type: str
    pi_volume_shareable:
        description:
            - Flag to indicate if the volume can be shared across multiple instances?
        required: False
        type: bool
    pi_volume_size:
        description:
            - (Required for new resource) Size of the volume in GB
        required: False
        type: float
    pi_volume_type:
        description:
            - (Required for new resource) Volume type
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) Cloud Instance ID - This is the service_instance_id.
        required: False
        type: str
    volume_status:
        description:
            - Volume status
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
    ('pi_volume_name', 'str'),
    ('pi_volume_size', 'float'),
    ('pi_volume_type', 'str'),
    ('pi_cloud_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'volume_id',
    'pi_volume_name',
    'pi_volume_shareable',
    'pi_volume_size',
    'pi_volume_type',
    'pi_cloud_instance_id',
    'volume_status',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    volume_id=dict(
        required=False,
        type='str'),
    pi_volume_name=dict(
        required=False,
        type='str'),
    pi_volume_shareable=dict(
        required=False,
        type='bool'),
    pi_volume_size=dict(
        required=False,
        type='float'),
    pi_volume_type=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    volume_status=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_pi_volume',
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
