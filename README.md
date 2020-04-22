# IBM Cloud Ansible Collections

Ansible modules collection for IBM cloud.

## Getting Started
Below steps are follwed to install ansible collections for the IBM Cloud resources. All the resources are documented under the [Docs] directory.

## Prerequisites

1. Install [Python3]

2. [RedHat Ansible] 2.9+

    ```
    pip install "ansible>=2.9.2"
    ```


## Install

1. Download and Install collection

    ```
    ansible-galaxy collection install ibmcloud.ibmcollection
    ```

### Example Projects

1. [VPC Virtual Server Instance](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/simple-vm-ssh)

2. [Power Virtual Server Instance](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/simple-vm-power-vs)


## Dynamic Inventory

IBM Cloud has a dynamic inventory plugin for ansible. It can detect your vpc gen 1 and gen 2 instances so you don't have to keep static inventory files around.

### Set up dynamic inventory

1. Install collection as above (Prerequisites)

1. Install python dependencies for inventory (`plugins/inventory/requirements.txt`)

1. Set up `ansible.cfg` (add the following)

    ```
    [inventory]
    enable_plugins = auto
    ```

1. Set up `ibmcloud.yaml`

```
plugin: ibmcloud.ibmcollection.vpcinventory
```

1. Export or set your [IBM Cloud API Key](https://cloud.ibm.com/docs/iam?topic=iam-userapikey#create_user_key)

```bash
export IBMCLOUD_API_KEY='93nift8rl1h8f93tl3itn3GGGST83n382921n11n"
```

1. Test using `ansible-inventory`

```bash
$ ansible-inventory -i ibmcloud.yaml --list all
```
```json
{
    "_meta": {
        "hostvars": {
            "marty-vm1": {
                "ansible_host": "10.240.0.4",
                "vpc_name": "marty-vpc"
            },
            "nibz-falco-2": {
                "ansible_host": "10.240.0.11",
                "vpc_name": "nibz"
            },
            "svergara-vpc-vm1-ubu": {
                "ansible_host": "10.240.128.4",
                "vpc_name": "svergara-vpc"
            },
            "svergara-vpc-vm1-win": {
                "ansible_host": "10.240.128.36",
                "vpc_name": "svergara-vpc"
            },
            "testinstance": {
                "ansible_host": "10.240.0.4",
                "vpc_name": "nibz"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "marty-vm1",
            "nibz-falco-2",
            "svergara-vpc-vm1-ubu",
            "svergara-vpc-vm1-win",
            "testinstance"
        ]
    }
}
```


[IBM Cloud Terraform Provider]: https://github.com/IBM-Cloud/terraform-provider-ibm
[Python3]: https://www.python.org/downloads/
[Docs]: https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/docs
[Red Hat Ansible]: https://www.ansible.com/
