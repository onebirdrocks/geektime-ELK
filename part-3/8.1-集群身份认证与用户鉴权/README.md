# 集群身份认证与用户鉴权
- 如何为集群启用X-Pack Security
- 如何为内置用户设置密码
- 设置 Kibana与ElasticSearch通信鉴权
- 使用安全API创建对特定索引具有有限访问权限的用户

This tutorial involves a single node cluster, but if you had multiple nodes, you would enable Elasticsearch security features on every node in the cluster and configure Transport Layer Security (TLS) for internode-communication, which is beyond the scope of this tutorial. By enabling single-node discovery, we are postponing the configuration of TLS. For example, add the following setting:

discovery.type: single-node

## 课程demo
```
#启动单节点
bin/elasticsearch -E node.name=node0 -E cluster.name=geektime -E path.data=node0_data -E http.port=9200 -E xpack.security.enabled=true

#使用Curl访问ES，或者浏览器访问 “localhost:9200/_cat/nodes?pretty”。返回401错误
curl 'localhost:9200/_cat/nodes?pretty'

#运行密码设定的命令，设置ES内置用户及其初始密码。
bin/elasticsearch-setup-passwords interactive

curl -u elastic 'localhost:9200/_cat/nodes?pretty'

#设置 ES与Kibana之间的鉴权通信
./bin/kibana-keystore create

# 运行下面命令。按照提示，输入“kibana”
./bin/kibana-keystore add elasticsearch.username
#运行后，输入之前为kibana所设置的密码
./bin/kibana-keystore add elasticsearch.password

#启动。使用用户名，elastic，密码elastic
./bin/kibana


POST orders/_bulk
{"index":{}}
{"product" : "1","price" : 18,"payment" : "master","card" : "9876543210123456","name" : "jack"}
{"index":{}}
{"product" : "2","price" : 99,"payment" : "visa","card" : "1234567890123456","name" : "bob"}


#create a new role named read_only_orders, that satisfies the following criteria:
#The role has no cluster privileges
#The role only has access to indices that match the pattern sales_record
#The index privileges are read, and view_index_metadata
Using the Security API,


#create sales_user that satisfies the following criteria:
#Password is elastic
#The name of the user is "Order Viewer"
# Use your own email address
# Assign the user to two roles: read_only_orders and kibana_user
Using the Security API, create a new user named


#验证权限,可以执行
POST orders/_search
{}

#验证权限,报错
POST orders/_bulk
{"index":{}}
{"product" : "1","price" : 18,"payment" : "master","card" : "9876543210123456","name" : "jack"}
{"index":{}}
{"product" : "2","price" : 99,"payment" : "visa","card" : "1234567890123456","name" : "bob"}


```
