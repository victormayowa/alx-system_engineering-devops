# Define a class to manage SSH client configuration
class ssh_config {

  # Add a line to disable password authentication
  file_line { 'Turn off passwd auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^#?PasswordAuthentication',
  }

  # Add a line to declare the identity file
  file_line { 'Declare identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
    match  => '^#?IdentityFile',
  }
}

# Apply the class
include ssh_config
