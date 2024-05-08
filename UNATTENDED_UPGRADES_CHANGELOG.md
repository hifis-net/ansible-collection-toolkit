# Changelog

## [v3.3.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v3.3.0) (2024-03-01)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v3.2.1...v3.3.0)

**Closed issues:**

- Allow roles to run with INJECT\_FACTS\_AS\_VARS set to false [\#185](https://github.com/hifis-net/ansible-collection-toolkit/issues/185)
- Fix badges with Ansible Galaxy NG [\#174](https://github.com/hifis-net/ansible-collection-toolkit/issues/174)
- Version 3.2.1 doesn't seem to be available on ansible galaxy [\#169](https://github.com/hifis-net/ansible-collection-toolkit/issues/169)

**Merged pull requests:**

- ci: install a recent podman version [\#190](https://github.com/hifis-net/ansible-collection-toolkit/pull/190) ([Normo](https://github.com/Normo))
- chore\(deps\): bump ansible from 9.2.0 to 9.3.0 [\#189](https://github.com/hifis-net/ansible-collection-toolkit/pull/189) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release v3.3.0 [\#188](https://github.com/hifis-net/ansible-collection-toolkit/pull/188) ([Normo](https://github.com/Normo))
- refactor: refer to ansible facts through ansible\_facts.\* namespace [\#187](https://github.com/hifis-net/ansible-collection-toolkit/pull/187) ([Normo](https://github.com/Normo))
- Allow roles to run with INJECT\_FACTS\_AS\_VARS set to false [\#186](https://github.com/hifis-net/ansible-collection-toolkit/pull/186) ([kennethso168](https://github.com/kennethso168))
- chore\(deps-dev\): bump yamllint from 1.34.0 to 1.35.1 [\#184](https://github.com/hifis-net/ansible-collection-toolkit/pull/184) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule from 6.0.3 to 24.2.0 [\#182](https://github.com/hifis-net/ansible-collection-toolkit/pull/182) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule-plugins from 23.5.0 to 23.5.3 [\#181](https://github.com/hifis-net/ansible-collection-toolkit/pull/181) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.22.2 to 24.2.0 [\#180](https://github.com/hifis-net/ansible-collection-toolkit/pull/180) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump yamllint from 1.33.0 to 1.34.0 [\#179](https://github.com/hifis-net/ansible-collection-toolkit/pull/179) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible from 9.1.0 to 9.2.0 [\#178](https://github.com/hifis-net/ansible-collection-toolkit/pull/178) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.22.1 to 6.22.2 [\#177](https://github.com/hifis-net/ansible-collection-toolkit/pull/177) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump molecule from 6.0.2 to 6.0.3 [\#176](https://github.com/hifis-net/ansible-collection-toolkit/pull/176) ([dependabot[bot]](https://github.com/apps/dependabot))
- fix: make ansible galaxy badges work again [\#175](https://github.com/hifis-net/ansible-collection-toolkit/pull/175) ([tobiashuste](https://github.com/tobiashuste))
- chore\(deps\): bump ansible from 8.6.0 to 9.1.0 [\#172](https://github.com/hifis-net/ansible-collection-toolkit/pull/172) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 6.21.1 to 6.22.1 [\#171](https://github.com/hifis-net/ansible-collection-toolkit/pull/171) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump yamllint from 1.32.0 to 1.33.0 [\#167](https://github.com/hifis-net/ansible-collection-toolkit/pull/167) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible from 8.5.0 to 8.6.0 [\#164](https://github.com/hifis-net/ansible-collection-toolkit/pull/164) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.2.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v3.2.1) (2023-11-03)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v3.2.0...v3.2.1)

**Fixed bugs:**

- "Bullseye-Workaround" needs to be applied to bookworm and later as well [\#146](https://github.com/hifis-net/ansible-collection-toolkit/issues/146)

**Closed issues:**

- Unattended-Upgrade::Origins-Pattern from 50unattended-upgrades apparently can't be "overruled" [\#145](https://github.com/hifis-net/ansible-collection-toolkit/issues/145)

**Merged pull requests:**

- chore: prepare changelog for version 3.2.1 [\#161](https://github.com/hifis-net/ansible-collection-toolkit/pull/161) ([tobiashuste](https://github.com/tobiashuste))
- fix: reformat allowed origins pattern [\#160](https://github.com/hifis-net/ansible-collection-toolkit/pull/160) ([Normo](https://github.com/Normo))
- fix: allow ${distro\_codename}-security on Debian bookworm [\#159](https://github.com/hifis-net/ansible-collection-toolkit/pull/159) ([Normo](https://github.com/Normo))
- chore\(deps-dev\): bump ansible-lint from 6.18.0 to 6.21.1 [\#157](https://github.com/hifis-net/ansible-collection-toolkit/pull/157) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.3.0 to 8.5.0 [\#155](https://github.com/hifis-net/ansible-collection-toolkit/pull/155) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 3 to 4 [\#147](https://github.com/hifis-net/ansible-collection-toolkit/pull/147) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 6.0.1 to 6.0.2 [\#144](https://github.com/hifis-net/ansible-collection-toolkit/pull/144) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.2.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v3.2.0) (2023-08-25)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v3.1.0...v3.2.0)

**Implemented enhancements:**

- Add support for Debian Bookworm [\#134](https://github.com/hifis-net/ansible-collection-toolkit/issues/134)

**Closed issues:**

- Remove official support for EOL Ubuntu 18.04 [\#139](https://github.com/hifis-net/ansible-collection-toolkit/issues/139)

**Merged pull requests:**

- chore: prepare release of version 3.2.0 [\#142](https://github.com/hifis-net/ansible-collection-toolkit/pull/142) ([tobiashuste](https://github.com/tobiashuste))
- fix: remove official support for EOL Ubuntu 18.04 [\#141](https://github.com/hifis-net/ansible-collection-toolkit/pull/141) ([tobiashuste](https://github.com/tobiashuste))
- feat: add support for Debian 12 bookworm [\#140](https://github.com/hifis-net/ansible-collection-toolkit/pull/140) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.17.2 to 6.18.0 [\#138](https://github.com/hifis-net/ansible-collection-toolkit/pull/138) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.1.0 to 6.0.1 [\#137](https://github.com/hifis-net/ansible-collection-toolkit/pull/137) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.1.0 to 8.3.0 [\#136](https://github.com/hifis-net/ansible-collection-toolkit/pull/136) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule-plugins from 23.4.1 to 23.5.0 [\#133](https://github.com/hifis-net/ansible-collection-toolkit/pull/133) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.2 to 6.17.2 [\#131](https://github.com/hifis-net/ansible-collection-toolkit/pull/131) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.0.1 to 5.1.0 [\#130](https://github.com/hifis-net/ansible-collection-toolkit/pull/130) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.0.0 to 8.1.0 [\#129](https://github.com/hifis-net/ansible-collection-toolkit/pull/129) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.1.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v3.1.0) (2023-06-09)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v3.0.0...v3.1.0)

**Implemented enhancements:**

- Added custom of apt-daily timers apt-daily-upgrade [\#85](https://github.com/hifis-net/ansible-collection-toolkit/issues/85)
- Test custom apt-daily timers [\#121](https://github.com/hifis-net/ansible-collection-toolkit/pull/121) ([Normo](https://github.com/Normo))

**Closed issues:**

- Remove support for ansible-core 2.12 [\#124](https://github.com/hifis-net/ansible-collection-toolkit/issues/124)

**Merged pull requests:**

- Prepare release version 3.1.0 [\#127](https://github.com/hifis-net/ansible-collection-toolkit/pull/127) ([Normo](https://github.com/Normo))
- Update minimum ansible version to 2.13 [\#125](https://github.com/hifis-net/ansible-collection-toolkit/pull/125) ([Normo](https://github.com/Normo))
- Add support for custom apt-daily and apt-daily-upgrade timers [\#120](https://github.com/hifis-net/ansible-collection-toolkit/pull/120) ([pgassmann](https://github.com/pgassmann))
- Bump ansible from 7.6.0 to 8.0.0 [\#119](https://github.com/hifis-net/ansible-collection-toolkit/pull/119) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v3.0.0) (2023-05-26)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v2.0.1...v3.0.0)

**UPGRADE NOTES AND BREAKING CHANGES:**

As of this release, all Apt options for `unattended-upgrades` made in the default OS configuration files `/etc/apt/apt.conf.d/20auto-upgrades` and `/etc/apt/apt.conf.d/50unattended-upgrades` are now completely overwritten instead of being merged. This means that from now on only the options set by this role are active.

**Fixed bugs:**

- apt options are not overridden but merged [\#94](https://github.com/hifis-net/ansible-collection-toolkit/issues/94)

**Closed issues:**

- ValueError: not enough values to unpack \(expected 2, got 1\) on Ubuntu Jammy [\#55](https://github.com/hifis-net/ansible-collection-toolkit/issues/55)

**Merged pull requests:**

- Bump ansible from 7.5.0 to 7.6.0 [\#115](https://github.com/hifis-net/ansible-collection-toolkit/pull/115) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.31.0 to 1.32.0 [\#114](https://github.com/hifis-net/ansible-collection-toolkit/pull/114) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.1 to 6.16.2 [\#113](https://github.com/hifis-net/ansible-collection-toolkit/pull/113) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.0 to 6.16.1 [\#112](https://github.com/hifis-net/ansible-collection-toolkit/pull/112) ([dependabot[bot]](https://github.com/apps/dependabot))
- fix: reformat config template [\#111](https://github.com/hifis-net/ansible-collection-toolkit/pull/111) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.14.3 to 6.16.0 [\#109](https://github.com/hifis-net/ansible-collection-toolkit/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Erase all unattended-upgrades options first [\#107](https://github.com/hifis-net/ansible-collection-toolkit/pull/107) ([Normo](https://github.com/Normo))
- Bump yamllint from 1.28.0 to 1.31.0 [\#106](https://github.com/hifis-net/ansible-collection-toolkit/pull/106) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.1.0 to 7.5.0 [\#105](https://github.com/hifis-net/ansible-collection-toolkit/pull/105) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.4 to 5.0.1 [\#104](https://github.com/hifis-net/ansible-collection-toolkit/pull/104) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add test for Unattended-Upgrade::Sender [\#103](https://github.com/hifis-net/ansible-collection-toolkit/pull/103) ([Normo](https://github.com/Normo))
- Unattended-Upgrade::Sender support [\#101](https://github.com/hifis-net/ansible-collection-toolkit/pull/101) ([turikhay](https://github.com/turikhay))
- Bump ansible-lint from 6.10.2 to 6.14.3 [\#99](https://github.com/hifis-net/ansible-collection-toolkit/pull/99) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.10.0 to 6.10.2 [\#82](https://github.com/hifis-net/ansible-collection-toolkit/pull/82) ([dependabot[bot]](https://github.com/apps/dependabot))
- Do not cancel ci jobs if one ci job in the matrix fails [\#81](https://github.com/hifis-net/ansible-collection-toolkit/pull/81) ([Normo](https://github.com/Normo))
- Prepare release version 3.0.0 [\#117](https://github.com/hifis-net/ansible-collection-toolkit/pull/117) ([Normo](https://github.com/Normo))

## [v2.0.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v2.0.1) (2022-12-15)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v2.0.0...v2.0.1)

**Fixed bugs:**

- Fix minimum specification of Ansible version [\#77](https://github.com/hifis-net/ansible-collection-toolkit/pull/77) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- `unattended_dl_limit` doesn't work [\#76](https://github.com/hifis-net/ansible-collection-toolkit/issues/76)
- ansible.builtin.import\_tasks problem [\#75](https://github.com/hifis-net/ansible-collection-toolkit/issues/75)
- Detach fork [\#66](https://github.com/hifis-net/ansible-collection-toolkit/issues/66)

**Merged pull requests:**

- Bump ansible-lint from 6.9.1 to 6.10.0 [\#79](https://github.com/hifis-net/ansible-collection-toolkit/pull/79) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.0.0 to 7.1.0 [\#74](https://github.com/hifis-net/ansible-collection-toolkit/pull/74) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.3 to 4.0.4 [\#73](https://github.com/hifis-net/ansible-collection-toolkit/pull/73) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.9.0 to 6.9.1 [\#72](https://github.com/hifis-net/ansible-collection-toolkit/pull/72) ([dependabot[bot]](https://github.com/apps/dependabot))
- Make sure GitHub Actions runs on the main branch [\#70](https://github.com/hifis-net/ansible-collection-toolkit/pull/70) ([tobiashuste](https://github.com/tobiashuste))
- Fix deprecation warning in GitHub Actions [\#69](https://github.com/hifis-net/ansible-collection-toolkit/pull/69) ([tobiashuste](https://github.com/tobiashuste))
- Prepare release v2.0.1 [\#78](https://github.com/hifis-net/ansible-collection-toolkit/pull/78) ([Normo](https://github.com/Normo))
- Leave a hint about the original fork [\#71](https://github.com/hifis-net/ansible-collection-toolkit/pull/71) ([Normo](https://github.com/Normo))

## [v2.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v2.0.0) (2022-12-02)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v1.12.2...v2.0.0)

**UPGRADE NOTES AND BREAKING CHANGES:**

If you have used this role before version 2.0.0, the files `20auto-upgrades` and `50unattended-upgrades` will differ from the system defaults (instead of the configuration being placed in a separate file, as we do now).
These can be left as-is as they will be overridden.
During OS upgrades, when asked if these files should be overwritten by the maintainer's package, say yes.
They will then be reset to their default states, and you won't be asked these questions again.

**Implemented enhancements:**

- \[Feature Request\] Use force\_apt\_get [\#32](https://github.com/hifis-net/ansible-collection-toolkit/issues/32)
- Override configuration in a separate apt.conf.d file [\#10](https://github.com/hifis-net/ansible-collection-toolkit/issues/10)
- Test role via Molecule [\#8](https://github.com/hifis-net/ansible-collection-toolkit/issues/8)

**Fixed bugs:**

- Molecule folder not linted by molecule [\#48](https://github.com/hifis-net/ansible-collection-toolkit/issues/48)
- Change caused by indentation [\#53](https://github.com/hifis-net/ansible-collection-toolkit/issues/53)
- Fix installation of powermgmt-base package [\#35](https://github.com/hifis-net/ansible-collection-toolkit/issues/35)

**Closed issues:**

- Documentation role name mismatch [\#41](https://github.com/hifis-net/ansible-collection-toolkit/issues/41)
- Some configurations options are missing [\#56](https://github.com/hifis-net/ansible-collection-toolkit/issues/56)
- Remove support for OS that reached EOL [\#38](https://github.com/hifis-net/ansible-collection-toolkit/issues/38)
- Add changelog [\#33](https://github.com/hifis-net/ansible-collection-toolkit/issues/33)
- Add contribution guide [\#16](https://github.com/hifis-net/ansible-collection-toolkit/issues/16)
- Rename default branch to `main` [\#13](https://github.com/hifis-net/ansible-collection-toolkit/issues/13)

**Merged pull requests:**

- Bump ansible-lint from 6.8.6 to 6.9.0 [\#62](https://github.com/hifis-net/ansible-collection-toolkit/pull/62) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.5.0 to 7.0.0 [\#60](https://github.com/hifis-net/ansible-collection-toolkit/pull/60) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add missing option Unattended-Upgrade::MailReport [\#57](https://github.com/hifis-net/ansible-collection-toolkit/pull/57) ([nono-lqdn](https://github.com/nono-lqdn))
- Bump ansible-lint from 6.8.2 to 6.8.6 [\#54](https://github.com/hifis-net/ansible-collection-toolkit/pull/54) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#49](https://github.com/hifis-net/ansible-collection-toolkit/pull/49) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.1 to 4.0.2 [\#47](https://github.com/hifis-net/ansible-collection-toolkit/pull/47) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.1 to 6.8.2 [\#46](https://github.com/hifis-net/ansible-collection-toolkit/pull/46) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.4.0 to 6.5.0 [\#45](https://github.com/hifis-net/ansible-collection-toolkit/pull/45) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.0 to 6.8.1 [\#44](https://github.com/hifis-net/ansible-collection-toolkit/pull/44) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.5.0 to 6.8.0 [\#43](https://github.com/hifis-net/ansible-collection-toolkit/pull/43) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix role name in README [\#42](https://github.com/hifis-net/ansible-collection-toolkit/pull/42) ([lukashass](https://github.com/lukashass))
- Bump molecule-podman from 2.0.2 to 2.0.3 [\#40](https://github.com/hifis-net/ansible-collection-toolkit/pull/40) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.4.0 [\#25](https://github.com/hifis-net/ansible-collection-toolkit/pull/25) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.27.1 to 1.28.0 [\#24](https://github.com/hifis-net/ansible-collection-toolkit/pull/24) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update README.md [\#19](https://github.com/hifis-net/ansible-collection-toolkit/pull/19) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.4.0 to 6.5.0 [\#15](https://github.com/hifis-net/ansible-collection-toolkit/pull/15) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 2.0.0 [\#67](https://github.com/hifis-net/ansible-collection-toolkit/pull/67) ([Normo](https://github.com/Normo))
- Add codeowners to autoassign reviewers [\#65](https://github.com/hifis-net/ansible-collection-toolkit/pull/65) ([Normo](https://github.com/Normo))
- Ensure new default branch main is used by Galaxy [\#64](https://github.com/hifis-net/ansible-collection-toolkit/pull/64) ([Normo](https://github.com/Normo))
- Lint molecule folder [\#63](https://github.com/hifis-net/ansible-collection-toolkit/pull/63) ([Normo](https://github.com/Normo))
- Fix indentation for unattended\_origins\_patterns in template file [\#61](https://github.com/hifis-net/ansible-collection-toolkit/pull/61) ([Normo](https://github.com/Normo))
- Remove support for OS that reached EOL [\#39](https://github.com/hifis-net/ansible-collection-toolkit/pull/39) ([Normo](https://github.com/Normo))
- Add changelog [\#37](https://github.com/hifis-net/ansible-collection-toolkit/pull/37) ([Normo](https://github.com/Normo))
- Fix installation of powermgmt-base [\#36](https://github.com/hifis-net/ansible-collection-toolkit/pull/36) ([Normo](https://github.com/Normo))
- Force usage of apt-get instead of aptitude [\#34](https://github.com/hifis-net/ansible-collection-toolkit/pull/34) ([Normo](https://github.com/Normo))
- Test Remove-Unused-Kernel-Packages option [\#31](https://github.com/hifis-net/ansible-collection-toolkit/pull/31) ([Normo](https://github.com/Normo))
- Add options for controlling the removal of unused kernel packages [\#29](https://github.com/hifis-net/ansible-collection-toolkit/pull/29) ([gcotelli](https://github.com/gcotelli))
- Stop overwriting default config [\#28](https://github.com/hifis-net/ansible-collection-toolkit/pull/28) ([alpha0010](https://github.com/alpha0010))
- Add contribution guide [\#22](https://github.com/hifis-net/ansible-collection-toolkit/pull/22) ([Normo](https://github.com/Normo))
- Remove custom ansible-lint config [\#18](https://github.com/hifis-net/ansible-collection-toolkit/pull/18) ([Normo](https://github.com/Normo))
- Fix 'All names should start with an uppercase letter' warnings [\#17](https://github.com/hifis-net/ansible-collection-toolkit/pull/17) ([Normo](https://github.com/Normo))
- Fix CI badge in README [\#14](https://github.com/hifis-net/ansible-collection-toolkit/pull/14) ([tobiashuste](https://github.com/tobiashuste))
- Replace deprecated include with import\_tasks [\#12](https://github.com/hifis-net/ansible-collection-toolkit/pull/12) ([Normo](https://github.com/Normo))
- Update README.md [\#11](https://github.com/hifis-net/ansible-collection-toolkit/pull/11) ([Normo](https://github.com/Normo))
- Test the role via molecule and update supported OS [\#9](https://github.com/hifis-net/ansible-collection-toolkit/pull/9) ([tobiashuste](https://github.com/tobiashuste))
- Bump actions/checkout from 2 to 3 [\#6](https://github.com/hifis-net/ansible-collection-toolkit/pull/6) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint-action from 6.0.2 to 6.3.0 [\#5](https://github.com/hifis-net/ansible-collection-toolkit/pull/5) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add dependabot config to daily check for GitHub actions updates [\#4](https://github.com/hifis-net/ansible-collection-toolkit/pull/4) ([Normo](https://github.com/Normo))
- Force quoted strings [\#3](https://github.com/hifis-net/ansible-collection-toolkit/pull/3) ([Normo](https://github.com/Normo))
- Add yamllint configuration  [\#2](https://github.com/hifis-net/ansible-collection-toolkit/pull/2) ([Normo](https://github.com/Normo))
- Fork https://github.com/jnv/ansible-role-unattended-upgrades [\#1](https://github.com/hifis-net/ansible-collection-toolkit/pull/1) ([Normo](https://github.com/Normo))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
