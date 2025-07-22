
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

