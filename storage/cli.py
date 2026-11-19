from storage.client import S3MockClient

def main():
    s3 = S3MockClient()
    s3.put_object("resumes/divyasree.pdf", b"%PDF-mock-resume", "application/pdf")
    print("Bucket objects:", s3.list_objects("resumes/"))

if __name__ == "__main__":
    main()
