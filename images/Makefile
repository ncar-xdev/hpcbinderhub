DOCKER := docker

.PHONY: all prune

%: %/Dockerfile
	${DOCKER} build --tag $(subst _,,$@) $@/

all: base head jupyterhub pbsmom pbsserver

jupyterhub: base

head: base

pbsmon: base

pbsserver: base

prune:
	${DOCKER} image prune
