from urllib.parse import urljoin
import requests
import urllib3
import sys
import os

class LockerClientException(Exception):
    pass


class LockerStat():
    def __init__(self, path):
        self.path = path
        self.basename = os.path.basename(path)
        
        self.mtime = None
        self.size = None
        self.type = None


    def __str__(self):
        return f'{self.path} {self.type} {self.size} {self.mtime}'

class LockerClient():
    
    def __init__(self, host, key, insecure=False):
        assert(host)
        self.host = host
        self.key = key
        self.verify = not insecure # do not verify ssl

        if not self.verify:
            print("Insecure mode!")
            urllib3.disable_warnings()

        if self.host.startswith('http://') or self.host.startswith('https://'):
            self.base_url = self.host
        else:
            self.base_url = f'https://{self.host}'

        self.app_url = urljoin(self.base_url, 'app/')

        self.headers = {
            'User-Agent': 'locker-admin/0.1',
            'X-API-KEY': self.key
        }

    def path_url(self, path):
        if path.startswith('/'):
            path = path[1:]

        return urljoin(self.app_url, path)

    def stat(self, path):

        url = self.path_url(path)
        r = requests.head(url, headers=self.headers, verify=self.verify)    
        # if r.status_code == 200:
        r.raise_for_status()
        st = LockerStat(path)
        st.type = r.headers['X-FileType']
        st.mtime = r.headers['X-FileMTime']
        st.size = r.headers['X-FileSize']
        return st
        #    raise LockerClientException(f"ERROR! stat for {url} returned HTTP code {r.status_code}")

    def get(self, path, stream=False):
        url = self.path_url(path)
        r = requests.get(url, headers=self.headers, stream=stream, verify=self.verify)    
        r.raise_for_status()
        return r
        # raise LockerClientException(f"ERROR! get for {url} returned HTTP code {r.status_code}")

    def put(self, path, data):
        url = self.path_url(path)
        r = requests.put(url, headers=self.headers, data=data, verify=self.verify)
        r.raise_for_status()
        return r

    def __str__(self):
        return 'Locker host:{} key:{}'.format(self.host, bool(self.key))



