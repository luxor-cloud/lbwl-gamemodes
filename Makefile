DOCKER=$(shell which docker)

mode_flash:
	./metadata.py --update flash
	cd flash && ./collect.py
	$(eval ver=$(shell ./metadata.py --mode-version flash))
	docker_build.sh lbwl-flash $(ver) flash/
