![SentinelPi Logo](https://raw.githubusercontent.com/imosudi/SentinelPi/main/images/SentinelPiLogo.jpeg)

# 🛰️ SentinelPi

[![CI](https://github.com/imosudi/sentinelpi/actions/workflows/ci.yml/badge.svg)](https://github.com/imosudi/sentinelpi/actions)
[![Docker Hub](https://img.shields.io/docker/pulls/imosudi/flask-ui?label=flask-ui)](https://hub.docker.com/r/imosudi/flask-ui)
[![License](https://img.shields.io/github/license/imosudi/sentinelpi)](LICENSE)

**SentinelPi** is a secure, modular, AI-powered home surveillance system built for Orange Pi and ARM SBCs. It integrates Frigate (YOLOv5/TFLite), MotionEye, MQTT alerts, VPN access, Telegram notifications, Home Assistant, and more—fully automated with Docker and Ansible



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
├── .env.example                # Environment variables
├── Makefile                    # Common automation tasks
├── install.sh                  # Full CLI installer
├── docker-compose.yml          # Core services
├── flask_ui/
│   ├── Dockerfile              # Flask overlay app
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── styles.css
├── configs/
│   ├── motioneye/
│   └── frigate/
├── scripts/
│   ├── ddns-update.sh
│   ├── usb-modem.sh
│   └── reverse-ssh.service
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
├── storage/
│   ├── motioneye/
│   ├── frigate/media/
│   ├── mosquitto/data/
│   └── mosquitto/log/
│   └── recordings/ (mounted)
└── .env

```

## 📡 Access Points

| Service       | Address                     | Notes             |
| ------------- | --------------------------- | ----------------- |
| MotionEye     | `http://<device-ip>:8765`   | Local access only |
| Flask UI      | `https://<domain>:5000`     | TLS via DuckDNS   |
| Frigate NVR   | `http://<device-ip>:5001`   | AI-based NVR      |
| MQTT Broker   | `mqtt://<device-ip>:1883`   | Secure via ACL    |
| WireGuard VPN | `wg.conf in ansible/roles/` | Manual import     |
| Reverse SSH   | `autossh.service`           | Uses port `22`    |

```
![Python](https://img.shields.io/badge/python-3.10-blue)
![Ansible](https://img.shields.io/badge/ansible-2.9-red)
![Docker](https://img.shields.io/badge/docker-compose-blue)
![ARM](https://img.shields.io/badge/ARM-Optimised-success)

```

## 🛠 Common Tasks

```
make install      # Run full setup with CLI installer
make deploy       # Apply Ansible playbook to localhost
make test         # Lint Docker/Ansible/Python configs
make clean        # Stop and remove all containers/volumes
make status       # Check systemd and container status
```


