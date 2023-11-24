# install flask with puppet
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => 'pip3 install Flask==2.1.0',
  path        => '/usr/bin',
  refreshonly => true,
  require     => Package['python3-pip'],
}
