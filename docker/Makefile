PHONEY: help
help:
	@echo "build"
	@echo "down"
build:
	docker build --rm  --force-rm -t pycharm  .
up: down
	docker-compose up --build
down:
	docker-compose down --remove-orphans --volumes
