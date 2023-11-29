# Define a class for Nginx installation and configuration
class { 'nginx':
  package_ensure => 'latest',
}

# Define the default Nginx server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Nginx default configuration\n
              server {\n
                listen 80 default_server;\n
                listen [::]:80 default_server;\n
                root /var/www/html;\n
                index index.html index.htm index.nginx-debian.html;\n
                server_name _;\n
                location / {\n
                  try_files \$uri \$uri/ =404;\n
                }\n
                location ~ /redirect_me {\n
                  return 301 https://www.example.com;\n
                }\n
              }\n",
  require => Class['nginx'],
}

# Define the custom 404 page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Class['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], File['/var/www/html/404.html']],
}

