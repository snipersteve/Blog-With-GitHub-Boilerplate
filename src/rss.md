---
layout: post
title: 科学RSS
slug: rss
date: 2020/1/4 20:26:00
author: ste
---

十年前是RSS盛行的年代，十年后已变成了微信公众号的天下。微信公众号某种程度上有RSS的影子，但是不够开放，算是进步和退步吧。我已经很少用RSS了，因为大部分网站都不支持。2019年8、9月份的时候，因为需要跟踪上海发改委网站上关于奉贤海上风电项目竞价的情况，每天打开网站看一遍，真是太蛋疼了。于是想到了自己去烧制一个RSS。

通过Google找到的了Feed43，原理蛮简单，就是定时去读取网站内容，然后用类似正则的方式去匹配内容信息。试了一下就会了，制作了国家发改委、能源局等网站的RSS。
![Feed43](./images/feed43.png)

下一步就是要找个RSS阅读器了，这类app现在做的人也不多了，iOS上尚有不少优秀app，安卓上都找不到合适。转而想到Telegram，果然有人提供rss bot可以直接用。在对话框中告诉机器人要订阅的rss链接，机器人就会在有更新时推送消息给你，轻量而且方便。不过由于是第三方的bot，没几天就告诉我因服务器问题下线了。所以还是得自己动手。

辗转找到了一个go语言写的开源机器人flowerss-bot，我一看有Docker版，第一时间想到就是用群晖跑，然而一直没弄清config要放在哪个文件夹下，没跑成功。

回家就想起那个吃灰的N1，原本刷了coreelec看片用，后来换Plex就用不上了。于是拿出来刷成Armbian并写入emmc，因为有前人经验，所以这一步很顺利。
![armbian](./images/armbian.jpg)

然后继续装上Docker，并弄好图形界面，这一步也挺顺利。
![Portainer](./images/portainer.jpg)

然而再进一步要运行flowerss的Docker时才发现，这个docker并不支持arm框架，等于白搞了。事实上，这些现成的docker普遍都不支持arm。本来用docker是想简单些，却反而弄复杂了，还不如直接编译。于是装了go，然后直接编译了一个。
![flowerss](./images/flowerss.jpg)

终于跑起来了，还是为了配置文件的位置折腾了一下，不过最终搞定了，效果如下：
![Telegram](./images/telegram.jpg)

完结撒花。