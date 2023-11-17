#task 2 - changing the OS configuratio
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
