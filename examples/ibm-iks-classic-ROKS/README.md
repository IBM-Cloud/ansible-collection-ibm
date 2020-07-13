# IBM Cloud Ansible: Openshift cluster on IBM Classic Infrastructure

This example shows how to create Openshift cluster on classic infrastructure .
In this example, a openshift cluster with 2 default worker pool nodes.

## Configuration Parameters

The following parameters can be set by the user:

* `name:`: used for the instance name.
* `datacenter`: datacenter name
* `machine_type`: machine type.
* `hardware`: hardware shared/isolated type.
* `private_vlan_id`: private vlan id, to list vlans under your account - `ibmcloud ks vlan ls --zone <zone_name>`
* `public_vlan_id`: public vlan id, to list vlans under your account - `ibmcloud ks vlan ls --zone <zone_name>`
* `cluster_name`: cluster name
* `default_worker_pool_size`: number of worker nodes in default workerpool
* `entitlement`: Entitlement info for openshift cluster
* `kube_version`: Kube versions, to list the kubeversions supported by ibmcloud - `ibmcloud ks versions`


## Running

### Set API Key and Region

1. [Obtain an IBM Cloud API key].

2. Export your API key to the `IC_API_KEY` environment variable:

    ```
    export IC_API_KEY=<YOUR_API_KEY_HERE>
    ```

    Note: Modules also support the 'ibmcloud_api_key' parameter, but it is
    recommended to only use this when encrypting your API key value.

### Create

1. To create openshift cluster, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```

### Destroy

1. To destroy cluster run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/iam?topic=iam-userapikey
