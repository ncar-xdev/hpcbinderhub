default: all

all: jupyter pbsrpms userbase jupyterhub pbsmom pbsserver head

jupyter: ./jupyter/Dockerfile
	docker build --tag jupyter jupyter/

pbsrpms: ./pbsrpms/Dockerfile
	docker build --tag pbsrpms pbsrpms/

userbase: ./userbase/Dockerfile pbsrpms jupyter
	docker build --tag userbase userbase/

jupyterhub: ./jupyterhub/Dockerfile userbase
	docker build --tag jupyterhub jupyterhub/

pbsmom: ./pbsmom/Dockerfile userbase
	docker build --tag pbsmom pbsmom/

pbsserver: ./pbsserver/Dockerfile pbsrpms
	docker build --tag pbsserver pbsserver/

head: ./head/Dockerfile userbase
	docker build --tag head head/
