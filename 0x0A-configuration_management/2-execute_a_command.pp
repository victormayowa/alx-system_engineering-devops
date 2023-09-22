# 2-execute_a_command.pp
# This Puppet manifest kills a process named killmenow.

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep killmenow',
}
