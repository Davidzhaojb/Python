---
title: Ionic4-component-ion-checked
tags: David - Work is for a better life
date: 2019-05-09 11:00:01
categories: Ionic4
---
## Ionic 4

### ion-checkbox

`<ion-checkbox slot="start" color="warning" disabled="true" checked="true"></ion-checkbox>
`

```
 <ion-item>
    <ion-label>Awesome Label</ion-label>
    <ion-checkbox slot="start" color="warning" disabled="true" checked="true"></ion-checkbox>
</ion-item>
```
### 属性
> slot:string --- 选框的位置<br>  
    `start|end star--单选框位于文字左侧 end--单选框位于文字右侧`

> color:string ---选中后选框的颜色<br>
    `"primary", "secondary", "tertiary", "success", "warning", "danger", "light", "medium", and "dark"`
    
> disabled:boolean ---选框是否可以被选中 <br>
    `true|false(default)`
    
> checked:boolean --- 选框是否是选中状态<br>
    `true|false(default)`