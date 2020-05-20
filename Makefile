DOCKER=$(shell which docker)

mode_flash:
	./metadata.py --update flash
	cd flash && ./collect.py
