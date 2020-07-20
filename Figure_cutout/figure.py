# 需要提前安装requests库，pip install requests

import requests
import os

API_ENDPOINT = 'https://api.remove.bg/v1.0/removebg'
ITEM_PATH = r'file_path'  # file_path为去除背景的文件路径，例c:\Users\Desktop\image

path_list = [filename for filename in os.listdir(ITEM_PATH) if filename.endswith('jpg') or filename.endswith('png')]

for file_name in path_list:
    response = requests.post(
        API_ENDPOINT,
        files={'image_file': open(r'{}\{}'.format(ITEM_PATH, file_name), 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},  # 需要在removebg注册，获取API_KEY
    )
    if response.status_code == requests.codes.ok:
        with open(r'{}\no-bg_{}.png'.format(ITEM_PATH, file_name), 'wb') as out:
            out.write(response.content)
            # 去除下列两行注释，可在去除背景后自动打开图片
            # fileDir = r'{}\no-bg_{}.png'.format(ITEM_PATH, file_name)
            # os.startfile(fileDir)  
    else:
        print("Error:", response.status_code, response.text)
        
