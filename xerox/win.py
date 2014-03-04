""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

import ctypes

_CF_TEXT = 1

def copy(string): 
    """Copy given string into system clipboard."""
    GMEM_DDESHARE = 0x2000
    ctypes.windll.user32.OpenClipboard(0)
    ctypes.windll.user32.EmptyClipboard()
    hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(string.encode('utf-8')) + 1)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), string.encode('utf-8'))
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(_CF_TEXT, hCd)
    ctypes.windll.user32.CloseClipboard()
    

def paste():
    """Returns system clipboard contents."""
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(_CF_TEXT)
    data = ctypes.c_char_p(pcontents).value
    #ctypes.windll.kernel32.GlobalUnlock(pcontents)
    ctypes.windll.user32.CloseClipboard()
    return data.decode('utf-8')
