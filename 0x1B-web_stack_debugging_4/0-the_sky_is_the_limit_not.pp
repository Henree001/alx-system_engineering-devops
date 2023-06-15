# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'nginx_fix':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
}

# Restart Nginx
exec { 'nginx-restart':
  command  => 'service nginx restart',
  provider => shell,
}
