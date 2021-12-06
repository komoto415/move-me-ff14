## Avoid The AFK Timer
Just a simple boi that will move your character in game a bit to keep you from getting logged out!

***DISCLAIMER*** This is not something that is really intended to run completely passively as it will just send key inputs
into the currently focused window.


Tested with:
* Python 3.8.x
* Windowed mode

Required Packages:
* pygame
* win32gui

Known Issues:
* FF14 window will not be brought into foreground causing the script to error out:  
Current Resolution: Setting to foreground is currently disabled