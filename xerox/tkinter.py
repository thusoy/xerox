""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

try:
    from Tkinter import Tk
except ImportError as why:
    raise TkinterNotFound

# stolen from here http://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python/4203897#4203897

def copy(string): 
    """Copy given string into system clipboard."""

    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append(string)
    window.destroy()
    return
    

def paste():
    """Returns system clipboard contents."""
    window = Tk()
    window.withdraw()
    d = window.selection_get(selection = 'CLIPBOARD')
    return d 

 
