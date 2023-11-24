# kill a process with puppet

exec { 'kill_killmenow_process':
  command => 'pkill -f "killmenow"',
  path    => '/bin:/usr/bin';
}
