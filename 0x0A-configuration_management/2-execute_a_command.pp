exec { 'kill_killmenow_process':
  command     => 'pkill -f "killmenow"',
  path        => '/bin:/usr/bin';
}
