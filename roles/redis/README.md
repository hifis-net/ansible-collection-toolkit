<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.redis` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/redis.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/redis.yml)

A role to set up Redis instances to be used as caching servers in a high
availability and scalability context.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS

## Requirements

None.

## Role variables

The Redis version to install:

```yaml
redis_version: '7.2.1'
```

Specifies whether the current node is `master`, or a `replica` instance:

```yaml
redis_instance_type: 'master'
```

The IP address to bind Redis to:

```yaml
redis_instance_ip: "127.0.0.1"
```

The Redis Master instance IP address:

```yaml
redis_master_instance_ip: "{{ redis_instance_ip if redis_instance_type == 'master' else None }}"
```

The name of the Redis cluster monitored by Sentinel:

```yaml
redis_cluster_name: 'redis-cluster'
```

Password used to authenticate in the Redis cluster:

```yaml
redis_password: 'changeme'
```

List of dependent packages required by Redis Server:

```yaml
redis_dependencies:
  - 'build-essential'
```

URL from which Redis Server can be downloaded:

```yaml
redis_download_url: "https://download.redis.io/releases/redis-{{ redis_version }}.tar.gz"
```

File path to the Redis Server binary:

```yaml
redis_bin: '/usr/local/bin/redis-server'
```

File path to the directory in which Redis Server is build:

```yaml
redis_build_dir: '/usr/local/src/redis-{{ redis_version }}'
```

Directory into which Redis service files are copied:

```yaml
redis_systemd_dir: '/etc/systemd/system'
```

Redis Server service file path:

```yaml
redis_server_service_file: '{{ redis_systemd_dir }}/redis-server.service'
```

Redis Sentinel service file path:

```yaml
redis_sentinel_service_file: '{{ redis_systemd_dir }}/redis-sentinel.service'
```

Password for Redis Sentinel. This is unset by default.

```yaml
redis_sentinel_password: 'changeme'
```

Redis configuration directory path:

```yaml
redis_configuration_dir: '/etc/redis'
```

Path to Redis Server configuration file:

```yaml
redis_server_configuration_file: '{{ redis_configuration_dir }}/redis.conf'
```

Path to Redis Sentinel configuration file:

```yaml
redis_sentinel_configuration_file: '{{ redis_configuration_dir }}/sentinel.conf'
```

Redis library directory:

```yaml
redis_lib_dir: '/var/lib/redis'
```

Redis logging directory:

```yaml
redis_log_dir: '/var/log/redis'
```

Path to Redis Server log file:

```yaml
redis_server_log_file_path: "{{ redis_log_dir }}/redis-server.log"
```

Path to Redis Sentinel log file:

```yaml
redis_sentinel_log_file_path: "{{ redis_log_dir }}/redis-sentinel.log"
```

Redis log level, can be one of: `debug`, `verbose`, `notice`, `warning`:

```yaml
redis_log_level: 'notice'
```

Sentinel log level, can be one of: `debug`, `verbose`, `notice`, `warning`:

```yaml
sentinel_log_level: 'notice'
```

Enable/disable Redis Server protected mode:

```yaml
redis_protected_mode: 'yes'
```

Enable/disable Redis Sentinel protected mode:

```yaml
sentinel_protected_mode: 'yes'
```

Redis username:

```yaml
redis_user: 'redis'
```

Redis group name:

```yaml
redis_group: 'redis'
```

Redis Server service name:

```yaml
redis_server_service_name: 'redis-server'
```

Redis Sentinel service name:

```yaml
redis_sentinel_service_name: 'redis-sentinel'

```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: hifis.toolkit.redis
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net)
