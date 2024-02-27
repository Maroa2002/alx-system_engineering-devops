#!/usr/bin/env bash
# Puppet manifest that alters config file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>"
  #config .ssh for server connect
  Host*
  IdentityFile ~/.ssh/school
  PasswordAuthentication no"
}
