# Shopify2022

To Set up the correct settings to run the program

## Environment Set Up

You will need Python installed (3.6 or higher)

`git clone` [repo]
  
`cd` [repo]
  
`pip install virtualenv` (if you don't already have virtualenv installed)
  
`virtualenv venv` to create your new environment (venv can be any name for the virtual environment)
  
`source venv/bin/activate` to enter the virtual environment
  
`pip install -r requirements.txt`  
  
## Running Backend
  
To Run the Backend you will open a terminal and set go to this project directory then run `python ./endpoints`
  
This will serve the API at `http://localhost:5000/`

To send requests the server use a platform like Postman to make the following requests: 

1. `GET` to `http://localhost:5000/item` this will retrive a list of all items

2. `POST` to `http://localhost:5000/item`  this will create an item 

Request must send a body of data in this format:{"project_name":<string>, "stock": <int>, "price", <float>, "warehouse", <string>}
  
3. `PATCH` to `http://localhost:5000/item/<id>` this will update an item
  
Id for item can be found from running GET method
Request must send a body of data in this format:{"project_name":<string>, "stock": <int>, "price", <float>, "warehouse", <string>}
  
4. `DELETE` to `http://localhost:5000/item/<id>` this will delete an item
Id for item can be found from running GET method
  
5. `GET` to `http://localhost:5000/item/csv` this will create a csv in the app directory with the project data
  
## Running Frontend
Open another terminal set at the `../http/web/app` directory and run `npm start`. 
  
Then follow the link provided to open to webpage: `http://localhost:3000`


  
