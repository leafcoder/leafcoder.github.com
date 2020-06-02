---
layout: post
title: 如何在 python 中改变 ulimit 最大值
description: "如何在 python 中改变 ulimit 最大值"
category: articles
tags: [python, ulimit]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

    import resource

    print "修改ulimit前:", resource.getrlimit(resource.RLIMIT_NOFILE)
    resource.setrlimit(resource.RLIMIT_NOFILE, (131072, 131072)) # 131072 代表要修改的ulimit数
    print "修改ulimit后:", resource.getrlimit(resource.RLIMIT_NOFILE)

以上代码可以用于修改当前进程的*ulimit*最大值，避免文件句柄数不足，发生异常：

`socket.error: [Errno 24] Too many open files`
