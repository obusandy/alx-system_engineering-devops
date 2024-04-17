# This function modifies the default worker
# processes value in the nginx
# imroves the amount of traffic nginx can handle

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# puts 'nginx restart'
# Simulate nginx restart


exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
