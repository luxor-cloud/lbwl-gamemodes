DOCKER=$(shell which docker)

mode_flash:
	./metadata.py --update flash
	cd flash && ./collect.py
	$(eval ver=$(./metadata.py --mode-version))
	$(DOCKER) build -t freggyy/lbwl-flash:$(ver) -f flash/Dockerfile flash/
	$(DOCKER) push freggyy/lbwl-flash:$(ver)
