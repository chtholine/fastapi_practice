.PHONY: help
help:
	@echo "Commands:"
	@echo "  make run-app   | start fastapi using docker compose"
	@echo "  make run-tests | test fastapi using docker compose"
	@echo "  make purge     | purge all data related with services"

.PHONY: run-app
run-app:
	docker-compose --profile app up --build

.PHONY: run-tests
run-tests:
	docker-compose --profile tests up --build

.PHONY: purge
purge:
	docker-compose down --volumes --remove-orphans --rmi local --timeout 0
