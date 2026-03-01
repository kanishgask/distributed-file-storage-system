CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE files (
    file_id UUID PRIMARY KEY,
    owner_id UUID REFERENCES users(user_id),
    filename VARCHAR(255),
    version INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE file_chunks (
    chunk_id UUID PRIMARY KEY,
    file_id UUID REFERENCES files(file_id),
    chunk_order INT,
    storage_node_id VARCHAR(50)
);
