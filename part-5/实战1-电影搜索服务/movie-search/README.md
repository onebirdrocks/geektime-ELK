课程demo
```
安装配置
app-search.yml:
allow_es_settings_modification: true

#Allow Elasticsearch to create indexes automatically: Add the following line #within either Elasticsearch cluster settings or elasticsearch.yml:

action.auto_create_index: ".app-search-*-logs-*,-.app-search-*,+*"

```