import hashlib
import time
from typing import Dict, Optional, List

class S3MockClient:
    def __init__(self, bucket_name: str = "portfolio-bucket"):
        self.bucket_name = bucket_name
        self.objects: Dict[str, dict] = {}

    def put_object(self, key: str, data: bytes, content_type: str = "application/octet-stream") -> dict:
        etag = hashlib.md5(data).hexdigest()
        obj = {
            "key": key,
            "size": len(data),
            "content_type": content_type,
            "etag": etag,
            "last_modified": time.time(),
            "data": data
        }
        self.objects[key] = obj
        return {"ETag": etag, "Key": key, "Bucket": self.bucket_name}

    def get_object(self, key: str) -> Optional[dict]:
        return self.objects.get(key)

    def list_objects(self, prefix: str = "") -> List[str]:
        return [k for k in self.objects.keys() if k.startswith(prefix)]

    def delete_object(self, key: str) -> bool:
        return self.objects.pop(key, None) is not None
