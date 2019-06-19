---
title: Hexo Hiker主题配置与美化
tags: David
date: 2019-05-07 15:41:20
categories: Hexo
top: 9996

---


## 安装步骤
> git下载地址
`https://github.com/iTimeTraveler/hexo-theme-hiker.git `

***
##### 启用主题
>  把Hexo主目录下的 _config.yml 文件中的字段 theme 修改为 hiker
![](http://lv005.com/otherimgs/cut/cut01.jpg)
***
##### 自定义首页背景图
>  您可以将图片放到 hexo\themes\hiker\source\css\images 文件夹下. 然后更改 hiker/_config.yml文件里的home_background_image字段
![](http://lv005.com/otherimgs/cut/cut02.jpg)
##### 首页背景填充方式有三种可选mode(默认为image)：

* image: 大图模式
* trianglify: 多边形渐变背景
* polyline: 随机彩色折线
#### 如果在使用image模式时url为空（enable仍然保持true）, 主题也会自动使用polyline模式
![](http://lv005.com/otherimgs/cut/cut03.jpg)
***

#### 色彩主题：

##### Hiker 共有六种主题可选,配置在主题文件夹下的 _config.yml文件中
![](http://lv005.com/otherimgs/cut/cut04.jpg)

> default, normal, night, night blue, night bright, night eighties
```
# Code Highlight theme
# Available value:
#    default | gray | normal | night | night eighties | night blue | night bright
# https://github.com/chriskempson/tomorrow-theme
highlight_theme: default
```
***
#### 主题色：

##### Hiker 共有五种主题色可选,配置在主题文件夹下的 _config.yml文件中

> orange, blue, red, green, black
```
# Article theme color
# Available value:
#random | orange | blue | red | green | black
theme_color: random
```
***
#### 修改头像：
>
```
# 头像设置
# Put your favicon.ico or avatar.jpg into `hexo-site/themes/hiker/source/` directory.
avatar: 
  enable: true
  border: true
  width: 124
  height: 124
  top: 0
  url: css/images/mylogo.jpg  #头像修改位置
```
***

#### 站内搜索：

##### Hiker 共有五种主题色可选,配置在主题文件夹下的 _config.yml文件中

> orange, blue, red, green, black
```
# Article theme color
# Available value:
#random | orange | blue | red | green | black
theme_color: random
```
***

#### 打赏功能：
```
donate: 
 enable: true
 message: '描述'
 wechatImage: 微信图片  
 alipayImage: 支付宝图片
```

#### 设置标签、分类、关于页面：
```
hexo new page about         新建about
hexo new page tags          新建标签
hexo new page categories    新建分类
```
#### 在blog/source/中会多出三个文件夹，每个文件夹里都有一个index.md
> 以tags为例，修改其中的index.md，如
```
title: tags
date: 2017-08-10 09:35:41
layout: tags
comments: false   #此页评论关闭
```
***
#### 搜索功能
`npm install -S hexo-generator-ison-content`
***
#### 评论功能
> 修改主题文件下_config.yml
```
# comment ShortName, you can choose only ONE to display.
# 评论系统
gentie_productKey: #your-gentie-product-key
duoshuo_shortname: 
disqus_shortname: 
livere_shortname: MTAyMC8yOTQ4MS82MDQ5
uyan_uid: 
wumii: 
```
***


#### 修改主页图片轮播速度
> 路径 hiker/layout/_partial/header.ejs
```
$('section.awSlider .carousel').carousel({
    pause: '',
    interval: 4000
});  
``` 
***
