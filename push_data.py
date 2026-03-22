import os
import sys
import json
from dotenv import load_dotenv

import certifi
import pymongo
import pandas as pd
import numpy as np

from networksecurity.logger import logging
from networksecurity.exception import CustomException


load_dotenv()

db_username = os.getenv("MONGODB_USERNAME")
db_password = os.getenv("MONGODB_PASSWORD")

uri = "mongodb+srv://{0}:{1}@cluster0.rqqgfao.mongodb.net/?appName=Cluster0".format(
    db_username,
    db_password
)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(uri)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise CustomException(e, sys)



if __name__=="__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "Netsec"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json_convertor(FILE_PATH)
    # print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records=records, database=DATABASE, collection=COLLECTION)
    print(no_of_records)