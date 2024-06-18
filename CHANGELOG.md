# Changelog

## [v4.4.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.4.0) (2024-06-18)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.3.0...v4.4.0)

**Implemented enhancements:**

- Make GitLab DB port configurable in role gitlab [\#272](https://github.com/hifis-net/ansible-collection-toolkit/issues/272) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]

**Merged pull requests:**

- Make GitLab DB port configurable in GitLab config template [\#273](https://github.com/hifis-net/ansible-collection-toolkit/pull/273) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([christianhueserhzdr](https://github.com/christianhueserhzdr))

## [v4.3.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.3.0) (2024-06-04)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.2.0...v4.3.0)

**Implemented enhancements:**

- Add Debian 12 Bookworm support for ssh\_keys role [\#263](https://github.com/hifis-net/ansible-collection-toolkit/issues/263) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)]
- Bump keepalived to version 2.3.1 [\#262](https://github.com/hifis-net/ansible-collection-toolkit/issues/262) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)]
- Support HAProxy 2.8 [\#254](https://github.com/hifis-net/ansible-collection-toolkit/issues/254) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]
- Add Debain support [\#243](https://github.com/hifis-net/ansible-collection-toolkit/issues/243) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]
- Add second test instance to molecule unattended\_upgrades scenario [\#122](https://github.com/hifis-net/ansible-collection-toolkit/issues/122) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)]
- Add issue templates [\#264](https://github.com/hifis-net/ansible-collection-toolkit/pull/264) ([Normo](https://github.com/Normo))
- Add support for Ubuntu 24.04 [\#253](https://github.com/hifis-net/ansible-collection-toolkit/pull/253) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))

**Merged pull requests:**

- Prepare release version 4.3.0 [\#265](https://github.com/hifis-net/ansible-collection-toolkit/pull/265) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Bump netaddr from 1.2.1 to 1.3.0 [\#261](https://github.com/hifis-net/ansible-collection-toolkit/pull/261) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add second test instance to unattended\_upgrades molecule scenario [\#260](https://github.com/hifis-net/ansible-collection-toolkit/pull/260) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- Bump keepalived from version 2.3.0 to 2.3.1 [\#259](https://github.com/hifis-net/ansible-collection-toolkit/pull/259) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Add Debian Support for HAProxy role [\#258](https://github.com/hifis-net/ansible-collection-toolkit/pull/258) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Test ssh\_keys role on Debian 12 \(Bookworm\) [\#257](https://github.com/hifis-net/ansible-collection-toolkit/pull/257) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([Normo](https://github.com/Normo))
- Support HAProxy 2.8 [\#255](https://github.com/hifis-net/ansible-collection-toolkit/pull/255) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Bump keepalived from version 2.2.8 to 2.3.0 [\#251](https://github.com/hifis-net/ansible-collection-toolkit/pull/251) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))

## [v4.2.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.2.0) (2024-05-23)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.1.0...v4.2.0)

**Implemented enhancements:**

- Include hifis.gitlab role into collection [\#240](https://github.com/hifis-net/ansible-collection-toolkit/issues/240) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]
- Include hifis.redis role into collection [\#236](https://github.com/hifis-net/ansible-collection-toolkit/issues/236) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)]
- Include hifis.netplan into collection [\#234](https://github.com/hifis-net/ansible-collection-toolkit/issues/234) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)]
- Include hifis.haproxy into collection [\#228](https://github.com/hifis-net/ansible-collection-toolkit/issues/228) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]

**Fixed bugs:**

- Use dnf instead of yum module [\#232](https://github.com/hifis-net/ansible-collection-toolkit/pull/232) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))

**Closed issues:**

- Version 3.3.0 doesn't seem to be available on ansible galaxy [\#201](https://github.com/hifis-net/ansible-collection-toolkit/issues/201)
- Remove master branch [\#245](https://github.com/hifis-net/ansible-collection-toolkit/issues/245)
- Switch to Ubuntu 24.04 image for GitHub Actions hosted runners [\#231](https://github.com/hifis-net/ansible-collection-toolkit/issues/231)
- License headers in jinja templates should use jinja style comments [\#229](https://github.com/hifis-net/ansible-collection-toolkit/issues/229)

**Merged pull requests:**

- Prepare release version 4.2.0 [\#249](https://github.com/hifis-net/ansible-collection-toolkit/pull/249) ([Normo](https://github.com/Normo))
- Add hifis.gitlab role [\#241](https://github.com/hifis-net/ansible-collection-toolkit/pull/241) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Use jinja style comments for license headers in jinja templates [\#239](https://github.com/hifis-net/ansible-collection-toolkit/pull/239) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Switch to Ubuntu 24.04 image for GitHub Actions hosted runners [\#238](https://github.com/hifis-net/ansible-collection-toolkit/pull/238) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Add hifis.redis role [\#237](https://github.com/hifis-net/ansible-collection-toolkit/pull/237) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- Add hifis.netplan role [\#235](https://github.com/hifis-net/ansible-collection-toolkit/pull/235) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([Normo](https://github.com/Normo))
- chore\(deps\): bump ansible from 9.5.1 to 9.6.0 [\#233](https://github.com/hifis-net/ansible-collection-toolkit/pull/233) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add hifis.haproxy role [\#230](https://github.com/hifis-net/ansible-collection-toolkit/pull/230) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))

## [v4.1.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.1.0) (2024-05-16)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.0.0...v4.1.0)

**Implemented enhancements:**

- Include hifis.keepalived role into collection [\#214](https://github.com/hifis-net/ansible-collection-toolkit/issues/214)
- Include hifis.ssh-keys role into collection [\#212](https://github.com/hifis-net/ansible-collection-toolkit/issues/212)
- Include hifis.gitlab\_runner role into collection [\#210](https://github.com/hifis-net/ansible-collection-toolkit/issues/210)

**Closed issues:**

- Configure Dependabot to update dependencies in prepare action [\#217](https://github.com/hifis-net/ansible-collection-toolkit/issues/217)

**Merged pull requests:**

- chore\(deps-dev\): bump ansible-lint from 24.2.3 to 24.5.0 [\#220](https://github.com/hifis-net/ansible-collection-toolkit/pull/220) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps\): bump ansible/ansible-lint from 24.2.3 to 24.5.0 [\#219](https://github.com/hifis-net/ansible-collection-toolkit/pull/219) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 4.1.0 [\#224](https://github.com/hifis-net/ansible-collection-toolkit/pull/224) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Always run ansible-lint in GitHub Actions [\#221](https://github.com/hifis-net/ansible-collection-toolkit/pull/221) ([tobiashuste](https://github.com/tobiashuste))
- Make sure to update prepare-action via Dependabot [\#218](https://github.com/hifis-net/ansible-collection-toolkit/pull/218) ([tobiashuste](https://github.com/tobiashuste))
- Integrate gitlab\_runner role into hifis toolkit [\#216](https://github.com/hifis-net/ansible-collection-toolkit/pull/216) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Add hifis.keepalived role [\#215](https://github.com/hifis-net/ansible-collection-toolkit/pull/215) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Add hifis.ssh\_keys role [\#213](https://github.com/hifis-net/ansible-collection-toolkit/pull/213) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([Normo](https://github.com/Normo))

## [v4.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.0.0) (2024-05-08)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v3.3.0...v4.0.0)

**UPGRADE NOTES:**

The `hifis.unattended_upgrades` role has been migrated to the `hifis.toolkit` collection. Please ensure that you install the new collection as follows:

```sh
ansible-galaxy collection install hifis.toolkit
```

To continue using the [`unattended_upgrades`](roles/unattended_upgrades) role as before, please include it as described:

```yaml
- hosts: all
  roles:
     - role: hifis.toolkit.unattended_upgrades
```

**Breaking changes:**

- Migrate role to role in a collection [\#165](https://github.com/hifis-net/ansible-collection-toolkit/issues/165)

**Closed issues:**

- Make collection REUSE-compliant [\#197](https://github.com/hifis-net/ansible-collection-toolkit/issues/197)

**Merged pull requests:**

- chore\(deps\): bump ansible/ansible-lint from 24.2.1 to 24.2.3 [\#208](https://github.com/hifis-net/ansible-collection-toolkit/pull/208) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump ansible-lint from 24.2.0 to 24.2.1 [\#194](https://github.com/hifis-net/ansible-collection-toolkit/pull/194) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 4.0.0 [\#209](https://github.com/hifis-net/ansible-collection-toolkit/pull/209) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- chore\(deps\): bump ansible from 9.3.0 to 9.5.1 [\#204](https://github.com/hifis-net/ansible-collection-toolkit/pull/204) ([dependabot[bot]](https://github.com/apps/dependabot))
- Release version 4.0.0 [\#198](https://github.com/hifis-net/ansible-collection-toolkit/pull/198) ([Normo](https://github.com/Normo))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
