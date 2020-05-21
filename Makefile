DOCKER=$(shell which docker)

define buildpush
	$(DOCKER) build -t $(1) -f $(2)/Dockerfile $(2)/
        $(DOCKER) push $(1)
endef

mode_flash:
	./metadata.py --update flash
	cd flash && ./collect.py
        $(eval ver=$(./metadata.py --mode-version))
	$(DOCKER) build -t freggyy/lbwl-flash:$(ver) -f flash/Dockerfile flash/
	$(DOCKER) push freggyy/lbwl-flash:$(ver)
