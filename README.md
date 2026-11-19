# ☁️ serverless-aws-s3-file-manager

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![AWS](https://img.shields.io/badge/Cloud-AWS_S3_API-orange?style=for-the-badge&logo=amazonaws)](storage/)

Cloud Object Storage Abstraction Layer with S3 compatibility, multipart upload simulation, and metadata indexing.

## Features
- **Object Storage Abstraction:** Standard S3 operations (`PutObject`, `GetObject`, `ListObjectsV2`).
- **Multipart Uploads:** High-reliability chunking for large datasets.
- **Content Integrity:** ETag MD5 verification matching AWS S3 standards.
