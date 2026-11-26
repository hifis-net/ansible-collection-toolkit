<!--
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.docker_compose` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/docker_compose.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/docker_compose.yml)

A generic role to deploy a service on a host using [Docker Compose](https://docs.docker.com/compose/).
The role renders templates and copies static files into a project directory and then runs
`docker compose up`. This keeps the actual service configuration in the inventory, while the role
takes care of the deployment mechanics.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Ubuntu 26.04 LTS

## Requirements

- Docker Engine with the Docker Compose plugin (>= 2.18.0) installed on the target host
- The [community.docker](https://galaxy.ansible.com/ui/repo/published/community/docker/) collection

## Role variables

The name of the Docker Compose project:

```yaml
docker_compose_project_name: 'docker_compose'
```

Directory on the target host that holds the rendered templates, copied files and the Compose file.
All `dest` paths are relative to this directory. It is created if it does not exist:

```yaml
docker_compose_dir: "{{ ('/opt', docker_compose_project_name) | path_join }}"
```

Owner and group of the project directory and all deployed files:

```yaml
docker_compose_owner: 'root'
docker_compose_group: 'root'
```

Permissions of the project directory and of the directories created for `dest` entries:

```yaml
docker_compose_dir_mode: '0755'
```

Default permissions of deployed files. This can be overridden for each entry with the optional
`mode` key:

```yaml
docker_compose_default_file_mode: '0640'
```

Templates rendered into the project directory before the Compose setup is started. Each entry
requires a `src` and a `dest`. Missing parent directories of `dest` are created. The optional
`mode` defaults to `docker_compose_default_file_mode`:

```yaml
docker_compose_template_files:
  - src: 'docker-compose.yml.j2'
    dest: 'docker-compose.yml'
    mode: '0640'
```

Static files copied into the project directory before the Compose setup is started. Each entry
requires a `src` and a `dest`. Missing parent directories of `dest` are created. The optional
`mode` defaults to `docker_compose_default_file_mode`:

```yaml
docker_compose_files:
  - src: 'app.env'
    dest: 'config/app.env'
    mode: '0600'
```

Image pull policy for `docker compose up`. One of `always`, `missing`, `never` or `policy`:

```yaml
docker_compose_pull: 'missing'
```

## Dependencies

The role requires Docker with the Compose plugin on the target host, but it does not install or
configure Docker itself. The [geerlingguy.docker](https://galaxy.ansible.com/ui/repo/published/geerlingguy/docker/)
role can be used for that, for example in a prepare playbook.

## Example Playbook

```yaml
- hosts: servers
  vars:
    docker_compose_project_name: 'my-service'
    docker_compose_template_files:
      - src: 'docker-compose.yml.j2'
        dest: 'docker-compose.yml'
    docker_compose_files:
      - src: 'my-service.env'
        dest: 'my-service.env'
  roles:
    - role: hifis.toolkit.docker_compose
```

The referenced Compose file can look like this:

```yaml
# templates/docker-compose.yml.j2
services:
  app:
    image: "{{ my_service_image }}"
    restart: "unless-stopped"
    env_file:
      - "my-service.env"
    ports:
      - "{{ my_service_port }}:8080"
```

If a rendered template or copied file changes, the role restarts the Compose project via a
handler.

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net).
