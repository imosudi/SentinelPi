#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y python3-pip docker-compose

# Install Python dependencies
pip3 install -r flask_ui/requirements.txt

# Set up Docker containers
docker-compose up -d

# Run Ansible playbook for additional configuration
cd ansible
ansible-playbook install.yml

# Print completion message
echo "Installation complete. Access the Flask UI at https://<your-domain>:5000"