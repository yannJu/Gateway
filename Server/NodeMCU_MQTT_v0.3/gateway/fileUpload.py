import requests

def fileUpload(file_path, upload_url):
    file_name = file_path.split('/')[-1]
    
    data = {
        "file_name" : file_name
    }
    files = {
        "sec_file" : open(file_path, "rb")
    }
    
    response = requests.post(upload_url, data = data, files = files)
    
    msg = response.json()
    if msg["result"] == "success": print("Upload Success!")
    else: print("Upload Fail . . .")