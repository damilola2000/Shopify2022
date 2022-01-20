import React, {useState} from "react"

function Inventory()

{
    const [product_name, setProduct]=useState("")
    const [price, setPrice]=useState("")
    const [stock, setStock]=useState("")
    const [warehouse, setWarehouse]=useState("")
    const [all_items, setItems]=useState([])

    const url = "http://127.0.0.1:5000/"

    async function reload() {
        let items = await fetch(`${url}/item`, {
        method:'GET',
        headers: {
            "Content-Type": 'application/json',
            "Access-Control-Allow-Origin": "*"
        }
    })
    items = await items.json()
    setItems(items)
    }


    async function createItem(){
        let data = {product_name, price, stock, warehouse}

        let result = await fetch(`${url}/item`, {
            method:'POST', 
            body:JSON.stringify(data),
            headers: {
                "Content-Type": 'application/json',
                "Access-Control-Allow-Origin": "*"
            }
        })
        result = await result.json()
        reload()
        console.log(result)
    }

    async function updateItem(id){
        let data = {product_name, price, stock, warehouse}
        let result = await fetch(`${url}/item/${id}` , {
            method:'PATCH', 
            body:JSON.stringify(data),
            headers: {
                "Content-Type": 'application/json',
                "Access-Control-Allow-Origin": "*"
            }
        })
        result = await result.json()
        reload()
        console.log(result)
    }

    async function deleteItem(id){
        let result = await fetch(`${url}/item/${id}` , {
            method:'DELETE', 
            headers: {
                "Content-Type": 'application/json',
                "Access-Control-Allow-Origin": "*"
            }
        })
        result = await result.json()
        reload()
        console.log(result)
    }

    return (
        <div>
            <div className="col-sm-3 offset-sm-3">
                <h1>Inventory</h1>
                <input type="text" value={product_name} onChange={(e)=>setProduct(e.target.value)} placeholder="Product Name" />
                <input type="number" value={price} onChange={(e)=>setPrice(e.target.value)} placeholder="Price" />
                <input type="number" value={stock} onChange={(e)=>setStock(e.target.value)} placeholder="Stock" />
                <input type="text" value={warehouse} onChange={(e)=>setWarehouse(e.target.value)} placeholder="Warehouse Location" />
                <button onClick={createItem}>Create Item</button>
                <a href="https://quiet-crag-06642.herokuapp.com/item" target="blank"><button>CSV</button></a>
            </div>
            <div>
                <h1>Items</h1>
                <h3>To update an Item type the required changes into the form above and then click the update button for the item you want to change</h3>
                <ul>
                {all_items.map(item => <div><li key={item.id}>Product Name:{item.product_name} - Price: ${item.price} - Stock: {item.stock} - Warehouse: {item.warehouse}</li><button onClick={() => updateItem(item._id)}>Update</button><button onClick={() => deleteItem(item._id)}>Delete</button></div>)}
                </ul>
            </div>
        </div>
        
    )
}

export default Inventory