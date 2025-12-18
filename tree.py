"""Animated ASCII Christmas tree with randomly color-changing stars."""

import random
import sys
import time
from typing import Dict, List, Optional, Tuple

# Raw tree shape using only structural characters.
TREE_LINES: List[str] = [
    "          *",
    "         /\\",
    "        /**\\",
    "       /****\\",
    "      /******\\",
    "     /********\\",
    "    /**********\\",
    "   /************\\",
    "  /**************\\",
    " /****************\\",
    "/******************\\",
    "        |||",
]

# ANSI color codes for bright, festive colors.
COLORS: List[str] = [
    "\033[91m",  # bright red
    "\033[93m",  # bright yellow
    "\033[92m",  # bright green
    "\033[96m",  # bright cyan
    "\033[95m",  # bright magenta
]

RESET = "\033[0m"
CLEAR_AND_HOME = "\033[2J\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"


def _find_star_positions() -> List[Tuple[int, int]]:
    """Return (row, column) offsets for every star in the tree shape."""
    positions: List[Tuple[int, int]] = []
    for row, line in enumerate(TREE_LINES):
        for col, char in enumerate(line):
            if char == "*":
                positions.append((row, col))
    return positions


def _build_frame(color_overrides: Dict[Tuple[int, int], str]) -> str:
    """Construct a single colored frame for the tree."""
    lines: List[str] = []
    for row, line in enumerate(TREE_LINES):
        rendered_chars: List[str] = []
        for col, char in enumerate(line):
            if char == "*":
                color = color_overrides.get((row, col), "\033[32m")  # base green
                rendered_chars.append(f"{color}{char}{RESET}")
            elif char == "|":
                rendered_chars.append(f"\033[33m{char}{RESET}")
            else:
                rendered_chars.append(char)
        lines.append("".join(rendered_chars))
    return "\n".join(lines)


def _random_blink_map(stars: List[Tuple[int, int]]) -> Dict[Tuple[int, int], str]:
    """Pick a few stars to light up with random colors for this frame."""
    if not stars:
        return {}
    blink_count = max(1, min(len(stars), random.randint(3, 8)))
    selected = random.sample(stars, blink_count)
    return {pos: random.choice(COLORS) for pos in selected}


def animate_tree(interval: float = 0.5, frames: Optional[int] = None) -> None:
    """Continuously render the tree, blinking random stars every interval seconds.

    Args:
        interval: Seconds to wait between frames.
        frames: Optional number of frames to render before exiting.
    """
    stars = _find_star_positions()
    sys.stdout.write(HIDE_CURSOR)
    rendered = 0
    try:
        while True:
            overrides = _random_blink_map(stars)
            frame = _build_frame(overrides)
            sys.stdout.write(f"{CLEAR_AND_HOME}{frame}\n")
            sys.stdout.flush()
            rendered += 1
            if frames is not None and rendered >= frames:
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()


if __name__ == "__main__":
    user_interval = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    user_frames = int(sys.argv[2]) if len(sys.argv) > 2 else None
    animate_tree(interval=user_interval, frames=user_frames)
