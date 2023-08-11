import json

def read_data():
    try:
        with open('Snack.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}
    
def write_data(data):
    with open('Snack.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def add_food(data,id,name,price,availability):
    data[id]={
        "name":name,
        "price":price,
        "availability":availability
    }
    write_data(data)
    print("Data added sucessfully");


def updateFood(data,id,field,value):
    if id in data and field in data[id]:
        data[id][field]=value
        write_data(data)
        print("Data updated successfully.")
    else:
        print("Field or id is not valid")

def deleteData(data,id):
    if id in data:
        del data[id]
        write_data(data)
        print("Data deleted successfully.")
    else:
        print("Invalid food id")

def viewData(data):
    print("Following items present in database")

    for food_id,food_info in data.items():
        print("===============================")
        print(f"Food_id={food_id}")
        print(f"Name={food_info['name']}")
        print(f"Price={food_info['price']}")
        print(f"availability={food_info['availability']}")
        print("===============================")
        



  




def print_List():
    print("\n Welcome to food hut.")
    print("1.Add Food")
    print("2.Update Food")
    print("3.Delete Food")
    print("4.View Food")
    print("5.Quite")

# snack ID, snack name, price, and availability (yes or no).
def main():

    while True:
        fData=read_data()

        print_List()
        choice=input("Enter Your choice:-")

        if(choice=="1"):
            id=input("Enter food Id:-")
            name=input("Eneter food name:-")
            price=input("Enter price:-")
            availability=input("Enter availability of food in terms of yes or no:-")
            add_food(fData,id,name,price,availability);
        elif(choice=="2"):
            foodId=input("Eneter food id:-")
            print("Enter choice for update food item")
            print("1.Name\n2.price\n3.availability")
            uChoice=input("Enter your choice:-")

            if uChoice=="1":
                new_value=input("Enter name:-")
                updateFood(fData,foodId,"name",new_value)
            elif uChoice=="2":
                new_value=input("Enter price:-")
                updateFood(fData,foodId,"price",new_value)
            elif uChoice=="3":
                new_value=input("Enter availability:-")
                updateFood(fData,foodId,"availability",new_value)
            else:
                print("Invalid choice. Please try again latter")
        elif choice=="3":
            foodId=input("Enter food id:-")
            deleteData(fData,foodId);
        elif choice=="4":
            viewData(fData)
        elif choice=="5":
            print("Thank you");
            break;
   
   







main();

        

