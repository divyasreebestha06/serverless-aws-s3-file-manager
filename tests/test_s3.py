import unittest
from storage.client import S3MockClient
from storage.multipart import MultipartUploadManager

class TestS3Storage(unittest.TestCase):
    def setUp(self):
        self.s3 = S3MockClient("test-bucket")
        self.mp = MultipartUploadManager(self.s3)

    def test_put_and_get(self):
        res = self.s3.put_object("docs/test.txt", b"Hello Cloud!")
        self.assertIn("ETag", res)
        obj = self.s3.get_object("docs/test.txt")
        self.assertEqual(obj["data"], b"Hello Cloud!")

    def test_multipart_assembly(self):
        uid = self.mp.initiate_upload("large.dat")
        self.mp.upload_part(uid, 1, b"Part1-")
        self.mp.upload_part(uid, 2, b"Part2")
        self.mp.complete_upload(uid)
        obj = self.s3.get_object("large.dat")
        self.assertEqual(obj["data"], b"Part1-Part2")

if __name__ == "__main__":
    unittest.main()
