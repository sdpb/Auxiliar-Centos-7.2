Vagrant.configure("2") do |config|

  config.vm.define "Centos_Samuel"

  config.vm.box = "bento/centos-7.2"
  config.vm.box_version = "2.3.1"

  config.vm.provision :ansible do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
    vb.cpus = "1"
  end
end
