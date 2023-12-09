#!/usr/bin/env bash
# set up web servers for deployment

# install nginx
sudo apt-get -y update &> /dev/null
sudo apt-get -y install nginx &> /dev/null

# create directories
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"

#create fake test html content
echo "<h1>Deploying web static!!! wait for it</h1>" | sudo tee  "/data/web_static/releases/test/index.html" &> /dev/null

# create symbolic link
sudo ln -sf "/data/web_static/releases/test" "/data/web_static/current"

# give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# change nginx default server root directory
nginx_config="/etc/nginx/sites-available/default"
echo "
# Default server configuration

server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}

}

" | sudo tee "$nginx_config" &> /dev/null

# restart nginx
sudo service nginx restart

