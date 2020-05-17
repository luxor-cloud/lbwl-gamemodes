DOCKER=$(shell which docker)

# TODO: build docker image
mode_flash:
    ./metadata.py --update flash
	cd flash && ./collect.py
