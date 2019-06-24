import requests
import json

indexName ="tmdb"

def extract():
    f = open('./tmdb.json')
    if f:
         return json.loads(f.read());        
    return {}


def reindex(analysisSettings={}, mappingSettings={}, movieDict={}):
    settings = { 
        "settings": {
            "number_of_shards": 1, 
            "index": {
                "analysis" : analysisSettings, 
            }}}

    if mappingSettings:
        settings['mappings'] = mappingSettings 

    resp = requests.delete("http://localhost:9200/"+indexName) #D
    resp = requests.put("http://localhost:9200/"+indexName+"/_doc", 
                        data=json.dumps(settings))

    bulkMovies = ""
    print "building..."
    for id, movie in movieDict.iteritems(): 
        addCmd = {"index": {"_index": indexName, 
                            "_type": "_doc",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    print "indexing..."
    resp = requests.post("http://localhost:9200/_bulk", headers={"content-type":"application/json"}, data=bulkMovies)
    print resp.content



def main():
    movieDict = extract()
    reindex(movieDict=movieDict)
  
if __name__== "__main__":
  main()    