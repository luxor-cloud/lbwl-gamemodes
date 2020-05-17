DOCKER=$(shell which docker)

# TODO: build docker image
mode_flash:
	cd flash && ./collect.py