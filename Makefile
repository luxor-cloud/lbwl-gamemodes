DOCKER=$(shell which docker)

define buildpush
	$(DOCKER) build -t $(1) -f $(2)/Dockerfile $(2)/
        $(DOCKER) push $(1)
endef

mode_flash:
	./metadata.py --update flash
	cd flash && ./collect.py
        VER := $(./metadata.py --mode-version)
	$(call buildpush freggyy/lbwl-flash:$(VER) flash)
