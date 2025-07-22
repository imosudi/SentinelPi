# 🛰️ SentinelPi

[![CI](https://github.com/imosudi/sentinelpi/actions/workflows/ci.yml/badge.svg)](https://github.com/imosudi/sentinelpi/actions)
[![Docker Hub](https://img.shields.io/docker/pulls/imosudi/flask-ui?label=flask-ui)](https://hub.docker.com/r/imosudi/flask-ui)
[![License](https://img.shields.io/github/license/imosudi/sentinelpi)](LICENSE)

**SentinelPi** is a secure, modular, AI-powered home surveillance system for Orange Pi and ARM SBCs. Includes Frigate (YOLOv5/TFLite), MotionEye, Flask UI, MQTT, Telegram alerts, Home Assistant integration, VPN (WireGuard), TLS (DuckDNS), reverse SSH, and full Docker + Ansible automation.

---

## 🔧 Features

- 🎥 Multi-camera support (USB + RTSP/IP)
- 🧠 AI detection (YOLOv5 Nano / TensorFlow Lite via Frigate)
- 🌀 Motion detection (MotionEye)
- 🖥️ Custom Flask overlay dashboard
- 🔔 MQTT alerts + Telegram bot notifications
- 🏡 Home Assistant integration
- 🔐 VPN (WireGuard), TLS via DuckDNS + certbot
- 🔁 Reverse SSH fallback for remote access
- 📦 Docker + Ansible automation
- 💾 Optional NAS or USB video storage
- 🔐 Designed for low-resource edge environments.
- ⚡️ Tuned for performance, extensibility, and privacy.

---

## 🚀 Quick Install

```bash
git clone https://github.com/imosudi/sentinelpi.git
cd sentinelpi
cp .env.example .env    # Fill in your secrets
make install            # Or ./install.sh

```

## 📁 Directory Structure

```
sentinelpi/
├── .env.example                 # Environment variables
├── Makefile                    # Common automation tasks
├── install.sh                  # Full CLI installer
├── docker-compose.yml          # Core services
├── flask_ui/                   # Flask overlay app
│   ├── app.py
│   ├── Dockerfile
│   └── templates/
├── telegram_bot/               # Bot & alert handler
│   ├── alert_bot.py
│   └── alert_bot.service
├── nginx_tls/                  # HTTPS reverse proxy
├── ansible/                    # Full deployment automation
│   ├── inventory
│   ├── install.yml
│   └── roles/
├── home-assistant/             # Lovelace UI + MQTT topics
├── .github/workflows/ci.yml    # GitHub CI/CD pipeline

```

## 📡 Access Points

| Service         | Default Address                       |
| --------------- | ------------------------------------- |
| MotionEye       | `http://<device-ip>:8765`             |
| Flask UI        | `https://<your-domain>:5000`          |
| Frigate NVR     | `http://<device-ip>:5001`             |
| MQTT Broker     | `mqtt://<device-ip>:1883`             |
| VPN (WireGuard) | Config in `ansible/roles/vpn/files/`  |
| Reverse SSH     | Enabled via `autossh` systemd service |

## 🛠 Common Tasks

make install      # Run full setup with CLI installer
make deploy       # Apply Ansible playbook to localhost
make test         # Lint Docker/Ansible/Python configs
make clean        # Stop and remove all containers/volumes
make status       # Check systemd and container status

