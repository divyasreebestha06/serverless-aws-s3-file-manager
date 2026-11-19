import uuid
from storage.client import S3MockClient

class MultipartUploadManager:
    def __init__(self, s3_client: S3MockClient):
        self.client = s3_client
        self.active_uploads = {}

    def initiate_upload(self, key: str) -> str:
        upload_id = str(uuid.uuid4())
        self.active_uploads[upload_id] = {"key": key, "parts": {}}
        return upload_id

    def upload_part(self, upload_id: str, part_num: int, chunk: bytes):
        if upload_id not in self.active_uploads:
            raise ValueError("Invalid upload ID")
        self.active_uploads[upload_id]["parts"][part_num] = chunk

    def complete_upload(self, upload_id: str):
        if upload_id not in self.active_uploads:
            raise ValueError("Invalid upload ID")
        info = self.active_uploads.pop(upload_id)
        combined = b"".join(info["parts"][p] for p in sorted(info["parts"].keys()))
        return self.client.put_object(info["key"], combined)
