## Overview

> This Vagrantfile is a configuration file for setting up a virtual machine using Vagrant. It defines the specifications for the virtual machine, including the box to use, network settings, provider-specific configurations, and provisioning scripts.

## Prerequisites

Before using this Vagrantfile, make sure you have the following installed:

- Vagrant
- Vagrant VMware Provider

## Usage

1. Clone or download the repository containing the Vagrantfile.

    ```bash
    git clone https://github.com/Adhaammohammed/DevOps-Exercise.git
    ```
    
2. Navigate to the directory containing the Vagrantfile.
   
    ```bash
    cd vagrantfile
    ```
3. Start the virtual machine.

    ```bash
    vagrant up
    ```
4. Access the virtual machine.
    
    ```bash
    vagrant ssh
    ```
5. To halt and destroy the virtual machine

    ```bash
    vagrant halt
    vagrant destroy
    ```

## Configuration Details    

Box Settings
- Box: This Vagrantfile uses the "hashicorp/precise64" box as the base box for the virtual machine. You can change it to another box if needed.

Network Settings
- Forwarded Port: Forwards port 80 from the guest machine to port 8080 on the host machine. You can modify the guest and host values to suit your requirements.

Provider-Specific Settings (VMware Fusion)
- Memory: Sets the virtual machine memory to 1024 MB.
- CPUs: Allocates 2 virtual CPUs to the virtual machine.

Provisioning
The Vagrantfile includes a simple shell provisioning script that performs the following actions:

- Updates the package repository.
- Upgrades installed packages.
- Cleans up unnecessary packages.

You can customize the provisioning script by adding or modifying commands within the config.vm.provision "shell" block.

    
