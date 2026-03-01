# 📦 Distributed File Storage System

> Day 7 – Advanced Distributed Systems Design

---

## 📌 Problem Statement

Design a scalable file storage system like Dropbox or Google Drive.

System should:

- Upload files
- Download files
- Handle large files (GBs)
- Support file versioning
- Scale to millions of users
- Ensure high durability

---

# 🎯 Functional Requirements

- Upload file
- Download file
- Delete file
- File version history
- File sharing (optional)

---

# ⚙️ Non-Functional Requirements

- Highly durable (99.999%)
- High availability
- Low latency metadata access
- Horizontal scalability
- Fault tolerance

---

# 📊 Capacity Estimation (Example)

Assume:
- 100M users
- Average file size = 10MB
- 50 uploads per user yearly

Storage requirement ≈ 50PB+

Clearly distributed storage needed 🚀

---

# 🧠 High-Level Architecture

Client
   ↓
API Gateway
   ↓
Metadata Service
   ↓
Chunking Service
   ↓
Storage Nodes
   ↓
Distributed Database (Metadata)

---

# 🔑 Core Design Concepts

✔ File chunking (e.g., 5MB chunks)  
✔ Replication factor (3x)  
✔ Metadata separation  
✔ Consistent hashing  
✔ Background compaction  
✔ Version control  

---

# 🏆 Key Concepts Demonstrated

- Distributed storage design
- Data partitioning
- Replication strategy
- Scalability planning
- Fault tolerance
