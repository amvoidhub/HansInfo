# 说明文档

介绍：基于[漢典](https://www.zdic.net/)网站内容，爬取汉字信息。可获取包括：拼音，笔画，结构，类型，字表，反应时，频率% 等汉字信息。

---

## 变量说明

拼音py，笔画bh，结构jg，类型lx，字表zb，反应时rt，频率%zp

## Excel文件说明

CorpusCharacterlist提供汉字字频统计

DataBase提供汉字辨认平均反应时

HanList包含两个表格分别为list1-2500个常用字和list2-1000个次常用字，从[漢典](https://www.zdic.net/)站内抓取

hans文件内，以竖排第一列置入需要查询的字列并保存，程序会读取并重新写入字列中每个字的相关信息。每次使用查询前请新建sheet并删除原有的newhans表格。
