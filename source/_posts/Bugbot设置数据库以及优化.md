---
title: Bugbot设置数据库以及优化
date: 2023-07-11 17:59:12
tags: []
index_img: ../banner_images/banne_photo23.png
---
# 数据库

```
docker run -d -p 5432:5432 --name postgresql -v pgdata:/var/lib/postgresql/data -e  POSTGRES_PASSWORD=ken1140601003@@@ postgres
```

# 这里设置pgadmin4 登录邮箱和密码


```
docker run -d -p 5433:80 --name pgadmin4 -e PGADMIN_DEFAULT_EMAIL=1140601003@qq.com -e PGADMIN_DEFAULT_PASSWORD=ken1140601003@@@ dpage/pgadmin4
```
![](../images/Pasted%20image%2020230706133521.png)

# 优化
管理员中文pin置顶没有通知别人
