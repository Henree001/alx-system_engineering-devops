#install flask from pip3.
service { 'flask':
  ensure  => installed,
  version => 2.1.0}
