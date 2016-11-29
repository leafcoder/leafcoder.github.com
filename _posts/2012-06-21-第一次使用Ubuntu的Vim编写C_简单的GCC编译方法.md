---
layout: post
title: 第一次使用Ubuntu的Vim编写C_简单的GCC编译方法
description: "第一次使用Ubuntu的Vim编写C_简单的GCC编译方法"
category: articles
tags: [vi, vim, ubuntu, c]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
share: true
---

首先，打开终端，输入vi，启动vi编辑器，如下图所示：

![vim_01](/images/posts/vim_01.gif)

接着，开始在本编辑器中编写C代码，并且将其保存为.c文件，如下图所示。

![vim_01](/images/posts/vim_02.gif)


最后，你可以用命令gcc HelloLinux.c或者是gcc -Wall HelloLinux.c来编译本C源文件。如果源码无误，编译成。

由于之前没有指定可执行文件名，系统默认生成了a.out文件，我们在终端中使用./a.out来查看文件运行结果，如下图：

![vim_01](/images/posts/vim_03.gif)

成功！
