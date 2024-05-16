<!--
SPDX-FileCopyrightText: 2022 Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: 2022 Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# hifis.keepalived Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/keepalived.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/keepalived.yml)

Ansible role to set up Keepalived in a high availability and scalability context.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 22.04 LTS
- Ubuntu 20.04 LTS

## Requirements

None.

## Role Variables

### Required variables which are not set by default

#### Keepalived instance unicast peer IP addresses

Set the unicast peer IP addresses of the Keepalived instance:

```yaml
keepalived_unicast_peers: 
  - '192.168.33.15'
  - '192.168.33.16'
```

#### Keepalived instance virtual IP address

Set the virtual IP address of the Keepalived instance:

```yaml
keepalived_virtual_ip_address: '192.168.33.100'
```

#### Optional: List of virtual IP address configs

If you need to configure multiple virtual IP addresses you can define this
optional variable. This takes precedence over `keepalived_virtual_ip_address`.

```yaml
keepalived_virtual_ipaddress_configs:
  - "10.0.10.15 dev eth0"
  - "10.0.11.15 dev eht1"
```

### All other Default Variables

#### Keepalived version

Variable to pin the Keepalived version to a certain value:

```yaml
keepalived_version: '2.2.8'
```

#### List of dependencies of Keepalived

List of Keepalived dependencies to be installed:

```yaml
keepalived_dependencies:
  - 'build-essential'
  - 'curl'
  - 'gcc'
  - 'libssl-dev'
  - 'libnl-3-dev'
  - 'libnl-genl-3-dev'
  - 'libsnmp-dev'
```

#### Keepalived executable path

Path to the Keepalived executable:

```yaml
keepalived_executable_path: '/usr/local/sbin/keepalived'
```

#### Keepalived Download URL

URL from which Keepalived can be downloaded:

```yaml
keepalived_download_url: 'https://www.keepalived.org/software/keepalived-{{ keepalived_version }}.tar.gz'
```

#### Keepalived configuration file template name

Name of the template file for Keepalived configuration file

```yaml
keepalived_conf_template: 'keepalived.conf.j2'
```

#### Keepalived configuration directory

Directory which contains Keepalived configuration files:

```yaml
keepalived_conf_dir: '/etc/keepalived'
```

#### Keepalived configuration file path

Path to Keepalived configuration file:

```yaml
keepalived_conf_file_path: '/etc/keepalived/keepalived.conf'
```

#### Keepalived sysconfig file path

Path to Keepalived sysconfig file:

```yaml
keepalived_sysconfig_file_path: "/etc/keepalived/keepalived.sysconfig"
```

#### Systemd service template file name

Name of the template file for Systemd service:

```yaml
keepalived_service_template: 'keepalived.service.j2'
```

#### Keepalived service file path

Path to Keepalived service file:

```yaml
keepalived_service_file_path: '/etc/systemd/system/keepalived.service'
```

#### Keepalived PID file path

Path to the Keepalived PID file:

```yaml
keepalived_pid_file_path: "/run/keepalived/keepalived.pid"
```

#### Configure notification email address

Configure recipient of notification emails:

```yaml
keepalived_notification_email: 'name@localhost'
```

#### Configure notification sender

Configure sender of notification emails:

```yaml
keepalived_notification_email_from: 'keepalived@localhost'
```

#### Configure SMTP Server

Configure IP address or FQDN of SMTP server:

```yaml
keepalived_smtp_server: '127.0.0.1'
```

#### Keepalived instance state MASTER or BACKUP

Set the state of the Keepalived instance to MASTER or BACKUP:

```yaml
keepalived_state: 'BACKUP'
```

#### Keepalived instance priority

Set the priority of the Keepalived instance:

```yaml
keepalived_priority: '99'
```

#### Keepalived maximum increased automatic priority

Maximum priority to which Keepalived can automatically increase (must be in
range [0, 99] or -1 to disable):

```yaml
keepalived_max_auto_priority: '99'
```

#### Keepalived instance router ID

Set unique name of the Keepalived router:

```yaml
keepalived_router_id: 'KEEPALIVED_2'
```

#### Keepalived instance weight

Adjust the priority by this weight:

```yaml
keepalived_weight: '0'
```

#### Keepalived instance unicast source IP address

Set the unicast source IP address of the Keepalived instance:

```yaml
keepalived_unicast_src_ip: '{{ ansible_default_ipv4.address }}'
```

#### Keepalived instance network interface

Set network interface to which the floating IP address is associated:

```yaml
keepalived_interface: "{{ ansible_default_ipv4.interface }}"
```

#### Keepalived instance virtual IP address and network interface

Set the virtual IP address and network interface of the Keepalived instance:

```yaml
keepalived_virtual_ipaddress_config: "{{ keepalived_virtual_ip_address }} dev {{ keepalived_interface }}"
```

#### Keepalived instance authentication password

Set the authentication password of the Keepalived instance:

```yaml
keepalived_auth_pass: 'changeme'
```

#### Enable script security

Flag to enable script security to prevent script to run by root user
if any part of the path is writable by a non-root user:

```yaml
keepalived_set_script_security_flag: true
```

#### User for executing Keepalived script

Specify username to run Keepalived script under:

```yaml
keepalived_script_user: 'haproxy'
```

#### Group for executing Keepalived script

Specify groupname to run Keepalived script under:

```yaml
keepalived_script_group: 'haproxy'
```

#### Flag to activate process tracking

Activate process tracking in keepalived config:

```yaml
keepalived_enable_process_tracking: true
```

#### Define which process shall be tracked

```yaml
keepalived_track_process: 'haproxy'
```

#### Flag to activate a script to be executed

Activate script that is executed by Keepalived:

```yaml
keepalived_activate_script: false
```

#### Name of the script to be executed

Specify the script name to be executed by Keepalived:

```yaml
keepalived_script_name: 'chk_haproxy_process'
```

#### Command of the script to be executed

Specify the command to be executed by Keepalived:

```yaml
keepalived_script_command: '/usr/bin/killall -0 haproxy'
```

## Dependencies

None.

Note: This role is intended for use with, but not limited to, the
[hifis.haproxy](https://gitlab.com/hifis/ansible/haproxy-role) role.

## Example Playbook

```yaml
- hosts: loadbalancers
  roles:
    - role: hifis.toolkit.keepalived
      vars:
        keepalived_virtual_ip_address: '192.168.33.100'
        keepalived_unicast_peers:
          - '192.168.33.15'
          - '192.168.33.16'
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://www.hifis.net)
