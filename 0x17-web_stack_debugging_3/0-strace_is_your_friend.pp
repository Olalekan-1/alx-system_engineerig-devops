# fix word-press error

exec { 'fix-wordpress-erro':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
    }
