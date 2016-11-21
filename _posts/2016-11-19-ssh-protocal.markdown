---
layout: post
title:  "ssh-protocal"
date:  2016-11-18 23:58:38
---

# basic ssh usage

    ssh username@remote_hostname
    * if the username is omited, it will use the current username to login remote host,
    if remote host does not have this user, then the login failed

# login without password
  
    * generate the pubulic and private key pairs
    ssh-keygen -N ''
    1. you have two hosts, you are on hostA, and you want to login hostB without password.
    then you need copy A's pub key to B
    ssh-copy-id username@hostB
    2. will copy hostA public key to B ~/.ssh/authorized_keys, you can do it manually 
    without using the password.
    * the authentication process
    1. hostA send the login request to hostB, since hostB already has A's pub key, so B 
    use A's pub key encrypted a random string then send it back to A
    2. hostA use private key decrypted the message(including A's information and the random string), 
    3. hostA send back the random string(from step2), and encrypted with A's private key, 
    4. hostB decrypted the message and got the random string, then the authentication succeed.
    hostB allow A login.
