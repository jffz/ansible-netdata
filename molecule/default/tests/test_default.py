import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    s = host.service("netdata")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:19999").is_listening
