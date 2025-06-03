<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.netplan` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/netplan.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/netplan.yml)

Ansible role to install and configure Netplan.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS

## Requirements

None.

## Role variables

### Mandatory variables which are not set by default

#### Sample network configuration

Sample configuration to set up networking with Netplan:

```yaml
netplan_ethernets:
  - interface_name: 'eth0'
    dhcp4: 'no'
    routes:
      - to: 'default'
        via: '10.123.0.1'
    addresses:
      - '10.123.0.10/24'
    nameservers:
      addresses:
        - '8.8.8.8'
        - '9.9.9.9'
      search:
        - 'domain.local'
        - 'domain.name'
```

### Variables that are set with defaults

#### Flag to delete any pre-existing Netplan configuration files

Flag decides on whether pre-existing Netplan configuration files should be deleted:

```yaml
netplan_remove_existing_configs: true
```

#### Name of the Netplan configuration file template

Name of the template providing the Netplan configuration file:

```yaml
netplan_configuration_file_template: 'config.yaml.j2'
```

#### Directory of the Netplan configuration files

Directory of the Netplan configuration files:

```yaml
netplan_configuration_dir: '/etc/netplan'
```

#### Name of the Netplan configuration file

Name of the Netplan configuration file:

```yaml
netplan_configuration_file: 'config.yaml'
```

#### Path to the Netplan configuration file

Path to the Netplan configuration file:

```yaml
netplan_configuration_file_path: "{{ (netplan_configuration_dir, netplan_configuration_file) | path_join }}"
```

#### Packages to be installed

List of packages that need to be installed:

```yaml
netplan_packages:
  - 'netplan.io'
```

#### Package ifupdown network configuration file

Network configuration file that is present if networking is managed by package ifupdown:

```yaml
ifupdown_ifstate_file: '/run/network/ifstate'
```

## Troubleshooting

### Cleaning Up: Please uninstall package ifupdown manually

Before the package `ifupdown` can be safely removed netplan networking
needs to be properly configured.
If the package is removed too early, the role will hang.

For that reason this role does **not** handle the removal of the `ifupdown` package.

## Limitations

### Bootstrapping network configurations is not supported

Please note that networking configurations can not be bootstrapped during
role execution.
The respective managed nodes need networking to be configured beforehand.

### No support for changing the IP over which Ansible connects

Be aware that this role does not support changing the IP addresses
over which Ansible connects out of the box.
If you change the IP address over which Ansible connects,
you might end up in a hanging role as soon as `netplan apply`
is executed.
Ansible loses its SSH connection in that case.

## Dependencies

None.

## Example Playbook

```yaml
    - hosts: servers
      vars:
        netplan_ethernets:
          - interface_name: 'eth0'
            dhcp4: 'no'
            routes:
              - to: 'default'
                via: '10.123.0.1'
            addresses:
              - '10.123.0.10/24'
            nameservers:
              addresses:
                - '8.8.8.8'
                - '9.9.9.9'
              search:
                - 'domain.local'
                - 'domain.name'
      roles:
         - role: hifis.toolkit.netplan
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net/).
