# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "snipersteve/Blog@gh-pages"
}

# 站点设置
site_name = "科学生活"
site_logo = "${static_prefix}icon.png"
site_build_date = "2019-12-25T10:50+08:00"
author = "伪装兽"
email = "sfl05@163.com"
author_homepage = "https://861204.xyz"
description = "做什么都得走点技术流"
language = 'zh-CN'
external_links = [
    {
        "name": "关于法学",
        "url": "https://law.861204.xyz",
        "brief": "关于法律的学习心得"
    },
    {
        "name": "毛总的博客",
        "url": "https://blog.leo.red/",
        "brief": "人是万物的尺度"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/snipersteve",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/snipersteve",
        "icon": "gi gi-github"
    },
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
