---
layout: post
title: "如何修改结巴分词中jieba_cache文件的路径"
description: ""
category: articles
tags: [结巴分词]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

通过查看结分词源码，发现源码在全局位置初始化了一个名为 dt 的 Tokenizer 对象，初始化代码为 `dt = Tokenizer()`，
我们使用 Python 中常用的 Monkey Patch 方式，可以修改结巴分词的 jieba.cache 文件所在目录和名字，代码如下：

```
import jieba

jieba.dt.tmp_dir    = 'YOUR TMP DIRECTORY'
jieba.dt.cache_file = 'YOUR CACHE FILE NAME'
```