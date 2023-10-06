#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cm_offering
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_offering

short_description: Configure IBM Cloud 'ibm_cm_offering' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cm_offering' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.50.0
    - Terraform v0.12.20

options:
    label:
        description:
            - Display Name in the requested language.
        required: False
        type: str
    offering_docs_url:
        description:
            - URL for an additional docs with this offering.
        required: False
        type: str
    short_description_i18n:
        description:
            - A map of translated strings, by language code.
        required: False
        type: dict
        elements: str
    publish_to_ibm:
        description:
            - Whether you would like to publish this offering to IBM or not.
        required: False
        type: bool
    provider_info:
        description:
            - Information on the provider for this offering, or omitted if no provider information is given.
        required: False
        type: list
        elements: dict
    product_kind:
        description:
            - The product kind.  Valid values are module, solution, or empty string.
        required: False
        type: str
    name:
        description:
            - The programmatic name of this offering.
        required: False
        type: str
    offering_support_url:
        description:
            - [deprecated] - Use offering.support instead.  URL to be displayed in the Consumption UI for getting support on this offering.
        required: False
        type: str
    public_original_crn:
        description:
            - The original offering CRN that this publish entry came from.
        required: False
        type: str
    offering_icon_url:
        description:
            - URL for an icon associated with this offering.
        required: False
        type: str
    features:
        description:
            - list of features associated with this offering.
        required: False
        type: list
        elements: dict
    publish_to_public:
        description:
            - Whether you would like to publish this offering to the public catalog or not.
        required: False
        type: bool
    publish_public_crn:
        description:
            - The crn of the public catalog entry of this offering.
        required: False
        type: str
    portal_ui_url:
        description:
            - The portal UI URL.
        required: False
        type: str
    disclaimer:
        description:
            - A disclaimer for this offering.
        required: False
        type: str
    offering_id:
        description:
            - Offering identifier.  Provide this when an offering already exists and you wish to use it as a terraform resource.
        required: False
        type: str
    label_i18n:
        description:
            - A map of translated strings, by language code.
        required: False
        type: dict
        elements: str
    pc_managed:
        description:
            - Offering is managed by Partner Center.
        required: False
        type: bool
    share_with_all:
        description:
            - Denotes public availability of an Offering - if share_enabled is true.
        required: False
        type: bool
    share_with_ibm:
        description:
            - Denotes IBM employee availability of an Offering - if share_enabled is true.
        required: False
        type: bool
    share_enabled:
        description:
            - Denotes sharing including access list availability of an Offering is enabled.
        required: False
        type: bool
    metadata:
        description:
            - Map of metadata values for this offering.
        required: False
        type: dict
        elements: str
    hidden:
        description:
            - Determine if this offering should be displayed in the Consumption UI.
        required: False
        type: bool
    catalog_id:
        description:
            - (Required for new resource) Catalog identifier.
        required: True
        type: str
    long_description:
        description:
            - Long description in the requested language.
        required: False
        type: str
    long_description_i18n:
        description:
            - A map of translated strings, by language code.
        required: False
        type: dict
        elements: str
    publish_approved:
        description:
            - Offering has been approved to publish to permitted to IBM or Public Catalog.
        required: False
        type: bool
    publish_to_access_list:
        description:
            - A list of account IDs to add to this offering's access list.
        required: False
        type: list
        elements: str
    portal_approval_record:
        description:
            - The portal's approval record ID.
        required: False
        type: str
    image_pull_keys:
        description:
            - Image pull keys for this offering.
        required: False
        type: list
        elements: dict
    tags:
        description:
            - List of tags associated with this catalog.
        required: False
        type: list
        elements: str
    keywords:
        description:
            - List of keywords associated with offering, typically used to search for it.
        required: False
        type: list
        elements: str
    badges:
        description:
            - A list of badges for this offering.
        required: False
        type: list
        elements: dict
    short_description:
        description:
            - Short description in the requested language.
        required: False
        type: str
    media:
        description:
            - A list of media items related to this offering.
        required: False
        type: list
        elements: dict
    deprecate_pending:
        description:
            - Deprecation information for an Offering.
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
    ('catalog_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'label',
    'offering_docs_url',
    'short_description_i18n',
    'publish_to_ibm',
    'provider_info',
    'product_kind',
    'name',
    'offering_support_url',
    'public_original_crn',
    'offering_icon_url',
    'features',
    'publish_to_public',
    'publish_public_crn',
    'portal_ui_url',
    'disclaimer',
    'offering_id',
    'label_i18n',
    'pc_managed',
    'share_with_all',
    'share_with_ibm',
    'share_enabled',
    'metadata',
    'hidden',
    'catalog_id',
    'long_description',
    'long_description_i18n',
    'publish_approved',
    'publish_to_access_list',
    'portal_approval_record',
    'image_pull_keys',
    'tags',
    'keywords',
    'badges',
    'short_description',
    'media',
    'deprecate_pending',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('catalog_id', 'str'),
    ('offering_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'catalog_id',
    'offering_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    label=dict(
        required=False,
        type='str'),
    offering_docs_url=dict(
        required=False,
        type='str'),
    short_description_i18n=dict(
        required=False,
        elements='',
        type='dict'),
    publish_to_ibm=dict(
        required=False,
        type='bool'),
    provider_info=dict(
        required=False,
        elements='',
        type='list'),
    product_kind=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    offering_support_url=dict(
        required=False,
        type='str'),
    public_original_crn=dict(
        required=False,
        type='str'),
    offering_icon_url=dict(
        required=False,
        type='str'),
    features=dict(
        required=False,
        elements='',
        type='list'),
    publish_to_public=dict(
        required=False,
        type='bool'),
    publish_public_crn=dict(
        required=False,
        type='str'),
    portal_ui_url=dict(
        required=False,
        type='str'),
    disclaimer=dict(
        required=False,
        type='str'),
    offering_id=dict(
        required=False,
        type='str'),
    label_i18n=dict(
        required=False,
        elements='',
        type='dict'),
    pc_managed=dict(
        required=False,
        type='bool'),
    share_with_all=dict(
        required=False,
        type='bool'),
    share_with_ibm=dict(
        required=False,
        type='bool'),
    share_enabled=dict(
        required=False,
        type='bool'),
    metadata=dict(
        required=False,
        elements='',
        type='dict'),
    hidden=dict(
        required=False,
        type='bool'),
    catalog_id=dict(
        required=False,
        type='str'),
    long_description=dict(
        required=False,
        type='str'),
    long_description_i18n=dict(
        required=False,
        elements='',
        type='dict'),
    publish_approved=dict(
        required=False,
        type='bool'),
    publish_to_access_list=dict(
        required=False,
        elements='',
        type='list'),
    portal_approval_record=dict(
        required=False,
        type='str'),
    image_pull_keys=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    keywords=dict(
        required=False,
        elements='',
        type='list'),
    badges=dict(
        required=False,
        elements='',
        type='list'),
    short_description=dict(
        required=False,
        type='str'),
    media=dict(
        required=False,
        elements='',
        type='list'),
    deprecate_pending=dict(
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
        resource_type='ibm_cm_offering',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.50.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cm_offering',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.50.0',
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
