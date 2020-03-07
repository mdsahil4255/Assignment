# inserting data in MongoDB
from pymongo import MongoClient, collection

from BeanObject import BeanObject


class DataAccessObject:
    def __init__(self):
        print("This is non parametrized constructor from DataAcessObject ")

    def insertDataInMongoDB(self, beanObject=BeanObject()):
        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

            # database
        db = conn.database

        # Created or Switched to collection names: my_gfg_collection
        collections = db.my_gfg_collection

        employee = {"id": getattr(beanObject, beanObject.id), "name": getattr(beanObject, beanObject.name),
                    "street": getattr(beanObject, beanObject.street),
                    "city": getattr(beanObject, beanObject.city), "zip": getattr(beanObject, beanObject.zip),
                    "state": getattr(beanObject, beanObject.state)}

        # Insert Data
        result = collection.insert_one(employee)

        print("Data inserted with record ids", result)

        # Printing the data inserted
        cursor = collections.find()
        for record in cursor:
            print(record)
