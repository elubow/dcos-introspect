"""DCOS Introspection Subcommand

Usage:
    dcos introspect --info
    dcos introspect reservations --list --aggregate

Commands:
    reservations
        --list       List all open reservations on this master
        --aggregate  Aggregate all open reservations by framework

Options:
    --help           Show this screen
    --json           Print the output in JSON format if available
    --version        Show version
"""
import docopt

from dcos import cmds, emitting, mesos, util
from dcos.errors import DCOSException

from dcoscli.util import decorate_docopt_usage
from dcos_introspect import constants

logger = util.get_logger(__name__)
emitter = emitting.FlatEmitter()

def main():
    try:
        return _main()
    except DCOSException as e:
        emitter.publish(e)
        return 1

@decorate_docopt_usage
def _main():
    args = docopt.docopt(
        __doc__,
        version='dcos-introspect version {}'.format(constants.version))

    # TODO figure out what this is supposed to do and possibly uncomment
    # http.silence_requests_warnings()

    print(args)
    if args['info']:
        _info()

    cmds.execute(_cmds(), args)

    return 0


def _cmds():
    """
    :returns: all the supported commands for this package
    :rtype: list of dcos.cmds.Command
    """
    return [
        cmds.Command(
            hierarchy=['info'],
            arg_keys=[],
            function=_info),

        cmds.Command(
            hierarchy=['reservations', 'list'],
            arg_keys=['--json'],
            function=_list_reservations),
    ]

def _info():
    """The general information method
    """
    print("we are here")
    return 0

def _list_reservations(json_):
    """
    """
    print('Listing reservations')
    return 0

if __name__ == "__main__":
    main()
