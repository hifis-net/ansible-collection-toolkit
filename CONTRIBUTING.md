<!--
SPDX-FileCopyrightText: 2022 Helmholtz Centre for Environmental Research (UFZ)
SPDX-FileCopyrightText: 2022 Helmholtz-Zentrum Dresden-Rossendorf (HZDR)

SPDX-License-Identifier: Apache-2.0
-->

# Contributing

## Please Help to Improve this Project 

You would like to contribute to this project and want to know how to do that?
Let me tell you first that you are awesome because you take care!
Let's make this Ansible role even better.
Any contributions and help to improve this project via issues, pull requests
and more are most welcome and much appreciated.
We are here to help you with your contributions at any time.
Please mention us in issues and pull requests if you need help or if you have
questions.

## Why Do We Need Contributors and Contributions

Coding is team-work and open-source software is community-work.
In order to enhance the project or correct bugs and regressions in the project
we need you and your support because the project benefits from your expertise,
knowledge, opinions, perspectives, and labour.
Together we are improving this Ansible role step-by-step.
Please follow these guidelines and be respectful as we respect your work and
your contributions in the same manner and support you and help you with your
contributions.
Feel free to get into contact with us or with other contributors as the
community will help you with your questions and contributions.

## Contributions We are Looking For

There are different ways to contribute to this project:

1. Discuss issues and pull requests
2. Submit bug reports or contribute new feature proposals
3. Contribute fixes or implement new features
4. Do testing

### Investigate Before Contributing

Before you start contributing and create issues and pull requests we ask you
to first check whether an issue or pull request already exists for the error,
enhancement, feature or test case you have in mind. 

###  Discuss Issues and Pull Requests

You can contribute by participating in discussions you find in issues and 
pull requests or by starting your own discussions.

### Submit Bug Reports or Contribute New Feature Proposals

If you found a bug in the Ansible role or a typo in the documentation or
if you would like to discuss or suggest functional or quality aspects of the
role you are welcome to create issues to get in contact with us.

### Contribute Fixes or Implement New Features

If you would like to provide a fix for a bug or a typo in the documentation or
even add or change specific features of the role or specific parts of the
documentation, you are welcome to fork this repository, create a separate
branch, create a pull request and add your contributions.
Please also label the pull request, refer to related issues and assign
reviewers that take care of reviewing your suggested changes.
We would like you to check that the CI pipeline passes before asking reviewers
to review your suggestions.

### Do Testing

While automated tests are by far our preferred testing method we also
acknowledge contributors doing exploratory testing.
Sometimes the existing automated tests are not sufficient to account for
specific corner cases and to reveal hidden bugs.
Testing the role manually is always a good approach to make sure that the role
passes a particular additional test case.
Even more valuable are automated tests because they are repeatable.
That is why these test methods work best in combination.
Once a bug is revealed in an exploratory test, additional automated test-cases
need to be added that mark this behaviour as a defect.
As a consequence, a fix need to be developed that makes the CI pipeline and
the new regression tests pass again.
Please feel free to support the project by providing automated test cases.
In order to do so you need to fork the repository, create a separate branch,
create a pull request and add the test cases and fixes to that new branch.
Please also use labels for your pull request, name issues that you refer to
and assign reviewers who would be able to review your suggested test cases and
fixes.
Please make sure that the CI pipeline passes before you name reviewers for your
pull request.

### GitHub Actions CI Pipeline and Code Reviews

Finally, as soon as your changes are ready and you would like to ask someone
to review your contributions you need to check that all GitHub Actions CI
pipeline jobs pass in your pull request before assigning reviewers to your
pull request.

## Contributions Workflow via Pull Requests

In summary, if you would like to contribute with pull requests for
enhancements, bug-fixes or test cases, we kindly ask you to follow this
workflow:

![Workflow Blockdiagram with Kroki](https://kroki.hzdr.de/blockdiag/svg/eNqNU8tO5DAQvPMVrTmRwwrYF7tCcNkT30A4dJyejDXGDm0bNkL8-7YfM3I0WsEpUXd1uV1VHoxT-1HjBG9nAHokhAeDAxm4hc1VB4uLDJZec2vzeJNA9oV80BMGarBfO1A7UnvQW9DeR4KL3s7RGGB6jjLQWzRMOC5Af7UPvpBtHe8blm9dqTDNzuvgeCmwgdGqXQP8LscJm6yAtVmA9bAG-eOAXK9T4DiODfRnlwvpzr1VzgbWQwza2QIOa-LrDoy2AdCOudXbLFY711uRF41Z4NzNqYCmK1xKN0y_OnjCPYGPLFuGHQb4cw8zek_-cK0XTa_EzdDvsuyhc-4rs4_TlPxx1rdWXnZinHI8O85alLkWXcafiKfW1ysJQa6dylcDk6YmdnHOEQI4js7iIjKtFNncZIxjTTZgqgjSiIRe4Uyl2Qbsy10JhHxrBuSv7pDQ7_87_MSLz5ycBBX-8BG5uJNcLxr6zzCL33nxaqP8N8ofzso6H3VNoNVb2zoz0riKuUByhJtWqPWUsKbcxkK61eYj4Pj4lTOO0x2NnnZhMJHa8K-7E9OySs1Jm_LTeT_7B8Nka6c=)

For those of you who want to know how forked-based contributions work on
_GitHub_, we would like to point to the _GitHub Docs_ about
[contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

## Set Up a Local Development Environment (Optional)

In order to add contributions via pull requests you most probably need to
create a local development environment to make sure that your changes
work as expected.
After cloning the project locally the _Python_ dependencies need to be
installed:

```shell
$ pipenv install --dev
```

As mentioned in the suggested contribution workflow above, linting and testing
your contributions locally is optional, but we encourage you to do so.
The following sections show how to lint and test your contributions locally.

### Linting the Project

This role is linted via
[Ansible Lint](https://ansible-lint.readthedocs.io/en/latest/)
and
[yamllint](https://yamllint.readthedocs.io/en/stable/)
which guarantees that the role adheres to a set of
[Ansible Lint rules](https://ansible-lint.readthedocs.io/en/latest/default_rules/)
and
[yamllint rules](https://yamllint.readthedocs.io/en/stable/rules.html):

```shell
$ pipenv run molecule lint
```

### REUSE Specification Compliance

Each file in this project needs to have a proper license and copyright header.
Please check that each file you add to the project contains license and 
copyright information and that it thereby meets the
[REUSE Specification](https://reuse.software/spec/):

```shell
$ pipenv run reuse lint
```

### Testing the Ansible Role

This role is tested via
[Ansible Molecule](https://molecule.readthedocs.io/en/latest/).
During development of your changes we would like you to use _Molecule_ and
the existing automated test cases to verify that your changes do not break
existing test cases:

```shell
$ pipenv run molecule test
````

## How are Contributors Given Credit for Their Valuable Work?

Please add yourself to the list of contributors in file 
[README.md](README.md#contributors) 
via a pull request if you made significant contributions to this role.
Significant contributions are done by suggesting pull requests that fix
bugs or add features or test cases to the project.
Since all other contributions are welcome and may be significant as well 
you can request to be added as a contributor which is then decided on a 
case-by-case basis.

## Ground Rules and Contributions We are Not Looking For

While we welcome and appreciate all contributions we want people to be kind,
respectful and mindful and won't support people who aren't.
Please help and support each other.
In order to get an idea what this actually means and involves we would like to
ask you to read the Codes of Conduct of
[The Carpentries](https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html#code-of-conduct-detailed-view),
the
[Ansible Community](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html#community-code-of-conduct),
and the
[GitLab Community](https://about.gitlab.com/community/contribute/code-of-conduct/).
