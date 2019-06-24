## 第一部分：初识 Elasticsearch
### 第 1 章：概述
- 课程概述及学习建议
- Elasticsearch 简介及其发展历史
- Elastic Stack 家族成员其应用场景
### 第 2 章：安装上手
Elasticsearch 的安装与简单配置
Kibana 的安装与界面快速浏览
在 Docker 容器中运行 Elasticsearch，Kibana 和 Cerebro
Logstash 安装与导入数据
### 第 3 章：Elasticsearch 入门
- 基本概念（1）：索引，文档和 REST API
- 基本概念（2）：节点，集群，分片及副本
- 文档的基本 CRUD 与批量操作
- 倒排索引入门
- 通过分析器进行分词
- Search API 概览
- URI Search 详解
- Request Body 与 Query DSL 简介
- Query String & Simple Query String 查询
- Dynamic Mapping 和常见字段类型
- 显式 Mapping 设置与常见参数介绍
- 多字段特性及 Mapping 中配置自定义 Analyzer
- Index Template 和 Dynamic Template
- Elasticsearch 聚合分析简介
- 第一部分总结
## 第二部分：深入了解 Elasticsearch
### 第 4 章：深入搜索
- 基于词项和基于全文的搜索
- 结构化搜索
- 搜索的相关性算分
- Query & Filtering 与多字符串多字段查询
- 单字符串多字段查询：Dis Max Query
- 单字符串多字段查询：Multi Match
- 多语言及中文分词与检索
- Space Jam，一次全文搜索的实例 
- 使用 Search Template 和 Index Alias 查询
- 综合排序：Function Score Query 优化算分
- Term & Phrase Suggester
- 自动补全与基于上下文的提示
- 配置跨集群搜索
### 第 5 章：分布式特性及分布式搜索的机制
- 集群分布式模型及选主与脑裂问题
- 分片与集群的故障转移
- 文档分布式存储
- 分片及其生命周期
- 剖析分布式查询及相关性算分
- 排序及 Doc Values & Fielddata
- 分页与遍历：From, Size, Search After & Scroll API
- 处理并发读写操作
### 第 6 章：深入聚合分析
- Bucket & Metric 聚合分析及嵌套聚合
- Pipeline 聚合分析
- 作用范围与排序
- 聚合分析的原理及精准度问题
### 第 7 章：数据建模
- 对象及 Nested 对象
- 文档的父子关系
- Update By Query & Reindex API
- Ingest Pipeline & Painless Script 
- Elasticsearch 数据建模最佳实践
- 第二部分总结回顾
## 第三部分：管理 Elasticsearch 集群
### 第 8 章：保护你的数据
- 集群身份认证与用户鉴权
- 集群内部安全通信
- 集群与外部间的安全通信
### 第 9 章：水平扩展 Elasticsearch 集群
- 常见的集群部署方式
- Hot & Warm 架构与 Shard Filtering
- 如何对集群进行容量规划
- 分片设计及管理
- 在共有云上管理与部署 Elasticsearch 集群
- 在私有云上管理 Elasticsearch 集群的一些方法
### 第 10 章：生产环境中的集群运维
- 集群健康与问题排查
- 生产环境常用配置与上线清单
- 监控 Elasticsearch 集群
- 诊断集群的潜在问题  
- 解决集群 Yellow 与 Red 的问题
- 集群压力测试
- 段合并优化及注意事项
- 缓存及使用 Breaker 限制内存使用
- 一些运维的相关建议
### 第 11 章：索引生命周期管理
- 使用 Shrink 与 Rollover API 有效管理时间序列索引
- 索引全生命周期管理及工具介绍   
## 第四部分：利用 ELK 做大数据分析
### 第 12 章：用 Logstash 和 Beats 构建数据管道
- Logstash 入门及架构介绍
- Beats 介绍
### 第 13 章：用 Kibana 进行数据可视化分析
- 使用 Index Pattern 配置数据
- 使用 Kibana Discover 探索数据
- 基本可视化组件介绍
- Visual Builder 介绍 
- 构建 Dashboard  
## 第 14 章：探索 X-Pack 套件
- 用 Monitoring 和 Alerting 监控 Elasticsearch 集群
- 用 APM 进行程序性能监控
- 用机器学习实现时序数据的异常检测
- 用 ELK 进行日志管理
- 用 Canvas 做数据演示
- 用 Graph 进行数据分析
- 用 Timelion 分析时序型数据
## 第五部分：应用实战工作坊  
### 实战 1：电影搜索服务
- 项目需求分析及架构设计
- 将音乐数据导入 Elasticsearch
- 搭建你的电影搜索服务   
### 实战 2：Stackoverflow 用户调查问卷分析
- 需求分析及架构设计
- 数据 Extract & Enrichment
- 构建 Insights Dashboard
### 备战：Elastic 认证
- Elastic 认证介绍
- 考点梳理
