Configuration management
========================

# General
. All your files will be interpreted on Ubuntu 20.04 LTS
. All your files should end with a new line
. A README.md file at the root of the folder of the project is mandatory
. Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
. Your Puppet manifests must run without error
. Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
. Your Puppet manifests files must end with the extension .pp

# installing puppet
. $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
. $ apt-get install -y ruby-augeas
. $ apt-get install -y ruby-shadow
. $ apt-get install -y puppet

# installing puppet-lint
$ gem install puppet-lint
