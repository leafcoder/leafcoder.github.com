---
layout: post
title: "Nginx、uWSGI、Flask 项目部署"
description: ""
category: articles
tags: [Nginx, uWSGI, Flask 项目部署]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
share: true
---

我使用 Flask 作为开发框架比较少，所以在部署 Flask 项目方面经验相对较少，现将部署流程记录一下，留作今后参考。

# 1. 开发 Flask

开发好的 Flask 项目包含一个运行文件 manage.py，其中包含一个 app 对象，例如项目结构：

```
├── project
│   ├── __init__.py
│   ├── main
│   ├── models.py
│   ├── static
│   └── templates
├── manage.py
└── uwsgi.ini
```

# 2. 安装配置 Nginx

## 下载 nginx 源码 nginx-1.12.1.tar.gz，解压后安装；

```
$ cd Downloads
$ tar zxf nginx-1.12.1.tar.gz
$ cd nginx-1.12.1
$ ./configure --prefix=/opt/nginx
$ make && make install
```

## 配置 Nginx修改配置文件，增加 server 配置；

```
$ cd /opt/nginx
$ vi conf/nginx.conf
```


```
#user  nobody;
worker_processes  4;    #可以设置成cpu个数，体验较佳的性能

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;，

#pid        logs/nginx.pid;

worker_rlimit_nofile 65535; # 最大打开文件数，这个值需要<= worker_connections

events {
    worker_connections  65535;  # 最大连接数，这个值依赖系统的配置。
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    gzip  on;

    # 以下为您需要增加的配置

    upstream my_servers {
        server 192.168.0.100:8080;
        server 192.168.0.101:8080;
        server 192.168.0.102:8080;
    }

    # uWSGI dynamic
    server {
        listen       80;
        server_name  dynamic.youdomain.cn;

        location / {
            include      uwsgi_params;
            uwsgi_pass   http://my_servers;
            uwsgi_ignore_client_abort on;
            uwsgi_param UWSGI_PYHOME /home/ubuntu/.virtualenvs/pyenv;
            uwsgi_param UWSGI_CHDIR  /home/ubuntu/my_project;
            uwsgi_param UWSGI_SCRIPT manage;
        }
    }

    # uWSGI static
    server {
        listen       80;
        server_name  static.youdomain.cn;

        location /static {
            root html;
        }
    }

}
```

## 启动 Nginx

```
$ cd /opt/nginx/sbin
$ ./nginx
```

# 3. 安装配置uWSGI

## 安装 uWSGI

```
$ pip install uwsgi
```

## 创建配置文件 uwsgi.ini

```
[uwsgi]
socket = :8080
wsgi-file = manage.py
callable = app
master = true          //主进程
vhost = true           //多站模式
no-site = true         //多站模式时不设置入口模块和文件
workers = 24           //子进程数
reload-mercy = 10
vacuum = true          //退出、重启时清理文件
max-requests = 65535
limit-as = 512
buffer-size = 30000
chmod-socket = 666
pidfile = ./logs/%n.pid
daemonize = ./logs/%n.log
```

## 运行 uWSGI

```
$ cd /home/ubuntu/my_project
$ uwsgi --ini uwsgi.ini
```