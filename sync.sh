#!/bin/bash
#Author: timger <yishenggudou@gmail.com>
#weibo <http://t.sina.com/zhanghaibo>
#@yishenggudou http://twitter.com/yishenggudou

PWD＝$(pwd)
echo $PWD
#backup the old hosts file
cat /etc/hosts > /etc/hosts.old
#Create the link to myhosts
ln -sb "${PWD}/hosts/hosts" /etc/hosts

