"""
keyboard_handler.py
===================
Maps raw OpenCV key codes to high-level application actions.
Keeps all key-binding logic in one place.
"""

import cv2
from enum import Enum, auto
from logger_setup import get_logger

logger = get_logger("finger_counter.keyboard")


class Action(Enum):
    NONE   = auto()
    QUIT   = auto()
    TOGGLE_VOICE = auto()
    RESET  = auto()


# Key → Action mapping (lowercase ASCII)
_BINDINGS: dict[int, Action] = {
    ord("q"): Action.QUIT,
    ord("Q"): Action.QUIT,
    ord("s"): Action.TOGGLE_VOICE,
    ord("S"): Action.TOGGLE_VOICE,
    ord("r"): Action.RESET,
    ord("R"): Action.RESET,
    27:       Action.QUIT,   # ESC
}


class KeyboardHandler:
    """
    Poll OpenCV for keypresses and translate to Action enums.

    Usage
    -----
    kb = KeyboardHandler(wait_ms=1)
    action = kb.poll()
    if action == Action.QUIT:
        break
    """

    def __init__(self, wait_ms: int = 1):
        self._wait_ms = wait_ms

    def poll(self) -> Action:
        """
        Wait `wait_ms` milliseconds for a keypress.
        Returns the corresponding Action or Action.NONE.
        """
        raw = cv2.waitKey(self._wait_ms) & 0xFF
        action = _BINDINGS.get(raw, Action.NONE)
        if action != Action.NONE:
            logger.debug("Key %d → %s", raw, action.name)
        return action

    @staticmethod
    def describe_bindings() -> str:
        lines = ["Key Bindings:"]
        seen: set[Action] = set()
        for key, action in _BINDINGS.items():
            if action not in seen:
                seen.add(action)
                char = chr(key) if 32 <= key < 127 else f"\\x{key:02x}"
                lines.append(f"  [{char.upper()}]  {action.name.replace('_', ' ')}")
        return "\n".join(lines)
