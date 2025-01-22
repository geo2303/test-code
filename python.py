import boto3
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    # Initialize an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to bucket {bucket_name} as {object_name}")
        return True
    except FileNotFoundError:
        print(f"File {file_name} not found")
        return False
    except NoCredentialsError:
        print("AWS credentials not available")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    # Define your parameters
    file_name = "example.txt"
    bucket_name = "my-example-bucket"

    # Upload the file
    success = upload_file_to_s3(file_name, bucket_name)

    if success:
        print("File uploaded successfully!")
    else:
        print("File upload failed!")

if __name__ == "__main__":
    main()
