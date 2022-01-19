import pymongo
from app.database.secrets import MONOGO_PASSWORD

class MongoDatabase(object):
  def __init__(self):
    database = "Inventory"
    try:
        client = pymongo.MongoClient(f'mongodb+srv://damilola_2022:{MONOGO_PASSWORD}@cluster0.rzgfq.mongodb.net/{database}?retryWrites=true&w=majority', serverSelectionTimeoutMS = 1000)
        client.server_info() ## trigger exception if cannot connect to db
        self.db = client.API
    except:
        print("Error Cannot Connect to database")

  def create_item(self, item):
    """
    Calls database to create new item

    :param data: data for new item
    :return: id of new item
    """ 
    try:
      dbResponse = self.db.inventory.insert_one(item)
      return dbResponse.inserted_id
    except Exception as ex:
      print(ex)

  def update_item(self, id, data):
    """
    Calls database to update a given item

    :param id: the id of the item to update
    :param data: data to add/change in item
    :return: a tuple of ints on if the item was found and modified 
    """
    try:
      dbResponse = self.db.inventory.update_one(id, data)
      return (dbResponse.matched_count, dbResponse.modified_count) #The number of documents/items that were matched
    except Exception as ex:
      print(ex)

  def delete_item(self, id):
    """
    Calls database to delete a given item

    :param id: the id of the item to delete
    :return: a int of if an item was deleted
    """ 
    try:
      dbResponse = self.db.inventory.delete_one(id)
      return dbResponse.deleted_count  #The number of documents/items that were deleted
    except Exception as ex:
      print(ex)

  def get_items(self, id={}):
    """
    Calls database to gets items

    :param id: id of a given item or {} if getting all items
    :return: a list of all the items 
    """ 
    try:
      item = self.db.inventory.find(id)
      return item
    except Exception as ex:
      print(ex)
