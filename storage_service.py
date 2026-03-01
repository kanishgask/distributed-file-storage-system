import hashlib
from collections import defaultdict

class StorageNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.storage = {}

    def store_chunk(self, chunk_id, data):
        self.storage[chunk_id] = data

    def get_chunk(self, chunk_id):
        return self.storage.get(chunk_id)


class DistributedStorage:
    def __init__(self, replication_factor=2):
        self.nodes = []
        self.replication_factor = replication_factor

    def add_node(self, node):
        self.nodes.append(node)

    def _hash(self, key):
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)

    def _get_nodes_for_chunk(self, chunk_id):
        index = self._hash(chunk_id) % len(self.nodes)
        selected = []
        for i in range(self.replication_factor):
            selected.append(self.nodes[(index + i) % len(self.nodes)])
        return selected

    def store(self, chunk_id, data):
        nodes = self._get_nodes_for_chunk(chunk_id)
        for node in nodes:
            node.store_chunk(chunk_id, data)

    def retrieve(self, chunk_id):
        nodes = self._get_nodes_for_chunk(chunk_id)
        for node in nodes:
            data = node.get_chunk(chunk_id)
            if data:
                return data
        return None


# Demo
if __name__ == "__main__":
    ds = DistributedStorage(replication_factor=2)

    ds.add_node(StorageNode("A"))
    ds.add_node(StorageNode("B"))
    ds.add_node(StorageNode("C"))

    ds.store("chunk1", "Hello Distributed World")

    print(ds.retrieve("chunk1"))
