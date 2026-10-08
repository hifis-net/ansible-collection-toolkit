# Changelog

## [v7.0.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v7.0.1) (2026-10-08)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v7.0.0...v7.0.1)

**Fixed bugs:**

- haproxy: Upgrading to v7.0.0 breaks apt on Ubuntu hosts that use the PPA \(conflicting Signed-By\) [\#659](https://github.com/hifis-net/ansible-collection-toolkit/issues/659) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]

**Merged pull requests:**

- haproxy: remove legacy PPA source file on Ubuntu [\#660](https://github.com/hifis-net/ansible-collection-toolkit/pull/660) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))

## [v7.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v7.0.0) (2026-10-07)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.3.2...v7.0.0)

**UPGRADE NOTES:**

- The collection now requires ansible-core 2.19 or newer. ansible-core 2.17 and 2.18 are end-of-life.
- All roles now validate their variables via `meta/argument_specs.yml` before any task runs. Invalid values fail early.
- `haproxy_stats_enable` now only accepts `enable` or `disable`. Playbooks passing a boolean or any other value previously produced an invalid `stats` directive and now fail during role argument validation.
- The `gitlab_runner` role no longer supports GitLab Runner versions older than 17.7.0. If you pin `gitlab_runner_version` to an older release, upgrade to 17.7.0 or newer before updating the collection.
- The `gitlab_runner` role now always installs `gitlab-runner-helper-images` together with `gitlab-runner`. The APT pin applies to both packages, so the helper images are pinned to `gitlab_runner_version` too. If you install from local packages via `gitlab_runner_deb_file`, you must now also set `gitlab_runner_helper_images_deb_file`.
- `gitlab_runner_namerservers` has been renamed to `gitlab_runner_nameservers` to fix a typo. The role fails if the old variable is still set, so rename it in your inventory before upgrading.
- Entries in `gitlab_runner_list` are now validated against the documented options. Unknown keys fail the play. This includes misspelled option names and the removed `tags`, `locked` and `run_untagged` options, which the role no longer used. With runner authentication tokens (`glrt-…`), these properties are set in GitLab when you create the runner, so remove them from your `gitlab_runner_list` entries. `executor` and `docker_image` are now required, and so are the options that the selected executor or cache type depends on (e.g. `machine_driver`/`machine_name` for `docker+machine`, the bucket settings for the `s3` cache). Inventories that render a valid `config.toml` today are unaffected.
- `gitlab_runner_concurrent` is now enforced as a required variable. It has no default and was already needed to render `config.toml`. If it is missing, the play now fails immediately during argument validation rather than later when rendering the template.
- The boolean switches of the `gitlab` role now default to real booleans (`true`/`false`) instead of the strings `"true"`/`"false"`. Quoted values still work, but we recommend switching to unquoted booleans.
- `gitlab_feature_flags[].enabled: "false"` (quoted) now disables the feature flag. Previously, the string was evaluated as truthy, so the flag was enabled. Check your feature flags if you used quoted values.
- `gitlab_registry_external_url` was removed because it had no effect. Set the registry URL via `gitlab_ruby_configuration_calls` with the key `registry_external_url` instead.
- `gitlab_gpg_key_id` was removed because it has had no effect since the `apt_key` task was dropped. You can remove it from your inventory.
- The `zammad` role now installs Zammad 7.2.1 by default (previously 6.5.0).
- The `keepalived` role now installs keepalived 2.4.3 by default (previously 2.3.2).
- Debian 11 (Bullseye) is no longer supported by the `gitlab`, `gitlab_runner`, `haproxy`, `ssh_keys` and `unattended_upgrades` roles.

**Breaking changes:**

- gitlab-runner: Remove ineffective runner options [\#640](https://github.com/hifis-net/ansible-collection-toolkit/issues/640) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)]
- Rename misspelled variable gitlab\_runner\_namerservers [\#631](https://github.com/hifis-net/ansible-collection-toolkit/issues/631) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)]
- Drop support for Debian 11 \(Bullseye\) [\#626](https://github.com/hifis-net/ansible-collection-toolkit/issues/626) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]
- Add argument specifications for gitlab-runner role [\#630](https://github.com/hifis-net/ansible-collection-toolkit/pull/630) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Add argument specifications for gitlab role [\#629](https://github.com/hifis-net/ansible-collection-toolkit/pull/629) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- gitlab-runner: Simplify installation and drop support for versions \< 17.7.0 [\#625](https://github.com/hifis-net/ansible-collection-toolkit/pull/625) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Require ansible-core 2.19 as minimum version [\#591](https://github.com/hifis-net/ansible-collection-toolkit/pull/591) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Bump default Zammad version to 7.0.1 [\#581](https://github.com/hifis-net/ansible-collection-toolkit/pull/581) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))

**Implemented enhancements:**

- Add support for Ubuntu 26.04 \(Resolute Raccoon\) [\#601](https://github.com/hifis-net/ansible-collection-toolkit/issues/601)
- Add `no_log: true` to secret parameters in role argument specifications [\#592](https://github.com/hifis-net/ansible-collection-toolkit/issues/592)
- Enable role argument validation based on an argument specification [\#195](https://github.com/hifis-net/ansible-collection-toolkit/issues/195)
- Install keepalived 2.4.3 by default [\#652](https://github.com/hifis-net/ansible-collection-toolkit/pull/652) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Install Zammad 7.2.1 by default [\#651](https://github.com/hifis-net/ansible-collection-toolkit/pull/651) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- Hide secrets in task output and diffs by default [\#649](https://github.com/hifis-net/ansible-collection-toolkit/pull/649) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- Allow configurable NGINX locations for serving static files [\#580](https://github.com/hifis-net/ansible-collection-toolkit/pull/580) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))

**Fixed bugs:**

- haproxy, keepalived: config validation is skipped on initial run [\#634](https://github.com/hifis-net/ansible-collection-toolkit/issues/634) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]

**Closed issues:**

- Deprecation notice: migrate from `github-action-test-galaxy-import` [\#624](https://github.com/hifis-net/ansible-collection-toolkit/issues/624)
- Declare external collection dependencies in galaxy.yml [\#589](https://github.com/hifis-net/ansible-collection-toolkit/issues/589)

**Merged pull requests:**

- Prepare release version 7.0.0 [\#657](https://github.com/hifis-net/ansible-collection-toolkit/pull/657) ([Normo](https://github.com/Normo))
- Bump ansible to v14.5.0 [\#655](https://github.com/hifis-net/ansible-collection-toolkit/pull/655) ([Normo](https://github.com/Normo))
- Test GitLab-Runner 19.4.1 with molecule [\#654](https://github.com/hifis-net/ansible-collection-toolkit/pull/654) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Update Python dependencies [\#650](https://github.com/hifis-net/ansible-collection-toolkit/pull/650) ([Normo](https://github.com/Normo))
- build\(deps\): bump virtualenv from 20.36.1 to 21.7.13 [\#648](https://github.com/hifis-net/ansible-collection-toolkit/pull/648) ([dependabot[bot]](https://github.com/apps/dependabot))
- ci: run workflows on ubuntu-26.04 runners [\#647](https://github.com/hifis-net/ansible-collection-toolkit/pull/647) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- gitlab-runner: validate executor- and cache-specific options [\#646](https://github.com/hifis-net/ansible-collection-toolkit/pull/646) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- build\(deps-dev\): bump antsibull-nox from 1.9.1 to 1.9.3 [\#644](https://github.com/hifis-net/ansible-collection-toolkit/pull/644) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible-community/antsibull-nox from 1.9.1 to 1.9.3 [\#643](https://github.com/hifis-net/ansible-collection-toolkit/pull/643) ([dependabot[bot]](https://github.com/apps/dependabot))
- gitlab\_runner: remove ineffective tags, locked and run\_untagged options [\#641](https://github.com/hifis-net/ansible-collection-toolkit/pull/641) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- gitlab-runner: rename misspelled variable gitlab\_runner\_namerservers [\#638](https://github.com/hifis-net/ansible-collection-toolkit/pull/638) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- build\(deps-dev\): bump ansible-lint from 26.8.0 to 26.9.0 [\#637](https://github.com/hifis-net/ansible-collection-toolkit/pull/637) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump molecule from 26.8.0 to 26.9.0 [\#636](https://github.com/hifis-net/ansible-collection-toolkit/pull/636) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 26.8.0 to 26.9.0 [\#635](https://github.com/hifis-net/ansible-collection-toolkit/pull/635) ([dependabot[bot]](https://github.com/apps/dependabot))
- haproxy, keepalived: ensure config file is always validated [\#633](https://github.com/hifis-net/ansible-collection-toolkit/pull/633) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- fix\(haproxy\): defer configuration deployment until TLS certificate and dhparam files exist [\#632](https://github.com/hifis-net/ansible-collection-toolkit/pull/632) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([ndejesus](https://github.com/ndejesus))
- Migrate Galaxy import check to antsibull-nox [\#628](https://github.com/hifis-net/ansible-collection-toolkit/pull/628) ([Normo](https://github.com/Normo))
- Drop support for Debian 11 \(Bullseye\) [\#627](https://github.com/hifis-net/ansible-collection-toolkit/pull/627) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- build\(deps-dev\): bump ansible-lint from 26.6.0 to 26.8.0 [\#623](https://github.com/hifis-net/ansible-collection-toolkit/pull/623) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump molecule from 26.6.0 to 26.8.0 [\#622](https://github.com/hifis-net/ansible-collection-toolkit/pull/622) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 26.6.0 to 26.8.0 [\#621](https://github.com/hifis-net/ansible-collection-toolkit/pull/621) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add argument specifications for keepalived role [\#619](https://github.com/hifis-net/ansible-collection-toolkit/pull/619) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Enable ansible-lint rule role-argument-spec [\#618](https://github.com/hifis-net/ansible-collection-toolkit/pull/618) ([Normo](https://github.com/Normo))
- redis: mark password options as no\_log in argument specs [\#617](https://github.com/hifis-net/ansible-collection-toolkit/pull/617) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- haproxy: use integer type for nbproc and nbthread [\#616](https://github.com/hifis-net/ansible-collection-toolkit/pull/616) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Make HAProxy repository signing keys configurable [\#614](https://github.com/hifis-net/ansible-collection-toolkit/pull/614) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Enable HAProxy 3.2 on Debian 12 \(Bookworm\) [\#613](https://github.com/hifis-net/ansible-collection-toolkit/pull/613) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- build\(deps\): bump cryptography from 46.0.7 to 50.0.0 [\#612](https://github.com/hifis-net/ansible-collection-toolkit/pull/612) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add Ubuntu 26.04 support to gitlab role [\#610](https://github.com/hifis-net/ansible-collection-toolkit/pull/610) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Add Ubuntu 26.04 to unattended\_upgrades role [\#609](https://github.com/hifis-net/ansible-collection-toolkit/pull/609) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 26.04 to netplan role [\#608](https://github.com/hifis-net/ansible-collection-toolkit/pull/608) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([tobiashuste](https://github.com/tobiashuste))
- Add Ubuntu 26.04 support to Redis role [\#607](https://github.com/hifis-net/ansible-collection-toolkit/pull/607) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([tobiashuste](https://github.com/tobiashuste))
- Add Ubuntu 26.04 support to keepalived role [\#606](https://github.com/hifis-net/ansible-collection-toolkit/pull/606) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 26.04 to ssh\_keys role [\#605](https://github.com/hifis-net/ansible-collection-toolkit/pull/605) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([tobiashuste](https://github.com/tobiashuste))
- Add support for Ubuntu 26.04 in haproxy role [\#604](https://github.com/hifis-net/ansible-collection-toolkit/pull/604) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([tobiashuste](https://github.com/tobiashuste))
- Add Ubuntu 26.04 support to gitlab-runner role [\#603](https://github.com/hifis-net/ansible-collection-toolkit/pull/603) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Add Ubuntu 26.04 support to Zammad role [\#602](https://github.com/hifis-net/ansible-collection-toolkit/pull/602) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- build\(deps\): bump actions/labeler from 6.1.0 to 7.0.0 [\#600](https://github.com/hifis-net/ansible-collection-toolkit/pull/600) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump actions/setup-python from 6 to 7 in /.github/workflows/prepare-action [\#599](https://github.com/hifis-net/ansible-collection-toolkit/pull/599) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible-core from 2.19.5 to 2.19.11rc1 [\#598](https://github.com/hifis-net/ansible-collection-toolkit/pull/598) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): update molecule-plugins\[podman\] requirement from \>=25.8.12 to \>=26.7.15 [\#597](https://github.com/hifis-net/ansible-collection-toolkit/pull/597) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([dependabot[bot]](https://github.com/apps/dependabot))
- Switch to new Zammad repo [\#593](https://github.com/hifis-net/ansible-collection-toolkit/pull/593) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Declare external collection dependencies in galaxy.yml [\#590](https://github.com/hifis-net/ansible-collection-toolkit/pull/590) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- build\(deps-dev\): bump molecule from 26.4.0 to 26.6.0 [\#588](https://github.com/hifis-net/ansible-collection-toolkit/pull/588) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump ansible-lint from 26.4.0 to 26.6.0 [\#587](https://github.com/hifis-net/ansible-collection-toolkit/pull/587) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 26.4.0 to 26.6.0 [\#586](https://github.com/hifis-net/ansible-collection-toolkit/pull/586) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump actions/checkout from 6 to 7 [\#584](https://github.com/hifis-net/ansible-collection-toolkit/pull/584) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([dependabot[bot]](https://github.com/apps/dependabot))
- Configure ANSIBLE\_ROLES\_PATH for scenarios pulling Galaxy roles [\#583](https://github.com/hifis-net/ansible-collection-toolkit/pull/583) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- build\(deps-dev\): bump molecule from 26.3.0 to 26.4.0 [\#582](https://github.com/hifis-net/ansible-collection-toolkit/pull/582) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump actions/labeler from 6.0.1 to 6.1.0 [\#579](https://github.com/hifis-net/ansible-collection-toolkit/pull/579) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump cryptography from 45.0.6 to 46.0.7 [\#578](https://github.com/hifis-net/ansible-collection-toolkit/pull/578) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump ansible-lint from 26.3.0 to 26.4.0 [\#577](https://github.com/hifis-net/ansible-collection-toolkit/pull/577) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 26.3.0 to 26.4.0 [\#576](https://github.com/hifis-net/ansible-collection-toolkit/pull/576) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump pygments from 2.19.2 to 2.20.0 [\#575](https://github.com/hifis-net/ansible-collection-toolkit/pull/575) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump black from 25.1.0 to 26.3.1 [\#573](https://github.com/hifis-net/ansible-collection-toolkit/pull/573) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump filelock from 3.19.1 to 3.20.3 [\#571](https://github.com/hifis-net/ansible-collection-toolkit/pull/571) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump molecule from 25.12.0 to 26.3.0 [\#570](https://github.com/hifis-net/ansible-collection-toolkit/pull/570) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps-dev\): bump ansible-lint from 25.12.1 to 26.3.0 [\#569](https://github.com/hifis-net/ansible-collection-toolkit/pull/569) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 25.12.1 to 26.3.0 [\#568](https://github.com/hifis-net/ansible-collection-toolkit/pull/568) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump artis3n/ansible\_galaxy\_collection from 2.11.0 to 3.0.0 [\#564](https://github.com/hifis-net/ansible-collection-toolkit/pull/564) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add option to use apt instead of apt-get [\#563](https://github.com/hifis-net/ansible-collection-toolkit/pull/563) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([thomas-VIGINUM](https://github.com/thomas-VIGINUM))
- build\(deps-dev\): bump yamllint from 1.37.1 to 1.38.0 [\#560](https://github.com/hifis-net/ansible-collection-toolkit/pull/560) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add argument specifications for haproxy role [\#554](https://github.com/hifis-net/ansible-collection-toolkit/pull/554) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Add argument specifications for unattended\_upgrades role [\#553](https://github.com/hifis-net/ansible-collection-toolkit/pull/553) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- Add argument specifications for redis role [\#552](https://github.com/hifis-net/ansible-collection-toolkit/pull/552) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- Add argument specifications for netplan role [\#551](https://github.com/hifis-net/ansible-collection-toolkit/pull/551) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([Normo](https://github.com/Normo))
- Add argument specifications for zammad role [\#550](https://github.com/hifis-net/ansible-collection-toolkit/pull/550) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- build\(deps\): bump ansible-lint from 25.11.1 to 25.12.1 [\#549](https://github.com/hifis-net/ansible-collection-toolkit/pull/549) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible/ansible-lint from 25.11.1 to 25.12.1 [\#548](https://github.com/hifis-net/ansible-collection-toolkit/pull/548) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump ansible to 13.1.0 [\#547](https://github.com/hifis-net/ansible-collection-toolkit/pull/547) ([Normo](https://github.com/Normo))
- build\(deps\): bump molecule from 25.11.1 to 25.12.0 [\#544](https://github.com/hifis-net/ansible-collection-toolkit/pull/544) ([dependabot[bot]](https://github.com/apps/dependabot))
- ssh\_keys: Add AlmaLinux 10 support [\#538](https://github.com/hifis-net/ansible-collection-toolkit/pull/538) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([Normo](https://github.com/Normo))
- ssh\_keys: Add Debian 13 Trixie support [\#537](https://github.com/hifis-net/ansible-collection-toolkit/pull/537) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([Normo](https://github.com/Normo))
- Add argument specifications for ssh\_keys role [\#536](https://github.com/hifis-net/ansible-collection-toolkit/pull/536) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([Normo](https://github.com/Normo))

## [v6.3.2](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.3.2) (2025-12-01)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.3.1...v6.3.2)

**Merged pull requests:**

- Prepare release version 6.3.2 [\#541](https://github.com/hifis-net/ansible-collection-toolkit/pull/541) ([Normo](https://github.com/Normo))
- gitlab: restrict file permission for gitlab.rb [\#540](https://github.com/hifis-net/ansible-collection-toolkit/pull/540) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- gitlab: fix sensitive information disclosure [\#539](https://github.com/hifis-net/ansible-collection-toolkit/pull/539) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))

## [v6.3.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.3.1) (2025-11-28)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.3.0...v6.3.1)

**Closed issues:**

- Check for batched background migrations to be finished [\#247](https://github.com/hifis-net/ansible-collection-toolkit/issues/247) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]

**Merged pull requests:**

- Prepare release version 6.3.1 [\#534](https://github.com/hifis-net/ansible-collection-toolkit/pull/534) ([Normo](https://github.com/Normo))
- gitlab: fix check for batched background migrations [\#533](https://github.com/hifis-net/ansible-collection-toolkit/pull/533) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- gitlab-runner: Bump fleeting-plugin-openstack to v0.33.0 [\#532](https://github.com/hifis-net/ansible-collection-toolkit/pull/532) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- gitlab-runner: Fix empty gitlab\_runner\_version evaluation in version test [\#531](https://github.com/hifis-net/ansible-collection-toolkit/pull/531) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))

## [v6.3.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.3.0) (2025-11-26)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.2.2...v6.3.0)

**Fixed bugs:**

- Conditional errors with Ansible 2.19 [\#511](https://github.com/hifis-net/ansible-collection-toolkit/issues/511)
- Unattended Upgrades Fails on Ubuntu 24 [\#510](https://github.com/hifis-net/ansible-collection-toolkit/issues/510)

**Merged pull requests:**

- Prepare release of version 6.3.0 [\#529](https://github.com/hifis-net/ansible-collection-toolkit/pull/529) ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 25.11.0 to 25.11.1 [\#528](https://github.com/hifis-net/ansible-collection-toolkit/pull/528) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 25.11.0 to 25.11.1 [\#527](https://github.com/hifis-net/ansible-collection-toolkit/pull/527) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.11.0 to 25.11.1 [\#526](https://github.com/hifis-net/ansible-collection-toolkit/pull/526) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 5 to 6 [\#525](https://github.com/hifis-net/ansible-collection-toolkit/pull/525) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 25.7.0 to 25.11.0 [\#524](https://github.com/hifis-net/ansible-collection-toolkit/pull/524) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.9.2 to 25.11.0 [\#523](https://github.com/hifis-net/ansible-collection-toolkit/pull/523) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.9.2 to 25.11.0 [\#522](https://github.com/hifis-net/ansible-collection-toolkit/pull/522) ([dependabot[bot]](https://github.com/apps/dependabot))
- gitlab-runner: Add explicit become directives [\#521](https://github.com/hifis-net/ansible-collection-toolkit/pull/521) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Zammad: Add explicit become directives [\#519](https://github.com/hifis-net/ansible-collection-toolkit/pull/519) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- Switch back to pre built images [\#518](https://github.com/hifis-net/ansible-collection-toolkit/pull/518) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- gitlab: Add explicit become directives [\#517](https://github.com/hifis-net/ansible-collection-toolkit/pull/517) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Update molecule tests to catch missing become directives [\#516](https://github.com/hifis-net/ansible-collection-toolkit/pull/516) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- unattended\_upgrades: Add explicit become directives [\#514](https://github.com/hifis-net/ansible-collection-toolkit/pull/514) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- Bump ansible from 11.9.0 to 12.2.0 [\#513](https://github.com/hifis-net/ansible-collection-toolkit/pull/513) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 5.0.2 to 6.2.0 [\#512](https://github.com/hifis-net/ansible-collection-toolkit/pull/512) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.8.2 to 25.9.2 [\#509](https://github.com/hifis-net/ansible-collection-toolkit/pull/509) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.8.2 to 25.9.2 [\#508](https://github.com/hifis-net/ansible-collection-toolkit/pull/508) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump astral-sh/setup-uv from 6 to 7 in /.github/workflows/prepare-action [\#505](https://github.com/hifis-net/ansible-collection-toolkit/pull/505) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump fsfe/reuse-action from 5.0.0 to 6.0.0 [\#503](https://github.com/hifis-net/ansible-collection-toolkit/pull/503) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/setup-python from 5 to 6 in /.github/workflows/prepare-action [\#485](https://github.com/hifis-net/ansible-collection-toolkit/pull/485) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.2.2](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.2.2) (2025-09-18)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.2.1...v6.2.2)

**Fixed bugs:**

- gitlab\_runner: user\_data template issue with Ansible 2.19 [\#493](https://github.com/hifis-net/ansible-collection-toolkit/issues/493)

**Merged pull requests:**

- Prepare release of version 6.2.2 [\#499](https://github.com/hifis-net/ansible-collection-toolkit/pull/499) ([tobiashuste](https://github.com/tobiashuste))
- Fix user\_data template JSON encoding [\#496](https://github.com/hifis-net/ansible-collection-toolkit/pull/496) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- gitlab\_runner: add option to hide sensitive changes in diffs [\#492](https://github.com/hifis-net/ansible-collection-toolkit/pull/492) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Bump actions/labeler from 5.0.0 to 6.0.1 [\#487](https://github.com/hifis-net/ansible-collection-toolkit/pull/487) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.2.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.2.1) (2025-09-03)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.2.0...v6.2.1)

**Implemented enhancements:**

- Ensure stable order in gitlab\_rails monitoring\_whitelist [\#482](https://github.com/hifis-net/ansible-collection-toolkit/pull/482) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))

**Merged pull requests:**

- Prepare release of version 6.2.1 [\#483](https://github.com/hifis-net/ansible-collection-toolkit/pull/483) ([Normo](https://github.com/Normo))
- Bump ansible-lint from 25.8.1 to 25.8.2 [\#481](https://github.com/hifis-net/ansible-collection-toolkit/pull/481) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.8.1 to 25.8.2 [\#480](https://github.com/hifis-net/ansible-collection-toolkit/pull/480) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.2.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.2.0) (2025-08-22)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.1.1...v6.2.0)

**Implemented enhancements:**

- Make monitoring whitelist variable configurable [\#467](https://github.com/hifis-net/ansible-collection-toolkit/pull/467) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Ansible 2.19 compatibility [\#464](https://github.com/hifis-net/ansible-collection-toolkit/pull/464) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release of version 6.2.0 [\#478](https://github.com/hifis-net/ansible-collection-toolkit/pull/478) ([tobiashuste](https://github.com/tobiashuste))
- zammad role: prefix all internal variables with two underscores [\#477](https://github.com/hifis-net/ansible-collection-toolkit/pull/477) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- unattended\_upgrades role: prefix all internal variables with '\_\_' [\#476](https://github.com/hifis-net/ansible-collection-toolkit/pull/476) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- redis role: prefix all internal variables with '\_\_' [\#475](https://github.com/hifis-net/ansible-collection-toolkit/pull/475) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- netplan role: prefix all internal variables with '\_\_' [\#474](https://github.com/hifis-net/ansible-collection-toolkit/pull/474) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([Normo](https://github.com/Normo))
- Consistently access facts via the ansible\_facts.\* namespace [\#473](https://github.com/hifis-net/ansible-collection-toolkit/pull/473) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Use validate parameter to check Keepalived config file [\#472](https://github.com/hifis-net/ansible-collection-toolkit/pull/472) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Mark tempdir\_fleeting\_plugin as internal variable [\#471](https://github.com/hifis-net/ansible-collection-toolkit/pull/471) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- keepalived role: prefix all internal variables with '\_\_' [\#470](https://github.com/hifis-net/ansible-collection-toolkit/pull/470) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Use validate parameter to check HAProxy config file instead of handler task [\#469](https://github.com/hifis-net/ansible-collection-toolkit/pull/469) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- haproxy role: prefix all internal variables with '\_\_' [\#468](https://github.com/hifis-net/ansible-collection-toolkit/pull/468) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- GitLab-runner role: prefix all internal variables with '\_\_' [\#466](https://github.com/hifis-net/ansible-collection-toolkit/pull/466) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- GitLab role: Prefix all internal variables with '\_\_' [\#465](https://github.com/hifis-net/ansible-collection-toolkit/pull/465) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 25.7.0 to 25.8.1 [\#462](https://github.com/hifis-net/ansible-collection-toolkit/pull/462) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.1.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.1.1) (2025-08-13)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.1.0...v6.1.1)

**Fixed bugs:**

- Fix registry db migrations not executed upon gitlab upgrades [\#459](https://github.com/hifis-net/ansible-collection-toolkit/pull/459) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release v6.1.1 [\#461](https://github.com/hifis-net/ansible-collection-toolkit/pull/461) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 11.8.0 to 11.9.0 [\#460](https://github.com/hifis-net/ansible-collection-toolkit/pull/460) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump actions/checkout from 4 to 5 [\#458](https://github.com/hifis-net/ansible-collection-toolkit/pull/458) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.1.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.1.0) (2025-08-12)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.0.1...v6.1.0)

**Implemented enhancements:**

- Make sure to run registry metadata database migrations [\#455](https://github.com/hifis-net/ansible-collection-toolkit/pull/455) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Add AlmaLinux OS 9 support for GitLab role [\#440](https://github.com/hifis-net/ansible-collection-toolkit/pull/440) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))

**Merged pull requests:**

- Prepare release 6.1.0 [\#456](https://github.com/hifis-net/ansible-collection-toolkit/pull/456) ([tobiashuste](https://github.com/tobiashuste))
- Bump yamllint from 1.35.1 to 1.37.1 [\#453](https://github.com/hifis-net/ansible-collection-toolkit/pull/453) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 25.3.1 to 25.7.0 [\#452](https://github.com/hifis-net/ansible-collection-toolkit/pull/452) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.1.3 to 25.7.0 [\#451](https://github.com/hifis-net/ansible-collection-toolkit/pull/451) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix condition for compatibility with Ansible 2.19 [\#449](https://github.com/hifis-net/ansible-collection-toolkit/pull/449) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([tobiashuste](https://github.com/tobiashuste))
- Fix conditionals for Ansible 2.19 [\#448](https://github.com/hifis-net/ansible-collection-toolkit/pull/448) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([sur5r](https://github.com/sur5r))
- Bump ansible/ansible-lint from 25.6.0 to 25.7.0 [\#447](https://github.com/hifis-net/ansible-collection-toolkit/pull/447) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 11.7.0 to 11.8.0 [\#446](https://github.com/hifis-net/ansible-collection-toolkit/pull/446) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.0.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.0.1) (2025-06-19)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v6.0.0...v6.0.1)

**Merged pull requests:**

- Add host header to Zammad nginx config [\#443](https://github.com/hifis-net/ansible-collection-toolkit/pull/443) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible/ansible-lint from 25.5.0 to 25.6.0 [\#442](https://github.com/hifis-net/ansible-collection-toolkit/pull/442) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 11.6.0 to 11.7.0 [\#441](https://github.com/hifis-net/ansible-collection-toolkit/pull/441) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v6.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v6.0.0) (2025-06-04)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.3.0...v6.0.0)

**UPGRADE NOTES:**

- The deprecated `keepalived_notification_email` variable has been removed from the hifis.keepalived role. Please use `keepalived_notification_emails` instead.
- The deprecated `elasticsearch_url` variable has been removed from the hifis.zammad role. Please use `zammad_elasticsearch_url` instead.
- In preparation for GitLab 18.0, the `git_data_dirs` configuration has been replaced by `gitaly['configuration']` in the hifis.gitlab role. If `gitaly['configuration']` is already defined in the [`gitlab_additional_configurations`](https://github.com/hifis-net/ansible-collection-toolkit/tree/main/roles/gitlab#configurations-via-dictionary-like-ruby-variables) role variable, please ensure that Gitaly storage paths are configured manually.

**Breaking changes:**

- Remove keepalived\_notification\_email variable [\#394](https://github.com/hifis-net/ansible-collection-toolkit/issues/394) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)]
- Remove elasticsearch\_url variable [\#379](https://github.com/hifis-net/ansible-collection-toolkit/issues/379) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)]
- Deprecate git\_data\_dirs setting [\#366](https://github.com/hifis-net/ansible-collection-toolkit/issues/366) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]

**Fixed bugs:**

- Replace obsolete occurrences of Pipfile [\#409](https://github.com/hifis-net/ansible-collection-toolkit/pull/409) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Disable apt cache updates when removing repositories from sources.list [\#432](https://github.com/hifis-net/ansible-collection-toolkit/pull/432) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))

**Closed issues:**

- unattended upgrades unattended\_apt\_daily\_upgrade\_oncalendar is not scheduled [\#429](https://github.com/hifis-net/ansible-collection-toolkit/issues/429)
- unattended upgrades are not scheduled correctly [\#426](https://github.com/hifis-net/ansible-collection-toolkit/issues/426)
- Remove official support for EOL Ubuntu 20.04 [\#435](https://github.com/hifis-net/ansible-collection-toolkit/issues/435)
- Fix apt-key deprecation [\#412](https://github.com/hifis-net/ansible-collection-toolkit/issues/412) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]

**Merged pull requests:**

- Remove official support for EOL Ubuntu 20.04 [\#436](https://github.com/hifis-net/ansible-collection-toolkit/pull/436) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 25.4.0 to 25.5.0 [\#431](https://github.com/hifis-net/ansible-collection-toolkit/pull/431) ([dependabot[bot]](https://github.com/apps/dependabot))
- Do not pin GitLab in Molecule [\#424](https://github.com/hifis-net/ansible-collection-toolkit/pull/424) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 11.3.0 to 11.6.0 [\#423](https://github.com/hifis-net/ansible-collection-toolkit/pull/423) ([dependabot[bot]](https://github.com/apps/dependabot))
- Install Zammad 6.5.0 by default [\#419](https://github.com/hifis-net/ansible-collection-toolkit/pull/419) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Ensure role workflows are running when prepare-action is updated [\#418](https://github.com/hifis-net/ansible-collection-toolkit/pull/418) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 25.1.3 to 25.4.0 [\#417](https://github.com/hifis-net/ansible-collection-toolkit/pull/417) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump astral-sh/setup-uv from 5 to 6 in /.github/workflows/prepare-action [\#415](https://github.com/hifis-net/ansible-collection-toolkit/pull/415) ([dependabot[bot]](https://github.com/apps/dependabot))
- Replace pipenv by uv [\#406](https://github.com/hifis-net/ansible-collection-toolkit/pull/406) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Bump artis3n/ansible\_galaxy\_collection from 2.10.1 to 2.11.0 [\#405](https://github.com/hifis-net/ansible-collection-toolkit/pull/405) ([dependabot[bot]](https://github.com/apps/dependabot))
- Remove Docker 28 IPV6 related fix [\#404](https://github.com/hifis-net/ansible-collection-toolkit/pull/404) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 11.2.0 to 11.3.0 [\#403](https://github.com/hifis-net/ansible-collection-toolkit/pull/403) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix molecule docker startup for Debian and Ubuntu 20.04 [\#402](https://github.com/hifis-net/ansible-collection-toolkit/pull/402) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 25.2.0 to 25.3.1 [\#400](https://github.com/hifis-net/ansible-collection-toolkit/pull/400) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.1.2 to 25.1.3 [\#399](https://github.com/hifis-net/ansible-collection-toolkit/pull/399) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.1.2 to 25.1.3 [\#398](https://github.com/hifis-net/ansible-collection-toolkit/pull/398) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 24.12.0 to 25.2.0 [\#397](https://github.com/hifis-net/ansible-collection-toolkit/pull/397) ([Normo](https://github.com/Normo))
- Prepare release version 6.0.0 [\#437](https://github.com/hifis-net/ansible-collection-toolkit/pull/437) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Test gitlab-runner version 18.0.2 with molecule [\#434](https://github.com/hifis-net/ansible-collection-toolkit/pull/434) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Install HAProxy 3.2 by default [\#433](https://github.com/hifis-net/ansible-collection-toolkit/pull/433) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Allow users to overwrite gitlab\_rails\['repositories\_storages'\] [\#430](https://github.com/hifis-net/ansible-collection-toolkit/pull/430) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Remove support for Ansible EOL 2.16 [\#428](https://github.com/hifis-net/ansible-collection-toolkit/pull/428) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Install Redis 8 by default [\#425](https://github.com/hifis-net/ansible-collection-toolkit/pull/425) [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] ([Normo](https://github.com/Normo))
- Remove deprecated keepalived\_notification\_email variable from keepalived role [\#421](https://github.com/hifis-net/ansible-collection-toolkit/pull/421) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Remove deprecated elasticsearch\_url variable from zammad role [\#420](https://github.com/hifis-net/ansible-collection-toolkit/pull/420) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- Replace git\_data\_dirs [\#416](https://github.com/hifis-net/ansible-collection-toolkit/pull/416) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Use deb822\_repository module to add apt repositories [\#413](https://github.com/hifis-net/ansible-collection-toolkit/pull/413) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))

## [v5.3.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.3.0) (2025-02-18)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.2.1...v5.3.0)

**Closed issues:**

- community.general.yaml has been deprecated [\#392](https://github.com/hifis-net/ansible-collection-toolkit/issues/392)

**Merged pull requests:**

- Prepare release version 5.3.0 [\#395](https://github.com/hifis-net/ansible-collection-toolkit/pull/395) ([Normo](https://github.com/Normo))
- Replace deprecated community.general.yaml [\#393](https://github.com/hifis-net/ansible-collection-toolkit/pull/393) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Convert keepalived\_notification\_email to a list [\#391](https://github.com/hifis-net/ansible-collection-toolkit/pull/391) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Bump ansible-lint from 25.1.1 to 25.1.2 [\#390](https://github.com/hifis-net/ansible-collection-toolkit/pull/390) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.1.1 to 25.1.2 [\#389](https://github.com/hifis-net/ansible-collection-toolkit/pull/389) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 25.1.0 to 25.1.1 [\#388](https://github.com/hifis-net/ansible-collection-toolkit/pull/388) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 11.1.0 to 11.2.0 [\#387](https://github.com/hifis-net/ansible-collection-toolkit/pull/387) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 25.1.0 to 25.1.1 [\#386](https://github.com/hifis-net/ansible-collection-toolkit/pull/386) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v5.2.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.2.1) (2025-01-23)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.2.0...v5.2.1)

**Fixed bugs:**

- Ensure gitlab-runner and helper-images have the same version [\#381](https://github.com/hifis-net/ansible-collection-toolkit/issues/381) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)]
- \[gitlab-runner\] Manual installation from a deb file fails for version \>=17.7.0 [\#375](https://github.com/hifis-net/ansible-collection-toolkit/issues/375)
- Fix gitlab molecule tests [\#367](https://github.com/hifis-net/ansible-collection-toolkit/issues/367) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]
- Ensure gitlab-runner and helper-images have the same version [\#380](https://github.com/hifis-net/ansible-collection-toolkit/pull/380) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Support manual deb file installation for gitlab-runner version 17.7 or greater [\#373](https://github.com/hifis-net/ansible-collection-toolkit/pull/373) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))

**Closed issues:**

- Custom yamllint configurationis incompatible with ansible-lint [\#371](https://github.com/hifis-net/ansible-collection-toolkit/issues/371)

**Merged pull requests:**

- Release version 5.2.1 [\#383](https://github.com/hifis-net/ansible-collection-toolkit/pull/383) ([tobiashuste](https://github.com/tobiashuste))
- Rename elasticsearch\_url variable [\#377](https://github.com/hifis-net/ansible-collection-toolkit/pull/377) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Do not run search index rebuild by default [\#376](https://github.com/hifis-net/ansible-collection-toolkit/pull/376) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Fix incompatibilities with ansible-lint in custom yamllint config [\#372](https://github.com/hifis-net/ansible-collection-toolkit/pull/372) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 24.12.2 to 25.1.0 [\#370](https://github.com/hifis-net/ansible-collection-toolkit/pull/370) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 24.12.2 to 25.1.0 [\#369](https://github.com/hifis-net/ansible-collection-toolkit/pull/369) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix failing GitLab KAS in molecule test [\#368](https://github.com/hifis-net/ansible-collection-toolkit/pull/368) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Make sure to not output sensitive information [\#365](https://github.com/hifis-net/ansible-collection-toolkit/pull/365) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))

## [v5.2.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.2.0) (2025-01-16)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.1.1...v5.2.0)

**Fixed bugs:**

- Fix autoscaler URL template and install 0.28.0 by default [\#362](https://github.com/hifis-net/ansible-collection-toolkit/pull/362) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release v5.2.0 [\#363](https://github.com/hifis-net/ansible-collection-toolkit/pull/363) ([Normo](https://github.com/Normo))
- Install Zammad 6.4.1 by default [\#361](https://github.com/hifis-net/ansible-collection-toolkit/pull/361) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- Bump jinja2 from 3.1.4 to 3.1.5 [\#360](https://github.com/hifis-net/ansible-collection-toolkit/pull/360) ([dependabot[bot]](https://github.com/apps/dependabot))
- Update butane to v0.23.0 [\#359](https://github.com/hifis-net/ansible-collection-toolkit/pull/359) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))

## [v5.1.1](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.1.1) (2025-01-03)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.1.0...v5.1.1)

**Fixed bugs:**

- role ssh\_keys: ignores errors when in check-mode and users doesnt exist yet [\#356](https://github.com/hifis-net/ansible-collection-toolkit/pull/356) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] ([iceowlbeer](https://github.com/iceowlbeer))

**Merged pull requests:**

- Bump molecule-plugins from 23.5.3 to 23.6.0 [\#355](https://github.com/hifis-net/ansible-collection-toolkit/pull/355) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 24.10.0 to 24.12.2 [\#354](https://github.com/hifis-net/ansible-collection-toolkit/pull/354) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 24.10.0 to 24.12.2 [\#353](https://github.com/hifis-net/ansible-collection-toolkit/pull/353) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 24.9.0 to 24.12.0 [\#348](https://github.com/hifis-net/ansible-collection-toolkit/pull/348) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 10.6.0 to 11.1.0 [\#347](https://github.com/hifis-net/ansible-collection-toolkit/pull/347) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump keepalived from version 2.3.1 to 2.3.2 [\#346](https://github.com/hifis-net/ansible-collection-toolkit/pull/346) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([Normo](https://github.com/Normo))
- Bump ansible/ansible-lint from 24.9.2 to 24.10.0 [\#343](https://github.com/hifis-net/ansible-collection-toolkit/pull/343) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump fsfe/reuse-action from 4.0.0 to 5.0.0 [\#342](https://github.com/hifis-net/ansible-collection-toolkit/pull/342) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump reuse from 4.0.3 to 5.0.2 [\#341](https://github.com/hifis-net/ansible-collection-toolkit/pull/341) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 24.9.2 to 24.10.0 [\#340](https://github.com/hifis-net/ansible-collection-toolkit/pull/340) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v5.1.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.1.0) (2024-11-08)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v5.0.0...v5.1.0)

**Closed issues:**

- Drop support for Debian 10 Buster [\#333](https://github.com/hifis-net/ansible-collection-toolkit/issues/333)
- Drop support for ansible 2.15 [\#332](https://github.com/hifis-net/ansible-collection-toolkit/issues/332)

**Merged pull requests:**

- Prepare release version 5.1.0 [\#338](https://github.com/hifis-net/ansible-collection-toolkit/pull/338) ([tobiashuste](https://github.com/tobiashuste))
- Remove support for EOL Ansible 2.15 [\#337](https://github.com/hifis-net/ansible-collection-toolkit/pull/337) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] [[redis](https://github.com/hifis-net/ansible-collection-toolkit/labels/redis)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 10.5.0 to 10.6.0 [\#336](https://github.com/hifis-net/ansible-collection-toolkit/pull/336) ([dependabot[bot]](https://github.com/apps/dependabot))
- Remove the restriction for HAproxy 3.0 under Ubuntu 20.04 [\#335](https://github.com/hifis-net/ansible-collection-toolkit/pull/335) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Drop support for Debian 10 buster [\#334](https://github.com/hifis-net/ansible-collection-toolkit/pull/334) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))

## [v5.0.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v5.0.0) (2024-10-10)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.8.0...v5.0.0)

**Breaking changes:**

- Install HAProxy 3.0 by default [\#256](https://github.com/hifis-net/ansible-collection-toolkit/issues/256) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)]

**Implemented enhancements:**

- hifis.toolkit.gitlab\_runner: Support autoscaler boot\_time parameter [\#326](https://github.com/hifis-net/ansible-collection-toolkit/issues/326) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)]
- Add support for Ubuntu 24.04 \(Noble Numbat\) [\#252](https://github.com/hifis-net/ansible-collection-toolkit/issues/252)

**Fixed bugs:**

- hifis.toolkit.netplan Molecule test fails on Ubuntu 24.04 [\#318](https://github.com/hifis-net/ansible-collection-toolkit/issues/318)

**Merged pull requests:**

- Bump ansible from 10.4.0 to 10.5.0 [\#329](https://github.com/hifis-net/ansible-collection-toolkit/pull/329) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 24.7.0 to 24.9.2 [\#324](https://github.com/hifis-net/ansible-collection-toolkit/pull/324) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 24.7.0 to 24.9.2 [\#323](https://github.com/hifis-net/ansible-collection-toolkit/pull/323) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 24.8.0 to 24.9.0 [\#322](https://github.com/hifis-net/ansible-collection-toolkit/pull/322) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible from 10.3.0 to 10.4.0 [\#319](https://github.com/hifis-net/ansible-collection-toolkit/pull/319) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare release version 5.0.0 [\#331](https://github.com/hifis-net/ansible-collection-toolkit/pull/331) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([Normo](https://github.com/Normo))
- Replace deprecated gateway4 with routes [\#330](https://github.com/hifis-net/ansible-collection-toolkit/pull/330) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([Normo](https://github.com/Normo))
- Fix molecule tests for netplan on Ubuntu 24.04 [\#328](https://github.com/hifis-net/ansible-collection-toolkit/pull/328) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([Normo](https://github.com/Normo))
- Support fleeting-pluign-openstack boot\_time parameter [\#327](https://github.com/hifis-net/ansible-collection-toolkit/pull/327) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([Normo](https://github.com/Normo))
- Add custom routes [\#325](https://github.com/hifis-net/ansible-collection-toolkit/pull/325) [[netplan](https://github.com/hifis-net/ansible-collection-toolkit/labels/netplan)] ([axldd](https://github.com/axldd))
- Add Ubuntu 24.04 support to zammad role [\#317](https://github.com/hifis-net/ansible-collection-toolkit/pull/317) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([Normo](https://github.com/Normo))
- Install haproxy 3.0 by default [\#316](https://github.com/hifis-net/ansible-collection-toolkit/pull/316) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))
- Support Ubuntu 24.04 in HAProxy role  [\#315](https://github.com/hifis-net/ansible-collection-toolkit/pull/315) [[haproxy](https://github.com/hifis-net/ansible-collection-toolkit/labels/haproxy)] ([Normo](https://github.com/Normo))

## [v4.8.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.8.0) (2024-08-27)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.7.0...v4.8.0)

**Implemented enhancements:**

- Support docker host parameter to allow Podman support [\#312](https://github.com/hifis-net/ansible-collection-toolkit/pull/312) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Allow to customize butane config file [\#311](https://github.com/hifis-net/ansible-collection-toolkit/pull/311) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))

**Fixed bugs:**

- Add parameter to use specified configuration file [\#310](https://github.com/hifis-net/ansible-collection-toolkit/pull/310) [[keepalived](https://github.com/hifis-net/ansible-collection-toolkit/labels/keepalived)] ([boerngen-schmidt-next](https://github.com/boerngen-schmidt-next))

**Closed issues:**

- Link to SSH keys role in README results in 404 [\#306](https://github.com/hifis-net/ansible-collection-toolkit/issues/306)

**Merged pull requests:**

- Prepare release of version 4.8.0 [\#313](https://github.com/hifis-net/ansible-collection-toolkit/pull/313) ([tobiashuste](https://github.com/tobiashuste))
- Bump molecule from 24.7.0 to 24.8.0 [\#309](https://github.com/hifis-net/ansible-collection-toolkit/pull/309) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix link to SSH keys role in README [\#308](https://github.com/hifis-net/ansible-collection-toolkit/pull/308) ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 10.2.0 to 10.3.0 [\#307](https://github.com/hifis-net/ansible-collection-toolkit/pull/307) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v4.7.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.7.0) (2024-08-12)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.6.0...v4.7.0)

**Implemented enhancements:**

- Support new parameter use\_ignition [\#293](https://github.com/hifis-net/ansible-collection-toolkit/issues/293)
- Install fleeting-plugin-openstack directly from GitHub [\#303](https://github.com/hifis-net/ansible-collection-toolkit/pull/303) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release of version 4.7.0 [\#304](https://github.com/hifis-net/ansible-collection-toolkit/pull/304) ([tobiashuste](https://github.com/tobiashuste))
- Install Zammad 6.3.1 by default [\#302](https://github.com/hifis-net/ansible-collection-toolkit/pull/302) [[zammad](https://github.com/hifis-net/ansible-collection-toolkit/labels/zammad)] ([tobiashuste](https://github.com/tobiashuste))
- Remove support for OS that are EOL [\#301](https://github.com/hifis-net/ansible-collection-toolkit/pull/301) [[ssh_keys](https://github.com/hifis-net/ansible-collection-toolkit/labels/ssh_keys)] [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Support Ubuntu 24.04 and remove 18.04 support [\#299](https://github.com/hifis-net/ansible-collection-toolkit/pull/299) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 10.1.0 to 10.2.0 [\#297](https://github.com/hifis-net/ansible-collection-toolkit/pull/297) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 24.6.0 to 24.7.0 [\#292](https://github.com/hifis-net/ansible-collection-toolkit/pull/292) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible-lint from 24.5.0 to 24.7.0 [\#291](https://github.com/hifis-net/ansible-collection-toolkit/pull/291) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump molecule from 24.2.1 to 24.7.0 [\#290](https://github.com/hifis-net/ansible-collection-toolkit/pull/290) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v4.6.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.6.0) (2024-07-12)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.5.0...v4.6.0)

**Implemented enhancements:**

- Support the new use\_ignition parameter [\#294](https://github.com/hifis-net/ansible-collection-toolkit/pull/294) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))

**Merged pull requests:**

- Prepare release of version 4.6.0 [\#295](https://github.com/hifis-net/ansible-collection-toolkit/pull/295) ([tobiashuste](https://github.com/tobiashuste))
- Bump reuse from 3.0.2 to 4.0.3 [\#289](https://github.com/hifis-net/ansible-collection-toolkit/pull/289) ([dependabot[bot]](https://github.com/apps/dependabot))
- language, spelling [\#287](https://github.com/hifis-net/ansible-collection-toolkit/pull/287) [[unattended_upgrades](https://github.com/hifis-net/ansible-collection-toolkit/labels/unattended_upgrades)] ([dnmvisser](https://github.com/dnmvisser))
- Bump fsfe/reuse-action from 3.0.0 to 4.0.0 [\#286](https://github.com/hifis-net/ansible-collection-toolkit/pull/286) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v4.5.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.5.0) (2024-06-19)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.4.0...v4.5.0)

**Implemented enhancements:**

- Allow to configure more autoscaler policy values [\#278](https://github.com/hifis-net/ansible-collection-toolkit/issues/278) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)]

**Merged pull requests:**

- Prepare release of version 4.5.0 [\#281](https://github.com/hifis-net/ansible-collection-toolkit/pull/281) ([tobiashuste](https://github.com/tobiashuste))
- Make sure idle\_time is a string in the runner config [\#280](https://github.com/hifis-net/ansible-collection-toolkit/pull/280) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Support more autoscaler policy config options [\#279](https://github.com/hifis-net/ansible-collection-toolkit/pull/279) [[gitlab_runner](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab_runner)] ([tobiashuste](https://github.com/tobiashuste))
- Bump ansible from 9.6.0 to 10.1.0 [\#277](https://github.com/hifis-net/ansible-collection-toolkit/pull/277) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump ansible/ansible-lint from 24.5.0 to 24.6.0 [\#267](https://github.com/hifis-net/ansible-collection-toolkit/pull/267) ([dependabot[bot]](https://github.com/apps/dependabot))

## [v4.4.0](https://github.com/hifis-net/ansible-collection-toolkit/tree/v4.4.0) (2024-06-18)

[Full Changelog](https://github.com/hifis-net/ansible-collection-toolkit/compare/v4.3.0...v4.4.0)

**Implemented enhancements:**

- Make GitLab DB port configurable in role gitlab [\#272](https://github.com/hifis-net/ansible-collection-toolkit/issues/272) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)]

**Merged pull requests:**

- Make GitLab DB port configurable in GitLab config template [\#273](https://github.com/hifis-net/ansible-collection-toolkit/pull/273) [[gitlab](https://github.com/hifis-net/ansible-collection-toolkit/labels/gitlab)] ([christianhueserhzdr](https://github.com/christianhueserhzdr))
- Prepare release of version 4.4.0 [\#275](https://github.com/hifis-net/ansible-collection-toolkit/pull/275) ([tobiashuste](https://github.com/tobiashuste))

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
