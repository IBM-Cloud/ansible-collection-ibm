# Ansible Collection for IBM Cloud

This Ansible Collection provides a variety of Ansible Modules to help automate management of IBM Cloud services and resources.

Compatible with Ansible Core 2.12+


## Description

The primary purpose of this Ansible Collection is to provide Ansible-driven automation capabilities for interaction with IBM Cloud services and resources. This enables organizations to leverage Ansible for tasks that are executed and intersect/require activities to be performed on IBM Cloud to fulfil the objective.

The Ansible Collection for IBM Cloud contains many generated Ansible Modules, each Ansible Module is a wrapper around [Terraform Provider for IBM Cloud] elements (i.e. resource or data source). This provides an extensive list Ansible Modules to perform activities within IBM Cloud.

When any Ansible Module is executed, on-the-fly Terraform code is generated and executed; a one-time download of an appropriate Terraform binary and the [Terraform Provider for IBM Cloud from the Terraform Registry] is performed to the Ansible temporary directory.


## Contents

See the complete list of Ansible Modules within this Ansible Collection, are visible on the [Ansible Galaxy entry of the Ansible Collection for IBM Cloud] or in the [GitHub repository /docs subdirectory].

As each Ansible Module is a wrapper for a Terraform element, it is also possible to view other examples in the [documentation of the Terraform Provider for IBM Cloud].


## Getting Started

### Requirements

- [Python 3.10+] installation
  - Best practice recommendation when using Ansible, is to use Ansible Core from an isolated [venv] (e.g. `python3 -m venv ~/.py_venv/venv1 && source ~/.py_venv/venv1/bin/activate`)

- [Ansible Core] 2.12+ installation *(alternatively, using Ansible Community Edition which provides Ansible Core + various community Ansible Collections)*

### Install Ansible Collection for IBM Cloud

1. Execute Ansible Galaxy CLI to install the Ansible Collection for IBM Cloud. See alternative installation methods in the [Ansible User guide - Collections], such as version-locking and using a requirements file.

    ```shell
    ansible-galaxy collection install ibm.cloudcollection
    ```


## Example Ansible Playbooks

1. [IBM Cloud IAM User invite example](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/account-iam-user-invite)

1. [IBM Cloud Resource Group Example](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/account-resource-group)

1. [IBM Cloud managed-service for Red Hat OpenShift (ROKS) cluster with VPC networking](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/k8s-openshift-managed-service)

1. [IBM Cloud Virtual Server](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/vs-intel)

1. [IBM Power Virtual Server in IBM Cloud](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/vs-ibmpower)


## Changelog

For this Ansible Collection version, please see the matching version changelog of the Terraform Provider for IBM Cloud:
- [Terraform Provider for IBM Cloud Release Notes]
- [GitHub Releases (detailed) of Terraform Provider for IBM Cloud]


## Related Information

- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible User guide - Collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Developer guide - Collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)


[Terraform Provider for IBM Cloud]: https://cloud.ibm.com/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-about
[Terraform Provider for IBM Cloud from the Terraform Registry]: https://registry.terraform.io/providers/IBM-Cloud/ibm/latest
[Ansible Galaxy entry of the Ansible Collection for IBM Cloud]: https://galaxy.ansible.com/ui/repo/published/ibm/cloudcollection/docs/
[GitHub repository /docs subdirectory]: https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/docs
[documentation of the Terraform Provider for IBM Cloud]: https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs
[Python 3.10+]: https://python.org/downloads/
[venv]: https://docs.python.org/3/library/venv.html
[Ansible Core]: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
[Ansible User guide - Collections]: https://docs.ansible.com/ansible/latest/user_guide/collections_using.html
[Terraform Provider for IBM Cloud Release Notes]: https://cloud.ibm.com/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-release-notes
[GitHub Releases (detailed) of Terraform Provider for IBM Cloud]: https://github.com/IBM-Cloud/terraform-provider-ibm/releases
