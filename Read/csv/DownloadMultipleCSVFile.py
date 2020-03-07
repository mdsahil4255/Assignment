import os
import requests
from time import time
from multiprocessing.pool import ThreadPool
from ReadMultipleCSVFile import ReadMultipleCSVFile


class DownloadMultipleCSVFile:
    def __init__(self):
        print("This is non parametrized constructor from DownloadMultipleCSVFile ")

    def url_response(url):
        path, url = url

        r = requests.get(url, stream=True)

        with open(path, 'wb') as f:
            for ch in r:
                f.write(ch)

    urls = [("file1", "url1"),
            ("file2", "url2"),
            ("file3", "url3"),
            ("file4", "url4"),
            ("file5", "url5"),
            ("file6", "url6"),
            ("file7", "url7"),
            ("file8", "url8")]
    start = time()
    # for x in urls:
    #     url_response(x)
    ThreadPool(9).imap_unordered(url_response, urls)
    print(time() - start)
    readMultipleCSVFile = ReadMultipleCSVFile()
    readMultipleCSVFile.readCSVFile()
