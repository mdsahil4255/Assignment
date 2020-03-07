import pandas as pd
import glob
from ParseMultipleCSVFile import ParseMultipleCSVFile


class ReadMultipleCSVFile:
    def __init__(self):
        print("This is non parametrized constructor from ReadMultipleCSVFile ")

    def  readCSVFile(self):

        path = r'C:\Users\sahil\PycharmProjects\Read\csv'  # use your path
        all_files = glob.glob(path + "/*.csv")
        list = []
        count = -1
        parseMultipleCSVFile = ParseMultipleCSVFile()
        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            list.append(df)
        parseMultipleCSVFile.parseCSVFileData(list)
        print('***************************')
    # frame = pd.concat(li, axis=0, ignore_index=True)
