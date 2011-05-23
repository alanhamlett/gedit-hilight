
Selection Highlighting for Gedit
================================

A gedit plugin that adds support for selecting a string and highlighting all occurances of that string in the document.

Installation
--------------

####For Unix/Linux
* Move `hilight.gedit-plugin` and `hilight.py` into `~/.gnome2/gedit/plugins`.
* In Gedit, go to Edit &rarr; Preferences &rarr; Plugins to enable the plugin.

####For Windows
* Move `hilight.gedit-plugin` and `hilight.py` into `C:\Program Files\gedit\lib\gedit-2\plugins`.
* In Gedit, go to Edit &rarr; Preferences &rarr; Plugins to enable the plugin.

Usage
--------

* Select a word (double click) or any non-word string and press `Ctrl-Shift-F` to highlight all occurances of that string.
* Select nothing and press `Ctrl-Shift-F` to remove any highlights and return the text to original color.