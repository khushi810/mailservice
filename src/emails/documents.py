""" Instructions
Run following command to start logstash process in order to send events to elastic search
sudo <path-to-logstash-bin> -f <path-to-repo>/mailservice/src/mailservice/logstash.conf
"""

from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index
from .models import Email
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


# Initialize elasticsearch instance
client = Elasticsearch()
my_search = Search(using=client)

# Create a connection to ElasticSearch
connections.create_connection()

# Index emails table
email   = Index('emails')

email.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@email.doc_type
class EmailDocument(DocType):

    class Meta:
        model = Email
        fields = ['email_to', 'cc', 'bcc', 'subject', 'body']



def search(subject):
    query = my_search.query("match", subject=subject)
    response = query.execute()
    return response
