# Install and configure Nginx
class { 'nginx':
  package_ensure => 'latest',
}

# Configure Nginx default server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  require => Class['nginx'],
}

# Create a custom 404 page
file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => Class['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], File['/var/www/html/404.html']],
}


# Nginx default configuration
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;
  server_name _;

  location / {
    try_files $uri $uri/ =404;
  }

  location ~ /redirect_me {
    return 301 https://www.example.com;
  }
}

