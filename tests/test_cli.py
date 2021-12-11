"""Tests the tmux_utils project's CLI."""

from tmux_utils import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
