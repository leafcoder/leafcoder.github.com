---
layout: post
title:  Ubuntu 中 /etc/shadow 密码文件中密码的生成脚本（python）
author: digflybird
nav:    HOME
categories: python ubuntu
---

执行如下代码可以生产系统加密密码，如 `python password.py ''`

    import crypt
    from sys import argv
    from uuid import uuid4
    from random import randint

    assert len(argv) >= 2, 'please input password'
    size = randint(8, 12)
    salt = uuid4().hex[:size]
    print crypt.crypt(argv[1], '$6$%s' % salt)
