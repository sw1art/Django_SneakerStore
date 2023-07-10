from .models import Sneaker
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

@registry.register_document
class SneakerDocument(Document):
    class Index:
        name = 'sneakers'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Sneaker
        fields = {'title':{'fuzziness': 'AUTO'},}
