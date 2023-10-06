#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cm_version
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_version

short_description: Configure IBM Cloud 'ibm_cm_version' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cm_version' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    content:
        description:
            - Byte array representing the content to be imported. Only supported for OVA images at this time.
        required: False
        type: str
    label:
        description:
            - Display name of version. Required for virtual server image for VPC.
        required: False
        type: str
    product_kind:
        description:
            - Optional product kind for the software being onboarded.  Valid values are software, module, or solution.  Default value is software.
        required: False
        type: str
    offering_id:
        description:
            - (Required for new resource) Offering identification.
        required: True
        type: str
    include_config:
        description:
            - Add all possible configuration values to this version when importing.
        required: False
        type: bool
    x_auth_token:
        description:
            - Authentication token used to access the specified zip file.
        required: False
        type: str
    licenses:
        description:
            - List of licenses the product was built with.
        required: False
        type: list
        elements: dict
    tags:
        description:
            - Tags array.
        required: False
        type: list
        elements: str
    pre_install:
        description:
            - Optional pre-install instructions.
        required: False
        type: list
        elements: dict
    install_kind:
        description:
            - Install type. Example: instance. Required for virtual server image for VPC.
        required: False
        type: str
    iam_permissions:
        description:
            - List of IAM permissions that are required to consume this version.
        required: False
        type: list
        elements: dict
    catalog_id:
        description:
            - (Required for new resource) Catalog identifier.
        required: True
        type: str
    import_metadata:
        description:
            - Generic data to be included with content being onboarded. Required for virtual server image for VPC.
        required: False
        type: list
        elements: dict
    target_version:
        description:
            - The semver value for this new version, if not found in the zip url package content.
        required: False
        type: str
    install:
        description:
            - Script information.
        required: False
        type: list
        elements: dict
    working_directory:
        description:
            - Optional - The sub-folder within the specified tgz file that contains the software being onboarded.
        required: False
        type: str
    import_sha:
        description:
            - SHA256 fingerprint of the image file. Required for virtual server image for VPC.
        required: False
        type: str
    zipurl:
        description:
            - URL path to zip location.  If not specified, must provide content in the body of this call.
        required: False
        type: str
    flavor:
        description:
            - Version Flavor Information.  Only supported for Product kind Solution.
        required: False
        type: list
        elements: dict
    solution_info:
        description:
            - Version Solution Information.  Only supported for Product kind Solution.
        required: False
        type: list
        elements: dict
    is_consumable:
        description:
            - Is the version able to be shared.
        required: False
        type: bool
    format_kind:
        description:
            - Format of content being onboarded. Example: vsi-image. Required for virtual server image for VPC.
        required: False
        type: str
    is_vsi:
        description:
            - Indicates that the current terraform template is used to install a virtual server image.
        required: False
        type: bool
    repotype:
        description:
            - The type of repository containing this version.  Valid values are 'public_git' or 'enterprise_git'.
        required: False
        type: str
    name:
        description:
            - Name of version. Required for virtual server image for VPC.
        required: False
        type: str
    target_kinds:
        description:
            - Deployment target of the content being onboarded. Current valid values are iks, roks, vcenter, power-iaas, terraform, and vpc-x86. Required for virtual server image for VPC.
        required: False
        type: list
        elements: str
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
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('offering_id', 'str'),
    ('catalog_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'content',
    'label',
    'product_kind',
    'offering_id',
    'include_config',
    'x_auth_token',
    'licenses',
    'tags',
    'pre_install',
    'install_kind',
    'iam_permissions',
    'catalog_id',
    'import_metadata',
    'target_version',
    'install',
    'working_directory',
    'import_sha',
    'zipurl',
    'flavor',
    'solution_info',
    'is_consumable',
    'format_kind',
    'is_vsi',
    'repotype',
    'name',
    'target_kinds',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('version_loc_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'version_loc_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    content=dict(
        required=False,
        type='str'),
    label=dict(
        required=False,
        type='str'),
    product_kind=dict(
        required=False,
        type='str'),
    offering_id=dict(
        required=False,
        type='str'),
    include_config=dict(
        required=False,
        type='bool'),
    x_auth_token=dict(
        required=False,
        type='str'),
    licenses=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    pre_install=dict(
        required=False,
        elements='',
        type='list'),
    install_kind=dict(
        required=False,
        type='str'),
    iam_permissions=dict(
        required=False,
        elements='',
        type='list'),
    catalog_id=dict(
        required=False,
        type='str'),
    import_metadata=dict(
        required=False,
        elements='',
        type='list'),
    target_version=dict(
        required=False,
        type='str'),
    install=dict(
        required=False,
        elements='',
        type='list'),
    working_directory=dict(
        required=False,
        type='str'),
    import_sha=dict(
        required=False,
        type='str'),
    zipurl=dict(
        required=False,
        type='str'),
    flavor=dict(
        required=False,
        elements='',
        type='list'),
    solution_info=dict(
        required=False,
        elements='',
        type='list'),
    is_consumable=dict(
        required=False,
        type='bool'),
    format_kind=dict(
        required=False,
        type='str'),
    is_vsi=dict(
        required=False,
        type='bool'),
    repotype=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    target_kinds=dict(
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
        resource_type='ibm_cm_version',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.51.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cm_version',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.51.0',
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
