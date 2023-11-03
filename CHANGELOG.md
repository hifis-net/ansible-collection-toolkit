# Changelog

## [v3.2.1](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v3.2.1) (2023-11-03)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v3.2.0...v3.2.1)

**Fixed bugs:**

- "Bullseye-Workaround" needs to be applied to bookworm and later as well [\#146](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/146)

**Closed issues:**

- Unattended-Upgrade::Origins-Pattern from 50unattended-upgrades apparently can't be "overruled" [\#145](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/145)

**Merged pull requests:**

- fix: reformat allowed origins pattern [\#160](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/160) ([Normo](https://github.com/Normo))
- fix: allow ${distro\_codename}-security on Debian bookworm [\#159](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/159) ([Normo](https://github.com/Normo))
- chore\(deps-dev\): bump ansible-lint from 6.18.0 to 6.21.1 [\#157](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/157) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.3.0 to 8.5.0 [\#155](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/155) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 3 to 4 [\#147](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/147) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 6.0.1 to 6.0.2 [\#144](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/144) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.2.0](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v3.2.0) (2023-08-25)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v3.1.0...v3.2.0)

**Implemented enhancements:**

- Add support for Debian Bookworm [\#134](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/134)

**Closed issues:**

- Remove official support for EOL Ubuntu 18.04 [\#139](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/139)

**Merged pull requests:**

- chore: prepare release of version 3.2.0 [\#142](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/142) ([tobiashuste](https://github.com/tobiashuste))
- fix: remove official support for EOL Ubuntu 18.04 [\#141](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/141) ([tobiashuste](https://github.com/tobiashuste))
- feat: add support for Debian 12 bookworm [\#140](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/140) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible-lint from 6.17.2 to 6.18.0 [\#138](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/138) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.1.0 to 6.0.1 [\#137](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/137) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.1.0 to 8.3.0 [\#136](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/136) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule-plugins from 23.4.1 to 23.5.0 [\#133](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/133) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.2 to 6.17.2 [\#131](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/131) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 5.0.1 to 5.1.0 [\#130](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/130) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 8.0.0 to 8.1.0 [\#129](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/129) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.1.0](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v3.1.0) (2023-06-09)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v3.0.0...v3.1.0)

**Implemented enhancements:**

- Added custom of apt-daily timers apt-daily-upgrade [\#85](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/85)
- Test custom apt-daily timers [\#121](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/121) ([Normo](https://github.com/Normo))

**Closed issues:**

- Remove support for ansible-core 2.12 [\#124](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/124)

**Merged pull requests:**

- Prepare release version 3.1.0 [\#127](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/127) ([Normo](https://github.com/Normo))
- Update minimum ansible version to 2.13 [\#125](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/125) ([Normo](https://github.com/Normo))
- Add support for custom apt-daily and apt-daily-upgrade timers [\#120](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/120) ([pgassmann](https://github.com/pgassmann))
- Bump ansible from 7.6.0 to 8.0.0 [\#119](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/119) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v3.0.0](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v3.0.0) (2023-05-26)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v2.0.1...v3.0.0)

**UPGRADE NOTES AND BREAKING CHANGES:**

As of this release, all Apt options for `unattended-upgrades` made in the default OS configuration files `/etc/apt/apt.conf.d/20auto-upgrades` and `/etc/apt/apt.conf.d/50unattended-upgrades` are now completely overwritten instead of being merged. This means that from now on only the options set by this role are active.

**Fixed bugs:**

- apt options are not overridden but merged [\#94](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/94)

**Closed issues:**

- ValueError: not enough values to unpack \(expected 2, got 1\) on Ubuntu Jammy [\#55](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/55)

**Merged pull requests:**

- Bump ansible from 7.5.0 to 7.6.0 [\#115](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/115) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.31.0 to 1.32.0 [\#114](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/114) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.1 to 6.16.2 [\#113](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/113) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.16.0 to 6.16.1 [\#112](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/112) ([dependabot[bot]](https://github.com/apps/dependabot))
- fix: reformat config template [\#111](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/111) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.14.3 to 6.16.0 [\#109](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Erase all unattended-upgrades options first [\#107](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/107) ([Normo](https://github.com/Normo))
- Bump yamllint from 1.28.0 to 1.31.0 [\#106](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/106) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.1.0 to 7.5.0 [\#105](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/105) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.4 to 5.0.1 [\#104](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/104) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add test for Unattended-Upgrade::Sender [\#103](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/103) ([Normo](https://github.com/Normo))
- Unattended-Upgrade::Sender support [\#101](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/101) ([turikhay](https://github.com/turikhay))
- Bump ansible-lint from 6.10.2 to 6.14.3 [\#99](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/99) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.10.0 to 6.10.2 [\#82](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/82) ([dependabot[bot]](https://github.com/apps/dependabot))
- Do not cancel ci jobs if one ci job in the matrix fails [\#81](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/81) ([Normo](https://github.com/Normo))
- Prepare release version 3.0.0 [\#117](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/117) ([Normo](https://github.com/Normo))

## [v2.0.1](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v2.0.1) (2022-12-15)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v2.0.0...v2.0.1)

**Fixed bugs:**

- Fix minimum specification of Ansible version [\#77](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/77) ([tobiashuste](https://github.com/tobiashuste))

**Closed issues:**

- `unattended_dl_limit` doesn't work [\#76](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/76)
- ansible.builtin.import\_tasks problem [\#75](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/75)
- Detach fork [\#66](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/66)

**Merged pull requests:**

- Bump ansible-lint from 6.9.1 to 6.10.0 [\#79](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/79) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 7.0.0 to 7.1.0 [\#74](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/74) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.3 to 4.0.4 [\#73](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/73) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.9.0 to 6.9.1 [\#72](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/72) ([dependabot[bot]](https://github.com/apps/dependabot))
- Make sure GitHub Actions runs on the main branch [\#70](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/70) ([tobiashuste](https://github.com/tobiashuste))
- Fix deprecation warning in GitHub Actions [\#69](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/69) ([tobiashuste](https://github.com/tobiashuste))
- Prepare release v2.0.1 [\#78](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/78) ([Normo](https://github.com/Normo))
- Leave a hint about the original fork [\#71](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/71) ([Normo](https://github.com/Normo))

## [v2.0.0](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v2.0.0) (2022-12-02)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v1.12.2...v2.0.0)

**UPGRADE NOTES AND BREAKING CHANGES:**

If you have used this role before version 2.0.0, the files `20auto-upgrades` and `50unattended-upgrades` will differ from the system defaults (instead of the configuration being placed in a separate file, as we do now).
These can be left as-is as they will be overridden.
During OS upgrades, when asked if these files should be overwritten by the maintainer's package, say yes.
They will then be reset to their default states, and you won't be asked these questions again.

**Implemented enhancements:**

- \[Feature Request\] Use force\_apt\_get [\#32](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/32)
- Override configuration in a separate apt.conf.d file [\#10](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/10)
- Test role via Molecule [\#8](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/8)

**Fixed bugs:**

- Molecule folder not linted by molecule [\#48](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/48)
- Change caused by indentation [\#53](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/53)
- Fix installation of powermgmt-base package [\#35](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/35)

**Closed issues:**

- Documentation role name mismatch [\#41](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/41)
- Some configurations options are missing [\#56](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/56)
- Remove support for OS that reached EOL [\#38](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/38)
- Add changelog [\#33](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/33)
- Add contribution guide [\#16](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/16)
- Rename default branch to `main` [\#13](https://github.com/hifis-net/ansible-role-unattended-upgrades/issues/13)

**Merged pull requests:**

- Bump ansible-lint from 6.8.6 to 6.9.0 [\#62](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/62) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.5.0 to 7.0.0 [\#60](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/60) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add missing option Unattended-Upgrade::MailReport [\#57](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/57) ([nono-lqdn](https://github.com/nono-lqdn))
- Bump ansible-lint from 6.8.2 to 6.8.6 [\#54](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/54) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.2 to 4.0.3 [\#49](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/49) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 4.0.1 to 4.0.2 [\#47](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/47) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.1 to 6.8.2 [\#46](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/46) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.4.0 to 6.5.0 [\#45](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/45) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.8.0 to 6.8.1 [\#44](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/44) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 6.5.0 to 6.8.0 [\#43](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/43) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix role name in README [\#42](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/42) ([lukashass](https://github.com/lukashass))
- Bump molecule-podman from 2.0.2 to 2.0.3 [\#40](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/40) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 6.2.0 to 6.4.0 [\#25](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/25) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump yamllint from 1.27.1 to 1.28.0 [\#24](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/24) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update README.md [\#19](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/19) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 6.4.0 to 6.5.0 [\#15](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/15) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 2.0.0 [\#67](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/67) ([Normo](https://github.com/Normo))
- Add codeowners to autoassign reviewers [\#65](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/65) ([Normo](https://github.com/Normo))
- Ensure new default branch main is used by Galaxy [\#64](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/64) ([Normo](https://github.com/Normo))
- Lint molecule folder [\#63](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/63) ([Normo](https://github.com/Normo))
- Fix indentation for unattended\_origins\_patterns in template file [\#61](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/61) ([Normo](https://github.com/Normo))
- Remove support for OS that reached EOL [\#39](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/39) ([Normo](https://github.com/Normo))
- Add changelog [\#37](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/37) ([Normo](https://github.com/Normo))
- Fix installation of powermgmt-base [\#36](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/36) ([Normo](https://github.com/Normo))
- Force usage of apt-get instead of aptitude [\#34](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/34) ([Normo](https://github.com/Normo))
- Test Remove-Unused-Kernel-Packages option [\#31](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/31) ([Normo](https://github.com/Normo))
- Add options for controlling the removal of unused kernel packages [\#29](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/29) ([gcotelli](https://github.com/gcotelli))
- Stop overwriting default config [\#28](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/28) ([alpha0010](https://github.com/alpha0010))
- Add contribution guide [\#22](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/22) ([Normo](https://github.com/Normo))
- Remove custom ansible-lint config [\#18](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/18) ([Normo](https://github.com/Normo))
- Fix 'All names should start with an uppercase letter' warnings [\#17](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/17) ([Normo](https://github.com/Normo))
- Fix CI badge in README [\#14](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/14) ([tobiashuste](https://github.com/tobiashuste))
- Replace deprecated include with import\_tasks [\#12](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/12) ([Normo](https://github.com/Normo))
- Update README.md [\#11](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/11) ([Normo](https://github.com/Normo))
- Test the role via molecule and update supported OS [\#9](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/9) ([tobiashuste](https://github.com/tobiashuste))
- Bump actions/checkout from 2 to 3 [\#6](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/6) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint-action from 6.0.2 to 6.3.0 [\#5](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/5) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add dependabot config to daily check for GitHub actions updates [\#4](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/4) ([Normo](https://github.com/Normo))
- Force quoted strings [\#3](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/3) ([Normo](https://github.com/Normo))
- Add yamllint configuration  [\#2](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/2) ([Normo](https://github.com/Normo))
- Fork https://github.com/jnv/ansible-role-unattended-upgrades [\#1](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/1) ([Normo](https://github.com/Normo))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
