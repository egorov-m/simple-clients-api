.PHONY: help
help:
		@echo "USAGE"
		@echo "    make <commands>"
		@echo ""
		@echo "AVAILABLE COMMANDS"
		@echo "up             Create and start containers in the background."
		@echo "down           Stop and remove containers, networks."
		@echo "export-dep     Exporting poetry dependencies."
		@echo "export-dep-dev Exporting poetry dependencies with dev group."
		@echo "make-migrate   Create a new migration file"
		@echo "migrate        Apply migrations."
		@echo "run            Run server."

.PHONY: up
up:
		docker-compose -f docker-compose.yaml up -d

.PHONY: down
down:
		docker-compose -f docker-compose.yaml down

.PHONY: export-dep
export-dep:
		poetry export --without-hashes -f requirements.txt -o ./requirements.txt

.PHONY: export-dep-dev
		poetry export --without-hashes --with dev -f requirements.txt -o ./requirements-dev.txt

.PHONY: make-migrate
make-migrate:
		export PYTHONPATH=./src
		poetry run python ./src/simple_clients_api/manage.py makemigrations

.PHONY: migrate
migrate:
		export PYTHONPATH=./src
		poetry run python ./src/simple_clients_api/manage.py migrate

.PHONY: run
run:
		export PYTHONPATH=./src
		poetry run python ./src/simple_clients_api/manage.py runserver
