# IBM Cloud Ansible: IBM Certificate-Manager

This example illustrates how to use the Certificate Manager Import and Order resources to import a certificate and to order a certificate.

## Configuration Parameters

The following parameters can be set by the user:

`service_name`: The name of the Certificate Manager Service Instance.
`location`: The region where the resource has to be provisioned. Default: us-south
`import_name`: The display name for the imported certificate.
`order_name`: The display name for the ordered certificate.
`rotate_keys`: Rotate Keys of certificate.It is enable when the certificate is to be renewed. Default: False
`cis_id`: The CRN-based instance ID of the IBM Cloud Internet Services instance that manages the domains. If not present, Certificate Manager assumes a v4 or above Callback URL notifications channel with domain validation exists.

## Running

### Set API Key and Region

1. [Obtain an IBM Cloud API key].

2. Export your API key to the `IC_API_KEY` environment variable:

    ```
    export IC_API_KEY=<YOUR_API_KEY_HERE>
    ```

    Note: Modules also support the 'ibmcloud_api_key' parameter, but it is
    recommended to only use this when encrypting your API key value.
## Assumptions:

1. It's assumed that user has valid domain ownership while ordering certificates using IBM CIS.
2. [ Certificate Ordering Limitations ](https://cloud.ibm.com/docs/certificate-manager?topic=certificate-manager-ordering-certificates#certificate-ordering-limitations)
3. Before ordering certificates using IBM CIS [ Set up ordering certificates using CIS ](https://cloud.ibm.com/docs/certificate-manager?topic=certificate-manager-ordering-certificates#cis)
4. [ Certificate Ordering Limits ](https://cloud.ibm.com/docs/certificate-manager?topic=certificate-manager-limits#api-limits)
5. [ API Documentation for CMS ](https://cloud.ibm.com/apidocs/certificate-manager)

## Notes:
1. Terraform IBM provider doesn't supports ordering certificates using `Other DNS provider`.

2. With `auto_renew_enabled`, certificates are automatically renewed 31 days before they expire. If your certificate expires in less than 31 days, you must renew it by updating `rotate_keys`. After you do so, your future certificates are renewed automatically.


### Create

1. To create all resources, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```
### Note:
    1. Certificate import and order apis can import, order multiple certificates with same specification.
    2. On `ansible-playbook create.yml` twice it ll import and order certificates two times..

### Destroy

1. To destroy all resources run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/iam?topic=iam-userapikey
