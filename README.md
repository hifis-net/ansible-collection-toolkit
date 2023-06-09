# Unattended-Upgrades Role for Ansible

[![CI status](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/ci.yml/badge.svg)](https://github.com/hifis-net/ansible-role-unattended-upgrades/actions/workflows/ci.yml)
[![Ansible Role: hifis.unattended_upgrades](https://img.shields.io/ansible/role/59313)](https://galaxy.ansible.com/hifis/unattended_upgrades)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/59313)](https://galaxy.ansible.com/hifis/unattended_upgrades)
[![Ansible Role Downloads](https://img.shields.io/ansible/role/d/59313)](https://galaxy.ansible.com/hifis/unattended_upgrades)
[![Latest release](https://img.shields.io/github/v/release/hifis-net/ansible-role-unattended-upgrades)](https://github.com/hifis-net/ansible-role-unattended-upgrades/releases)

Install and setup [unattended-upgrades](https://launchpad.net/unattended-upgrades) for Ubuntu and Debian, to periodically install security upgrades.

## Requirements

The role uses [apt module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) which has additional dependencies.

If you set `unattended_mail` to an e-mail address, make sure `mailx` command is available and your system is able to send e-mails.

The role requires unattended-upgrades version 0.70 and newer, which is available since Debian Wheezy and Ubuntu 12.04 respectively. This is due to [Origins Patterns](#origins-patterns) usage; if this is not available on your system, you may use [the first version of the role](https://github.com/hifis-net/ansible-role-unattended-upgrades/tree/v0.1).

### Automatic Reboot

If you enable automatic reboot feature (`unattended_automatic_reboot`), the role will attempt to install `update-notifier-common` package, which is required on some systems for detecting and executing reboot after the upgrade. You may optionally define a specific time for rebooting (`unattended_automatic_reboot_time`).

## Role Variables

* `unattended_cache_valid_time`:
  * Default: `3600`
  * Description: Update the apt cache if it's older than the given time in seconds; passed to the [apt module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) during package installation.
* `unattended_origins_patterns`:
  * Default:
    * Debian: `['origin=Debian,codename=${distro_codename},label=Debian-Security']`
    * Ubuntu: `['origin=Ubuntu,archive=${distro_codename}-security,label=Ubuntu']`
  * Description: Array of origins patterns to determine whether the package can be automatically installed, for more details see [Origins Patterns](#origins-patterns) below.
* `unattended_package_blacklist`:
  * Default: `[]`
  * Description: Packages which won't be automatically upgraded.
* `unattended_autofix_interrupted_dpkg`:
  * Default: `true`
  * Description: Whether on unclean dpkg exit to run `dpkg --force-confold --configure -a`.
* `unattended_minimal_steps`:
  * Default: `true`
  * Description: Split the upgrade into the smallest possible chunks so that they can be interrupted with SIGUSR1.
* `unattended_install_on_shutdown`:
  * Default: `false`
  * Description: Install all unattended-upgrades when the machine is shutting down.
* `unattended_mail`:
  * Default: `false` (don't send any e-mail)
  * Description: E-mail address to send information about upgrades or problems with unattended upgrades.
* `unattended_mail_sender`:
  * Default: `false` (same as `root`)
  * Description: Use the specified value in the "From" field of outgoing mails
* `unattended_mail_only_on_error`:
  * Default: `false`
  * Description: Send e-mail only on errors, otherwise e-mail will be sent every time there's a package upgrade.
* `unattended_mail_report`:
  * Default: `false`
  * Description: Choose on what event to send an email. Possible values are "always", "only-on-error" or "on-change".
* `unattended_remove_unused_dependencies`:
  * Default: `false`
  * Description: Do automatic removal of all unused dependencies after the upgrade.
* `unattended_remove_new_unused_dependencies`:
  * Default: `true`
  * Description: Do automatic removal of new unused dependencies after the upgrade.
* `unattended_remove_unused_kernel_packages`:
  * Default: `false`
  * Description: Remove unused automatically installed kernel-related packages (kernel images, kernel headers and kernel version locked tools)
* `unattended_automatic_reboot`:
  * Default: `false`
  * Description: Automatically reboot system if any upgraded package requires it, immediately after the upgrade.
* `unattended_automatic_reboot_time`:
  * Default: `false`
  * Description: Automatically reboot system if any upgraded package requires it, at the specific time (_HH:MM_) instead of immediately after the upgrade.
* `unattended_update_days`:
  * Default: `None`
  * Description: Set the days of the week that updates should be applied. The days can be specified as localized abbreviated or full names. Or as integers where "0" is Sunday, "1" is Monday etc. Example: `{"Mon";"Fri"};`
* `unattended_ignore_apps_require_restart`:
  * Default: `false`
  * Description: Unattended-upgrades won't automatically upgrade some critical packages requiring restart after an upgrade (i.e. there is `XB-Upgrade-Requires: app-restart` directive in their debian/control file). With this option set to `true`, unattended-upgrades will upgrade these packages regardless of the directive.
* `unattended_syslog_enable`:
  * Default: `false`
  * Description: Write events to syslog, which is useful in environments where syslog messages are sent to a central store.
* `unattended_syslog_facility`:
  * Default: `None`
  * Description: Write events to the specified syslog facility, or the daemon facility if not specified. Will only have affect if `unattended_syslog_enable` is set to `true`.
* `unattended_verbose`:
  * Default: `0` (no report)
  * Description: Define verbosity level of APT for periodic runs. The output will be sent to root.
    * Possible options:
      * `0`: no report
      * `1`: progress report
      * `2`: + command outputs
      * `3`: + trace on
* `unattended_update_package_list`:
  * Default: `1`
  * Description: Do "apt-get update" automatically every n-days (0=disable).
* `unattended_download_upgradeable`:
  * Default: `0`
  * Description: Do "apt-get upgrade --download-only" every n-days (0=disable).
* `unattended_autoclean_interval`:
  * Default: `7`
  * Description: Do "apt-get autoclean" every n-days (0=disable).
* `unattended_clean_interval`:
  * Default: `0`
  * Description: Do "apt-get clean" every n-days (0=disable).
* `unattended_random_sleep`:
  * Default: `1800` (30 minutes)
  * Description: Define maximum for a random interval in seconds after which the apt job starts (only for systems without systemd).
* `unattended_dpkg_options`:
  * Default: `[]`
  * Description: Array of dpkg command-line options used during unattended-upgrades runs, e.g. `["--force-confdef"]`, `["--force-confold"]`.
* `unattended_dl_limit`:
  * Default: `None`
  * Description: Limit the download speed in kb/sec using apt bandwidth limit feature.
* `unattended_only_on_ac_power`:
  * Default: `false`
  * Description: Download and install upgrades only on AC power. It will also install the debian package `powermgmt-base`.
* `unattended_systemd_timer_override`
  * Default: `false`
  * Description: Deploy/Remove timer overrides.
* `unattended_apt_daily_oncalendar`
  * Default: `"*-*-* 6,18:00"`
  * Description: Apt daily schedule (download updates).
* `unattended_apt_daily_randomizeddelaysec`
  * Default: `"12h"`
  * Description: Apt daily randomized delay.
* `unattended_apt_daily_upgrade_oncalendar`
  * Default: `"*-*-* 6:00"`
  * Description: Apt daily upgrade schedule (install updates).
* `unattended_apt_daily_upgrade_randomizeddelaysec`
  * Default: `"60m"`
  * Description: Apt daily upgrade randomized delay.

## Origins Patterns

Origins Pattern is a more powerful alternative to the Allowed Origins option used in previous versions of unattended-upgrade.

Pattern is composed of specific keywords:

* `a`,`archive`,`suite` – e.g. `stable`, `trusty-security` (`archive=stable`)
* `c`,`component`   – e.g. `main`, `crontrib`, `non-free` (`component=main`)
* `l`,`label` – e.g. `Debian`, `Debian-Security`, `Ubuntu`
* `o`,`origin` – e.g. `Debian`, `Unofficial Multimedia Packages`, `Ubuntu`
* `n`,`codename` – e.g. `jessie`, `jessie-updates`, `trusty` (this is only supported with `unattended-upgrades` >= 0.80)
* `site` – e.g. `http.debian.net`

You can review the available repositories using `apt-cache policy` and debug your choice using `unattended-upgrades -d` command on a target system.

Additionally, unattended-upgrades support two macros (variables), derived from `/etc/debian_version`:

* `${distro_id}` – Installed distribution name, e.g. `Debian` or `Ubuntu`.
* `${distro_codename}` – Installed codename, e.g. `bullseye` or `jammy`.

Using `${distro_codename}` should be preferred over using `stable` or `oldstable` as a selected, as once `stable` moves to `oldstable`, no security updates will be installed at all, or worse, package from a newer distro release will be installed by accident. The same goes for upgrading your installation from `oldstable` to `stable`, if you forget to change this in your origin patterns, you may not receive the security updates for your newer distro release. With `${distro_codename}`, both cases can never happen.

## Systemd timers

Documentation for systemd/Timers: <https://wiki.archlinux.org/title/systemd/Timers>

### Debian Default Configuration

* Download daily at random times during the entire day.
* Install daily between 6am - 7am

```yaml
unattended_systemd_timer_override: false # (default)
# apt-daily timer
unattended_apt_daily_oncalendar: "*-*-* 6,18:00" # (default)
unattended_apt_daily_randomizeddelaysec: "12h" # (default)
# apt-daily-upgrade timer
unattended_apt_daily_upgrade_oncalendar: "*-*-* 6:00" # (default)
unattended_apt_daily_upgrade_randomizeddelaysec: "60m" # (default)
```

### Customized download and update timers

* Download starts between 00:30am - 01:30am
* Installation starts between 04:00am - 05:30am

```yaml
unattended_systemd_timer_override: true
# apt-daily timer
unattended_apt_daily_oncalendar: "*-*-* 00:30"
unattended_apt_daily_randomizeddelaysec: "60m"

# apt-daily-upgrade timer
unattended_apt_daily_upgrade_oncalendar: "*-*-* 4:00"
unattended_apt_daily_upgrade_randomizeddelaysec: "90m"
```

## Role Usage Examples

Example for Ubuntu, with custom [origins patterns](#patterns-examples), blacklisted packages and e-mail notification:

```yaml
- hosts: all
  roles:
  - role: hifis.unattended_upgrades
    unattended_origins_patterns:
    - 'origin=Ubuntu,archive=${distro_codename}-security'
    - 'o=Ubuntu,a=${distro_codename}-updates'
    unattended_package_blacklist: [cowsay, vim]
    unattended_mail: 'root@example.com'
```

_Note:_ You don't need to specify `unattended_origins_patterns`, the role will use distribution's default if the variable is not set.

### Running Only on Debian-based Systems

If you manage multiple distribution with the same playbook, you may want to skip running this role on non-Debian systems. You can [use `when` conditional with role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#conditionals-with-roles) to limit the role to particular systems:

```yaml
- hosts: all
  roles:
     - role: hifis.unattended_upgrades
       when: ansible_facts['os_family'] == 'Debian'
```

See [#38](https://github.com/jnv/ansible-role-unattended-upgrades/pull/38) for discussion.

### Patterns Examples

By default, only security updates are allowed for both Ubuntu and Debian. You can add more patterns to allow unattended-updates install more packages automatically, however be aware that automated major updates may potentially break your system.

#### For Debian

```yaml
unattended_origins_patterns:
  - 'origin=Debian,codename=${distro_codename},label=Debian-Security' # security updates
  - 'o=Debian,codename=${distro_codename},label=Debian' # updates including non-security updates
  - 'o=Debian,codename=${distro_codename},a=proposed-updates'
```

#### For Ubuntu

In Ubuntu, archive always contains the distribution codename

```yaml
unattended_origins_patterns:
  - 'origin=Ubuntu,archive=${distro_codename}-security'
  - 'o=Ubuntu,a=${distro_codename}'
  - 'o=Ubuntu,a=${distro_codename}-updates'
  - 'o=Ubuntu,a=${distro_codename}-proposed-updates'
```

#### For Raspbian

In Raspbian, it is only possible to update all packages from the default repository, including non-security updates, or updating none.

Updating all, including non-security:

```yaml
unattended_origins_patterns:
  - 'origin=Raspbian,codename=${distro_codename},label=Raspbian'
```

To not install any updates on a raspbian host, just set `unattended_origins_patterns` to an empty list:

```yaml
unattended_origins_patterns: []
```

## License

GPL-2.0-or-later

## Author

This role is maintained by [HIFIS Software Services](https://www.hifis.net/)
and was originally forked from [jnv/ansible-role-unattended-upgrades](https://github.com/jnv/ansible-role-unattended-upgrades),
created by [Jan Vlnas](https://github.com/jnv).

## Contributors

We would like to thank and give credits to the following contributors of this
project:

* [alpha0010](https://github.com/alpha0010)
* [gcotelli](https://github.com/gcotelli)
* [lukashass](https://github.com/lukashass)
* [nono-lqdn](https://github.com/nono-lqdn)
* [turikhay](https://github.com/turikhay)
* [mabed](https://github.com/mabed-fr)
* [pgassmann](https://github.com/pgassmann)
