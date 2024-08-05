<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: MIT
-->

# `hifis.toolkit.zammad` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/zammad.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/zammad.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/hifis-net/ansible-collection-toolkit/blob/main/LICENSES/MIT.txt)

An Ansible Role that installs and configures the web-based open source user
support/ticketing solution [Zammad](https://zammad.org/).

**Note:** This role does not install elasticsearch  and postgresql server.
See [Dependencies](#dependencies).

## Requirements

The below requirements are needed on the target host:

- [cryptography](https://pypi.org/project/cryptography/) >= 1.6.0

## Role Variables

```yaml
zammad_version: "6.3.0"
```

Zammad version to be installed.

```yaml
zammad_release_channel: "stable"
```

Choose another release channel for the Zammad packages.
Please refer to <https://packager.io/gh/zammad/zammad> for a complete list.

```yaml
zammad_domain_name: "{{ ansible_fqdn }}"
```

Zammad's fully qualified domain name.

```yaml
zammad_nginx_config_path: "/etc/nginx/sites-available/zammad.conf"
```

File path to Zammad's Nginx config.

```yaml
zammad_ssl_cert_path: "/etc/ssl/certs/zammad_cert.pem"
```

File path to the SSL/TLS certificate which is used for HTTPS.

```yaml
zammad_ssl_key_path: "/etc/ssl/private/zammad_key.pem"
```

File path to the SSL/TLS private key  which is used for HTTPS.

```yaml
zammad_ssl_cert:
```

Content of SSL/TLS certificate (**required**).

```yaml
zammad_ssl_key:
```

Content of SSL/TLS private key (**required**).
**Please note:** In the special case, that you previously put an SSL keypair
on the host, e.g. via Let's Encrypt, you must not configure the variables
`zammad_ssl_cert` and `zammad_ssl_key`.
Nevertheless, in each case the role will
validate, if the SSL key pair is given under the paths `zammad_ssl_key_path` and
`zammad_ssl_cert_path` are valid.

```yaml
zammad_nginx_server_tokens: "off"
```

Enable or disable emitting nginx version information in error pages or in the
_Server_ response header field. Please read the nginx
[docs](http://nginx.org/en/docs/http/ngx_http_core_module.html#server_tokens)
for further information.

```yaml
zammad_nginx_additional_server_configs:
  - |
      server {
        listen 80;
        server_name zammad.example.com zammad-old.example.com;
        return 301 https://zammad.example.com$request_uri;
      }
  - |
      server {
        listen 443 ssl;

        # ... SSL configuration

        server_name zammad-old.example.com;
        return 301 https://zammad.example.com$request_uri;
      }
```

Configure additional server directives in the Nginx configuration.
This allows to implement more use case specific adjustments, e.g.
configuring multiple domains or the redirection of outdated domains to the
most recent one.

```yaml
elasticsearch_url: "http://localhost:9200"
```

Elasticsearch server address.

## Dependencies

Zammad requires Elasticsearch and PostgreSQL database server.
This role has been successfully tested together with the following roles:

- Elasticsearch - [geerlingguy.elasticsearch](https://github.com/geerlingguy/ansible-role-elasticsearch)
- PostgreSQL - [geerlingguy.postgresql](https://galaxy.ansible.com/geerlingguy/postgresql)

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - role: hifis.toolkit.zammad
           become: yes
```

## License

MIT

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net/).
