from marshmallow import Schema, fields, ValidationError
from bson.objectid import ObjectId

Schema.TYPE_MAPPING[ObjectId] = fields.String

class InventorySchema(Schema):
  _id = fields.String(dump_only=True)
  product_name = fields.Str(required=True)
  stock = fields.Int()
  warehouse = fields.Str()
  price = fields.Float()
