"""DCOS Introspect Example Subcommand

Usage:
    dcos introspect --info

Options:
    --help           Show this screen
    --version        Show version
"""
import docopt
from dcos_introspect import constants


def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-introspect version {}'.format(constants.version))

    if args['introspect'] and args['--info']:
        print('Example of a DCOS subcommand')
    else:
        print(__doc__)
        return 1

    return 0


if __name__ == "__main__":
    main()
