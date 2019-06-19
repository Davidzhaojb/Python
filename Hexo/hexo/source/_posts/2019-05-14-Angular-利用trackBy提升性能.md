---
title: Angular 利用trackBy提升性能
tags: David - Work is for a better life
date: 2019-05-14 17:13:21
categories:
---
### 原文出处：https://www.cnblogs.com/cme-kai/archive/2018/01/26/8358915.html

### 目前我们遍历一个集合的通用方法是
```

<ul>
  <li *ngFor="let item of items">{{item}}</li>
</ul>
```

#### 有时候，后端接口会返回新的数据，用我们常用的方法，Angular把集合里面的项全部移除再添加，如果数据量大，会进行大量的DOM操作，消耗大量的性能。我们的解决方案是，为*ngFor添加一个trackBy函数，告诉Angular该怎么跟踪集合的各个项

#### 该函数需要两个参数，第一个是当前的index，第二个是当前项，并返回唯一标示

```
<ul><li *ngFor="let item of items; trackBy: trackByIndex">{{item.name}}</li></ul>
```

```
trackByIndex(index, item){
    return index;
  }
```

