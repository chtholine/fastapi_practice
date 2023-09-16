.PHONY: d-full-run
# Make all actions needed for run from zero.
d-full-run:
	@make init-dev && \
		make d-run

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose \
			up --build

.PHONY: d-local-run
# Just run
d-local-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker compose \
			up --build -d && \
	docker-compose logs -f postgres redis & \
	uvicorn app.main:app --reload

.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			down --volumes --remove-orphans --rmi local --timeout 0
