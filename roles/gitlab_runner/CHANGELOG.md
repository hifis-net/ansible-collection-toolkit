<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden - Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# Changelog

## [v3.0.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v3.0.0) (2024-05-07)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v2.1.0...v3.0.0)

**Implemented enhancements:**

- Add support for Ubuntu 24.04 [\#254](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/254)
- Allow to configure GitLab Runner Autoscaling without docker-machine [\#251](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/251)

**Fixed bugs:**

- Fix docker config file if variable is set to false [\#253](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/253) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- Require at least ansible-core 2.15 [\#257](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/257)

**Merged pull requests:**

- Require at least ansible-core 2.15 [\#258](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/258) ([tobiashuste](https://github.com/tobiashuste))
- Update all dependencies [\#256](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/256) ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 24.04 [\#255](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/255) ([tobiashuste](https://github.com/tobiashuste))
- Beta: implement autoscaling using new autoscaler method [\#252](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/252) ([tobiashuste](https://github.com/tobiashuste))
- Try new package registration method [\#239](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/239) ([tobiashuste](https://github.com/tobiashuste))

## [v2.1.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v2.1.0) (2024-04-19)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v2.0.2...v2.1.0)

**Implemented enhancements:**

- Support sentry\_dsn parameter [\#248](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/248)

**Merged pull requests:**

- feat: allow to configure the sentry\_dsn parameter [\#249](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/249) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps-dev\): bump reuse from 3.0.1 to 3.0.2 [\#247](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/247) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v2.0.2](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v2.0.2) (2024-03-12)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v2.0.1...v2.0.2)

**Merged pull requests:**

- Get rid of Poetry warning [\#245](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/245) ([tobiashuste](https://github.com/tobiashuste))
- Update Butane to version 0.20.0 [\#244](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/244) ([tobiashuste](https://github.com/tobiashuste))
- Install most recent docker-machine version 0.16.2-gitlab.25 [\#243](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/243) ([tobiashuste](https://github.com/tobiashuste))

## [v2.0.1](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v2.0.1) (2024-03-04)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v2.0.0...v2.0.1)

**Fixed bugs:**

- Allow to renew GPG repository key with same ID [\#240](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/240) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release 2.0.1 [\#241](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/241) ([tobiashuste](https://github.com/tobiashuste))

## [v2.0.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v2.0.0) (2024-02-29)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.15.0...v2.0.0)

**UPGRADE NOTES AND BREAKING CHANGES:**

As of this release the role switched to the new runner registration workflow.
The ability to pass a [deprecated](https://docs.gitlab.com/ee/security/token_overview.html#runner-registration-tokens-deprecated) runner registration token has been removed.
Please use a [runner authentication token](https://docs.gitlab.com/ee/security/token_overview.html#runner-authentication-tokens) to register your runner.
The `registration_token` parameter has been replaced by `authentication_token`.
Please make sure that you adjust your config accordingly. [More...](https://docs.gitlab.com/ee/ci/runners/new_creation_workflow.html)

**Implemented enhancements:**

- Allow to remove session\_server configuration [\#175](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/175)
- Allow to remove the cache configuration [\#4](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/4)

**Closed issues:**

- Apply new gitlab-runner package version scheme [\#234](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/234)
- gitlab-runner registration token deprecated [\#104](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/104)

**Merged pull requests:**

- chore: prepare release v2.0.0 [\#237](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/237) ([Normo](https://github.com/Normo))
- fix: apply new runner version scheme [\#236](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/236) ([Normo](https://github.com/Normo))
- Deploy runner configuration via a template file  [\#233](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/233) ([Normo](https://github.com/Normo))
- chore\(deps-dev\): bump yamllint from 1.35.0 to 1.35.1 [\#232](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/232) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.15.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.15.0) (2024-02-16)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.14.0...v1.15.0)

**Implemented enhancements:**

- feat: configure default-network-opts mtu [\#229](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/229) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- fix: use modern podman in ci to fix random failures [\#230](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/230) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps-dev\): bump yamllint from 1.34.0 to 1.35.0 [\#228](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/228) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule-plugins from 23.5.0 to 23.5.3 [\#227](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/227) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump yamllint from 1.33.0 to 1.34.0 [\#226](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/226) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump reuse from 2.1.0 to 3.0.1 [\#225](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/225) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule from 6.0.2 to 6.0.3 [\#220](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/220) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible from 8.6.1 to 8.7.0 [\#219](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/219) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.22.0 to 6.22.1 [\#218](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/218) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.14.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.14.0) (2023-12-14)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.13.0...v1.14.0)

**Implemented enhancements:**

- feat: allow to define the s3 bucket location [\#221](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/221) ([tobiashuste](https://github.com/tobiashuste))

## [v1.13.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.13.0) (2023-11-23)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.12.0...v1.13.0)

**Implemented enhancements:**

- Allow to downgrade GitLab-Runner package [\#214](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/214)

**Merged pull requests:**

- chore: prepare release version 1.13.0 [\#216](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/216) ([tobiashuste](https://github.com/tobiashuste))
- feat: allow to downgrade gitlab-runner package [\#215](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/215) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps\): bump ansible from 8.5.0 to 8.6.1 [\#213](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/213) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump yamllint from 1.32.0 to 1.33.0 [\#212](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/212) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.21.1 to 6.22.0 [\#210](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/210) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.12.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.12.0) (2023-10-26)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.11.0...v1.12.0)

**Implemented enhancements:**

- Allow configuration of network\_mtu in Docker executor [\#205](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/205)

**Merged pull requests:**

- refactor: strip whitespaces before registry-mirrors in flatcar template [\#207](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/207) ([Normo](https://github.com/Normo))
- chore: prepare release of version 1.12.0 [\#208](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/208) ([tobiashuste](https://github.com/tobiashuste))
- feat: allow to configure network\_mtu parameter [\#206](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/206) ([tobiashuste](https://github.com/tobiashuste))

## [v1.11.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.11.0) (2023-10-25)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.10.0...v1.11.0)

**Implemented enhancements:**

- Allow to configure insecure registries in Flatcar config [\#202](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/202)

**Merged pull requests:**

- chore: prepare release of v1.11.0 [\#203](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/203) ([tobiashuste](https://github.com/tobiashuste))
- feat: configure insecure registries in Flatcar config [\#201](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/201) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps-dev\): bump ansible-lint from 6.20.3 to 6.21.1 [\#200](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/200) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.10.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.10.0) (2023-10-13)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.9.0...v1.10.0)

**Fixed bugs:**

- Update Flatcar configuration [\#193](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/193)

**Closed issues:**

- Release version 1.10.0 [\#196](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/196)

**Merged pull requests:**

- chore: prepare release of v1.10.0 [\#197](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/197) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps-dev\): bump ansible-lint from 6.18.0 to 6.20.3 [\#195](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/195) ([dependabot[bot]](https://github.com/apps/dependabot))
- Make Flatcar configuration compatible with most recent release [\#194](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/194) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps\): bump ansible from 8.2.0 to 8.5.0 [\#192](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/192) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump actions/checkout from 3 to 4 [\#190](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/190) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule from 5.1.0 to 6.0.2 [\#189](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/189) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.17.2 to 6.18.0 [\#188](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/188) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule-plugins from 23.4.1 to 23.5.0 [\#184](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/184) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.9.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.9.0) (2023-07-21)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.8.0...v1.9.0)

**Implemented enhancements:**

- Allow to disable local Docker volumes based cache [\#181](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/181)

**Merged pull requests:**

- feat: allow to disable local docker cache [\#182](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/182) ([Normo](https://github.com/Normo))
- chore\(deps-dev\): bump reuse from 1.1.2 to 2.1.0 [\#180](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/180) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible from 8.1.0 to 8.2.0 [\#179](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/179) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.8.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.8.0) (2023-07-03)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.7.0...v1.8.0)

**Implemented enhancements:**

- Add support for Debian 12 [\#168](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/168)
- Add support for session\_server config  [\#165](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/165)
- Errors on first run in check\_mode [\#159](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/159)
- feat: add support for Debian 12 [\#170](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/170) ([tobiashuste](https://github.com/tobiashuste))
- feat: add initial dry-run support [\#158](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/158) ([Normo](https://github.com/Normo))

**Fixed bugs:**

- fix: skip registration tasks in initial dry run [\#166](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/166) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- Remove official support for unsupported Ansible versions [\#172](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/172)
- Remove official support for Ubuntu 18.04 [\#167](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/167)
- Provide citation metadata [\#160](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/160)

**Merged pull requests:**

- chore: update ansible-lint and update poetry reference [\#174](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/174) ([tobiashuste](https://github.com/tobiashuste))
- chore: prepare release v1.8.0 [\#176](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/176) ([Normo](https://github.com/Normo))
- chore: set minimum ansible version to 2.13 [\#173](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/173) ([Normo](https://github.com/Normo))
- feat: enable session\_server configuration [\#171](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/171) ([Normo](https://github.com/Normo))
- chore!: drop official support for Ubuntu 18.04 [\#169](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/169) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.15.0 to 6.17.0 [\#164](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/164) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.0.1 to 5.1.0 [\#163](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/163) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.0.0 to 8.1.0 [\#162](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/162) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore: add CITATION.cff [\#161](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/161) ([Normo](https://github.com/Normo))
- Bump ansible from 7.4.0 to 8.0.0 [\#157](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/157) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.30.0 to 1.32.0 [\#155](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/155) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.0.0 to 5.0.1 [\#151](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/151) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule-plugins from 23.4.0 to 23.4.1 [\#150](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/150) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.14.6 to 6.15.0 [\#147](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/147) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.4 to 5.0.0 [\#146](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/146) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.14.3 to 6.14.6 [\#145](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/145) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.7.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.7.0) (2023-03-30)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.6.1...v1.7.0)

**Closed issues:**

- Use Butane 0.17.0 by default [\#139](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/139)
- Update default docker-machine binary [\#137](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/137)

**Merged pull requests:**

- Bump ansible from 7.3.0 to 7.4.0 [\#141](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/141) ([dependabot[bot]](https://github.com/apps/dependabot))
- Use Butane 0.17.0 per default [\#140](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/140) ([tobiashuste](https://github.com/tobiashuste))
- Use Docker-Machine v0.16.2-gitlab.20 by default [\#138](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/138) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.12.2 to 6.14.3 [\#136](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/136) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.29.0 to 1.30.0 [\#135](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/135) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.2.0 to 7.3.0 [\#131](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/131) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.11.0 to 6.12.2 [\#128](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/128) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 1.1.0 to 1.1.2 [\#127](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/127) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.1.0 to 7.2.0 [\#125](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/125) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.6.1](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.6.1) (2023-01-31)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.6.0...v1.6.1)

**Fixed bugs:**

- Butane download link not valid for arm64 architecture [\#121](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/121)
- Download correct binaries for non x86\_64 architectures [\#122](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/122) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Bump ansible-lint from 6.10.2 to 6.11.0 [\#120](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/120) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update ansible-lint by using workaround [\#119](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/119) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 6.7.0 to 7.1.0 [\#118](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/118) ([dependabot[bot]](https://github.com/apps/dependabot))
- Require at least Python 3.9 to support the latest Ansible [\#117](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/117) ([tobiashuste](https://github.com/tobiashuste))
- Bump yamllint from 1.28.0 to 1.29.0 [\#116](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/116) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.6.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.6.0) (2023-01-05)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.5.0...v1.6.0)

**Merged pull requests:**

- Do not cancel jobs when a matrix job is failing [\#114](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/114) ([tobiashuste](https://github.com/tobiashuste))
- Allow to define a list of registry mirrors [\#113](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/113) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 6.6.0 to 6.7.0 [\#112](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/112) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.3 to 4.0.4 [\#111](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/111) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.5.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.5.0) (2022-12-02)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.4.0...v1.5.0)

**Implemented enhancements:**

- Switch to butane instead of container-linux-config-transpiler [\#107](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/107)

**Closed issues:**

- Molecule folder not linted by molecule lint [\#105](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/105)

**Merged pull requests:**

- Bump reuse from 1.0.0 to 1.1.0 [\#109](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Switch from ct to using butane [\#108](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/108) ([tobiashuste](https://github.com/tobiashuste))
- Lint folder molecule by molecule lint and fix linting violations [\#106](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/106) ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Bump ansible-lint from 6.8.6 to 6.8.7 [\#103](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/103) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.4.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.4.0) (2022-11-18)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.3.1...v1.4.0)

**Implemented enhancements:**

- Allow to configure cpus, memory and gpus [\#99](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/99)
- Add support for security\_opt and devices [\#97](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/97)

**Fixed bugs:**

- Configuration touched in check mode [\#87](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/87)
- Fix issues with newly introduced parameter gpu, memory and cpus [\#101](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/101) ([tobiashuste](https://github.com/tobiashuste))
- Specify version explicitly in Debian apt pinning [\#92](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/92) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Allow to configure cpus, memory and gpus [\#100](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/100) ([tobiashuste](https://github.com/tobiashuste))
- Allow to configure docker devices and security\_opts [\#98](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/98) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 6.5.0 to 6.6.0 [\#96](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/96) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.2 to 6.8.6 [\#95](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/95) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#93](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/93) ([dependabot[bot]](https://github.com/apps/dependabot))
- Use setup-python action version 4 [\#91](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/91) ([tobiashuste](https://github.com/tobiashuste))

## [v1.3.1](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.3.1) (2022-10-19)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.3.0...v1.3.1)

**Fixed bugs:**

- Fix touching the runner configuration in check mode [\#88](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/88) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release of version 1.3.1 [\#89](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/89) ([tobiashuste](https://github.com/tobiashuste))

## [v1.3.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.3.0) (2022-10-19)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.2.0...v1.3.0)

**Implemented enhancements:**

- Allow to configure the listen\_address option [\#82](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/82)

**Merged pull requests:**

- Prepare release of version 1.3.0 [\#85](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/85) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 4.0.1 to 4.0.2 [\#84](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/84) ([dependabot[bot]](https://github.com/apps/dependabot))
- Allow to configure the listen\_address [\#83](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/83) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.8.1 to 6.8.2 [\#81](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/81) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.4.0 to 6.5.0 [\#80](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/80) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.7.0 to 6.8.1 [\#79](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/79) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add codeowners [\#77](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/77) ([tobiashuste](https://github.com/tobiashuste))

## [v1.2.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.2.0) (2022-10-05)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.1.0...v1.2.0)

**Fixed bugs:**

- Use template module instead of copy [\#66](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/66) ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release of version 1.2.0 [\#74](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/74) ([tobiashuste](https://github.com/tobiashuste))
- Fix GitHub Actions tests [\#72](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/72) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule-podman from 2.0.2 to 2.0.3 [\#70](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/70) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.6.0 to 6.7.0 [\#69](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/69) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.5.2 to 6.6.0 [\#65](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/65) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.3.0 to 6.4.0 [\#64](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/64) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.27.1 to 1.28.0 [\#63](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/63) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.5.1 to 6.5.2 [\#62](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/62) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.4.0 to 6.5.1 [\#61](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/61) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.3.0 [\#60](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/60) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.1.0 to 6.2.0 [\#58](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/58) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.3.0 to 6.4.0 [\#57](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/57) ([dependabot[bot]](https://github.com/apps/dependabot))
- Specify molecule-podman dependency explicitly [\#56](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/56) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 4.0.0 to 4.0.1 [\#55](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/55) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.9.0 to 6.1.0 [\#54](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/54) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.26.3 to 1.27.1 [\#53](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/53) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.1.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.1.0) (2022-07-01)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v1.0.0...v1.1.0)

**Implemented enhancements:**

- Support configuration of shm\_size parameter [\#50](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/50)

**Merged pull requests:**

- Release version 1.1.0 [\#52](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/52) ([tobiashuste](https://github.com/tobiashuste))
- Always use the latest version of geerlingguy.docker dependency [\#49](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/49) ([Normo](https://github.com/Normo))

## [v1.0.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v1.0.0) (2022-06-29)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.6.0...v1.0.0)

**Implemented enhancements:**

- Switch from molecule-docker to molecule-podman [\#36](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/36)
- Add support for Debian 11 [\#42](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/42)
- Add support for Ubuntu 22.04 [\#40](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/40)
- Add support for Debian 11 [\#43](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/43) ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 22.04 [\#41](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/41) ([tobiashuste](https://github.com/tobiashuste))
- Use molecule-podman instead of molecule-docker [\#37](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/37) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- Do not install docker dependency automatically [\#47](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/47)
- Release version 1.0.0 [\#45](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/45)

**Merged pull requests:**

- Release version 1.0.0 [\#46](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/46) ([tobiashuste](https://github.com/tobiashuste))
- Install docker-machine version 0.16.2-gitlab.15 [\#44](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/44) ([tobiashuste](https://github.com/tobiashuste))
- Install container-linux-config-transpiler v0.9.3 [\#39](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/39) ([tobiashuste](https://github.com/tobiashuste))

## [v0.6.0](https://github.com/hifis-net/ansible-role-gitlab-runner/tree/v0.6.0) (2022-06-17)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.5.1...v0.6.0)

**Implemented enhancements:**

- Link issue\_tracker URL to GitHub [\#31](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/31)
- Add badges to README [\#11](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/11)
- Implement a daily scheduled run of the CI pipeline [\#6](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/6)
- Update dependencies via Dependabot [\#5](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/5)
- Migrate changelog to github-changelog-generator [\#21](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/21) ([tobiashuste](https://github.com/tobiashuste))
- Skip runner registration in molecule test run [\#14](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/14) ([tobiashuste](https://github.com/tobiashuste))
- Add badges to README [\#12](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/12) ([tobiashuste](https://github.com/tobiashuste))
- Use caching feature of setup-python action [\#10](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/10) ([tobiashuste](https://github.com/tobiashuste))

**Fixed bugs:**

- CI pipeline in forks fails [\#9](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/9)

**Closed issues:**

- Release version 0.6.0 [\#23](https://github.com/hifis-net/ansible-role-gitlab-runner/issues/23)

**Merged pull requests:**

- Bump ansible from 5.8.0 to 5.9.0 [\#34](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/34) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 3.6.1 to 4.0.0 [\#33](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/33) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update issue tracker link in the Galaxy meta information [\#32](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/32) ([tobiashuste](https://github.com/tobiashuste))
- Release version 0.6.0 [\#30](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/30) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.2.1 to 6.3.0 [\#29](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/29) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump robertdebock/galaxy-action from 1.2.0 to 1.2.1 [\#27](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/27) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 0.14.0 to 1.0.0 [\#26](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/26) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.7.1 to 5.8.0 [\#25](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/25) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.0.2 to 6.2.1 [\#24](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/24) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.7.0 to 5.7.1 [\#19](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/19) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.6.0 to 5.7.0 [\#18](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/18) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 3.5.2 to 3.6.1 [\#17](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/17) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 5.3.1 to 6.0.2 [\#16](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/16) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.1.0 to 5.6.0 [\#15](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/15) ([dependabot[bot]](https://github.com/apps/dependabot))
- fixes\(\#5\): added dependabot.yml [\#8](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/8) ([tharun634](https://github.com/tharun634))
- fixes\(\#6\): CI daily run [\#7](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/7) ([tharun634](https://github.com/tharun634))
- Implement full lint and test workflow via GitHub Actions [\#1](https://github.com/hifis-net/ansible-role-gitlab-runner/pull/1) ([tobiashuste](https://github.com/tobiashuste))

## [0.5.1](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.5.1) - 2022-03-17

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.5.0...v0.5.1)

### Fixed

* Fix install from deb file if version is older than installed
  ([!55](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/55)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.5.0](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.5.0) - 2022-03-16

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.4.0...v0.5.0)

### Added

* Add support for optionally installing gitlab-runner via a `.deb` file
  ([!53](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/53)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.4.0](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.4.0) - 2022-03-03

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.3.0...v0.4.0)

### Changed

* Allow to update the installed GPG keys
  ([!52](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/52)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.3.0](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.3.0) - 2022-01-11

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.2.2...v0.3.0)

### Added

* Add support for docker `tls_verify` parameter
  ([!46](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/46)
  by [Normo](https://gitlab.com/Normo)).

### Changed

* Bump geerlingguy.docker to version 4.1.1
  ([!48](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/48)
  by [Normo](https://gitlab.com/Normo)).
* Bump container linux config transpiler to v0.9.2
  ([!47](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/47)
  by [Normo](https://gitlab.com/Normo)).
* Bump Python dependencies to the latest version
  ([!50](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/50)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Fixed

* Fix debian docker issue in GitLab CI and bump runner version in tests
  ([!49](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/49)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.2.2](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.2.2) - 2021-07-30

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.2.1...v0.2.2)

### Fixed

* Fix failing binfmt-init.service for multiarch support
  ([!44](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/44)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.2.1](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.2.1) - 2021-07-30

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.2.0...v0.2.1)

### Fixed

* Correctly configure MTU and registry mirror for Docker-in-Docker
  ([!43](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/43)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Fix bug when `cache_type` is undefined
  ([!42](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/42)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.2.0](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.2.0) - 2021-07-28

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/v0.1.0...v0.2.0)

### Added
* Allow to configure autoscaling parameters
  ([!36](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/36)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Create a test machine via docker-machine once
  ([!39](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/39)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Changed
* Reference latest version of gitlab-runner throughout the role
  ([!38](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/38)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
* Skip ignition check tasks if flatcar config is unchanged
  ([!37](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/37)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

### Fixed
* Document the `limit` parameter
  ([!40](https://gitlab.com/hifis/ansible/gitlab-ci-openstack/-/merge_requests/40)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [0.1.0](https://github.com/hifis-net/ansible-role-gitlab-runner/releases/v0.1.0) - 2021-07-20

[List of commits](https://github.com/hifis-net/ansible-role-gitlab-runner/compare/359ac4d5e6371452d5488fcf7daa3a43d935ddc1...v0.1.0)

### Added
Initial release of the Ansible GitLab-Runner Role.


\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
