#!/bin/bash
echo "جاري تثبيت المتطلبات..."
sudo apt update
sudo apt install -y srsran python3
sudo mkdir -p /etc/srsran/
echo "تم التثبيت بنجاح."
