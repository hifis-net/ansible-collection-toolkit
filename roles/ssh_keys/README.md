<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# `hifis.toolkit.ssh_keys` Ansible Role

[![CI Status](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/ssh_keys.yml/badge.svg)](https://github.com/hifis-net/ansible-collection-toolkit/actions/workflows/ssh_keys.yml)

This Ansible role distributes authorized SSH public keys to users.

Currently [supported platforms](meta/main.yml) are:

- AlmaLinux 8
- AlmaLinux 9
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Debian 11 Bullseye
- Debian 12 Bookworm
- Debian 13 Trixie

## Requirements

None.

## Role Variables

```yaml
ssh_user_list:
  - name: jane
    create_user_account: true
    authorized_keys:
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJi3wBlOT+oR8Rd+YQsV8tUoQOd3NSUuyzJYQp8finD6 john@example.com
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDXkvy8jMmw45grnmYK+Ylk/mcc7IyG9taNseNiVrGjR8KRHVJpzEntW1g6SAomIGIpBLvviiyhal4E1v1bhpv2JopbiM3JDOck6gwc4AfpanjuZFPuq6stq5pF7bb2C+zliw16zTFL7bp09tD7nNs30GlchB5DU2sSn1zq4iC+eQ== john@example.com
```

In order to authorize SSH public keys you need to edit the variable
`ssh_user_list` and add a list entry containing the `name` of the user, a
list of `authorized_keys` and optionally the `create_user_account` flag if you
want the role to take care of creating the account. Each list entry corresponds
to one user account.

```yaml
ssh_authorized_keys_exclusive: true
```

Whether to remove all other non-specified keys from the authorized_keys file.

## Dependencies

None.

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - role: hifis.toolkit.ssh_keys
```

## License

[Apache-2.0](LICENSES/Apache-2.0.txt)

## Author Information

This role was created by [HIFIS Software Services](https://hifis.net/).
