from BeanObject import BeanObject
from DataAccessObject import DataAccessObject


class ParseMultipleCSVFile:
    def __init__(self):
        print("This is non parametrized constructor from ParseCSVFile ")

    def parseCSVFileData(self, list):
        beanObject = BeanObject()
        dataAccessObject = DataAccessObject()
        count = -1
        for index, line1 in enumerate(list[++count].split(',')):
            if index == 0:
                print ("**********")
                setattr(beanObject, beanObject.id, line1)
                print(getattr(beanObject, beanObject.id))
                print ("**********")
            elif index == 1:
                setattr(beanObject, beanObject.name, line1)
            elif index == 2:
                setattr(beanObject, beanObject.street, line1)
            elif index == 3:
                setattr(beanObject, beanObject.city, line1)
            elif index == 4:
                setattr(beanObject, beanObject.zip, line1)
            else:
                setattr(beanObject, beanObject.state, line1)
            dataAccessObject.insertDataInMongoDB(beanObject)
