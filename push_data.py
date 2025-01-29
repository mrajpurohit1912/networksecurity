import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

import certifi
ca = certifi.where

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,path):
        try:
            df = pd.read_csv(path)
            df.reset_index(drop=True,inplace=True)

            data = list(json.loads(df.T.to_json()).values())
            return data
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,db_name,collection_name):
        try:
            self.database = db_name
            self.collection = collection_name
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == "__main__":
    #data_path = "C:\\code\\learning\\udemy_projects\\networksecurity\\Network_Data\\`phisingData.csv"
    data_path = "Network_Data\\phisingData.csv"
    DATABASE = "MAHAVIRDB"
    Collection = "MAHAVIRCOLLECTION"

    obj = NetworkDataExtract()
    records = obj.csv_to_json_converter(data_path)
    if records != None:
        logging.info("Data converted to records")
    
    
    lent_records = obj.insert_data_mongodb(records=records,db_name=DATABASE,collection_name=Collection)

    logging.info(f"{lent_records} inserted in Mongo DB")