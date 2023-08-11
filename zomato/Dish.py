import json
def read_data():
    try:
        with open('Dish.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}
    
def write_data(data):
    with open('Dish.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_order_data():
    try:
        with open('Order.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

def write_order_data(data):
    with open('Order.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def print_List():
    print("1.Add dish")
    print("2.Remove dish")
    print("3.Update dish")
    print("4.Take Order")
    print("5.Update order status")
    print("6.Exit")

def add_food(data,id,name,price,quantity,availability):
    data[id]={
        "name":name,
        "price":price,
        "quantity":quantity,
        "availability":availability
    }
    write_data(data)
    print("Data added sucessfully");    

def delete_data(Ddata,id):
    if id in Ddata:
        del Ddata[id]
        write_data(Ddata)
        print("Data deleted sucessfully")
    else:
        print("Invalid dish id")

def update_dish(data,id,field,value):
    if id in data and field in data[id]:
        data[id][field]=value
        write_data(data)
        print("Data added successfully")
    else:
        print("Id or field in not field")

def ordes_desk(Ddata,odId,dId,quantity):
    oData=read_order_data()
    
    pri=Ddata[dId]["price"]
    new_pri=int(pri)
    total=new_pri*quantity;
   
   oData[odId]={
       
   }


    
def main():
    

    while True:
        Ddata=read_data()
        print_List()

        choice=input("Enter your choice:-")

        if choice=="1":
            id=input("Enter Dish Id:-")
            name=input("Eneter Dish name:-")
            price=input("Enter price:-")
            quantity=input("Enter quantity:-")
            availability=input("Enter availability of food in terms of yes or no:-")
            add_food(Ddata,id,name,price,quantity,availability);
        elif choice=="2":
            id=input("Enter id for removing dish:-")
            delete_data(Ddata,id);
        elif choice=="3":
            id=input("Enter id of dish")
            print("Enter choice for update dish")
            print("1.Name\n2.price\n3.quantity\n4.Availability")
            ch=input("Enter your choice:-")

            if ch=="1":
                value=input("Enter dish name:-")
                update_dish(Ddata,id,"name",value)
            elif ch=="2":
                value=input("Enter price")
                update_dish(Ddata,id,"price",value)
            elif ch=="3":
                value=input("Enter quantity")
                update_dish(Ddata,id,"quantity",value)
            elif ch=="4":
                value=input("Enter availability")
                update_dish(Ddata,id,"availability",value)
        elif choice=="4":
            odId=input("Enter order id:-")
            dId=input("Enter food id")
            quantity=input("Enter quantity:-")
            ordes_desk(Ddata,odId,dId,quantity)

main()