<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# Ansible Collection - hifis.software_services

[![Latest release](https://img.shields.io/github/v/release/hifis-net/ansible-role-unattended-upgrades)](https://github.com/hifis-net/ansible-role-unattended-upgrades/releases)
[![hifis.unattended_upgrades](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/unattended_upgrades.yml/badge.svg)](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/unattended_upgrades.yml)
[![hifis.zammad](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/zammad.yml/badge.svg)](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/zammad.yml)

## Description

This collection provides production-ready Ansible roles used for providing services used in research and by research
software engineers, but not exclusively. The following use cases are supported:

* DevOps platform:
  * GitLab (coming soon!)
  * GitLab-Runner (coming soon!)
  * Redis (coming soon!)
* Help desk:
  * [**Zammad**](roles/zammad)
* High Availability (HA) / Load Balancing:
  * HAProxy (coming soon!)
  * Keepalived (coming soon!)
* OS-related:
  * [**unattended-upgrades**](roles/unattended_upgrades)
  * netplan (coming soon!)
  * managing and distributing authorized SSH keys (coming soon!)

## Minimum required Ansible-version

* Ansible >= 2.14

## Installation

Install the collection via ansible-galaxy:

```shell
ansible-galaxy collection install hifis.software_services
```

## License

Apache-2.0

## Author

This role is maintained by [HIFIS Software Services](https://www.hifis.net/).
