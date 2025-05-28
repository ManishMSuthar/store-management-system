import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def showdata():
    df1 = pd.read_csv("updated data.csv")
    print(df1)
    input("Press any key to continue...")

def add_data():    
    data = []

    print("Insert data of particular product: ")
    Name = input("Enter product name: ")
    Category = input("Enter product category (groceries, cosmetics, pharmacy): ")
    Available_stock = float(input("Enter product stock: "))  
    Time_checked = input("Enter last checked date (DD-MM-YY): ")
    Unit_price = float(input("Enter per unit price: ")) 
    Order_quantity = input("Enter the order quantity: ")
    Barcode = input("Enter product's barcode (6 DIGITS): ")
    gr_no = input("Enter product's GR.No (4 DIGITS): ")
    product_id = input("Enter product ID (3 DIGITS,groc=154,cosm=243,pharm=487): ")
    Inventory_value = Available_stock * Unit_price

    data.append([Name, Category, Available_stock, Time_checked, Unit_price, Order_quantity, Barcode, gr_no, product_id, Inventory_value])

    df1 = pd.DataFrame(data)

    df1.to_csv('updated data.csv', mode='a', index=False, header=False)
    print("Data has been added")
    input("Press any key to continue...")

def calculate_inventory_value():
    df1 = pd.read_csv('updated data.csv')
    df1['Inventory Value'] = df1['Available stock'] * df1['Unit price']
    print(df1[['Name', 'Inventory Value']])
    input("Press any key to continue...")

def bar_chart():
    df1 = pd.read_csv('updated data.csv')
    Name = df1["Name"]
    Available_stock = df1["Available stock"]
    Unit_price = df1["Unit price"]
    
    print("        ++++++++++++++++--------------------------------------++++++++++++++++")
    print("                                 Bar Graph Menu                              ")
    print("        ++++++++++++++++--------------------------------------++++++++++++++++")
    print("1. Product wise Available stock")
    print("2. Per unit price of a product")
    print("3. Return to main menu")

    while True:
        y = int(input("Enter your choice to get bar graph displayed: "))
        
        if y == 1:
            plt.ylabel("Available Stock")
            plt.title("Available Stock of the Products")
            plt.bar(Name, Available_stock, color='r', width=0.5)
            plt.xlabel("Product Name")
            plt.xticks(rotation=45)
            plt.show()
        
        elif y == 2:
            plt.ylabel("Unit Price")
            plt.title("Product Price per Unit")
            plt.bar(Name, Unit_price, color='b', width=0.5)
            plt.xlabel("Product Name")
            plt.xticks(rotation=45)
            plt.show()
            
        elif y == 3:
            print("Returning to main menu...")
            break

def main_menu():
    while True:
        print()
        print('  ++++++++++++++++++++----------------------------+++++++++++++++++++++++++    ')
        print('                                 Main Menu                                     ')
        print('  ++++++++++++++++++++----------------------------+++++++++++++++++++++++++    ')

        print('''
            1. Show DataFrame
            2. Sorting by GR.No
            3. Add Product Data
            4. Edit a Record
            5. Delete a Record
            6. Bar Graph
            7. Line Chart
            8. Exit
            ''')
        ch = int(input('Enter Your Choice: '))
        if ch == 1:
            showdata()
        elif ch == 2:
            sort()  
        elif ch == 3:
            add_data()
        elif ch == 4:
            edit_data()  
        elif ch == 5:
            delete_data()  
        elif ch == 6:
            bar_chart()
        elif ch == 7:
            line_chart() 
        elif ch == 8:
            print("Thank you!")
            break

main_menu()
