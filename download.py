import requests
import os
import time
import sys
import gzip
import zipfile


class DownloadSegmentfault():
  '''
    初始化类文件
  '''

  def __init__(self):
    self.header = {"Accept-Encoding": "identity"}

  '''
    执行下载
  '''

  def download(self, file_url, file_name):
    have_length = True
    start = time.time()
    # 下载文件名
    if file_name is None:
      file_name = os.path.basename(file_url)
    print('downloading file %s' % file_name)
    temp_size = 0  # 已经下载文件大小
    res = requests.get(file_url, headers=self.header, stream=True)
    chunk_size = 1024  # 每次下载数据大小
    if ('Content-Length' in res.headers.keys()):
      total_size = int(res.headers.get("Content-Length"))
    else:
      # 响应头无 Content-Length
      have_length = False
      # 默认1G文件大小
      total_size = 1 * 1024 * 1024 * 1024

    if res.status_code == 200:
      if have_length:
        print('[文件大小]:%0.2f MB' % (total_size / chunk_size / 1024))
      else:
        print('[文件大小]:未知')
      # 保存下载文件
      with open(file_name, 'wb') as f:
        for chunk in res.iter_content(chunk_size=chunk_size):
          if chunk:
            temp_size += len(chunk)
            f.write(chunk)
            f.flush()
            #############花哨的下载进度部分###############
            done = int(50 * temp_size / total_size)
            # 相当于把每一行重新刷新一遍
            sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
            sys.stdout.flush()
      print()  # 避免上面\r 回车符，执行完后需要换行了，不然都在一行显示
      end = time.time()  # 结束时间
      print('全部下载完成!用时%.2f 秒' % (end - start))
    else:
      print(res.status_code)


if __name__ == '__main__':
  pre_train_url = 'https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip'
  final_train_model = 'https://doc-0o-14-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/rh15l8j636jjsptcdi1csm5efqo1c6ku/1550635200000/11180373435048558401/*/1QoCapWOlmgwjHWpozDn6wAo6QizKJjFu?e=download'
  down = DownloadSegmentfault()
  down.download(pre_train_url, 'chinese_L-12_H-768_A-12.zip')
  down.download(final_train_model, 'tmp.tgz')

