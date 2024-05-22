<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# Changelog

## [v2.2.0](https://github.com/hifis-net/ansible-role-haproxy/tree/v2.2.0) (2023-11-29)

[Full Changelog](https://github.com/hifis-net/ansible-role-haproxy/compare/v2.1.0...v2.2.0)

**Closed issues:**

- Add PPA for HAProxy error bookworm version [\#125](https://github.com/hifis-net/ansible-role-haproxy/issues/125)

**Merged pull requests:**

- Prepare release version 2.2.0 [\#130](https://github.com/hifis-net/ansible-role-haproxy/pull/130) ([Normo](https://github.com/Normo))
- ci: improve coverage of ansible-lint command again [\#129](https://github.com/hifis-net/ansible-role-haproxy/pull/129) ([Normo](https://github.com/Normo))
- ci: make ci workflow working again [\#128](https://github.com/hifis-net/ansible-role-haproxy/pull/128) ([Normo](https://github.com/Normo))
- Bypass Add PPA for HAProxy if haproxy\_ppa\_version is empty [\#126](https://github.com/hifis-net/ansible-role-haproxy/pull/126) ([cnaslain](https://github.com/cnaslain))
- Bump ansible from 8.1.0 to 9.0.1 [\#124](https://github.com/hifis-net/ansible-role-haproxy/pull/124) ([dependabot[bot]](https://github.com/apps/dependabot))
- Feat: Add optional backend port [\#122](https://github.com/hifis-net/ansible-role-haproxy/pull/122) ([mindovermiles262](https://github.com/mindovermiles262))
- Bump yamllint from 1.32.0 to 1.33.0 [\#121](https://github.com/hifis-net/ansible-role-haproxy/pull/121) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.17.2 to 6.22.0 [\#118](https://github.com/hifis-net/ansible-role-haproxy/pull/118) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 3 to 4 [\#110](https://github.com/hifis-net/ansible-role-haproxy/pull/110) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.1.0 to 6.0.2 [\#109](https://github.com/hifis-net/ansible-role-haproxy/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule-plugins from 23.4.1 to 23.5.0 [\#104](https://github.com/hifis-net/ansible-role-haproxy/pull/104) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 1.1.2 to 2.1.0 [\#102](https://github.com/hifis-net/ansible-role-haproxy/pull/102) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.2 to 6.17.2 [\#101](https://github.com/hifis-net/ansible-role-haproxy/pull/101) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.0.1 to 5.1.0 [\#100](https://github.com/hifis-net/ansible-role-haproxy/pull/100) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.0.0 to 8.1.0 [\#99](https://github.com/hifis-net/ansible-role-haproxy/pull/99) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v2.1.0](https://github.com/hifis-net/ansible-role-haproxy/tree/v2.1.0) (2023-06-01)

[Full Changelog](https://github.com/hifis-net/ansible-role-haproxy/compare/v2.0.0...v2.1.0)

**Fixed bugs:**

- \[WARNING\]: failed to look up user haproxy. Create user up to this point in real play [\#89](https://github.com/hifis-net/ansible-role-haproxy/issues/89)
- Molecule folder not linted by molecule [\#55](https://github.com/hifis-net/ansible-role-haproxy/issues/55)

**Closed issues:**

- Add CONTRIBUTING file [\#93](https://github.com/hifis-net/ansible-role-haproxy/issues/93)
- Provide citation metadata [\#91](https://github.com/hifis-net/ansible-role-haproxy/issues/91)
-  Add codeowners to autoassign reviewers [\#90](https://github.com/hifis-net/ansible-role-haproxy/issues/90)

**Merged pull requests:**

- Bump ansible from 7.6.0 to 8.0.0 [\#97](https://github.com/hifis-net/ansible-role-haproxy/pull/97) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release of version 2.1.0 [\#96](https://github.com/hifis-net/ansible-role-haproxy/pull/96) ([Normo](https://github.com/Normo))
- Add CONTRIBUTING.md [\#95](https://github.com/hifis-net/ansible-role-haproxy/pull/95) ([Normo](https://github.com/Normo))
- Add codeowners to autoassign reviewers [\#94](https://github.com/hifis-net/ansible-role-haproxy/pull/94) ([Normo](https://github.com/Normo))
- Bump ansible from 6.5.0 to 7.6.0 [\#88](https://github.com/hifis-net/ansible-role-haproxy/pull/88) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.14.3 to 6.16.2 [\#87](https://github.com/hifis-net/ansible-role-haproxy/pull/87) ([dependabot[bot]](https://github.com/apps/dependabot))
- Ignore haproy user lookup errors during first dry-run in check\_mode [\#86](https://github.com/hifis-net/ansible-role-haproxy/pull/86) ([Normo](https://github.com/Normo))
- Bump yamllint from 1.28.0 to 1.32.0 [\#85](https://github.com/hifis-net/ansible-role-haproxy/pull/85) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.3 to 5.0.1 [\#84](https://github.com/hifis-net/ansible-role-haproxy/pull/84) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.6 to 6.14.1 [\#83](https://github.com/hifis-net/ansible-role-haproxy/pull/83) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 1.0.0 to 1.1.2 [\#77](https://github.com/hifis-net/ansible-role-haproxy/pull/77) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.3 to 6.8.6 [\#59](https://github.com/hifis-net/ansible-role-haproxy/pull/59) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#57](https://github.com/hifis-net/ansible-role-haproxy/pull/57) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.2 to 6.8.3 [\#56](https://github.com/hifis-net/ansible-role-haproxy/pull/56) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.1 to 4.0.2 [\#54](https://github.com/hifis-net/ansible-role-haproxy/pull/54) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v2.0.0](https://github.com/hifis-net/ansible-role-haproxy/tree/v2.0.0) (2022-10-14)

[Full Changelog](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.6.0...v2.0.0)

**Closed issues:**

- Release version 2.0.0 [\#52](https://github.com/hifis-net/ansible-role-haproxy/issues/52)
- Add support for HAProxy 2.6 and remove official HAProxy 2.2 support [\#34](https://github.com/hifis-net/ansible-role-haproxy/issues/34)
- Remove support for deprecated variables `backends` and `frontend_ip` [\#2](https://github.com/hifis-net/ansible-role-haproxy/issues/2)

**Merged pull requests:**

- Prepare release of version 2.0.0 [\#53](https://github.com/hifis-net/ansible-role-haproxy/pull/53) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.8.1 to 6.8.2 [\#51](https://github.com/hifis-net/ansible-role-haproxy/pull/51) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.4.0 to 6.5.0 [\#50](https://github.com/hifis-net/ansible-role-haproxy/pull/50) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.6.0 to 6.8.1 [\#49](https://github.com/hifis-net/ansible-role-haproxy/pull/49) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule-podman from 2.0.2 to 2.0.3 [\#47](https://github.com/hifis-net/ansible-role-haproxy/pull/47) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.5.2 to 6.6.0 [\#44](https://github.com/hifis-net/ansible-role-haproxy/pull/44) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.3.0 to 6.4.0 [\#43](https://github.com/hifis-net/ansible-role-haproxy/pull/43) ([dependabot[bot]](https://github.com/apps/dependabot))
- Remove variables `backends` and `frontend_ip` [\#41](https://github.com/hifis-net/ansible-role-haproxy/pull/41) ([tobiashuste](https://github.com/tobiashuste))
- Support HAProxy 2.4 and 2.6 and default to 2.6 [\#40](https://github.com/hifis-net/ansible-role-haproxy/pull/40) ([tobiashuste](https://github.com/tobiashuste))
- Bump yamllint from 1.27.1 to 1.28.0 [\#39](https://github.com/hifis-net/ansible-role-haproxy/pull/39) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.4.0 to 6.5.2 [\#38](https://github.com/hifis-net/ansible-role-haproxy/pull/38) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.3.0 [\#36](https://github.com/hifis-net/ansible-role-haproxy/pull/36) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.6.0](https://github.com/hifis-net/ansible-role-haproxy/tree/v1.6.0) (2022-08-16)

[Full Changelog](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.5.0...v1.6.0)

**Implemented enhancements:**

- Support Ubuntu 22.04 [\#28](https://github.com/hifis-net/ansible-role-haproxy/issues/28)
- Migrate changelog to github-changelog-generator [\#7](https://github.com/hifis-net/ansible-role-haproxy/issues/7)

**Closed issues:**

- Release version 1.6.0 [\#31](https://github.com/hifis-net/ansible-role-haproxy/issues/31)

**Merged pull requests:**

- Prepare release 1.6.0 [\#33](https://github.com/hifis-net/ansible-role-haproxy/pull/33) ([tobiashuste](https://github.com/tobiashuste))
- Remove renovate.json [\#32](https://github.com/hifis-net/ansible-role-haproxy/pull/32) ([Normo](https://github.com/Normo))
- Use Python 3.10 in the project [\#30](https://github.com/hifis-net/ansible-role-haproxy/pull/30) ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 22.04 [\#29](https://github.com/hifis-net/ansible-role-haproxy/pull/29) ([tobiashuste](https://github.com/tobiashuste))
- Use molecule-podman instead of molecule-docker [\#27](https://github.com/hifis-net/ansible-role-haproxy/pull/27) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 5.7.1 to 6.2.0 [\#26](https://github.com/hifis-net/ansible-role-haproxy/pull/26) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.0.2 to 6.4.0 [\#25](https://github.com/hifis-net/ansible-role-haproxy/pull/25) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 3.6.1 to 4.0.1 [\#24](https://github.com/hifis-net/ansible-role-haproxy/pull/24) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.26.3 to 1.27.1 [\#22](https://github.com/hifis-net/ansible-role-haproxy/pull/22) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump robertdebock/galaxy-action from 1.2.0 to 1.2.1 [\#16](https://github.com/hifis-net/ansible-role-haproxy/pull/16) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 0.14.0 to 1.0.0 [\#15](https://github.com/hifis-net/ansible-role-haproxy/pull/15) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.6.0 to 5.7.1 [\#10](https://github.com/hifis-net/ansible-role-haproxy/pull/10) ([dependabot[bot]](https://github.com/apps/dependabot))
- Migrate manual changelog to github-changelog-generator [\#8](https://github.com/hifis-net/ansible-role-haproxy/pull/8) ([Normo](https://github.com/Normo))
- Bump molecule from 3.6.0 to 3.6.1 [\#6](https://github.com/hifis-net/ansible-role-haproxy/pull/6) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 5.3.2 to 6.0.2 [\#5](https://github.com/hifis-net/ansible-role-haproxy/pull/5) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.3.0 to 5.6.0 [\#4](https://github.com/hifis-net/ansible-role-haproxy/pull/4) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add badges to README.md [\#3](https://github.com/hifis-net/ansible-role-haproxy/pull/3) ([Normo](https://github.com/Normo))
- Implement GitHub actions workflows [\#1](https://github.com/hifis-net/ansible-role-haproxy/pull/1) ([Normo](https://github.com/Normo))

## [v1.5.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.5.0) - 2022-02-22

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.4.0...v1.5.0)

### Changed

* Test role against HAProxy versions 2.2 and 2.4
  ([!56](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/56)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Set default version of HAProxy from v2.2 (LTS) to v2.4 (LTS)
  ([!55](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/55)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

### Fixed

* Fix regexp to determine installed version before comparing versions
  ([!54](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/54)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v1.4.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.4.0) - 2022-02-10

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.3.0...v1.4.0)

### Fixed

* Fix failing dry-run if ppa changes
  ([!50](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/50)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Use http-check send instead of hiding options in httpchk
  ([!52](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/52)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Changed

* Update Python dependencies to the latest versions
  ([!51](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/51)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v1.3.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.3.0) - 2021-11-23

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.2.0...v1.3.0)

### Changed

* Increase HAProxy version in file README
  ([!45](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/45)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).
* Bump project dependencies python version to 3.9
  ([!47](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/47)
  by [Normo](https://gitlab.com/Normo)).
* Update project dependencies
  ([!48](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/48)
  by [Normo](https://gitlab.com/Normo)).

### Fixed

* Set empty default value for backends and frontend_ip
  ([!46](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/46)
  by [Normo](https://gitlab.com/Normo)).

## [v1.2.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.2.0) - 2021-06-18

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.1.1...v1.2.0)

### Added

* Copy TLS chain file when self-signed cert creation is disabled
  ([!42](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/42)
  by [Normo](https://gitlab.com/Normo)).

### Changed

* Set more restrictive file permissions for others
  ([!43](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/43)
  by [Normo](https://gitlab.com/Normo)).

## [v1.1.1](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.1.1) - 2021-06-14

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.1.0...v1.1.1)

### Added

* Automate import to Ansible Galaxy via GitHub Actions
  ([!39](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/39)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Fixed

* Fix initial role execution if SSL certificate generation disabled
  ([!40](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/40)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v1.1.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.1.0) - 2021-06-11

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.0.1...v1.1.0)

### Changed

* Reduce DHParam size in molecule tests
  ([!32](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/32)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Update all Python dependencies to the most recent version
  ([!35](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/35)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Fixed

* Fix initial dry run and improve molecule test sequence
  ([!33](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/33)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Use FQDN for Ansible modules
  ([!34](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/34)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Add galaxy namespace hifis to the role metadata
  ([!37](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/37)
  by [Normo](https://gitlab.com/Normo)).
* Prefix unprefixed variables with haproxy_
  ([!36](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/36)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Deprecated

* Deprecate the variables `frontend_ip` and `backends` which are replaced
  by `haproxy_frontend_ip` and `haproxy_backends`.
  Support for the unprefixed variables will be removed in version 2.0.

## [v1.0.1](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.0.1) - 2021-01-29

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v1.0.0...v1.0.1)

### Fixed

- Check HAProxy configuration file via an Ansible handler
  ([!27](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/27)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v1.0.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v1.0.0) - 2021-01-25

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v0.2.0...v1.0.0)

### Added

- Check HAProxy configuration via a role task
  ([!22](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/22)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).
  
### Changed

- Update role meta information
  ([!24](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/24)
  by [Normo](https://gitlab.com/Normo)).
- Update README.md
  ([!25](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/25)
  by [Normo](https://gitlab.com/Normo)).

### Fixed

- Check package version of HAProxy to decide on install / upgrade step
  ([!21](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/21)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v0.2.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v0.2.0) - 2020-12-03

[List of commits](https://github.com/hifis-net/ansible-role-haproxy/compare/v0.1.0...v0.2.0)

### Added

- Configure DH param size via variable
  ([!15](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/15)
  by [Normo](https://gitlab.com/Normo)).

### Changed

- Improve and speed up the CI pipeline
  ([!12](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/12)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
- Add missing Pipfile.lock file and update Ansible to 2.10.0
  ([!11](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/11)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
- Resolve "HAProxy isn't restarted/reloaded on SSL config change"
  ([!16](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/16)
  by [Normo](https://gitlab.com/Normo)).
- Resolve "Make self-signed SSL generation optional"
  ([!17](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/17)
  by [Normo](https://gitlab.com/Normo)).
- Bump Ansible to 2.10.4
  ([!19](https://gitlab.com/hifis/ansible/haproxy-role/-/merge_requests/19)
  by [Normo](https://gitlab.com/Normo)).

## [v0.1.0](https://github.com/hifis-net/ansible-role-haproxy/releases/tag/v0.1.0) - 2020-08-14

### Added

Initial release of the Ansible HAProxy Role.


\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
