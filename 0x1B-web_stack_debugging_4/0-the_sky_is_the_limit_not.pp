# task 1 - syracing the the sky
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

