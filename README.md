Gamemodes
=========

This repository contains all relevant configuration files for every gamemode.
The `.metadata` file contains the current revision of the gamemode configuration. This is used by CI to determine whether or not configuration has changed. 


After making changes to the configuration execute the following command to build the Docker image:
```
$ make mode_<name>
```