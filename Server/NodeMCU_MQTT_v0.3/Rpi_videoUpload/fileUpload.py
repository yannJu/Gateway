import requests

# file_name = "recored0.mp4"
# file_path = file_name
# upload_url = "http://172.20.10.5:8000/iot/upload/"
# INTRUSION_URL = "http://172.20.10.5:8000/iot/intrusion/"

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
    
def notify_instrusion():
    response = requests.get(INTRUSION_URL)
    res = response.json()
    
    if res['result'] == 'success': return True
    else: return False
