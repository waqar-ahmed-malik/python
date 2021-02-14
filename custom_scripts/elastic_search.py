from elasticsearch import Elasticsearch


class ElasticSearch:
    def __init__(self, username: str, password: str, host: str, port: str, timeout: int = 1000) -> None:
        self.connection = Elasticsearch("{}:{}@{}:{}".format(username, password, host, port), timeout=timeout)

    def get_data_from_index(self, index: str, batch_size: int, query: dict, scroll_id: str = None) -> str:
        if scroll_id is None:
            es_data = self.connection.search(index=index, scroll='2m', size=batch_size, body=query)
            scroll_id = es_data['_scroll_id']
            documents = es_data['hits']['hits']
            return {
                "documents": documents,
                "scroll_id": scroll_id
            }
        else:
            es_data = self.connection.scroll(scroll_id=scroll_id, scroll='2m')
            scroll_id = es_data['_scroll_id']
            documents = es_data['hits']['hits']
            return {
                "documents": documents,
                "scroll_id": scroll_id
            }
