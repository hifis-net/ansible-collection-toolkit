<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden - Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.gitlab_runner` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/gitlab_runner.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/gitlab_runner.yml)

This Ansible role provides a setup for GitLab CI in Openstack.

Currently [supported platforms](meta/main.yml) are:

- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Debian Buster
- Debian Bullseye
- Debian Bookworm

## Requirements

None.

## Role Variables

### GitLab-Runner variables

```yaml
gitlab_runner_version: "16.9.0"
```
The version of GitLab-Runner to install.

```yaml
gitlab_runner_pkg_version: "16.9.0-1"
```
The version to be used to determine the GitLab-Runner
[package](https://packages.gitlab.com/runner/gitlab-runner) (optional).

```yaml
gitlab_runner_deb_file: ""
```
If this is specified the package will be installed from a `.deb`-file.
If `://` is in the path, Ansible will attempt to download deb before installing.

```yaml
gitlab_runner_concurrent: 1
```
Limits how many jobs can run concurrently. The maximum number is all defined runners.
`0` does not mean unlimited.

```yaml
gitlab_runner_enable_session_server: false
```
Boolean flag to control whether the session_server should be configured.

```yaml
gitlab_runner_session_server_listen_address: "0.0.0.0:8093"
```
An internal URL (`host:port`) for the session server.

```yaml
gitlab_runner_sentry_dsn: "https://public@sentry.example.com/1"
```

Enables tracking of all system level errors to Sentry.
Empty string by default.

```yaml
gitlab_runner_session_server_advertise_address: "0.0.0.0:8093"
```
The URL (`host:port`) to access the session server. GitLab Runner exposes it to GitLab.

```yaml
gitlab_runner_session_server_timeout: 1800
```
Number of seconds the session can stay active after the job completes.

```yaml
gitlab_runner_install_docker: true
```
Decide wether to install Docker via
[geerlingguy.docker](https://galaxy.ansible.com/geerlingguy/docker) role.
Docker is required for the `docker` executor but not for the
`docker+machine` executor.

### Docker-machine variables

```yaml
gitlab_runner_docker_machine_binary_url: "https://gitlab.com/gitlab-org/ci-cd/docker-machine/-/releases/v0.16.2-gitlab.25/downloads/docker-machine-Linux-{{ ansible_architecture }}"
```

The URL where to download the docker-machine binary file from.

```yaml
gitlab_runner_docker_machine_binary_checksum: "sha256:04cc18c8f6ee0d71614064fa81116f20f3a37af53eeebf19bfb832ab9c46d3a0"
```

The checksum of the downloaded docker-machine binary. This must correspond to the file downloaded via the
`gitlab_runner_docker_machine_binary_url` variable.

### Flatcar Linux configuration

```yaml
gitlab_runner_transpiler_binary_url: "https://github.com/coreos/butane/releases/download/v0.20.0/butane-{{ ansible_architecture }}-unknown-linux-gnu"
```

The URL to the configuration transpiler binary that shall be used.

```yaml
gitlab_runner_transpiler_binary_checksum: "sha256:28003c61b991d17d66c23cd3f305202ae14736b8e7fd941986b6086cf931ed4b"
```

The checksum of the download transpiler binary. This must correspond to the file
downloaded via the `gitlab_runner_transpiler_binary_url` variable.

```yaml
gitlab_runner_namerservers:
    - 9.9.9.9
    - 149.112.112.112
```

The DNS nameservers to be used by the Openstack Flatcar virtual machine.

```yaml
gitlab_runner_registry_mirrors:
  - "http://registry-mirror-1.example"
  - "https://registry-mirror-2.example"
```

(Optional) A list of Docker registry mirrors to be used.
Takes precedence over the `gitlab_runner_registry_mirror` variable.

```yaml
gitlab_runner_insecure_registries:
  - "registry-mirror-1.example"
```

(Optional) A list of Docker registries or mirrors that are considered to be insecure.

```yaml
gitlab_runner_registry_mirror: "https://registry-mirror.example"
```

(Optional) The Docker registry mirror to be used.

```yaml
gitlab_runner_mtu: 1450
```

Configure the MTU (Maximum Transmission Unit) for the docker daemon in Flatcar
linux running in Openstack. The default of 1450 is proven to work for default
Openstack configurations. If you have a different setup, feel free to update
this value.  
**Please note:** This value can cause strange network issues if not configured
properly.

```yaml
gitlab_runner_set_default_network_opts: false
```

This variable enables the declaration of
[`default-network-opts`](https://docs.docker.com/engine/reference/commandline/dockerd/#default-network-options)
in the Docker daemon configuration options.
This helps to prevent docker-compose to create networks with an MTU of 1500,
even though a lower MTU is required.
With this change a user should not be required to set the MTU
on their own in docker-compose files.
Requires at least Docker 24.

```yaml
gitlab_runner_ssh_public_key: "./files/id_ed25519.pub"
gitlab_runner_ssh_private_key: "./files/id_ed25519"
```

The (optional) file path to the SSH key pair on the Ansible controller used for
communicating with Runners. If this is left empty the role creates a new SSH
key pair at `/etc/gitlab-runner/gitlab_runner_key(.pub)`.

```yaml
gitlab_runner_ssh_key_type: "ed25519"
```
Specifies the type of SSH key to create. The possible values are `ed25519`
(default), `ecdsa` or `rsa`.

```yaml
gitlab_runner_ssh_private_key_path: "/etc/gitlab-runner/gitlab_runner_key"
gitlab_runner_ssh_public_key_path: "/etc/gitlab-runner/gitlab_runner_key.pub"
```
The file paths to the SSH key pair on the Runner host.

### GitLab-Runner registration

In order to register a runner with the GitLab instance of your choice, you need
to edit the `gitlab_runner_list` variable and add a list entry.
Each list entry corresponds to one registered GitLab-Runner.

Below table lists and describes all available configuration options you can
specify for registering your GitLab-Runner with this Ansible role.

| Key                         | Example                         | Description                                                                                                                    |
|-----------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `name`                      | `"my-docker-runner"`            | The name of the registered runner.                                                                                             |
| `url`                       | `"https://gitlab.com"`          | The URL of the GitLab instance you want to register the runner with.                                                           |
| `description`               | `"My first Docker runner"`      | Description of the runner.                                                                                                     |
| `authentication_token`      | `"MY_SECURE_TOKEN"`             | The runner authentication token required to register the runner.                                                               |
| `executor`                  | `docker`                        | Specify, the runner [executor](https://docs.gitlab.com/runner/executors/#selecting-the-executor).                              |
| `limit`                     | `0`                             | Limit how many jobs can be handled concurrently by this token. Default is `0` (no limit).                                      |
| `environment`               | `["DOCKER_TLS_CERTDIR=/certs"]` | Append or overwrite environment variables.                                                                                     |
| `docker_image`              | `"python:3.8"`                  | Specify the default docker image to be used. Required for `docker` and `docker+machine` executor.                              |
| `docker_security_opts`      | `["seccomp=unconfined"]`        | Configure Docker security options.                                                                                             |
| `docker_devices`            | `["/dev/kfd", "/dev/dri"]`      | Add a host device to the container. Same syntax as the Docker `--device` flag.                                                 |
| `docker_volumes`            | `["/cache", "/certs/client"]`   | Additional volumes that should be mounted. Same syntax as the Docker -v flag.                                                  |
| `docker_shm_size`           | `2147483648`                    | Shared memory size for images (in bytes). Default is 0 resulting in a fallback to the Docker default.                          |
| `docker_cpus`               | `2`                             | Number of CPUs. Unset by default.                                                                                              |
| `docker_memory`             | `2g`                            | Docker container memory limit. Unset by default.                                                                               |
| `docker_gpus`               | `all`                           | Specify GPUs to make available in Docker containers. Unset by default.                                                         |
| `docker_network_mtu`        | `1442`                          | A custom MTU is necessary in some environments like VMs in Openstack. Requires Gitlab-Runner >= `16.5`                         |
| `docker_privileged`         | `False`                         | Specify, if the container runs in privileged mode (insecure). Default is `False`.                                              |
| `docker_tls_verify`         | `True`                          | Specify, if TLS connections to the Docker daemon should be verified. Default is `False`.                                       |
| `docker_disable_cache`      | `False`                         | Specify, to disable the use of automatically created docker volumes for caching.                                               |
| `machine_driver`            | `"openstack"`                   | The driver to use when creating the machine via `docker-machine`.                                                              |
| `machine_name`              | `"auto-scale-%s"`               | The machine name template. (You need to include `%s`).                                                                         |
| `machine_options`           | See the machine example.        | Additional machine creation options.                                                                                           |
| `machine_idle_count`        | `2`                             | Number of machines that need to be created and waiting in Idle state. Default is `0`.                                          |
| `machine_idle_scale_factor` | `0.0`                           | *(Experimental)* Number of Idle machines as a factor of the number of machines currently in use. Default is `0.0`.             |
| `machine_idle_count_min`    | `1`                             | Minimal number of machines that need to be created and waiting in Idle state when the IdleScaleFactor is in use. Default is 1. |
| `machine_idle_time`         | `1800`                          | Time (in seconds) for machine to be in Idle state before it is removed. Default is `0`.                                        |
| `machine_max_growth_rate`   | `1`                             | The maximum number of machines that can be added to the runner in parallel. Default is `0` (no limit).                         |
| `machine_max_builds`        | `1`                             | Maximum job (build) count before machine is removed. Default is `0`.                                                           |
| `cache_type`                | `"s3"`                          | Type of caching to use. Currently only `s3` is supported by this role.                                                         |
| `cache_server_address`      | `"https://s3.hifis.net"`        | A `host:port` for the S3-compatible server.                                                                                    |
| `cache_access_key`          | `"key"`                         | The access key specified for your S3 instance..                                                                                |
| `cache_secret_key`          | `"secret"`                      | The secret key specified for your S3 instance.                                                                                 |
| `cache_bucket_name`         | `"bucket-name"`                 | Name of the storage bucket where cache is stored.                                                                              |
| `cache_bucket_location`     | `"eu-west-1"`                   | Name of S3 region. (optional)                                                                                                  |
| `cache_insecure`            | `"false"`                       | Set to `"true"` if the S3 service is available by HTTP. Default is `"false"`.                                                  |

#### Docker Example

```yaml
gitlab_runner_list:
    - name: "my-docker-runner"
      url: "https://gitlab.com"
      description: "My first Docker runner via Ansible."
      authentication_token: ${AUTHENTICATION_TOKEN}
      executor: "docker"
      environment: ["CI_CPUS=8", "DOCKER_TLS_CERTDIR=/certs"]
      docker_image: "python:3.8"
      docker_volumes: ["/cache", "/certs/client"]
      limit: 5
      # Optional cache configuration, only S3 is supported for now
      cache_type: "s3"
      cache_server_address: "https://cache.example"
      cache_access_key: "key"
      cache_secret_key: "secret"
      cache_bucket_name: "bucket"
      cache_insecure: "false"
```

For registering a runner using the Docker backend, a sample configuration is
given above.
Therefore, you need to obtain a registration token.
This can be either done on an instance, a group or a project level.
Visit the [GitLab documentation](https://docs.gitlab.com/runner/register/#requirements)
for further information.
In a production setup, please make sure to encrypt the token using
[Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

### Docker-machine Example

```yaml
gitlab_runner_list:
    - name: "test01"
      url: "https://gitlab.com"
      description: "Molecule test runner"
      authentication_token: "AUTHENTICATION_TOKEN"
      executor: "docker+machine"
      docker_image: "python:3.8"
      docker_volumes: ["/cache", "/certs/client"]
      machine_idle_count: 2
      machine_idle_time: 3600
      machine_max_growth_rate: 2
      machine_max_builds: 5
      machine_driver: "openstack"
      machine_name: "auto-scale-%s"
      machine_options:
        - "openstack-auth-url=https://openstack.example:5000/v3"
        - "openstack-image-id=73f07dd3-fa8b-468f-b6bc-b0cd4510f5d0"
        - "openstack-flavor-name=m1.small"
        - "openstack-net-id=7834deeb-8bd5-4fc7-b35b-24035d8f47a7"
        - "openstack-username=gitlab-runner"
        - "openstack-password=secret"
        - "openstack-tenant-id=123456"
        - "openstack-domain-name=default"
        - "openstack-ssh-user=core"
        - "openstack-sec-groups=Internal"
        - "openstack-keypair-name=runners-internal"
        - "openstack-private-key-file=/etc/gitlab-runner/gitlab_runner_key"
        - "openstack-user-data-file=/etc/gitlab-runner/ignition.json"
        - "openstack-active-timeout=300"
        - "engine-registry-mirror=https://registry-mirror.example"
```

The most important changes compared to the docker runner registration is the
configuration of docker-machine.
Therefore, a suitable configuration for the
[driver](https://docs.docker.com/machine/drivers/) of your choice needs to be
created.
This project focuses on providing the best integration with Openstack but is
probably not limited to that.
The Openstack driver lists all possible configuration options that can be
specified via `machine_options`: https://docs.docker.com/machine/drivers/openstack/

## Docker-in-Docker if MTU other than 1500

If the Docker-MTU does not match 1500 which is very often the case for
Openstack installations, certain additional configuration is required.
Please make sure to add

```
"engine-opt=mtu={{ gitlab_runner_mtu }}"
```

to the list of your runner's `machine_options`.
`gitlab_runner_mtu` needs to be set to the correct value.

Also you can configure Docker-in-Docker to make use of a registry mirror by
setting `gitlab_runner_registry_mirrors` or`gitlab_runner_registry_mirror`
to the required value.
This is optional.

To make this all work you finally need to mount a file in your runner volume
configuration by adding

```
"/opt/docker/daemon.json:/etc/docker/daemon.json:ro"
```

to the list of configured `volumes`.

### Beta: GitLab-Runner Autoscaling

GitLab-Runner Autoscaling is the future way of implementing autoscaling on
cloud infrastructures.
This is the successor to the autoscaling technology based on Docker Machine,
which is deprecated and will no longer be supported through the course of 2025.
The new beta feature implements support for the new method in Openstack.

#### Variables

It is important to set these variables. Otherwise the role execution will fail.

```yaml
gitlab_runner_autoscaler_plugin_url: "https://down.load/fleeting-plugin-openstack-binary"
```

The URL where to download the autoscaler plugin binary from.

```yaml
gitlab_runner_autoscaler_plugin_checksum: "sha256:..."
```

The checksum of the autoscaler plugin binary file.

```yaml
gitlab_runner_autoscaler_openstack_auth_url: "https://openstack.example:5000/v3"
```

The Openstack authentication URL of Keystone.

```yaml
gitlab_runner_autoscaler_openstack_username: "gitlab-runner"
```

The username of the Openstack user to interact with the API.

```yaml
gitlab_runner_autoscaler_openstack_password: "123456"
```

The corresponding password of the user.

```yaml
gitlab_runner_autoscaler_openstack_project_id: "project_id"
```

Specify the project id in Openstack.

```yaml
gitlab_runner_autoscaler_openstack_user_domain_name: "Default"
```

Domain name of the user authenticating with Openstack.

```yaml
gitlab_runner_autoscaler_openstack_region_name: "RegionOne"
```

Region name of the Openstack cluster.

#### Example configuration

```yaml
gitlab_runner_list:
  - name: "Test Runner"
    url: "https://gitlab.com"
    description: "Autoscale Runner for Openstack"
    limit: 0
    authentication_token: "{{ gitlab_runner_authentication_token }}"
    executor: "docker-autoscaler"
    environment: "test"
    docker_image: "ubuntu:latest"
    docker_disable_cache: True
    docker_volumes: ["/tmp/certs:/certs", "/opt/docker/daemon.json:/etc/docker/daemon.json:ro"]
    docker_shm_size: 2147483648
    docker_privileged: true
    docker_network_mtu: "{{ gitlab_runner_mtu }}"
    locked: false
    tags: "{{ gitlab_runner_tags | default([]) }}"
    run_untagged: "{{ gitlab_runner_run_untagged | default(false) }}"
    cache_insecure: "false"
    autoscaler_max_builds: 1
    autoscaler_idle_count: 4
    autoscaler_max_instances: "10"
    autoscaler_group_name: "autoscaler-runners"
    autoscaler_cloud_name: "openstack"
    autoscaler_clouds_config: "/etc/gitlab-runner/clouds.yaml"
    autoscaler_flavor_ref: "5be35abe-a4d5-427f-a0f8-c7afe19961e2"
    autoscaler_image_ref: "8225b31c-86fc-4e48-a3e4-8bf800d5fc8d"
    autoscaler_network_id: "ea80dd07-5dc2-4f18-af04-733ace5892ef"
    autoscaler_security_group: "c693de06-7dba-4694-9fd6-1b785904eff3"
    autoscaler_scheduler_hint: "c98090ea-6893-4810-b066-5c3f34038c2a"
    autoscaler_username: "core"
    autoscaler_keyname: "runner-internal"
```

## Dependencies

GitLab-Runner for Openstack depends on `docker-machine` requiring docker to be available on the system.

- Docker - [geerlingguy.docker](https://galaxy.ansible.com/geerlingguy/docker)

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: hifis.toolkit.gitlab_runner
      become: true
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net/).
