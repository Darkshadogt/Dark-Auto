import __future__
import ctypes
import platform
import ctypes.wintypes
import queue
import tkinter
import tkinter.filedialog
import distutils
import tkinter.font
import tkinter.ttk

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from classes import GUI, clicker, presser
    else:
        from ..classes import GUI, clicker, presser
    window = GUI.Interface()
    window.main()


