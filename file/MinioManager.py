from minio import Minio
from minio.deleteobjects import DeleteObject
import os

class MinioManager:
    def __init__(self,bucket_name="langchain-test-bucket",host="127.0.0.1:9000",access_key="",secret_key=""):
        self.bucket_name = bucket_name
        self.client = Minio(host,
            access_key=access_key,
            secret_key=secret_key,
            secure=False
        )

    def put_object(self,file_path,file_name):
        self.client.fput_object(
            self.bucket_name, file_name, file_path,
        )

    def put_stream_object(self,file_obj:object,file_length):
        self.client.put_object(
            bucket_name=self.bucket_name,
            object_name=file_obj.filename,
            data=file_obj.stream,
            length=file_length,
            content_type=file_obj.content_type
        )

    def list_objects(self) -> list:
        objects = self.client.list_objects(self.bucket_name)
        return objects

    def delete_object(self,object):
        self.client.remove_object(self.bucket_name, object)

    def delete_objects(self,objects:list):
        delete_list = [DeleteObject(obj) for obj in objects]
        errors = self.client.remove_objects(
            self.bucket_name,
            delete_list,
        )
        for error in errors:
            print(f"❌ 删除失败: {error}")

    def get_object(self,file_name):
        download_dir = r"D:\STUDY\CloudComputing\Essential\langchain\file\filestorage"
        file_path = os.path.join(download_dir, file_name)
        self.client.fget_object(self.bucket_name, file_name, file_path)
        return file_path