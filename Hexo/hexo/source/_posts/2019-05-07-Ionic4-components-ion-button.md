---
title: Ionic4 components【ion-button】
date: 2019-05-07 00:09:11
tags: Ionic4
categories: Ionic4
---

## Ionic 4

### ion-button

#### 本地调试导入下面两个文件

```bash
<script src="https://unpkg.com/@ionic/core@latest/dist/ionic.js"></script>
<link href="https://unpkg.com/@ionic/core@latest/css/ionic.bundle.css" rel="stylesheet"/>
```

#### 按钮样式

```bash
<!-- button -->
        <!-- full 不带圆角的100%宽度按钮 -->
        <ion-button expand="full" shape="round" color="danger">this is a button</ion-button>
        <!-- block 带小圆角圆角的100%宽度按钮 -->
        <ion-button expand="block" color="danger">this is a button</ion-button>
        <!-- Colors -->
        <!-- shape="round" 圆角按钮 -->
        <ion-button strong="true" shape="round" color="primary">Primary</ion-button>
        <ion-button size="large" color="secondary">Secondary</ion-button>
        <ion-button size="small" color="tertiary">Tertiary</ion-button>
        <ion-button disabled="true" color="success">Success</ion-button>
        <ion-button fill="clear" color="warning">Warning</ion-button>
        <ion-button color="warning">Warning</ion-button>
        <ion-button fill="outline" color="danger">Danger</ion-button>
        <ion-button color="danger">Danger</ion-button>
        <ion-button color="light">Light</ion-button>
        <ion-button fill="solid" color="light">Light</ion-button>
        <ion-button mode="md" color="medium">Medium</ion-button>
        <ion-button mode="ios" color="medium">Medium</ion-button>
        <ion-button color="dark">Dark</ion-button>
```

#### 带icon的button
```bash
<!-- Icons left-->
        <ion-button>
          <ion-icon slot="start" name="star"></ion-icon>
          Left Icon
        </ion-button>
        <!-- Icons right -->
        <ion-button>
          <ion-icon slot="end" name="star"></ion-icon>
          Right Icon
        </ion-button>
        <ion-button>
          <ion-icon slot="icon-only" name="star"></ion-icon>
        </ion-button>
```

