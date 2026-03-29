import os
import requests
import tarfile   # tar 压缩文件处理库
from pathlib import Path

def download():

    
        # __file__ : D:\Study\GLA\G-Designer\demo.py
        # __file__[0]: D
        # os.path.split(__file__) : ('D:\\Study\\GLA\\G-Designer', 'demo.py')
        # os.path.split(__file__)[0] : D:\Study\GLA\G-Designer

    
    # 当前脚本所在的绝对目录路径 ，可以直接用 os.path.dirname(__file__) 获取
    this_file_path = os.path.split(__file__)[0]
    # this_file_path = os.path.dirname(__file__)
    this_file_path = Path(this_file_path).as_posix()
    tar_path = os.path.join(this_file_path, "data.tar")
    # tar_path = Path(tar_path).as_posix()
    print('begining ')
    if not os.path.exists(tar_path):
        print('tar_path not exists, downloading...')
        url = "https://people.eecs.berkeley.edu/~hendrycks/data.tar"
        print(f"Downloading {url}")
        r = requests.get(url, allow_redirects=True) # requests.get() 发送 GET 请求下载文件
        
        with open(tar_path, 'wb') as f:
            # 'wb' = write binary，以二进制写入模式保存文件
            f.write(r.content)
        print(f"Saved to {tar_path}")

    data_path = os.path.join(this_file_path, "data")
    if not os.path.exists(data_path):
        tar = tarfile.open(tar_path)
        tar.extractall(this_file_path) # 解压到脚本所在目录
        tar.close()
        print(f"Saved to {data_path}")


if __name__ == "__main__":
    download()
