#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo sh -c 'echo "hi ;)" > /data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    server_name mennatallah.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

sudo service nginx restart