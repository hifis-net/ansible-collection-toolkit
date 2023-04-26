# Changelog

## [Unreleased](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/HEAD)

[Full Changelog](https://github.com/hifis-net/ansible-role-unattended-upgrades/compare/v2.0.1...HEAD)

**Merged pull requests:**

- Add test for Unattended-Upgrade::Sender [\#103](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/103) ([Normo](https://github.com/Normo))
- Unattended-Upgrade::Sender support [\#101](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/101) ([turikhay](https://github.com/turikhay))
- Bump ansible-lint from 6.10.0 to 6.10.2 [\#82](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/82) ([dependabot[bot]](https://github.com/apps/dependabot))
- Do not cancel ci jobs if one ci job in the matrix fails [\#81](https://github.com/hifis-net/ansible-role-unattended-upgrades/pull/81) ([Normo](https://github.com/Normo))

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
