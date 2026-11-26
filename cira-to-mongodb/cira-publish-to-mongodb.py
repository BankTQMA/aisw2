from pymongo import MongoClient
from datetime import datetime


# Function to extract data from the request
def getReqData(req):
    # Implement your logic to extract data from the request
    pass


# Function to create a response data
def makeRespData(payload, img):
    # Implement your logic to create a response data
    pass


url = "mongodb://localhost:27017"
db_name = "CiRA_to_MongoDB_Demonstration"
collection_name = "Turtle"


def insert_data_into_mongodb(data):
    with MongoClient(url) as client:
        try:
            print("Connected to MongoDB successfully")
            db = client[db_name]
            collection = db[collection_name]
            result = collection.insert_one(data)
            print("Insertion successful. Inserted document ID:", result.inserted_id)
        except Exception as e:
            print(f"An error occurred: {e}")


# Function to handle request
def handle_request(req):
    payload, img = getReqData(req)

    # Implement your process here
    # objects = payload['DeepDetect']['objects']
    resp = makeRespData(payload, img)
    # Example data to insert into MongoDB
    data_to_insert = {
        "timestamp": datetime.now(),  # Include the current datetime
        "Payload. ": payload,  # Or payload['DeepDetect'] / payLoad['DeepClassif']
    }

    insert_data_into_mongodb(data_to_insert)
    return resp
