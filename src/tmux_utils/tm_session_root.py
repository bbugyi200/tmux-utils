"""Stores and Retrieves Default Directories for tmuxinator Sessions"""

import os
import pickle
import typing as Type
from typing import Optional, Sequence

from bugyi.lib import xdg
import clap
from logutils import Logger
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class _Arguments(clap.Arguments):
    get: bool
    put: bool
    session_name: str
    root_dir: Optional[str]


def _parse_cli_args(argv: Sequence[str]) -> _Arguments:
    parser = clap.Parser()
    exgroup = parser.add_mutually_exclusive_group()
    exgroup.add_argument(
        "--get",
        action="store_true",
        help="Print the root directory of the tmux session to stdout.",
    )
    exgroup.add_argument(
        "--put",
        action="store_true",
        help="Map SESSION to ROOT_DIR in the database.",
    )
    parser.add_argument(
        "session_name",
        metavar="SESSION",
        type=str,
        help="The name of the tmux session.",
    )
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        type=str,
        nargs="?",
        help="The name of the directory to be mapped to the tmux session.",
    )

    args = parser.parse_args(argv[1:])
    kwargs = vars(args)

    return _Arguments(**kwargs)


def _run(args: _Arguments) -> int:
    log = Logger(__name__).bind_fargs(locals())

    fpath = "{}/default-dirs.pickle".format(xdg.init_full_dir("data"))

    default_dirs: Type.Dict[str, str] = {}
    if not os.path.isfile(fpath):
        with open(fpath, "wb+") as f:
            pickle.dump(default_dirs, f)
    else:
        with open(fpath, "rb") as f:
            default_dirs = pickle.load(f)

    if args.get:
        _home = os.environ.get("HOME")
        _root_dir = default_dirs.get(args.session_name, _home)
        print(_root_dir.replace("/home/bryan", _home), end="")  # type: ignore
    elif args.put:
        if args.root_dir is None:
            log.error(
                "The ROOT_DIR argument is required when --put is specified."
            )
            return 1

        default_dirs[args.session_name] = args.root_dir
        with open(fpath, "wb") as f:
            pickle.dump(default_dirs, f)

    return 1


main = clap.main_factory(_parse_cli_args, _run)
