---
layout: post
title:  "OpenShift v3 installation"
date:  2016-04-04 15:13:19
---

# v3 install

## pre-task install

* wildcard dns resolution

    hostname -f
    host $(hostname -f)

* static ip address

* setup your repo

* generate the keys
	
        ssh-keygen

* build the ssh tunel through the master and nodes

        ssh-copy-id

* stop and disable NetworkManager
	
        systemctl stop NetworkManager; systemctl disable NetworkManager; systemctl is-enabled NetworkManager

* stop and disable firewalld

        systemctl stop firewalld; systemctl disable firewalld; systemctl is-enabled firewalld

* install docker

        yum -y install docker

* start docker 
	
        systemctl start docker; systemctl enable docker

* install the necessary packages

        yum install -y wget git net-tools bind-utils iptables-services bridge-utils python-virtualenv gcc

