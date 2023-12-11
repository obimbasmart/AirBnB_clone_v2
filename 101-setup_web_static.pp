# set up web servers for deployment

# update library and install nginx
exec { 'update-lib':
  command => 'sudo apt-get -y update &> /dev/null',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}


# create directories
file { ['/data/',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}

#create fake test html content
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<h1>Okay, Deploying web static!!! wait for it</h1>',
  owner   => 'ubuntu',
  group   => 'ubuntu'
}


# create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test'
}


# change nginx default server root directory
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
	# Default server configuration

	server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;

        location / {
                try_files $uri $uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
                index index.html;
        }

}',
}

# check nginx config files
exec { 'check_config':
  command => 'sudo nginx -t',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}


# restart nginx
exec { 'restart-nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}
