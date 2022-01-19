from database.db import MongoDatabase as db
from schema import InventorySchema
from bson.objectid import ObjectId
import csv

INVENTORY_INFO = ['_id','product_name', 'stock', 'warehouse', 'price']

class Service(object):
    def __init__(self):
        self.db = db()

    def create(self, data):
        """
        Creates new item

        :param data: data for new item
        :return: returns formatted data
        """ 
        self.db.create_item(data.data)
        return self.dump(data.data)

    def update(self, id, data):
        """
        Updates a given item

        :param id: the id of the item to update
        :param data: data to add/change in item
        :return: a tuple of booleans on if the item was found and modified 
        """ 
        new_data = {}
        for key in data.data:
            if data.data[key] != "":
                new_data[key] = data.data[key]

        response_info = self.db.update_item({'_id': ObjectId(id)}, {"$set":new_data})
        return (response_info[0] > 0, response_info[1] > 0) #to check that an item was matched and/or modified

    def delete(self, id):
        """
        Calls database to delete a given item

        :param id: the id of the item to delete
        :return: a boolean of if an item was deleted
        """ 
        delete_count = self.db.delete_item({'_id': ObjectId(id)})
        return delete_count > 0 #to check that an item was deleted

    def list_items(self):
        """
        Gets all items

        :return: a list of all the items 
        """ 
        items = self.db.get_items()
        if items != None: 
            all = [self.dump(item) for item in items]
            return all 
        return []
    
    def export_csv(self):
        """
        Creates a csv file of all the data in the database
        """ 
        items = self.db.get_items()
        with open('dict.csv', 'w') as csv_file:  
            writer = csv.DictWriter(csv_file, fieldnames = INVENTORY_INFO)
            writer.writeheader()
            writer.writerows(items)

    def dump(self, data):
        """
        Formats data into useable form 

        :param data: data of an item
        :return: returns formatted data
        """ 
        return InventorySchema().dump(data).data