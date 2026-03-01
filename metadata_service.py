import uuid

class MetadataService:

    def __init__(self):
        self.files = {}  # file_id -> metadata

    def create_file(self, filename, owner_id, chunks):
        file_id = str(uuid.uuid4())
        self.files[file_id] = {
            "filename": filename,
            "owner_id": owner_id,
            "chunks": chunks,
            "version": 1
        }
        return file_id

    def get_metadata(self, file_id):
        return self.files.get(file_id)

    def new_version(self, file_id, new_chunks):
        if file_id in self.files:
            self.files[file_id]["chunks"] = new_chunks
            self.files[file_id]["version"] += 1
