<p><img src="https://pbs.twimg.com/profile_images/734637357480194048/dqVkYxwm_400x400.jpg" alt="netdata logo" title="netdata" align="right" height="60" /></p>

# Ansible Role: netdata

[![Build Status](https://travis-ci.org/jffz/ansible-netdata.svg?branch=master)](https://travis-ci.org/jffz/ansible-netdata)
[![License](https://img.shields.io/badge/license-BSD%20License-brightgreen.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-jffz.netdata-blue.svg)](https://galaxy.ansible.com/jffz/ansible/)
[![GitHub tag](https://img.shields.io/github/tag/jffz/ansible-netdata.svg)](https://github.com/cloudalchemy/ansible-netdata/tags)

## Description

Deploy [netdata](https://github.com/firehol/netdata) monitoring system using ansible.

## Requirements

- Ansible >= 2.4

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `netdata_registry` | "" | Use custom netdata registry |
| `netdata_notifications` | True | Enable email notifications. This feature uses `sendmail` command for sending emails which isn't configured by this role |

## Example

### Playbook

```yaml
---
- hosts: all
  roles:
  - jffz.netdata
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py27-ansible25 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## License

This project is licensed under BSD License. See [LICENSE](/LICENSE) for more details.
