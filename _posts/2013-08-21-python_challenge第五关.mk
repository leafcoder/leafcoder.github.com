---
layout: post
title: python chanllenge 第五关
description: "python chanllenge 第五关"
category: articles
tags: [python, chanllenge, 第五关]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

{% highlight python %}
#/usr/bin/python3
import re
import pickle
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/banner.p"

res = urllib.request.urlopen(url)
data = res.read()
pick = pickle.loads(data)
for line in pick:
    print(''.join(map(lambda pair: pair[0]*pair[1], line)))
{% endhighlight %}
