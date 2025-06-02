<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.haproxy` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/haproxy.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/haproxy.yml)

A role to set up HAProxy to be used as a load balancer in a high availability
and scalability context.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 24.04 LTS
- Ubuntu 22.04 LTS
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)

This role is tested against the four latest LTS versions of HAProxy.
Currently, this results in official support for the HAProxy release series:

- `3.0`
- `2.8` (not supported on Ubuntu 24.04)
- `2.6` (not supported on Ubuntu 24.04)
- `2.4` (not supported on Debian 12 and Ubuntu 24.04)

Other versions are known to work as well but are not automatically tested.

## Requirements

None.

## Role Variables

### Mandatory variables which are not set by default

#### Backend GitLab IP addresses

Specify a list of backends with name and IP address (Port is optional, defaults to `80`):

```yaml
haproxy_backends:
  - backend_name: 'backend_server_1'
    backend_ip: '192.168.33.10'
    backend_port: '80'
```

#### Frontend floating IP address

Specify the floating IP address of the frontend:

```yaml
haproxy_frontend_ip: '192.168.33.100'
```

### Compulsory variables which are set by default but need to be adapted

#### Number of processors used by HAProxy

Sets number of processors used by HAProxy:

```yaml
haproxy_nbproc: '1'
```

#### Number of threads used by HAProxy

Sets number of threads used by HAProxy:

```yaml
haproxy_nbthread: '2'
```

#### HAProxy CPU Map for Multithreading

Mapping threads to CPU cores:

```yaml
haproxy_cpumap: 'auto:1/1-2 0-1'
```

#### Enable/disable stats

Variable to enable or disable the stats:

```yaml
haproxy_stats_enable: 'enable'
```

#### Stats admin username

Variable to hold the stats admin username:

```yaml
haproxy_stats_admin_user: 'admin'
```

#### Stats admin user password

Variable to hold the stats admin user password:

```yaml
haproxy_stats_admin_user_password: 'changeme'
```

### All other default variables

#### Path to the executable of HAProxy

Path variable pointing to the location of the HAProxy executable:

```yaml
haproxy_executable_path: '/usr/sbin/haproxy'
```

#### HAProxy PPA version

Variable to pin the PPA version to a certain value:

```yaml
haproxy_ppa_version: 'ppa:vbernat/haproxy-3.2'
```

#### HAProxy version

Variable to pin the HAProxy version to a certain value:

```yaml
haproxy_version: '3.2.*'
```

#### HAProxy user

Variable to specify the HAProxy system user:

```yaml
haproxy_user: 'haproxy'
```

#### HAProxy group

Variable to specify the HAProxy system group:

```yaml
haproxy_group: 'haproxy'
```

#### HAProxy dependencies to be installed

List of HAProxy dependencies to be installed:

```yaml
haproxy_dependencies:
  - 'software-properties-common'
```

#### HAProxy binary name

Name of the HAProxy binary:

```yaml
haproxy_name: 'haproxy'
```

#### HAProxy configuration template

Provide the path to the HAProxy configuration template:

```yaml
haproxy_config_template: 'haproxy.cfg.j2'
```

#### HAProxy configuration directory path

Give the path to the HAProxy configuration directory:

```yaml
haproxy_conf_dir: '/etc/haproxy/'
```

#### HAProxy configuration file path

Give the path to the HAProxy configuration file:

```yaml
haproxy_conf_file_path: "/etc/haproxy/haproxy.cfg"
```

#### HAProxy logging socket path

Give the path to the HAProxy logging socket:

```yaml
haproxy_log_socket: '/dev/log'
```

#### HAProxy log level

Specify the log level of HAProxy.
Possible values are:
`emerg, alert, crit, err, warning, notice, info, debug`.

```yaml
haproxy_log_level: 'info'
```

#### HAProxy socket file path

Give the path to the HAProxy socket file:

```yaml
haproxy_socket: '/run/haproxy/admin.sock'
```

#### HAProxy self-signed SSL certificate creation

Whether to create a self-signed SSL certificate:

```yaml
haproxy_create_self_signed_cert: true
```

#### Country Name for SSL certificate

Set country to be used for the SSL certificate:

```yaml
haproxy_country_name: 'DE'
```

#### State name for SSL certificate

Set state to be used for the SSL certificate:

```yaml
haproxy_state_or_province_name: 'Saxony'
```

#### Locality Name for SSL certificate

Set locality to be used for the SSL certificate:

```yaml
haproxy_locality_name: 'Dresden'
```

#### Organization name for SSL certificate

Set organization to be used for the SSL certificate:

```yaml
haproxy_organization_name: 'Helmholtz-Zentrum Dresden-Rossendorf (HZDR)'
```

#### Organization Unit Name for SSL certificate

Set organization unit to be used for the SSL certificate:

```yaml
haproxy_organizational_unit_name: 'FWCC / Computational Science'
```

#### Email address for SSL certificate

Set email address to be used for the SSL certificate:

```yaml
haproxy_email_address: 'hifis-help@hzdr.de'
```

#### Common Name for SSL certificate

Set common name to be used for the SSL certificate:

```yaml
haproxy_common_name: 'Helmholtz Association'
```

#### HAProxy SSL directory path

Give the path to the HAProxy SSL directory:

```yaml
haproxy_ssl_certificate_dir: '/etc/haproxy/ssl'
```

#### HAProxy Private Key file path

Give the path to the HAProxy Private Key file:

```yaml
haproxy_ssl_certificate_key_file: "/etc/haproxy/ssl/haproxy.key"
```

#### HAProxy Certificate Signing Request file path

Give the path to the HAProxy Certificate Signing Request file:

```yaml
haproxy_ssl_certificate_csr_file: '/etc/haproxy/ssl/haproxy.csr'
```

#### HAProxy Certificate file path

Give the path to the HAProxy Certificate file:

```yaml
haproxy_ssl_certificate_crt_file: "/etc/haproxy/ssl/haproxy.crt"
```

#### HAProxy PKCS12 file path

Give the path to the HAProxy PKCS12 file:

```yaml
haproxy_ssl_certificate_pkcs12_file: "/etc/haproxy/ssl/haproxy.p12"
```

#### HAProxy Certificate Chain file path

Give the path to the HAProxy Certificate Chain file:

```yaml
haproxy_ssl_certificate_chain_file: "/etc/haproxy/ssl/haproxy.pem"
```

#### HAProxy Certificate Chain source file path

Give the path to the HAProxy Certificate Chain source file on the control node
which will be copied to the remote host:

```yaml
haproxy_ssl_cert_chain_src_file_path: "haproxy.pem"
```

**Note:** This variable is mandatory when `haproxy_create_self_signed_cert` is
set to `false`. The file should be PEM formatted and include at least the
public certificate and the private key.

#### HAProxy DH Parameter file path

Give the path to the DH Parameter file:

```yaml
haproxy_ssl_dhparam_file: "/etc/haproxy/ssl/dhparam.pem"
```

#### HAProxy DH Parameter size

Size (in bits) of the generated DH-params:

```yaml
haproxy_ssl_dhparam_size: 4096
```

## Dependencies

None.

**Please note:** This role is intended for use with, but not limited to, the
[`hifis.toolkit.keepalived`](roles/keepalived) role.

## Example playbook

```yaml
- hosts: loadbalancers
  roles:
    - role: hifis.toolkit.haproxy
      vars:
        haproxy_frontend_ip: '192.168.33.100'
        haproxy_backends:
          - backend_name: 'backend_server_1'
            backend_ip: '192.168.33.10'
            backend_port: 80
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net)

## Contributors

We would like to thank and give credits to the following contributors of this
project:

- [mindovermiles262](https://github.com/mindovermiles262)
- [cnaslain](https://github.com/cnaslain)
