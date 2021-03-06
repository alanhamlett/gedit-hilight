Selection Highlighting for Gedit
================================

A gedit plugin that adds support for selecting a string and highlighting all occurances of that string in the document.

Installation
--------------

####Unix/Linux
If you're using Ubuntu 14.04(32-bit);
* (32-bit) move `hilight.gedit-plugin` and `hilight.py` to `/usr/lib/i386-linux-gnu/gedit/plugins/` 
* (64-bit) move `hilight.gedit-plugin` and `hilight.py` to`/usr/lib/x86_64-linux-gnu/gedit/plugins/`

Or you can try to move `hilight.gedit-plugin` and `hilight.py` into `~/.gnome2/gedit/plugins`.
* In Gedit, go to Edit &rarr; Preferences &rarr; Plugins to enable the plugin.

####Windows
* Move `hilight.gedit-plugin` and `hilight.py` into `C:\Program Files\gedit\lib\gedit-2\plugins`.
* In Gedit, go to Edit &rarr; Preferences &rarr; Plugins to enable the plugin.

Usage
--------

* Select a word (double click) or any non-word string and press `Ctrl-Shift-F` to highlight all occurances of that string.
* Select nothing and press `Ctrl-Shift-F` to remove any highlights and return the text to original color.
