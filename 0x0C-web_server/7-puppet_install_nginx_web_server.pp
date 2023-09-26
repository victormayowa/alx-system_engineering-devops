# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => template('nginx/default.erb'),
  notify => Service['nginx'],
}

# Create a custom HTML page for the root path
file { '/var/www/html/index.html':
  ensure => present,
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
}

# Create a custom HTML page for the redirection
file { '/var/www/html/redirect_me':
  ensure => present,
  content => '<html><head><meta http-equiv="refresh" content="0;url=https://www.youtube.com/watch?v=QH2-TGUlwu4"></head></html>',
  require => Package['nginx'],
}

# Configure Nginx to perform a 301 redirect
file_line { 'add_redirect_config':
  path => '/etc/nginx/sites-available/default',
  line => '        location /redirect_me { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; }',
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Enable and start Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
