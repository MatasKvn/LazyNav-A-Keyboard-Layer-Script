from typing import Dict, Tuple
import keyboard
from pynput.keyboard import Key, Controller
from time import time

holdKey: str = 'capsLock'
capsTimeout: float = 0.2  # CapsLock is enabled if it is pressed for shorter than this

# Arrow Keys (Use 'pynput' for keys that are within nupad)
MAPPINGS_numpad: Dict[str, str] = {
    'i': Key.up,
    'j': Key.left,
    'k': Key.down,
    'l': Key.right,
    'u': Key.home,
    #
    'o': Key.end,
    'y': Key.page_up,
    #
    'h': Key.page_down,
}

# Uses 'keyboard' module
MAPPINGS_other: Dict[str, str] = {
    # 
    ';': 'backspace',
    'p': 'del',
    #
    'd': 'shift',
    'f': 'ctrl'
}


KeyboardController = Controller()

is_lazywrite_enabled: bool = False
lastToggle: float | None = None

def enable_lazy_write():
    global is_lazywrite_enabled, lastToggle
    if is_lazywrite_enabled:
        return
    lastToggle = time()
    is_lazywrite_enabled = True
    for key, val in MAPPINGS_other.items():
        keyboard.remap_key(key, val)
    for key, val in MAPPINGS_numpad.items():
        keyboard.on_press_key(key, lambda keyEvent, val=val: KeyboardController.tap(val), suppress=True)

def disable_lazy_write():
    global is_lazywrite_enabled, lastToggle
    is_lazywrite_enabled = False
    if time() - lastToggle >= capsTimeout:
        keyboard.press_and_release(holdKey)
    keyboard.unhook_all()
    keyboard.on_press_key(holdKey, lambda key: enable_lazy_write())
    keyboard.on_release_key(holdKey, lambda key: disable_lazy_write())


keyboard.on_press_key(holdKey, lambda key: enable_lazy_write())
keyboard.on_release_key(holdKey, lambda key: disable_lazy_write())

keyboard.wait()