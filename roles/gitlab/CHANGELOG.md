<!--
SPDX-FileCopyrightText: Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->
# Changelog

## [v1.6.1](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.6.1) (2023-11-07)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.6.0...v1.6.1)

**Fixed bugs:**

- conditional check 'gitlab\_ctl.stat.exists' failed [\#134](https://github.com/hifis-net/ansible-role-gitlab/issues/134)

**Merged pull requests:**

- chore: prepare release version 1.6.1 [\#136](https://github.com/hifis-net/ansible-role-gitlab/pull/136) ([Normo](https://github.com/Normo))
- fix: remove obsolete conditional check [\#135](https://github.com/hifis-net/ansible-role-gitlab/pull/135) ([Normo](https://github.com/Normo))

## [v1.6.0](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.6.0) (2023-11-03)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.5.0...v1.6.0)

**Closed issues:**

- Check for background migrations only when updating GitLab [\#130](https://github.com/hifis-net/ansible-role-gitlab/issues/130)

**Merged pull requests:**

- chore: prepare release version 1.6.0 [\#132](https://github.com/hifis-net/ansible-role-gitlab/pull/132) ([Normo](https://github.com/Normo))
- Check for background migration on GitLab update only [\#131](https://github.com/hifis-net/ansible-role-gitlab/pull/131) ([Normo](https://github.com/Normo))

## [v1.5.0](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.5.0) (2023-10-19)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.4.0...v1.5.0)

**Implemented enhancements:**

- Configure redis sentinel password [\#119](https://github.com/hifis-net/ansible-role-gitlab/issues/119)

**Closed issues:**

- Gitaly: Implement Gitaly configuration structure change [\#105](https://github.com/hifis-net/ansible-role-gitlab/issues/105)

**Merged pull requests:**

- chore: prepare release version 1.5.0 [\#127](https://github.com/hifis-net/ansible-role-gitlab/pull/127) ([Normo](https://github.com/Normo))
- chore\(deps\): bump ansible-lint from 6.20.3 to 6.21.0 [\#126](https://github.com/hifis-net/ansible-role-gitlab/pull/126) ([Normo](https://github.com/Normo))
- chore\(deps\): bump ansible from 8.4.0 to 8.5.0 [\#124](https://github.com/hifis-net/ansible-role-gitlab/pull/124) ([Normo](https://github.com/Normo))
- feat: configure redis sentinel authentication [\#120](https://github.com/hifis-net/ansible-role-gitlab/pull/120) ([Normo](https://github.com/Normo))
- fix: use changed\_when on shell and command tasks [\#118](https://github.com/hifis-net/ansible-role-gitlab/pull/118) ([Normo](https://github.com/Normo))
- chore: upgrade python dependencies [\#114](https://github.com/hifis-net/ansible-role-gitlab/pull/114) ([Normo](https://github.com/Normo))
- Bump yamllint from 1.29.0 to 1.32.0 [\#108](https://github.com/hifis-net/ansible-role-gitlab/pull/108) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.1.0 to 7.4.0 [\#104](https://github.com/hifis-net/ansible-role-gitlab/pull/104) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.28.0 to 1.29.0 [\#88](https://github.com/hifis-net/ansible-role-gitlab/pull/88) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.4.0](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.4.0) (2023-01-11)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.3.0...v1.4.0)

**Merged pull requests:**

- Release version 1.4.0 [\#86](https://github.com/hifis-net/ansible-role-gitlab/pull/86) ([tobiashuste](https://github.com/tobiashuste))
- Flush handlers only if required [\#85](https://github.com/hifis-net/ansible-role-gitlab/pull/85) ([tobiashuste](https://github.com/tobiashuste))
- Allow to set GitLab feature flags [\#84](https://github.com/hifis-net/ansible-role-gitlab/pull/84) ([tobiashuste](https://github.com/tobiashuste))
- Report no changes when apt cache is updated in check mode [\#83](https://github.com/hifis-net/ansible-role-gitlab/pull/83) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.10.0 to 6.10.2 [\#82](https://github.com/hifis-net/ansible-role-gitlab/pull/82) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.9.1 to 6.10.0 [\#81](https://github.com/hifis-net/ansible-role-gitlab/pull/81) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.0.0 to 7.1.0 [\#80](https://github.com/hifis-net/ansible-role-gitlab/pull/80) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.3 to 4.0.4 [\#79](https://github.com/hifis-net/ansible-role-gitlab/pull/79) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v1.3.0](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.3.0) (2022-12-05)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.2.0...v1.3.0)

**Implemented enhancements:**

- Add support for Ubuntu 22.04 [\#18](https://github.com/hifis-net/ansible-role-gitlab/issues/18)

**Closed issues:**

- Update package cache in check-mode [\#70](https://github.com/hifis-net/ansible-role-gitlab/issues/70)
- Switch to molecule-podman [\#33](https://github.com/hifis-net/ansible-role-gitlab/issues/33)
- Remove Centos 8 and add support for AlmaLinux 8 [\#4](https://github.com/hifis-net/ansible-role-gitlab/issues/4)

**Merged pull requests:**

- Bump ansible-lint from 6.8.5 to 6.8.6 [\#65](https://github.com/hifis-net/ansible-role-gitlab/pull/65) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.2 to 6.8.5 [\#64](https://github.com/hifis-net/ansible-role-gitlab/pull/64) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#61](https://github.com/hifis-net/ansible-role-gitlab/pull/61) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 1.3.0 [\#77](https://github.com/hifis-net/ansible-role-gitlab/pull/77) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.8.7 to 6.9.1 [\#76](https://github.com/hifis-net/ansible-role-gitlab/pull/76) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 1.0.0 to 1.1.0 [\#75](https://github.com/hifis-net/ansible-role-gitlab/pull/75) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update README.md [\#74](https://github.com/hifis-net/ansible-role-gitlab/pull/74) ([Normo](https://github.com/Normo))
- Add codeowners to autoassign reviewers [\#73](https://github.com/hifis-net/ansible-role-gitlab/pull/73) ([Normo](https://github.com/Normo))
- Add Ubuntu 22.04 as supported platform [\#72](https://github.com/hifis-net/ansible-role-gitlab/pull/72) ([Normo](https://github.com/Normo))
- Ensure package cache is updated in check-mode [\#71](https://github.com/hifis-net/ansible-role-gitlab/pull/71) ([Normo](https://github.com/Normo))
- Bump ansible from 6.5.0 to 7.0.0 [\#68](https://github.com/hifis-net/ansible-role-gitlab/pull/68) ([dependabot[bot]](https://github.com/apps/dependabot))
- Switch from molecule-docker to molecule-podman [\#34](https://github.com/hifis-net/ansible-role-gitlab/pull/34) ([tobiashuste](https://github.com/tobiashuste))

## [v1.2.0](https://github.com/hifis-net/ansible-role-gitlab/tree/v1.2.0) (2022-10-21)

[Full Changelog](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.1.0...v1.2.0)

**Implemented enhancements:**

- Improve Molecule verification step [\#35](https://github.com/hifis-net/ansible-role-gitlab/issues/35)
- Add badges to README [\#6](https://github.com/hifis-net/ansible-role-gitlab/issues/6)
- Add Debian 11 \(bullseye\) as platform [\#50](https://github.com/hifis-net/ansible-role-gitlab/pull/50) ([flyinggecko](https://github.com/flyinggecko))
- Use FQCN throughout the whole project [\#10](https://github.com/hifis-net/ansible-role-gitlab/pull/10) ([tobiashuste](https://github.com/tobiashuste))

**Fixed bugs:**

- Molecule folder not linted by molecule [\#52](https://github.com/hifis-net/ansible-role-gitlab/issues/52)
- Update issue tracker in Ansible Galaxy meta information [\#7](https://github.com/hifis-net/ansible-role-gitlab/issues/7)
- Specify Debian 11 correctly in role metadata [\#56](https://github.com/hifis-net/ansible-role-gitlab/pull/56) ([tobiashuste](https://github.com/tobiashuste))
- Lint molecule files via ansible-lint [\#53](https://github.com/hifis-net/ansible-role-gitlab/pull/53) ([christianhueserhzdr](https://github.com/christianhueserhzdr))

**Closed issues:**

- Use FQCN everywhere [\#9](https://github.com/hifis-net/ansible-role-gitlab/issues/9)
- Add a contribution guide [\#11](https://github.com/hifis-net/ansible-role-gitlab/issues/11)
- Add auto-generated CHANGELOG file [\#8](https://github.com/hifis-net/ansible-role-gitlab/issues/8)

**Merged pull requests:**

- Prepare release version 1.2.0 [\#58](https://github.com/hifis-net/ansible-role-gitlab/pull/58) ([tobiashuste](https://github.com/tobiashuste))
- Use setup-python action version 4 [\#57](https://github.com/hifis-net/ansible-role-gitlab/pull/57) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 4.0.1 to 4.0.2 [\#55](https://github.com/hifis-net/ansible-role-gitlab/pull/55) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.1 to 6.8.2 [\#54](https://github.com/hifis-net/ansible-role-gitlab/pull/54) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.5.0 [\#51](https://github.com/hifis-net/ansible-role-gitlab/pull/51) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.4.0 to 6.8.1 [\#49](https://github.com/hifis-net/ansible-role-gitlab/pull/49) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.27.1 to 1.28.0 [\#43](https://github.com/hifis-net/ansible-role-gitlab/pull/43) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.1.0 to 6.2.0 [\#38](https://github.com/hifis-net/ansible-role-gitlab/pull/38) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.3.0 to 6.4.0 [\#37](https://github.com/hifis-net/ansible-role-gitlab/pull/37) ([dependabot[bot]](https://github.com/apps/dependabot))
- Improve molecule verification step [\#36](https://github.com/hifis-net/ansible-role-gitlab/pull/36) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 3.6.1 to 4.0.1 [\#32](https://github.com/hifis-net/ansible-role-gitlab/pull/32) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.7.1 to 6.1.0 [\#31](https://github.com/hifis-net/ansible-role-gitlab/pull/31) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.26.3 to 1.27.1 [\#30](https://github.com/hifis-net/ansible-role-gitlab/pull/30) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.0.2 to 6.3.0 [\#27](https://github.com/hifis-net/ansible-role-gitlab/pull/27) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump robertdebock/galaxy-action from 1.2.0 to 1.2.1 [\#24](https://github.com/hifis-net/ansible-role-gitlab/pull/24) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 0.14.0 to 1.0.0 [\#22](https://github.com/hifis-net/ansible-role-gitlab/pull/22) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 5.6.0 to 5.7.1 [\#17](https://github.com/hifis-net/ansible-role-gitlab/pull/17) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add CONTRIBUTING file and workflow diagram [\#15](https://github.com/hifis-net/ansible-role-gitlab/pull/15) ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Prepare HISTORY file and add auto-generated CHANGELOG file [\#14](https://github.com/hifis-net/ansible-role-gitlab/pull/14) ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Exchange link to issue tracker in Ansible Galaxy meta information [\#13](https://github.com/hifis-net/ansible-role-gitlab/pull/13) ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Add badges to README [\#12](https://github.com/hifis-net/ansible-role-gitlab/pull/12) ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Bump ansible from 5.3.0 to 5.6.0 [\#5](https://github.com/hifis-net/ansible-role-gitlab/pull/5) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 5.4.0 to 6.0.2 [\#3](https://github.com/hifis-net/ansible-role-gitlab/pull/3) ([dependabot[bot]](https://github.com/apps/dependabot))
- Create GitHub Actions for linting, testing and releasing [\#2](https://github.com/hifis-net/ansible-role-gitlab/pull/2) ([christianhueserhzdr](https://github.com/christianhueserhzdr))

**Changed**

- Update Python dependencies and use Python 3.9 in GitLab CI
  ([!49](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/49)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
- Add role variable to specify apt key identifier
  ([!50](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/50)
  by [Normo](https://gitlab.com/Normo)).

## [v1.1.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v1.1.0) - 2021-12-08

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.0.2...v1.1.0)

### Added

- Add galaxy namespace to role metadata
  ([!44](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/44)
  by [Normo](https://gitlab.com/Normo)).

### Changed

- Replace include with import_tasks
  ([!45](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/45)
  by [Normo](https://gitlab.com/Normo)).
- Bump Python dependencies to the latest versions
  ([!42](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/42)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
- Prevent restarting puma and sidekiq services in Mattermost only context
  ([!46](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/46)
  by [Normo](https://gitlab.com/Normo)).
- Install latest available GitLab version if no version has been pinned
  ([!47](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/47)
  by [Normo](https://gitlab.com/Normo)).

## [v1.0.2](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v1.0.2) - 2021-06-29

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.0.1...v1.0.2)

### Fixed

- Allow initial dry-runs without causing role deployments to fail
  ([!41](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/41)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v1.0.1](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v1.0.1) - 2021-03-16

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v1.0.0...v1.0.1)

### Fixed

- Stop role execution after failed ``apt`` package installation
  ([!39](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/39)
  by [Normo](https://gitlab.com/Normo)).

## [v1.0.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v1.0.0) - 2021-03-03

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.5.0...v1.0.0)

### Added

- Automate role import into Ansible Galaxy via GitHub Actions
  ([!34](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/34)
  by [Normo](https://gitlab.com/Normo)).
- Merge gitlab_base into gitlab role
  ([!32](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/32)
  by [Normo](https://gitlab.com/Normo)).
- Reconfigure GitLab if a previous reconfiguration had failed
  ([!35](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/35)
  by [Normo](https://gitlab.com/Normo)).

### Changed

- Upgrade project dependencies
  ([!33](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/33)
  by [Normo](https://gitlab.com/Normo)).
- Use fully qualified collection names
  ([!36](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/36)
  by [Normo](https://gitlab.com/Normo)).

## [v0.5.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.5.0) - 2021-01-18

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.4.0...v0.5.0)

### Added

- Add handlers to restart puma and sidekiq
  ([!30](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/30)
  by [Normo](https://gitlab.com/Normo)).

## [v0.4.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.4.0) - 2020-10-13

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.3.4...v0.4.0)

### Added

- Supply generic way to configure GitLab via Ansible variables that are translated to Ruby function calls
  ([!27](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/27)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

### Changed

- Improve and speed up the CI pipeline
  ([!24](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/24)
  by [tobiashuste](https://gitlab.com/tobiashuste)).
- Bump dependency Ansible to ansible = "~=2.10.0"
  ([!25](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/25)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v0.3.4](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.3.4) - 2020-09-24

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.3.3...v0.3.4)

### Fixed

- Create file skip-auto-backup on non-primary GitLab nodes
  ([!21](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/21)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).
- Split handler to reconfigure GitLab into one for primary and one for non-primary nodes
  ([!22](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/22)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v0.3.3](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.3.3) - 2020-09-10

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.3.2...v0.3.3)

### Fixed

- Rename role 'gitlab_base_role' to 'gitlab_base' in meta and requirements files
  ([!20](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/20)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v0.3.2](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.3.2) - 2020-09-10

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.3.1...v0.3.2)

### Fixed

- Handler 'Reconfigure GitLab' needs to listens to handler 'GitLab has been installed or upgraded'
  ([!19](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/19)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v0.3.1](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.3.1) - 2020-09-09

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.3.0...v0.3.1)

### Fixed

- Fix reconfigure handler not run when GitLab package is upgraded
  ([!17](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/17)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v0.3.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.3.0) - 2020-09-08

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.2.0...v0.3.0)

### Added

- Trigger GitLab reconfigure if GitLab package has been installed or upgraded
  ([!16](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/16)
  by [christian.hueser.hzdr](https://gitlab.com/christian.hueser.hzdr)).

## [v0.2.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.2.0) - 2020-08-26

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.1.1...v0.2.0)

### Added

- Implement a basic configuration for the container registry
  ([!14](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/14)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v0.1.1](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.1.1) - 2020-08-21

[List of commits](https://github.com/hifis-net/ansible-role-gitlab/compare/v0.1.0...v0.1.1)

### Fixed

- Fix creation of skip-auto-reconfigure file
  ([!12](https://gitlab.com/hifis/ansible/gitlab-role/-/merge_requests/12)
  by [tobiashuste](https://gitlab.com/tobiashuste)).

## [v0.1.0](https://github.com/hifis-net/ansible-role-gitlab/releases/tag/v0.1.0) - 2020-08-20

### Added

Initial release of the Ansible GitLab Role.


\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
