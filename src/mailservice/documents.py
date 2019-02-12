from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index
from .models import Email
# Create a connection to ElasticSearch
connections.create_connection()


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
