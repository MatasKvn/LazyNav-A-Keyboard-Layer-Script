# LazyWrite 

**LazyWrite** is a simple python script that allows you to have an additional keyboard layer for navigation. This temporarily remaps easily accessible keys like 'j', 'k', and 'l' to frequently used, far away keys like the arrow, or page up/down keys to make text navigation easy and convenient. When \<CAPSLOCK> is held down the navigation mode is enabled and is disabled when \<CAPSLOCK> is released.

## The keybindings
    Arrow Keys:
    'i': UP
    'j': LEFT
    'k': DOWN
    'l': RIGHT

    Other:
    'u': Home
    'o': End
    'y': Page Up
    'h': Page Down

    Deletion Keys:
    'p': Delete
    ';': Backspace
    'd': 'shift'
    'f': 'ctrl'


## Prerequisites
1. Python
2. Python libraries (installed using *pip*):
    * The *keyboard* module: `pip install keyboard`
    * The *pyinput* module: `pip install keyboard`

## Usage
Windows: Simply put the `.pyw` file in the Startup folder. This will start the script everytime your pc turn on.
If you run into problems or want to end the script (why would you), you can kill the process using *Task Manager* by ending the python process.

## FAQ
Q: What platforms does this work on?
A: Currently it only works on Windows. Mainly because it uses the `winsound` python module.

Q: Can I customize my key mappings?
A: Yes! You can customize them by editing the `.pyw` file and adding or removing entries in the `MAPPINGS_...` objects.

Q: Why not use *Vim*?
A: Vim only works in Vim itself, not other apps like browsers. Also, I think that the Vim default arrow key mappings are uncomfortable. Plus, I made this :).

Q: How much performance does this require?
A: Not much. It uses about 12 MB or ram consistenly.




    
