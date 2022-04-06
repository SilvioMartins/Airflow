import win32com.client as win32
import pandas as pd
from datetime import datetime

class data_transform:
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


    def extract(self):
        DFrame = pd.DataFrame()
        tabela = win32.gencache.EnsureDispatch('Excel.Application')
        tabela.Visible = True
        wb = tabela.Workbooks.Open(self._file_name)