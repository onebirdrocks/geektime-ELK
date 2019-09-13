# 集群Backup & Restore
## 课程demo
```
PUT /_snapshot/my_fs_backup
{
    "type": "fs",
    "settings": {
        "location": "/Users/yiruan/geektime/mount/my_backup",
        "compress": true
    }
}


PUT /_snapshot/my_fs_backup/snapshot_5?wait_for_completion=true
DELETE /_snapshot/my_fs_backup/snapshot_2

GET /_snapshot/my_fs_backup/_all

GET /_snapshot/my_fs_backup/_current


POST /_snapshot/my_fs_backup/snapshot_1/_restore
{
  "indices": "testxxx",
  "index_settings": {
    "index.number_of_replicas": 5
  },
  "ignore_index_settings": [
    "index.refresh_interval"
  ]
}

GET testxxx/_settings

DELETE testxxx

GET testxxx

PUT /_snapshot/my_fs_backup/snapshot_3?wait_for_completion=true
{
  "indices": "testxxx",
  "ignore_unavailable": true,
  "include_global_state": false,
  "metadata": {
    "taken_by": "yiming",
    "taken_because": "backup before upgrading"
  }
}

```