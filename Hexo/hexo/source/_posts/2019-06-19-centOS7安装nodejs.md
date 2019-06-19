---
title: centOS7安装nodejs
tags: David - Work is for a better life
date: 2019-06-19 14:46:23
categories: nodejs
---
## 在CentOS 7上安装Node.js
- 源码安装
1. 官网下载源码 http://nodejs.cn/download/
2. 解压 `tar xzvf node-v*`
3. 进入目录编译安装 (安装依赖sudo yum install gcc gcc-c++)
```
cd node-v*
./configure
make （等待时间比较久）
sudo make install
```
4. 查看版本
```
node -v
npm -v
```