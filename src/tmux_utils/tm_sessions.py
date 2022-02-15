"""Displays formatted tmux sessions for tmux status-line"""

from __future__ import annotations

import subprocess as sp
from typing import Sequence

import clack
from logrus import Logger


class Config(clack.Config):
    """Clack configuration."""

    window: str
    session_name: str

    @classmethod
    def from_cli_args(cls, argv: Sequence[str]) -> Config:
        """Parse command-line arguments."""
        parser = clack.Parser()
        parser.add_argument(
            "window",
            help=(
                "Dummy argument. Allows the active window name to be passed in"
                " as a command-line argument, but this script does not use"
                " this argument in any way. Sending in the active window name"
                " as an argument forces tmux to update the status-line"
                " properly."
            ),
        )
        parser.add_argument(
            "session_name",
            help="The name of the currently active tmux session.",
        )
        args = parser.parse_args(argv[1:])
        kwargs = vars(args)

        return Config(**kwargs)


def run(cfg: Config) -> int:
    """Clack runner function."""
    log = Logger(__name__)

    ps = sp.check_output(["tmux", "ls"])
    out = ps.decode().strip()

    raw_sessions = out.split("\n")
    log.debug(f"raw_sessions={raw_sessions}")
    log.debug(f"cfg={cfg}")

    sessions = []
    for S in raw_sessions:
        T = S[: S.index(":")]

        if T == cfg.session_name:
            sessions.append("[{}]".format(T))
        else:
            sessions.append(T)

    print("  ".join(sessions), end="")

    return 0


main = clack.main_factory("tm-sessions", run)
