

```

bin/elasticsearch -E node.name=node0 -E cluster.name=geektime -E path.data=node0_data -E http.port=9200 -E xpack.security.enabled=true -E xpack.security.transport.ssl.enabled=true -E xpack.security.transport.ssl.verification_mode=certificate -E xpack.security.transport.ssl.keystore.path=certs/elastic-stack-ca.p12 -E xpack.security.http.ssl.enabled=true -E xpack.security.http.ssl.keystore.path=certs/elastic-stack-ca.p12 -E xpack.security.http.ssl.truststore.path=certs/elastic-stack-ca.p12





```


# 相关阅读
- https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring-tls.html#tls-http
