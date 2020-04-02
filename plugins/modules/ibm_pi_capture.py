#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_capture
short_description: Configure IBM Cloud 'ibm_pi_capture' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_pi_capture' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    pi_capture_name:
        description:
            - (Required for new resource) Name of the capture to create. Note : this must be unique
        required: False
        type: str
    pi_capture_volume_ids:
        description:
            - List of volume names that need to be passed in the input
        required: False
        type: str
    pi_capture_cloud_storage_access_key:
        description:
            - Name of Cloud Storage Access Key
        required: False
        type: str
    pi_capture_storage_image_path:
        description:
            - Name of the Image Path
        required: False
        type: str
    pi_cloud_instance_id:
        description:
            - (Required for new resource) Cloud Instance ID - This is the service_instance_id.
        required: False
        type: str
    pi_instance_name:
        description:
            - (Required for new resource) Instance Name of the Power VM
        required: False
        type: str
    pi_capture_destination:
        description:
            - (Required for new resource) Name of destination to store the image capture to
        required: False
        type: str
    pi_capture_cloud_storage_region:
        description:
            - List of Regions to use
        required: False
        type: str
    pi_capture_cloud_storage_secret_key:
        description:
            - Name of the Cloud Storage Secret Key
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
    ('pi_capture_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_instance_name', 'str'),
    ('pi_capture_destination', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'pi_capture_name',
    'pi_capture_volume_ids',
    'pi_capture_cloud_storage_access_key',
    'pi_capture_storage_image_path',
    'pi_cloud_instance_id',
    'pi_instance_name',
    'pi_capture_destination',
    'pi_capture_cloud_storage_region',
    'pi_capture_cloud_storage_secret_key',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    pi_capture_name=dict(
        required=False,
        type='str'),
    pi_capture_volume_ids=dict(
        required=False,
        type='str'),
    pi_capture_cloud_storage_access_key=dict(
        required=False,
        type='str'),
    pi_capture_storage_image_path=dict(
        required=False,
        type='str'),
    pi_cloud_instance_id=dict(
        required=False,
        type='str'),
    pi_instance_name=dict(
        required=False,
        type='str'),
    pi_capture_destination=dict(
        required=False,
        type='str'),
    pi_capture_cloud_storage_region=dict(
        required=False,
        type='str'),
    pi_capture_cloud_storage_secret_key=dict(
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_pi_capture',
        tf_type='resource',
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
