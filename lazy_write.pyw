import keyboard
from pynput.keyboard import Key, Controller
import winsound

# Sounds
sound_navigate = 'C:\\Windows\\Media\\chimes.wav'
sound_default = 'C:\\Windows\\Media\\Windows Balloon.wav'

toggle_navigate_mode_hotkey = 'alt + capsLock'

# Arrow Keys (Use 'pynput' for keys that are within nupad)
MAPPINGS_numpad = {
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
MAPPINGS_other = {
    # 
    ';': 'backspace',
    'p': 'del',
    #
    'd': 'shift',
    'f': 'ctrl'
}


is_navigate: bool = False

def on_toggle_navigate_mode():
    global is_navigate
    is_navigate = not is_navigate
    enable_navigate_mode() if is_navigate else disable_navigate_mode()
        
KeyboardController = Controller()
def enable_navigate_mode():
    winsound.PlaySound(sound_navigate, winsound.SND_ASYNC)
    for key, val in MAPPINGS_other.items():
        keyboard.remap_key(key, val)
    for key, val in MAPPINGS_numpad.items():
        keyboard.on_press_key(key, lambda keyEvent, val=val: KeyboardController.tap(val), suppress=True)

def disable_navigate_mode():
    winsound.PlaySound(sound_default, winsound.SND_ASYNC)
    keyboard.unhook_all()
    keyboard.add_hotkey(toggle_navigate_mode_hotkey, on_toggle_navigate_mode, suppress=True)
    

keyboard.add_hotkey(toggle_navigate_mode_hotkey, on_toggle_navigate_mode, suppress=True)

keyboard.wait()