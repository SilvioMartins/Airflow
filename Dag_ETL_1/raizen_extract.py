import requests
import os

class base_extraxt:
    def __init__(self):
        self._url = None
        
        self._file_name = None

    def set_url(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def set_file_name(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def download_file(self):
        # Download the file from the URL to the specified file name.
        arquivo = requests.get(self._url, allow_redirects=True)
        open(self._file_name, 'wb').write(arquivo.content)

def extract_xls_origin(path_bronze_zone, file_dest_name):
    receiver = base_extraxt()
    receiver.set_url('https://github.com/raizen-analytics/data-engineering-test/raw/master/assets/vendas-combustiveis-m3.xls')
    receiver.set_file_name(file_dest_name)
    receiver.download_file()