#!/bin/sh

if [ ! -f /usr/local/bin/librarian-puppet ]
then
    cd /tmp
    wget --quiet https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
    sudo dpkg -i puppetlabs-release-trusty.deb
    sudo apt-get update
    sudo apt-get install ruby-dev -y
    sudo gem install librarian-puppet --no-ri --no-rdoc -v 2.1.0
fi

echo "Updating puppet modules"
cd /vagrant/vagrant/puppet
librarian-puppet install --path=/etc/puppet/modules
