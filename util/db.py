from pymongo import MongoClient

uri = 'mongodb+srv://nsnandhaa1:40OPEueX4gtlcIJW@cluster0.5lplwtw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri)
database = client.get_database("zoho")
coll = database.get_collection("user")



def save_one(data):
    result = coll.insert_one(data)
    print(result)

    return result


def get_by_uid(uid):
    res = coll.find({uid})
    print(res)
    # return res

def check_username(username):
    res = coll.find({'username':username})
    return res[0]['_id']
    # return res[0]