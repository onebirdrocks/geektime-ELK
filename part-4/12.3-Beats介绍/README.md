# Beats介绍
## 课程demo
```

##
# 查看 packetbeat 模块
# 设置 packetbeat 的mysql 模块
# 启动运行
#
./metricbeat modules list
./metricbeat modules enable mysql
./metricbeat setup --dashboards

# 安装mysql
create database db_example
use db_example;
show tables;
select * from user

curl localhost:8080/demo/add -d name=First -d email=first@xyz.com
curl localhost:8080/demo/add -d name=Second -d email=second@xyz.com
curl localhost:8080/demo/add -d name=Third -d email=thrid@xyz.com



# 配置 packetbeat
# 启动
sudo chown root packetbeat.yml
sudo ./packetbeat


# 查看所有 Filebeat 模块
# 查看所有的modules
./filebeat modules list

#
./filebeat modules enable mysql

```
