"""Displays formatted tmux sessions for tmux status-line"""

import subprocess as sp
from typing import Sequence

import clap
from logutils import Logger
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class _Arguments(clap.Arguments):
    window: str
    session_name: str


def _parse_cli_args(argv: Sequence[str]) -> _Arguments:
    parser = clap.Parser()
    parser.add_argument(
        "window",
        help=(
            "Dummy argument. Allows the active window name to be passed in as"
            " a command-line argument, but this script does not use this"
            " argument in any way. Sending in the active window name as an"
            " argument forces tmux to update the status-line properly."
        ),
    )
    parser.add_argument(
        "session_name", help="The name of the currently active tmux session."
    )
    args = parser.parse_args(argv[1:])
    kwargs = vars(args)

    return _Arguments(**kwargs)


def _run(args: _Arguments) -> int:
    log = Logger(__name__)

    ps = sp.check_output(["tmux", "ls"])
    out = ps.decode().strip()

    raw_sessions = out.split("\n")
    log.debug(f"raw_sessions={raw_sessions}")
    log.debug(f"args={args}")

    sessions = []
    for S in raw_sessions:
        T = S[: S.index(":")]

        if T == args.session_name:
            sessions.append("[{}]".format(T))
        else:
            sessions.append(T)

    print("  ".join(sessions), end="")

    return 0


main = clap.main_factory(_parse_cli_args, _run)
