# Ensure nginx package is present and installed
package { 'nginx':
  ensure  => 'present',
  require => Exec['update_apt_store'],  # Require 'update_apt_store' exec before installing nginx
}

# Executing apt-get update to refresh package repositories
exec { 'update_apt_store':
  command => '/usr/bin/apt-get update',
}

# Add a line to nginx configuration file for custom HTTP header
file_line { 'http_header':
  path    => '/etc/nginx/nginx.conf',   # Path to nginx configuration file
  line    => "http {\n\tadd_header X-Served-By \"${hostname}\";",  # Line to add with custom header
  match   => 'http {',  # Matching line before which new line should be added
  require => Package ['nginx'],  # Require nginx package before modifying the configuration
}

# Restart nginx service if configuration file has been updated
exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
  require => File_line ['http_header']  # Require file modification before restarting nginx
}

