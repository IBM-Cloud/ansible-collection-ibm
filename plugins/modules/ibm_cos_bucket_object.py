#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cos_bucket_object
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cos_bucket_object

short_description: Configure IBM Cloud 'ibm_cos_bucket_object' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cos_bucket_object' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    bucket_location:
        description:
            - (Required for new resource) COS bucket location
        required: True
        type: str
    endpoint_type:
        description:
            - COS endpoint type: public, private, direct
        required: False
        type: str
        default: public
    content:
        description:
            - COS object content
        required: False
        type: str
    object_lock_legal_hold_status:
        description:
            - An object lock configuration on the object, the valid states are ON/OFF. When ON prevents deletion of the object version.
        required: False
        type: str
    website_redirect:
        description:
            - Redirect a request to another object or an URL
        required: False
        type: str
    content_base64:
        description:
            - COS object content in base64 encoding
        required: False
        type: str
    key:
        description:
            - (Required for new resource) COS object key
        required: True
        type: str
    force_delete:
        description:
            - COS buckets need to be empty before they can be deleted. force_delete option empty the bucket and delete it.
        required: False
        type: bool
        default: True
    object_lock_mode:
        description:
            - Retention modes apply different levels of protection to the objects.
        required: False
        type: str
    object_lock_retain_until_date:
        description:
            - An object cannot be deleted when the current time is earlier than the retainUntilDate. After this date, the object can be deleted.
        required: False
        type: str
    bucket_crn:
        description:
            - (Required for new resource) COS bucket CRN
        required: True
        type: str
    content_file:
        description:
            - COS object content file path
        required: False
        type: str
    etag:
        description:
            - COS object MD5 hexdigest
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
    iaas_classic_username:
        description:
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('bucket_location', 'str'),
    ('key', 'str'),
    ('bucket_crn', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'bucket_location',
    'endpoint_type',
    'content',
    'object_lock_legal_hold_status',
    'website_redirect',
    'content_base64',
    'key',
    'force_delete',
    'object_lock_mode',
    'object_lock_retain_until_date',
    'bucket_crn',
    'content_file',
    'etag',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('bucket_location', 'str'),
    ('key', 'str'),
    ('bucket_crn', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'bucket_location',
    'key',
    'endpoint_type',
    'bucket_crn',
]

TL_CONFLICTS_MAP = {
    'content': ['content_base64', 'content_file'],
    'content_base64': ['content', 'content_file'],
    'content_file': ['content', 'content_base64'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    bucket_location=dict(
        required=False,
        type='str'),
    endpoint_type=dict(
        required=False,
        type='str'),
    content=dict(
        required=False,
        type='str'),
    object_lock_legal_hold_status=dict(
        required=False,
        type='str'),
    website_redirect=dict(
        required=False,
        type='str'),
    content_base64=dict(
        required=False,
        type='str'),
    key=dict(
        required=False,
        type='str'),
    force_delete=dict(
        required=False,
        type='bool'),
    object_lock_mode=dict(
        required=False,
        type='str'),
    object_lock_retain_until_date=dict(
        required=False,
        type='str'),
    bucket_crn=dict(
        required=False,
        type='str'),
    content_file=dict(
        required=False,
        type='str'),
    etag=dict(
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
        resource_type='ibm_cos_bucket_object',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cos_bucket_object',
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
