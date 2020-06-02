---
layout: post
title: 如何关闭Ubuntu默认开启的dnsmasq服务
description: "如何关闭Ubuntu默认开启的dnsmasq服务"
category: articles
tags: [faq, dns]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

Q: Ubuntu 默认开启 dnsmasq 服务，占用了本机53端口，当需要在本机测试或使用其他 dns 服务器时，如何关闭 dnsmasq 服务而且重启电脑后 dnsmasq 服务不会重新被开启？

A: `$ sudo vi /etc/NetworkManager/NetworkManager.conf`

注释掉 `dns=dnsmasq`，如下：

`# dns=dnsmasq`

保存后重启 network-manager，

`sudo restart network-manger`
