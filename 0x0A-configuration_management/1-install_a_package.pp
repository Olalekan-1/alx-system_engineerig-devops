# install flask version 2.1.0

package { 'werkzueg':
  ensure   => '2.2.1'
  provider => 'pip3',
}


package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
