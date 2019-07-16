
## demos
```
DELETE /employees
PUT /employees/
{
  "mappings" : {
      "properties" : {
        "age" : {
          "type" : "integer"
        },
        "gender" : {
          "type" : "keyword"
        },
        "job" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 50
            }
          }
        },
        "name" : {
          "type" : "keyword"
        },
        "salary" : {
          "type" : "integer"
        }
      }
    }
}

PUT /employees/_bulk
{ "index" : {  "_id" : "1" } }
{ "name" : "Perkins","age":32,"job":"Product Manager","gender":"male","salary":35000 }
{ "index" : {  "_id" : "2" } }
{ "name" : "Underwood","age":41,"job":"Dev Manager","gender":"male","salary": 50000}
{ "index" : {  "_id" : "3" } }
{ "name" : "Tran","age":25,"job":"Web Designer","gender":"male","salary":18000 }
{ "index" : {  "_id" : "4" } }
{ "name" : "Rivera","age":26,"job":"Web Designer","gender":"male","salary": 22000}
{ "index" : {  "_id" : "5" } }
{ "name" : "Graham","age":25,"job":"QA","gender":"male","salary":15000 }
{ "index" : {  "_id" : "6" } }
{ "name" : "Shaw","age":31,"job":"QA","gender":"male","salary": 25000}
{ "index" : {  "_id" : "7" } }
{ "name" : "Byrd","age":27,"job":"QA","gender":"male","salary":20000 }
{ "index" : {  "_id" : "8" } }
{ "name" : "Foster","age":27,"job":"Java Programmer","gender":"male","salary": 20000}
{ "index" : {  "_id" : "9" } }
{ "name" : "Gregory","age":32,"job":"Java Programmer","gender":"male","salary":22000 }
{ "index" : {  "_id" : "10" } }
{ "name" : "Bryant","age":38,"job":"Java Programmer","gender":"male","salary": 2500}
{ "index" : {  "_id" : "11" } }
{ "name" : "Reese","age":36,"job":"Java Programmer","gender":"male","salary":28000 }
{ "index" : {  "_id" : "12" } }
{ "name" : "Mcdonald","age":31,"job":"Java Programmer","gender":"male","salary": 32000}
{ "index" : {  "_id" : "13" } }
{ "name" : "Hansen","age":30,"job":"Java Programmer","gender":"male","salary":30000 }
{ "index" : {  "_id" : "14" } }
{ "name" : "Marshall","age":32,"job":"Javascript Programmer","gender":"male","salary": 25000}
{ "index" : {  "_id" : "15" } }
{ "name" : "King","age":33,"job":"Java Programmer","gender":"male","salary":28000 }
{ "index" : {  "_id" : "16" } }
{ "name" : "Mccarthy","age":21,"job":"Javascript Programmer","gender":"male","salary": 16000}
{ "index" : {  "_id" : "17" } }
{ "name" : "Goodwin","age":25,"job":"Javascript Programmer","gender":"male","salary": 16000}
{ "index" : {  "_id" : "18" } }
{ "name" : "Padilla","age":22,"job":"Javascript Programmer","gender":"male","salary": 19000}
{ "index" : {  "_id" : "19" } }
{ "name" : "Boone","age":30,"job":"DBA","gender":"male","salary": 30000}
{ "index" : {  "_id" : "20" } }
{ "name" : "Reyes","age":31,"job":"DBA","gender":"male","salary": 25000}



POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"job.keyword"
      }
    }
  }
}

# 对 Text 字段进行 terms 分词，失败
POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"job"
      }
    }
  }
}

# 对 Text 字段打开 fielddata，支持terms aggregation
PUT employees/_mapping
{
  "properties" : {
    "job":{
       "type":     "text",
       "fielddata": true
    }
  }
}


# 对 Text 字段进行 terms 分词。分词后的terms
POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"job"
      }
    }
  }
}


POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"gender"
      }
    }
  }
}


POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"age"
      }
    }
  }
}

POST employees/_search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "terms": {
        "field":"job.keyword"
      }
      ,
    "aggs": {
      "salary": {
          "stats" : { "field" : "salary" }
      }
    }
    }
  }
}

```

## 相关阅读
- https://www.elastic.co/guide/en/elasticsearch/reference/7.1/search-aggregations-metrics.html
- https://www.elastic.co/guide/en/elasticsearch/reference/7.1/search-aggregations-bucket.html
