---
layout: post
title: 获取国内城市天气预报 JSON 数据的 Python 小脚本
description: "获取国内城市天气预报 JSON 数据的 Python 小脚本"
category: articles
tags: [python, JSON, 天气预报, 脚本]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

脚本中的数据源是中国天气网，根据传输的参数不同，返回相应的天气数据;

{% highlight python %}
# coding: utf-8
import urllib2

provinces = {
  "北京": "01",
  "上海": "02",
  "天津": "03",
  "重庆": "04",
  "黑龙江": "05",
  "吉林": "06",
  "辽宁": "07",
  "内蒙古": "08",
  "河北": "09",
  "山西": "10",
  "陕西": "11",
  "山东": "12",
  "新疆": "13",
  "西藏": "14",
  "青海": "15",
  "甘肃": "16",
  "宁夏": "17",
  "河南": "18",
  "江苏": "19",
  "湖北": "20",
  "浙江": "21",
  "安徽": "22",
  "福建": "23",
  "江西": "24",
  "湖南": "25",
  "贵州": "26",
  "四川": "27",
  "广东": "28",
  "云南": "29",
  "广西": "30",
  "海南": "31",
  "香港": "32",
  "澳门": "33",
  "台湾": "34"
}

def fetch(url):
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    content = f.read()
    f.close()
    return content

def parse(content):
    data = {}
    for item in content.split(','):
        code, name = item.split('|')
        data[name] = code
    return data

#url = 'http://m.weather.com.cn/data/101210201.html'
#url = 'http://service.weather.com.cn/plugin/data/city02.xml?level=1'

tmpl = 'http://service.weather.com.cn/plugin/data/city%s.xml'

province = raw_input('%s\n请输入省、直辖市：' % ' '.join(provinces.keys()))

citys = parse(fetch(tmpl % provinces[province]))
city = raw_input('%s\n请输入市名：' % (' '.join(citys.keys())))

countys = parse(fetch(tmpl % citys[city]))
county = raw_input('%s\n请输入区县：' % ' '.join(countys.keys()))

code, name = fetch(tmpl % countys[county]).split('|')

print fetch('http://m.weather.com.cn/data/%s.html' % name)
{% endhighlight %}


