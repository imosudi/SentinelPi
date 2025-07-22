#!/bin/bash

# DuckDNS domain and token
DOMAIN="your-domain"
TOKEN="your-token"

# Get the current public IP address
IP=$(curl -s http://api.ipify.org)

# Update DuckDNS with the current IP address
curl -s "https://www.duckdns.org/update?domains=${DOMAIN}&token=${TOKEN}&ip=${IP}" > /dev/null

# Log the update
echo "$(date): Updated DuckDNS for ${DOMAIN} to IP ${IP}" >> /var/log/ddns-update.log