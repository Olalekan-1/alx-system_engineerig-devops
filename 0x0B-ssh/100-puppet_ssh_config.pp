# Include the stdlib module
class { 'stdlib': }

file_line { 'identity file name is set to school':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^(\s*)IdentityFile\s.*$',
}

file_line { 'no password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^(\s*)PasswordAuthentication\s.*$',
}

