Gamemodes
=========

This repository contains all relevant configuration files for every gamemode.
The `.metadata` file contains the current revision of the gamemode configuration. This is used by CI to determine whether or not configuration has changed. 

**Directory structure**
```
├───gamemode1
│   ├───...
|   ├───mode.json
│   └───Dockerfile
├───gamemode2
|   ├───...
|   ├───mode.json
│   └───Dockerfile
├───gamemode3
|   ├───...
|   ├───mode.json
│   └───Dockerfile
└───gamemode4
    ├───...
    ├───mode.json
    └───Dockerfile
```
Every directory contains configuration for each gamemode. The Dockerfile is used to build the final image.


After making changes to the configuration execute the following command to build the Docker image:
```
$ make mode_<name>
```
