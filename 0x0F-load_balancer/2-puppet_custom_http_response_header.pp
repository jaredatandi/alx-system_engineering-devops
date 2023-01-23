# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Add custom HTTP header to Nginx configuration
file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "add_header X-Served-By $hostname;",
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

