<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# Ansible Collection - hifis.toolkit

[![Latest release](https://img.shields.io/github/v/release/hifis-net/ansible-collection-toolkit)](https://github.com/hifis-net/ansible-collection-toolkit/releases)
[![hifis.unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/unattended_upgrades.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/unattended_upgrades.yml)
[![hifis.zammad](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/zammad.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/zammad.yml)
[![DOI](https://zenodo.org/badge/495697576.svg)](https://zenodo.org/doi/10.5281/zenodo.11147483)

## Description

This collection provides production-ready Ansible roles used for providing services used in research and by research
software engineers, but not exclusively. The following use cases are supported:

* DevOps platform:
    * [GitLab](https://github.com/hifis-net/ansible-role-gitlab) (**coming soon!**)
    * deploy [**GitLab-Runner**](roles/gitlab_runner) with a focus, but not limited, on Openstack autoscaling
    * [Redis](https://github.com/hifis-net/ansible-role-redis) (**coming soon!**)
* Help desk:
    * [**Zammad**](roles/zammad)
* High Availability (HA) / Load Balancing:
    * [HAProxy](https://github.com/hifis-net/ansible-role-haproxy) (*coming soon!*)
    * [**Keepalived**](roles/keepalived)
* OS-related:
    * [**unattended-upgrades**](roles/unattended_upgrades)
    * [netplan](https://github.com/hifis-net/ansible-role-gitlab-netplan) (*coming soon!*)
    * distribute authorized [**SSH keys**](role/ssh_keys) to users

## Minimum required Ansible-version

* Ansible >= 2.14

## Installation

Install the collection via ansible-galaxy:

```shell
ansible-galaxy collection install hifis.toolkit
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache-2.0

## Author

This role is maintained by [HIFIS Software Services](https://www.hifis.net/).
