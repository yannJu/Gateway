import requests

# file_name = "20230406_15_03.mp4"
# file_path = file_name
# upload_url = "http://172.20.10.5:8000/iot/upload/"

def upload(file_path, upload_url):
    file_name = file_path.split('/')[-1]

    data = {
        "file_name" : file_name
    }
    files = {
        "sec_file" : open(file_path, "rb")
    }

    response = requests.post(upload_url, data=data, files=files)

    msg = response.json()
    if msg['result'] == 'success': print('Upload Success!')
    else: print('Upload Fail. .')