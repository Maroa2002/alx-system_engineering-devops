# Puppet manifest that replaces a line in a file on a server
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
