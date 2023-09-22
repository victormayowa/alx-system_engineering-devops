# 0-create_a_file.pp
# This Puppet manifest creates a file in /tmp with specified permissions, owner, group, and content.

file { '/tmp/school':
  ensure  => 'file',        # Ensure that it's a file
  mode    => '0744',        # Set file permissions
  owner   => 'www-data',    # Set file owner
  group   => 'www-data',    # Set file group
  content => 'I love Puppet',  # Set file content
}
