# Ensure the APT repository is up-to-date before installing nginx
Apt::Update { 'update_apt':
  before => Package['nginx'],
}

# Install nginx package
package { 'nginx':
  ensure  => 'present',
  require => Apt::Update,
}

# Manage nginx service
class { 'nginx':
  service_ensure => 'running', # Ensure nginx service is running
  service_enable => true,      # Enable nginx service to start on boot
}

# Add a custom HTTP header to nginx configuration
file_line { 'http_header':
  path    => '/etc/nginx/nginx.conf',          # Path to nginx configuration file
  line    => "add_header X-Served-By \"${hostname}\";", # Custom HTTP header line
  match   => '^http\s*{',                       # Match the beginning of the http block
  require => Package['nginx'],                  # Require nginx package to be installed
}

