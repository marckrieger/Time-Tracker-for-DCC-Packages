# Time-Tracker-for-DCC-Packages
Time tracking python script for The Foundry Nuke, Autodesk Maya, Autodesk 3dsMax and SideFX Houdini


This is a bunch of scripts for different DCC Packages which track the time a specific user is working on a scene file. It creates log files which contain the current time of every event in which the scene has been loaded, saved or closed. For that it uses the specific Python APIs for every DCC. It then also creates one summmary log file, which contains the total time that each user has worked on the scene and the total time that multiple users have worked on the same scene.

The log files are created inside a ```.log``` folder up one folder of the scene.

## Currently supported DCCs are:
- The Foundry Nuke
- Autodesk Maya
- Autodesk 3dsMax
- SideFX Houdini

Integrations for more DCCs are planned.

## How to use the scripts:

<details><summary>For Windows users:</summary>
</br>

(Tested with Maya 2023, Nuke 13.1 and 14.0, 3dsMax 2023 and 2024 and Houdini 19.5)

**Replace ```user``` with your username, ```maya-version``` with your Maya version, ```3dsmax-version``` with your 3dsMax version and ```houdini-version``` with your Houdini version.**

- Nuke: Copy the ```menu.py``` and ```nukelog.py``` files in the nuke folder to the path ```C:\Users\user\.nuke\```. If the file ```menu.py``` already existed before, only add the content of the new menu.py to the existing file.

- Maya: Make sure PyMEL is already installed or install it beforehand. Copy the ```userSetup.py``` file inside the maya folder to the path ```C:\Users\user\Documents\maya\scripts\```. If the file already existed, just add the lines.

- 3dsMax: Copy the ```3dsmaxlog.py``` and ```startup.ms``` files inside the 3dsmax folder to the path ```C:\Users\user\AppData\Local\Autodesk\3dsMax\3dsmax-version\ENU\scripts\startup\```. Edit the ```user``` and ```3dsmax-version``` parts in the ```startup.ms``` file to match your username and 3dsMax version (example: 2024 - 64bit).

- Houdini: Copy the ```456.py``` file inside the houdini folder to the path: ```C:\Users\user\Documents\houdini-version\scripts\```. If the ```scripts``` folder does not exist, create it.

</details>
