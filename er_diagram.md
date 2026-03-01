# 📊 ER Diagram - File Storage

USERS
- user_id (PK)
- email

FILES
- file_id (PK)
- owner_id (FK)
- filename
- version

FILE_CHUNKS
- chunk_id (PK)
- file_id (FK)
- chunk_order
- storage_node_id

Relationships:

User 1 → N Files  
File 1 → N File Chunks
