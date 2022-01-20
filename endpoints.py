from flask import Flask, Response, request, send_file
from flask_cors import CORS, cross_origin
from schema import InventorySchema
from marshmallow import ValidationError
from service import Service
import json

app = Flask(__name__)
CORS(app)

@app.route('/item', methods=['POST'])
@cross_origin()
def create():
    try:
        inventory_data = InventorySchema().load(json.loads(request.data))
    except ValidationError as err:     
        return response({"error": err.messages}, 400)
    if not inventory_data.data["product_name"]:
        return response({"error": "Missing Product Name"}, 400)
    created_item = Service().create(inventory_data)
    return response(created_item, 201)

@app.route("/item", methods=["GET"])
@cross_origin()
def list_items():
    items = Service().list_items()
    return response(items)

@app.route("/item/csv", methods=["GET"])
@cross_origin()
def export_csv():
    Service().export_csv()
    return send_file('dict.csv',
                     mimetype='text/csv',
                     attachment_filename='test.csv')


@app.route('/item/<id>', methods=['PATCH'])
@cross_origin()
def update(id):
    try:
        inventory_data = InventorySchema().load(json.loads(request.data))
    except ValidationError as err:
        return response({"error": err.messages}, 400)

    update_response = Service().update(id, inventory_data)
    if not update_response[0]:
        return response({"error": f"Item ({id}) was not found"}, 404) 
    elif not update_response[1]:
        return response({"Message": f"No Modifications made to ({id})"}, 304)
    else:
        return response({"Message": f"Item ({id}) was succesfully modified"})
        

@app.route("/item/<id>", methods=["DELETE"])
@cross_origin()
def delete(id):
    if Service().delete(id):
        return response({"message": f"Item ({id}) was sucsessuly deleted"})
    else:
        return response({"error": f"Item ({id}) was not found"}, 404)


def response(payload, status=200):
  return Response( 
    response= json.dumps(payload),
    status=status,
    mimetype="application/json"
  )

if __name__ == '__main__':
    app.run(debug=True)