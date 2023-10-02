# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define a custom HTTP header
file { '/etc/nginx/sites-available/custom-header':
  content => "add_header X-Served-By ${::hostname} always;\n",
}

# Create a symbolic link to enable the custom header configuration
file { '/etc/nginx/sites-enabled/custom-header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom-header',
}

# Reload Nginx to apply the changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/sites-available/custom-header'], File['/etc/nginx/sites-enabled/custom-header']],
}
