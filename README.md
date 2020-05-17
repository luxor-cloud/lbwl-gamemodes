Gamemodes
=========

This repository contains all relevant configuration files for every gamemode.
The `.metadata` file contains the current revision of the gamemode configuration. This is used by CI to determine whether or not configuration has changed. 

**Directory structure**
```
├───gamemode1
│   ├───...
│   └───Dockerfile
├───gamemode2
|   ├───...
│   └───Dockerfile
├───gamemode3
|   ├───...
│   └───Dockerfile
└───gamemode4
    ├───...
    └───Dockerfile
```
Every directory contains configuration for each gamemode. The Dockerfile is used to build the final image.


After making changes to the configuration execute the following command to build the Docker image:
```
$ make mode_<name>
```
