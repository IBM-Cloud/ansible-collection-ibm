# Example for IKS Cluster Creation and creating and binding COS Bucket with the cluster.

This example shows how to create a Kubernetes Cluster in IBM IKS service and bind an 
cos bucket with the IKS cluster using the ansible playbook.

Following types of resources are supported:

* [ Container Cluster Resource](https://cloud.ibm.com/docs/terraform?topic=terraform-container-resources)
* [Object Storage resources](https://cloud.ibm.com/docs/terraform?topic=terraform-object-storage-resources)
* [Resource management data sources](https://cloud.ibm.com/docs/terraform?topic=terraform-resource-mgmt-resources)
ibm_container_bind_service
## Terraform versions

Terraform required_version = ">= 0.12". Branch - `master`.

## Configuration Parameters

The following parameters can be set by the user:

* `datacenter`: The datacenter of the worker nodes
* `machine_type`: The machine type of the worker nodes
* `hardware`: The level of hardware isolation for your worker node
* `default_pool_size`: The default pool size of the IKS cluster
* `private_vlan_id`: The private VLAN of the worker node
* `public_vlan_id`: The public VLAN ID for the worker node
* `cluster_name`: The name provided for the cluster
* `kube_version`: The desired Kubernetes version of the created cluster
* `instance_name`: The name Should be in format [a-z0-9] like instance1
* `plan_type`: The plan opted by the user.
* `location_info`: This is set to global.

## Running

### Set API Key and Region

1. [Obtain an IBM Cloud API key]: https://cloud.ibm.com/docs/iam?topic=iam-userapikey

2. Export your API key to the `IC_API_KEY` environment variable:

    ```
    export IC_API_KEY=<YOUR_API_KEY_HERE>
    ```

    Note: Modules also support the 'ibmcloud_api_key' parameter, but it is
    recommended to only use this when encrypting your API key value.

### Create

1. To create all resources and test public SSH connection to the VM, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```
## Example Usage

Create a container cluster:

```hcl
resource "ibm_container_cluster" "testacc_cluster" {
  name            = "test"
  datacenter      = "dal10"
  machine_type    = "b3c.4x16"
  hardware        = "shared"
  private_vlan_id = "2709721"
  private_service_endpoint = true
}
```

```hcl

data "ibm_container_cluster" "cluster_foo" {
  cluster_name_id = "FOO"
}

```
Create a COS instance and bucket:

```hcl

data "ibm_resource_group" "cos_group" {
  name = "cos-resource-group"
}

resource "ibm_resource_instance" "cos_instance" {
  name              = "cos-instance"
  resource_group_id = data.ibm_resource_group.cos_group.id
  service           = "cloud-object-storage"
  plan              = "standard"
  location          = "global"
}
```

```hcl
resource "ibm_cos_bucket" "standard-ams03" {
  bucket_name = "a-standard-bucket-at-ams"
  resource_instance_id = ibm_resource_instance.cos_instance.id
  single_site_location = "ams03"
  storage_class = "standard"
}
```
Adding binding service:

```hcl
resource "ibm_container_bind_service" "bind_service" {
  cluster_name_id             = "mycluster"
  service_instance_name       = "myservice"
  namespace_id                = "default"
}
```
## Examples

* [ Container cluster ](https://github.com/IBM-Cloud/terraform-provider-ibm/tree/master/examples/ibm-iks-openshift)
* [ Cos bucket ](https://github.com/IBM-Cloud/terraform-provider-ibm/tree/master/examples/ibm-cos-bucket)
