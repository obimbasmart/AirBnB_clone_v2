#!/usr/bin/env bash
# set up web servers for deployment

# create directories
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"

# give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#create fake test html content
echo "<h1>Deploying web static!!! wait for it</h1>" > "/data/web_static/releases/test/index.html"

# create symbolic link
sudo ln -sf "/data/web_static/releases/test" "/data/web_static/current"


# change nginx default server root directory
nginx_config="/etc/nginx/sites-available/default"
new_content="
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
	}

}

"
sudo chown -R ubuntu:ubuntu "$nginx_config"
echo "$new_content" > "$nginx_config"

# restart nginx
sudo service nginx restart
