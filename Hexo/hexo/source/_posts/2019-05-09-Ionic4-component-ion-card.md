---
title: Ionic4-component 【ion-card】
tags: Ionic4
date: 2019-05-09 10:28:50
categories: Ionic4
---

## Ionic 4

### ion-card


```
<ion-card color="warning">
    <ion-card-header>
      <img src="http://lv005.com/otherimgs/img-02.jpg" alt="">
      <ion-card-title>Card Title</ion-card-title>
      <ion-card-subtitle>Card Subtitle</ion-card-subtitle>
    </ion-card-header>
    <ion-card-content>
        <ion-item href="#" class="activated">
            <ion-icon name="wifi" slot="start"></ion-icon>
            <ion-label>Card Link Item 1 .activated</ion-label>
          </ion-item>
        
          <ion-item href="#">
            <ion-icon name="wine" slot="start"></ion-icon>
            <ion-label>Card Link Item 2</ion-label>
          </ion-item>
        
          <ion-item class="activated">
            <ion-icon name="warning" slot="start"></ion-icon>
            <ion-label>Card Button Item 1 .activated</ion-label>
          </ion-item>
        
          <ion-item>
            <ion-icon name="walk" slot="start"></ion-icon>
            <ion-label>Card Button Item 2</ion-label>
          </ion-item>
    </ion-card-content>
  </ion-card>
```
---
## 标签
> ion-card <br>
`  表示该标签是一个ion-card `

> ion-card-header <br>
`卡片标签的头部，里面可以放标题，副标题，图片等`<br>
`属性 translucent=“true” ，设置卡片头部为半透明`<br>
`只有在ion-card设置了color属性的时候，效果比较明显`

> ion-card-subtitle <br>
`副标题`

> ion-card-title <br>
`标题`

***
## 属性
> color
`设置卡片的整体背景颜色`

> mode 
`设置卡片的主题风格`  
#### mode="md",color="warning"
![mode="md",color="warning"](http://lv005.com/otherimgs/cut/mode-md.png)

#### mode="ios",color="warning"
![mode="ios",color="warning"](http://lv005.com/otherimgs/cut/mode-md.png)

### 卡片中还可以跟列表
![图片演示](http://lv005.com/otherimgs/cut/ion-card.jpg)


