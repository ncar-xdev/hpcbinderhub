IMAGES := $(subst /,,$(dir $(wildcard */Dockerfile)))
TARGETS := $(patsubst %,.target-%,$(IMAGES))
OPTS :=

all: $(TARGETS)

clean:
	@rm -rf $(TARGETS)
	@docker image prune -f

purge: clean
	@docker image rm $(IMAGES)

$(TARGETS): .target-%: %/Dockerfile
	docker build $(OPTS) -t $* $*/ && \
	echo '$* image built' && \
	touch $@

define DEPRULE
.target-$(1): $$(wildcard $(1)/*)
endef

$(foreach d,$(IMAGES),$(eval $(call DEPRULE,$(d))))

.target-userbase: .target-conda .target-pbsrpms
.target-pbsserver: .target-pbsrpms
.target-binderhub .target-jupyterhub .target-pbsmom .target-head: .target-userbase
