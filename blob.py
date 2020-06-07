import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    # print("Azure Blob storage v12 - Python quickstart sample")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # print(connect_str)
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "datasetcontainer" 

    # Create the container
    # container_client = blob_service_client.create_container(container_name)
    # Create a file in local data directory to upload and download
    local_path = "./"
    local_file_name = "a.txt"
    upload_file_path = os.path.join(local_path, local_file_name)


# Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
     # Instantiate a ContainerClient
    container_client = blob_service_client.get_container_client("datasetcontainer")
    # container_client.delete_blob("a.txt")

    # print("\nDeleting blob from Azure Storage:\n\t" + local_file_name)

    # print("\n\n Now, uploading to Azure Storage as blob:\n\t" + local_file_name)
  
# Upload the created /file
    # with open(upload_file_path, "rb") as data:
    #     blob_client.upload_blob(data)

    
# List the blobs in the container
    # blob_list = container_client.list_blobs()
    # print("\n----------List of blobs in the container ----------")
    # for blob in blob_list:
    #     print("----> " + blob.name)

    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)

    # with open(download_file_path, "wb") as download_file:
    #     download_file.write(blob_client.download_blob().readall())
    print("Deleting blob container...")
    container_client.delete_container()
  
except Exception as ex:
    print('Exception:')
    print(ex)