import pymongo

if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb+srv://mongo:mongo@cluster0.pcwyrxd.mongodb.net/?retryWrites=true&w=majority")
    # which db we want to use.
    db = client["blog"]
    # which collection we want to use.
    collections = db["test"]

    # Find all
    allData = collections.find()
    for data in allData:
        pass
        # print("data =",data)

    # find one
    oneData= collections.find_one({"title":"Post 1"})
    print("one data",oneData)

    # insert
    newData = collections.insert_one({"name":"Al fahim bin faruk","role":"Backend dev","Age":33})
    # insert many 
    newDataOfArr = collections.insert_many([
    {"name":"suhan","role":"Frontend dev","Age":53},
    {"name":"aldin","role":"UI dev","Age":53},
    {"name":"akib","role":"UX dev","Age":63},
    {"name":"zayn","role":"DB dev","Age":23}])

    # update
    dataToUpdate = collections.update_one({"name":"Al fahim bin faruk"},{"$set":{"role":"Backend,DevOPS,Security"}})

    # delete
    dataToDelete = collections.delete_one({"name":"Al fahim bin faruk"})

    # delete many
    manyDataToDelete = collections.delete_many({"name":"Al fahim bin faruk"})

    print("DB connected = ",db.list_collection_names())
