
class { 'stdlib': }

file_line { 'identity file set to school':
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

