<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->
# Changelog

## [v0.5.1](https://github.com/hifis-net/ansible-role-netplan/tree/v0.5.1) (2024-05-22)

[Full Changelog](https://github.com/hifis-net/ansible-role-netplan/compare/v0.5.0...v0.5.1)

**Merged pull requests:**

- chore\(deps-dev\): bump netaddr from 0.10.1 to 1.0.0 [\#119](https://github.com/hifis-net/ansible-role-netplan/pull/119) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule from 6.0.3 to 24.2.0 [\#118](https://github.com/hifis-net/ansible-role-netplan/pull/118) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.22.2 to 24.2.0 [\#116](https://github.com/hifis-net/ansible-role-netplan/pull/116) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump yamllint from 1.33.0 to 1.34.0 [\#115](https://github.com/hifis-net/ansible-role-netplan/pull/115) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible from 9.1.0 to 9.2.0 [\#114](https://github.com/hifis-net/ansible-role-netplan/pull/114) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump reuse from 3.0.0 to 3.0.1 [\#111](https://github.com/hifis-net/ansible-role-netplan/pull/111) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump reuse from 2.1.0 to 3.0.0 [\#110](https://github.com/hifis-net/ansible-role-netplan/pull/110) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.22.1 to 6.22.2 [\#109](https://github.com/hifis-net/ansible-role-netplan/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump netaddr from 0.9.0 to 0.10.1 [\#108](https://github.com/hifis-net/ansible-role-netplan/pull/108) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 6.0.2 to 6.0.3 [\#106](https://github.com/hifis-net/ansible-role-netplan/pull/106) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v0.5.0](https://github.com/hifis-net/ansible-role-netplan/tree/v0.5.0) (2023-12-13)

[Full Changelog](https://github.com/hifis-net/ansible-role-netplan/compare/v0.4.0...v0.5.0)

**Fixed bugs:**

- Fix wide permissions warning [\#98](https://github.com/hifis-net/ansible-role-netplan/pull/98) ([chrisvanmeer](https://github.com/chrisvanmeer))

**Merged pull requests:**

- Update Ansible to 9.1.0 [\#105](https://github.com/hifis-net/ansible-role-netplan/pull/105) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-core from 2.15.2 to 2.15.8 [\#103](https://github.com/hifis-net/ansible-role-netplan/pull/103) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.17.2 to 6.22.1 [\#102](https://github.com/hifis-net/ansible-role-netplan/pull/102) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.32.0 to 1.33.0 [\#101](https://github.com/hifis-net/ansible-role-netplan/pull/101) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump netaddr from 0.8.0 to 0.9.0 [\#90](https://github.com/hifis-net/ansible-role-netplan/pull/90) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 3 to 4 [\#87](https://github.com/hifis-net/ansible-role-netplan/pull/87) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.1.0 to 6.0.2 [\#86](https://github.com/hifis-net/ansible-role-netplan/pull/86) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v0.4.0](https://github.com/hifis-net/ansible-role-netplan/tree/v0.4.0) (2023-08-22)

[Full Changelog](https://github.com/hifis-net/ansible-role-netplan/compare/v0.3.1...v0.4.0)

**Implemented enhancements:**

- Use FQCN everywhere [\#9](https://github.com/hifis-net/ansible-role-netplan/issues/9)
- Add badges to README [\#7](https://github.com/hifis-net/ansible-role-netplan/issues/7)

**Fixed bugs:**

- Molecule folder not linted by molecule [\#46](https://github.com/hifis-net/ansible-role-netplan/issues/46)
- Computed fully qualified role name of netplan does not follow current galaxy requirements [\#5](https://github.com/hifis-net/ansible-role-netplan/issues/5)
- Update Ansible Galaxy meta information [\#6](https://github.com/hifis-net/ansible-role-netplan/pull/6) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- Fix ansible-lint violations [\#79](https://github.com/hifis-net/ansible-role-netplan/issues/79)
- Replace deprecated gateway4 by routes [\#77](https://github.com/hifis-net/ansible-role-netplan/issues/77)
- Switch to molecule-podman [\#56](https://github.com/hifis-net/ansible-role-netplan/issues/56)
- Deprecation: Use 'ansible.utils.ipaddr' module instead [\#12](https://github.com/hifis-net/ansible-role-netplan/issues/12)

**Merged pull requests:**

- chore: setup changelog-generator and prepare version 0.4.0 [\#84](https://github.com/hifis-net/ansible-role-netplan/pull/84) ([tobiashuste](https://github.com/tobiashuste))
- fix: replace deprecated gateway4 by routes [\#83](https://github.com/hifis-net/ansible-role-netplan/pull/83) ([tobiashuste](https://github.com/tobiashuste))
- fix: get rid of ansible-lint violations [\#80](https://github.com/hifis-net/ansible-role-netplan/pull/80) ([tobiashuste](https://github.com/tobiashuste))
- fix: switch from docker to podman in molecule [\#78](https://github.com/hifis-net/ansible-role-netplan/pull/78) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.8.2 to 6.8.6 [\#51](https://github.com/hifis-net/ansible-role-netplan/pull/51) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#47](https://github.com/hifis-net/ansible-role-netplan/pull/47) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.1 to 4.0.2 [\#45](https://github.com/hifis-net/ansible-role-netplan/pull/45) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.4.0 to 6.8.2 [\#44](https://github.com/hifis-net/ansible-role-netplan/pull/44) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.4.0 to 6.5.0 [\#43](https://github.com/hifis-net/ansible-role-netplan/pull/43) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.4.0 [\#37](https://github.com/hifis-net/ansible-role-netplan/pull/37) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.27.1 to 1.28.0 [\#36](https://github.com/hifis-net/ansible-role-netplan/pull/36) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.6.0 to 6.2.0 [\#31](https://github.com/hifis-net/ansible-role-netplan/pull/31) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.0.2 to 6.4.0 [\#30](https://github.com/hifis-net/ansible-role-netplan/pull/30) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 3.6.1 to 4.0.1 [\#29](https://github.com/hifis-net/ansible-role-netplan/pull/29) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.26.3 to 1.27.1 [\#27](https://github.com/hifis-net/ansible-role-netplan/pull/27) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump robertdebock/galaxy-action from 1.2.0 to 1.2.1 [\#20](https://github.com/hifis-net/ansible-role-netplan/pull/20) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 0.14.0 to 1.0.0 [\#19](https://github.com/hifis-net/ansible-role-netplan/pull/19) ([dependabot[bot]](https://github.com/apps/dependabot))
- Use FQCN everywhere [\#10](https://github.com/hifis-net/ansible-role-netplan/pull/10) ([tobiashuste](https://github.com/tobiashuste))
- Add badges to README [\#8](https://github.com/hifis-net/ansible-role-netplan/pull/8) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 5.3.0 to 5.6.0 [\#4](https://github.com/hifis-net/ansible-role-netplan/pull/4) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 3.6.0 to 3.6.1 [\#3](https://github.com/hifis-net/ansible-role-netplan/pull/3) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 5.4.0 to 6.0.2 [\#2](https://github.com/hifis-net/ansible-role-netplan/pull/2) ([dependabot[bot]](https://github.com/apps/dependabot))
- Implement CI pipeline via GitHub Actions [\#1](https://github.com/hifis-net/ansible-role-netplan/pull/1) ([tobiashuste](https://github.com/tobiashuste))

**Changed on GitLab.com:**

- Update Python dependencies and use Python 3.9 in GitLab CI
  ([!17](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/17)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.3.1](https://gitlab.com/hifis/ansible/netplan-role/-/releases/v0.3.1) - 2021-05-05

[List of commits](https://gitlab.com/hifis/ansible/netplan-role/-/compare/v0.3.0...v0.3.1)

### Fixed

- Add checks to determine whether reboot of hosts are necessary when switching to Netplan
  ([!15](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/15)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [0.3.0](https://gitlab.com/hifis/ansible/netplan-role/-/releases/v0.3.0) - 2021-03-17

[List of commits](https://gitlab.com/hifis/ansible/netplan-role/-/compare/v0.2.1...v0.3.0)

### Added

- Backup configuration file when changing the Netplan network configuration
  ([!8](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/8)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).
- Add a section to file README to inform users about networking limitations of the role
  ([!10](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/10)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).
  
### Changed

- Use templating comments for copyright notice in template config.yaml.j2
  ([!7](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/7)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

### Fixed

- Reboot managed node if migrating networking from ifupdown to netplan
  ([!13](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/13)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [0.2.1](https://gitlab.com/hifis/ansible/netplan-role/-/releases/v0.2.1) - 2021-03-10

[List of commits](https://gitlab.com/hifis/ansible/netplan-role/-/compare/v0.2.0...v0.2.1)

### Fixed

- Remove task that uninstalls package 'ifupdown' from role tasks
  ([!6](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/6)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [0.2.0](https://gitlab.com/hifis/ansible/netplan-role/-/releases/v0.2.0) - 2021-03-01

[List of commits](https://gitlab.com/hifis/ansible/netplan-role/-/compare/v0.1.0...v0.2.0)

### Added

- Add a task that removes the package 'ifupdown' in favour of 'netplan'
  ([!2](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/2)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

### Changed

- Refine the Netplan configuration file template
  ([!3](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/3)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

### Changed

- Call handler to gather facts after IP addresses have been changed by Netplan
  ([!4](https://gitlab.com/hifis/ansible/netplan-role/-/merge_requests/4)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [0.1.0](https://gitlab.com/hifis/ansible/netplan-role/-/releases/v0.1.0) - 2021-01-25

### Added

Initial release of the Ansible Netplan Role.


\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
