from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    dirs = [
    ]
    files = [
    ]
    for directory in dirs:
        d = host.file(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("netdata")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:19999").is_listening
