---
layout: post
title: "docker 中的 ubuntu 使用 Elasticsearch 遇到的错误集合"
description: ""
category: articles
tags: [docker, ubuntu, Elasticsearch]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

当修改 Elasticsearch 6.2.4 的配置文件 config/elasticsearch.yml 时，将 network.host 项设置为 0.0.0.0，遇到如下错误：

```
ERROR: [2] bootstrap checks failed
[1] initial heap size [132120576] not equal to maximum heap size [2092957696]; this can cause resize pauses and prevents mlockall from locking the entire heap
[2] max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

2. 错误1：initial heap size [132120576] not equal to maximum heap size [2092957696]; this can cause resize pauses and prevents mlockall from locking the entire heap

    修改 Elasticsearch 的配置文件 `config/jvm.options`，取消以下两行前的`#`号，保存后重启 Elasticsearch 即可。

    # -Xms1g

    # -Xmx1g

2. 错误2：max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]

    错误原因：系统的 vm.max_map_count 参数太小

    解决办法：

    修改宿主机（即 docker 所在的主机本身），然后重启 docker 容器即可。修改宿主机参数的命令如下：

    1. 方法1，命令修改

        `sysctl -w vm.max_map_count=655360`

    2. 方法2，修改配置文件

        $ sudo vi /etc/sysctl.conf

        在文件的底部增加 `vm.max_map_count=262144`。