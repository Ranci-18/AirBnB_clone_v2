#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
service nginx start
sudo mkdir -p /data/web_static/releases/test/
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$content" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "38i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/; \n\t}\n" /etc/nginx/sites-available/default
service nginx restart
exit 0
