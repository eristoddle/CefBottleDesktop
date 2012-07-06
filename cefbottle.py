# Copyright (c) 2012 CefPython Authors. All rights reserved.
# License: New BSD License.
# Website: http://code.google.com/p/cefpython/

import sys
sys.path.append("./lib/cefpython/cefexample")

import win32con # pywin32 extension
import win32gui

import cefpython # cefpython.pyd
import cefwindow


from urllib import urlopen
import subprocess

def QuitApplication(windowID, msg, wparam, lparam):
	
	serverpid = urlopen("http://localhost:800/pid/").read()
	subprocess.Popen('taskkill /F /PID {0}'.format(serverpid), shell=True)
	
	browser = cefpython.GetBrowserByWindowID(windowID)
	browser.CloseBrowser()
	cefwindow.DestroyWindow(windowID)
	win32gui.PostQuitMessage(0)


def CefAdvanced():

	# Programming API:
	# http://code.google.com/p/cefpython/wiki/API
	
	cefwindow.__debug = True # Whether to print debug output to console.
	cefpython.__debug = True

	appSettings = {} # See: http://code.google.com/p/cefpython/wiki/AppSettings
	appSettings["multi_threaded_message_loop"] = False
	appSettings["log_severity"] = cefpython.LOGSEVERITY_DISABLE  # LOGSEVERITY_DISABLE - will not create "debug.log" file.
	cefpython.Initialize(appSettings)

	wndproc = {
		win32con.WM_CLOSE: QuitApplication, 
		win32con.WM_SIZE: cefpython.wm_Size,
		win32con.WM_SETFOCUS: cefpython.wm_SetFocus,
		win32con.WM_ERASEBKGND: cefpython.wm_EraseBkgnd
	}
	windowID = cefwindow.CreateWindow("CefAdvanced", "cefadvanced", 800, 600, None, None, "icon.ico", wndproc)

	browserSettings = {} # See: http://code.google.com/p/cefpython/wiki/BrowserSettings
	browserSettings["history_disabled"] = False
	browser = cefpython.CreateBrowser(windowID, browserSettings, "http://localhost:800/hello/Steve")

	cefpython.MessageLoop()
	cefpython.Shutdown()

if __name__ == "__main__":
	
	CefAdvanced()
