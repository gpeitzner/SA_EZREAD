
import boto3
import base64
import tempfile
import uuid
import creds
import imghdr


class Bucket:
    """Clase para acceso fácil al cliente de S3 de AWS"""
    BUCKET_NAME = creds.s3_bucket_name

    def __init__(self):
        self.CLIENT = boto3.client(
            's3',
            aws_access_key_id=creds.bucket['access-key-id'],
            aws_secret_access_key=creds.bucket['secret-access-key'],
        )

    def delete_picture(self, key):
        response = self.CLIENT.delete_object(
            Bucket=self.BUCKET_NAME,
            Key=key,
        )
        return response

    def write_image(self, user, image64, ext):
        """Guardar imagen de profesor en bucket"""
        file_content = base64.b64decode(image64)
        for tf in imghdr.tests:
            res = tf(file_content, None)
            if res:
                break
        print("Extension OR Type of the Image =====>", res)
        ext = res
        file_path = '{}-{}.{}'.format(user.replace(' ',
                                      '_'), uuid.uuid4(), ext)

        with tempfile.TemporaryFile(suffix='.{}'.format(ext)) as f:
            f.write(file_content)
            f.seek(0)

            response = self.CLIENT.put_object(
                Body=f,
                Bucket=self.BUCKET_NAME,
                Key=file_path,
                ContentType='image/{}'.format(ext)
            )

        # print(response)
        return file_path

    def get_image64(self, image_path):
        get = self.CLIENT.get_object(
            Bucket=self.BUCKET_NAME,
            Key=image_path
        )
        content_bytes = get['Body'].read()
        base64_bytes = base64.b64encode(content_bytes)
        return {'base64': base64_bytes.decode('ascii'), 'type': get['ContentType']}
