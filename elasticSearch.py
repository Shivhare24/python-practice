from elasticsearch import Elasticsearch
es = Elasticsearch(Host="http://127.0.0.1/", port=9200)
es = Elasticsearch()

#creating index
es.indices.create(index="first_index",ignore=400)

#check index
es.indices.exists(index="first_index")

#delete index
es.indices.delete(index="certificate")

#creating document data
doc1 = {"city":"New Delhi","country":"india"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country": "USA"}

#feeding document data to elastic search
es.index(index="cities",doc_type="places",id=1, body=doc3)

es.update(index='certificate', doc_type='certifcates', id=)

#search data with index
response = es.get(index="cities",doc_type="places",id=1)
response['_source']

#search data by query


