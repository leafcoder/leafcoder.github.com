---
layout: post
title: 如何用 python 生成 Ubuntu 系统的空字符串密码
description: "使用空密码后，sudo 的时候再也不需要麻烦的输入密码了，直接回车就行（千万别跟我谈什么安全之类的，这个我可管不了）。"
modified: 2014-08-20
category: articles
tags: [python, ubuntu, shadow, 密码]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
share: true
---

将以下的 [python](http://www.python.org) 代码保存到一个文件，并运行就能生成一个空密码的字符串;当然，其实它也可以生成其他任意密码的字符串。

生成空密码：`python password.py`

{% highlight python %}
#!/usr/bin/python
import crypt
from sys import argv
from uuid import uuid4
from random import randint

password = ''
if len(argv) > 1:
    password = argv[1]
size = randint(8, 12)
salt = uuid4().hex[:size]
print crypt.crypt(password, '$6$%s' % salt)
{% endhighlight %}

将生成好的密码字符串覆盖 `/etc/shadow` 中的密码段即可。

使用空密码后，`sudo` 的时候再也不需要麻烦的输入密码了，直接回车就行（千万别跟我谈什么安全之类的，这个我可管不了）。

除了 Python 代码的方式，你也可以通过下面的命令生成密码串：

`mkpasswd -m SHA-512 password`

空密码：

`mkpasswd -m SHA-512 ''`
