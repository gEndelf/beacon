# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

dir = File.dirname(File.expand_path(__FILE__))
data = YAML::load(File.open("#{dir}/vagrant/config.yaml"))

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = data['vm']['hostname']

  config.vm.provision "shell", path: "vagrant/shell/init-puppet.sh"
  config.vm.provision :puppet, :module_path => "modules" do |puppet|
	puppet.module_path = "vagrant/puppet/modules"
	puppet.manifests_path = "vagrant/puppet/manifests"
	puppet.hiera_config_path = "vagrant/puppet/hiera.yaml"
	#puppet.options = "--debug --verbose"
  end
  config.vm.provider "virtualbox" do |v|
	v.memory = data["vm"]["memory"]
	v.cpus = data["vm"]["cpus"]
  end

  config.vm.network "private_network", ip: data['vm']['ip']

  data["vm"]["forwarded_ports"].each do |i, port|
	config.vm.network :forwarded_port, guest: port["guest"].to_i, host: port["host"].to_i
  end
  config.ssh.forward_x11 = true
end
