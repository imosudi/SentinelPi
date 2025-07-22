# Makefile

.PHONY: install deploy test clean status

install:
	@echo "Running full setup with CLI installer..."
	@bash install.sh

deploy:
	@echo "Applying Ansible playbook to localhost..."
	@ansible-playbook ansible/install.yml -i ansible/inventory

test:
	@echo "Linting Docker/Ansible/Python configs..."
	@docker-compose run --rm lint
	@ansible-lint ansible/install.yml
	@flake8 flask_ui

clean:
	@echo "Stopping and removing all containers/volumes..."
	@docker-compose down -v

status:
	@echo "Checking systemd and container status..."
	@systemctl status reverse-ssh.service
	@docker ps -a