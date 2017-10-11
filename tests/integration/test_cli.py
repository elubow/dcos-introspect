from common import exec_command


def test_help():
    returncode, stdout, stderr = exec_command(
        ['dcos-introspect', 'introspect', '--help'])

    assert returncode == 0
    assert stdout == b"""DCOS Introspect Example Subcommand

Usage:
    dcos introspect --info

Options:
    --help           Show this screen
    --version        Show version
"""
    assert stderr == b''
