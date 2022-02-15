"""Stores and Retrieves Default Directories for tmuxinator Sessions"""

from __future__ import annotations

import os
import pickle
import typing as Type
from typing import Final, Optional, Sequence

import clack
from clack import xdg
from logrus import Logger


APP_NAME: Final = "tm-session-root"


class Config(clack.Config):
    """Clack configuration."""

    get: bool
    put: bool
    session_name: str
    root_dir: Optional[str]

    @classmethod
    def from_cli_args(cls, argv: Sequence[str]) -> Config:
        """Parse command-line arguments."""
        parser = clack.Parser()
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

        return Config(**kwargs)


def run(cfg: Config) -> int:
    """Clack runner function."""
    log = Logger(__name__).bind_fargs(locals())

    fpath = "{}/default-dirs.pickle".format(
        xdg.init_full_dir("data", APP_NAME)
    )

    default_dirs: Type.Dict[str, str] = {}
    if not os.path.isfile(fpath):
        with open(fpath, "wb+") as f:
            pickle.dump(default_dirs, f)
    else:
        with open(fpath, "rb") as f:
            default_dirs = pickle.load(f)

    if cfg.get:
        _home = os.environ.get("HOME")
        _root_dir = default_dirs.get(cfg.session_name, _home)
        print(_root_dir.replace("/home/bryan", _home), end="")  # type: ignore
    elif cfg.put:
        if cfg.root_dir is None:
            log.error(
                "The ROOT_DIR argument is required when --put is specified."
            )
            return 1

        default_dirs[cfg.session_name] = cfg.root_dir
        with open(fpath, "wb") as f:
            pickle.dump(default_dirs, f)

    return 1


main = clack.main_factory(APP_NAME, run)
