import requests

file_name = "20230406_15_03.mp4"
file_path = file_name
data = {
    "file_name" : file_name
}

files = {
    "sec_file" : open(file_path, "rb")
}

response = requests.post("http://172.20.10.5:8000/iot/upload/", data=data, files=files)

msg = response.json()
if msg['result'] == 'success': print('Upload Success!')
else: print('Upload Fail. .')
