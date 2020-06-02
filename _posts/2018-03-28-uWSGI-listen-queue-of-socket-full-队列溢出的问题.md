---
layout: post
title: "uWSGI listen queue of socket full 队列溢出的问题"
description: ""
category: articles
tags: [uWSGI, 队列溢出]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

使用 uWSGI 时，uWSGI的日志中出现错误 `uWSGI listen queue of socket full` 的错误信息，想要解决这个问题，需要修改服务器的配置，具体如下：


```
$ vi /etc/sysctl.conf

在文件最后添加一行记录：

net.core.somaxconn = 1024
```

```
重载配置，使配置立即生效：
$ sysctl -p
```

在 uWSGI 的配置项中增加 --listen 1024，也可以将此配置项写入 uWSGI 的配置文件中；

重启 uWSGI，如此可以在某种程度上缓解此问题。