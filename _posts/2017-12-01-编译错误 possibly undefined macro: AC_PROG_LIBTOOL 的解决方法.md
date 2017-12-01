---
layout: post
title: 编译错误 possibly undefined macro: AC_PROG_LIBTOOL 的解决方法
description: "编译错误 possibly undefined macro: AC_PROG_LIBTOOL 的解决方法"
category: articles
tags: [QA]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
share: true
---

在Linux系统中，经常需要依赖 autoconf / automake 来完成软件的编译，然而，安装它们后经常会碰到一个编译错误，其中关键的错误信息具体如下：

```
configure.ac:21: error: possibly undefined macro: AC_PROG_LIBTOOL
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
autoreconf: /usr/bin/autoconf failed with exit status: 1
```

出现此类错误信息，一般可通过安装一个工具包 libtool 来解决，各 Linux 系统命令可能不同，以 Ubuntu 系统为例，命令如下：

```
sudo apt-get install libtool
```
