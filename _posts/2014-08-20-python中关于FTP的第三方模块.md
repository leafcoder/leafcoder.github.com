---
layout: post
title: python 中关于 FTP 的第三方模块
description: "列举平时使用 python 时用过的关于 FTP 的模块"
modified: 2014-08-20
category: articles
tags: [python ubuntu shadow password]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
share: true
---

###1.[pyftpdlib](https://github.com/giampaolo/pyftpdlib) 是一款 Python FTP 服务器库。

Quick Start（快速创建一个 FTP 服务器）：

{% highlight python %}
#!/usr/bin/python
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/username", perm="elradfmw")
authorizer.add_anonymous("/home/nobody")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
{% endhighlight %}
