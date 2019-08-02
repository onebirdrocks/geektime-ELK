# 第二部分总结与测验
##课程demo
```
DELETE test
PUT test/_doc/1
{
  "content":"Hello World"
}

PUT test/_doc/2
{
  "content":"hello world"
}


POST test/_search
{
  "profile": "true",
  "query": {
    "match": {
      "content": "Hello World"
    }
  }
}

POST test/_search
{
  "profile": "true",
  "query": {
    "match": {
      "content.keyword": "Hello World"
    }
  }
}



POST test/_search
{
  "profile": "true",
  "query": {
    "term": {
      "content": "Hello World"
    }
  }
}

POST test/_search
{
  "profile": "true",
  "query": {
    "term": {
      "content.keyword": "Hello World"
    }
  }
}
```
