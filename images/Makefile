DOCKER := docker

.PHONY: all clean

%: %/Dockerfile
	${DOCKER} build --tag $(subst _,,$@) $@/

all: base head jupyterhub pbsmom pbsserver

jupyterhub: base

head: base

pbsmon: base

pbsserver: base

clean:
	${DOCKER} image prune --force
