DOCKER := docker
IMGDIRS := $(subst /,,$(wildcard */))

.PHONY: all prune

%: %/Dockerfile
	${DOCKER} build --tag $(subst _,,$@) $@/

all: jupyterhub login pbsmom pbsserver

jupyterhub: _base

login: _base

pbsmon: _base

pbsserver: _base

prune:
	${DOCKER} image prune
