store_room={
    "lays":16,
    "chocolate":10,
    "kurkure":5,
    "goodday":12
}
print("Inventory Store Mangament".center(50,"="))
user_action=input("To View Stock Type '1'\nTo Delete Item Type '2'\nTo Add Item Type '3'\n")
if user_action=="1":
    print(list(store_room.items()))
elif user_action=="2":
    add_remove=input("Enter ADD to add item and DEL to remove: ").lower()
    if add_remove=="del":
        to_delete=input("Enter name of item you want to delete :\n").lower()
        for key in store_room:
            if key==to_delete:
                del store_room[key]
                print("Item Deletion Sucessfull, Updated Inventory : ")
                print(store_room)
                break
            else:
                print("Element not found")
elif user_action=="3":
    keys=input("Enter Product Name  : \n")
    value=input("Enter Quantity : \n")
    store_room.update({keys:value})
    print("Item Added Sucessfully")
    print(store_room)