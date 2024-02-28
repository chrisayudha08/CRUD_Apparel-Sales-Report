#---------------- CAPSTONE MODULE 1 - 'APPAREL SALES REPORT' - CRUD PROGRAM ------------------------
#---------------------------------------------------------------------------------------------------

from tabulate import tabulate
from datetime import datetime

head = ['Products Id', 'Products', 'Stock', 'Initial Fund', 'Sales Price', 'Sales']
data = [
    ['101', 'Shirt', 50, 20000, 50000, 35],
    ['102', 'Hoodie', 25, 50000, 100000, 15],
    ['103', 'Vest', 30, 25000, 50000, 20],
    ['104', 'Jacket', 40, 75000, 120000, 28],
    ['105', 'Sweater', 20, 70000, 100000, 15],
    ['106', 'Hat', 10, 15000, 60000, 5]
]

# FUNCTIONS
def time():
    print(f'Updated on: {datetime.now()}')

def print_invalid():
    print("The option you entered is invalid, please enter the right input.")

def print_noData():
    print('The data you looking for does not exist, please input the right option.')

def print_dataExisted():
    print('Products_ID already existed. please add a new data.')

def print_table():
    print(tabulate(data, headers = head, tablefmt = 'pretty'))

def searchData_ID():
    if len(data) > 0:
        for i in data:
            if i[0] != search:
                continue
            elif i[0] == search:
                showtable = [i]
                print(tabulate(showtable, headers = head, numalign='center', tablefmt = 'pretty'))
                print()
                time()
                return True
        if i[0] != search:
            print_noData()
            return False
    else:
        print_noData()

def searchData_Name():
    for i in data:
        if i[1] != search:
            continue
        elif i[1] == search:
            showtable = [i]
            print(tabulate(showtable, headers = head, numalign='center', tablefmt = 'pretty'))
            print()
            time()
            break
    if i[1] != search:
        print_noData()
        return False

def checkData_ID():
    if len(data) > 0:
        for i in range(len(data)):
            for i in data:
                if i[0] != id:
                    continue        
                elif i[0] == id:
                    return True
            if i[0] != id:                               
                return False
    else:
        print("There are no data's in the database")

def check_column():
    for i in range(len(head)):
        for a in head:
            if a != col:
                continue        
            elif a == col:
                return True
        if a != col:
            print_noData()
            return False
        
def delete():
    for x in enumerate(data):
        if x[1][0] == id:
            show_1Table(id)
            print()
            if continue_opt() == True:
                data.pop(x[0])
                print_table()
                break
            else:
                print('Data deletion operation canceled')
                break
            
        elif x[1][0] != id:
            continue
    
def newData():
    new = []
    while True:
        products = input('Input new Products_Name: ').title()
        if products.replace(" ","").isalpha() == True:
            break
        else:
            print_invalid()
            continue
    while True:
        stock = (input('Input stock(pcs): '))
        if stock.isdigit() == True:
            s = int(stock)
            break
        else:
            print_invalid()
            continue
    while True:
        modal = input('Input initial fund: ')
        if modal.isdigit() == True:
            fu = int(modal)
            break
        else:
            print_invalid()
            continue
    while True:
        price = input('Input selling price: ')
        if price.isdigit() == True:
            p = int(price)
            break
        else:
            print_invalid()
            continue
    while True:
        sales = input('Input sales: ')
        if sales.isdigit() == True:
            s = int(sales)
            break
        else:
            print_invalid()
            continue
    
    print()    
    if continue_opt() == True:
        new.extend([id,products,s,fu,p,s])
        data.append(new)
        print()
        print("Data has been succesfully updated!")
        print_table()
        time()
    
    else:
        print('Data saving canceled.')

def show_1Table(id):
    for i in data:
        if i[0] != id:
            continue
        elif i[0] == id:
            display = [i]
            print(tabulate(display, headers = head, tablefmt='pretty'))
            break

def row():  
    baris = 0  
    for x in range (len(data)):
        for i in data:
            if i[0] != id:
                baris +=1
                continue
            elif i[0] == id:
                break
        return baris
       
def column():
    kolom = 0    
    for a in range (len(head)):
        for i in head:
            if i != col:
                kolom += 1
                continue
            elif i == col:
                break                
        return kolom
    
def continue_opt():
    save = input("Are you sure to continue this operation?(y/n) ").lower()
    if save == 'y':
        return True
    elif save == 'n':
        return False
    else:
        print_invalid()
        return False

while True:
    print("""
          
        ================================
              Apparel Sales Report
        ================================
                    Main Menu
      
        1. Show Data
        2. Add New Data
        3. Update Data
        4. Delete Data
        5. Financial Report
        6. Database Size
        7. Exit Program
        """)
    
    userInput = (input('Please input menu number(1-7) to run: '))

    # ---------------------------------------------
    # READ 
    #----------------------------------------------
    if userInput == '1':

        while True:
            print("""
            ---------------------------------
                        READ MENU
            1. Show all data available
            2. Show specified data available
            3. Sort data
            4. Back to main menu
                """)
            
            read = input('Data to be showed (1-4): ')

            if read == '1':
                print_table()
                print()
                time()
                break

            elif read == '2':
                search = input('Please input ID_Products/Products name to show: ').title()

                if search.isalpha() == True:
                    searchData_Name()                    

                elif search.isdigit() == True:
                    searchData_ID()

                else:
                    print_invalid()

            elif read == '3':
                while True:
                    print("""
                    -----------------------------
                            Sorting Data
                          
                    1. Sort by Name
                    2. Sort by Stock
                    3. Sort by Initial Fund
                    4. Sort by Sales Price
                    5. Sort by Sales
                    6. Back to read menu
                        """)
                    sortby = input('Please input sort option (1-6): ')
                    if sortby ==  '1':
                        print()
                        print("Sorted by Name ASCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[1],), headers=head, tablefmt='pretty'))
                        print()
                        print("Sorted by Name DESCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[1], reverse=True), headers=head, tablefmt='pretty'))
                    elif sortby == '2':
                        print()
                        print("Sorted by Stock ASCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[2]), headers=head, tablefmt='pretty'))
                        print()
                        print("Sorted by Stock DESCENDED")
                        print(tabulate(sorted(data, key=lambda x: x[2], reverse=True), headers=head, tablefmt='pretty'))
                    elif sortby == '3':
                        print()
                        print("Sorted by Initial Fund ASCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[3]), headers=head, tablefmt='pretty'))
                        print()
                        print("Sorted by Initial Fund DESCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[3], reverse=True), headers=head, tablefmt='pretty'))
                    elif sortby == '4':
                        print()
                        print("Sorted by Sales Price ASCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[4]), headers=head, tablefmt='pretty'))
                        print()
                        print("Sorted by Sales Price DESCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[4], reverse=True), headers=head, tablefmt='pretty'))
                    elif sortby == '5':
                        print()
                        print("Sorted by Sales ASCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[5]), headers=head, tablefmt='pretty'))
                        print()
                        print("Sorted by Sales DESCENDED")                        
                        print(tabulate(sorted(data, key=lambda x: x[5], reverse=True), headers=head, tablefmt='pretty'))
                    elif sortby == '6':
                        break
                    else:
                        print_invalid()
                
            elif read == '4':
                break

            else:
                print_invalid()
                continue

#     #==========================================
#     # CREATE
#     #==========================================
    elif userInput == '2':

        while True:

            print("""
            ---------------------------
                    CREATE MENU
                
            1. Add a new data
            2. Add multiple new data
            3. Back to main Menu           
                """)
            
            option = input('Choose option (1-3): ')
            
            if option == '1':
                while True:
                    print_table()
                    id = (input('Input new Products_Id: '))
                    if id.isdigit() == False:
                        print_invalid()
                        continue
                    else:
                        break

                if checkData_ID() == True:
                    print_dataExisted()
                else:
                    newData()
                    break   
                    
            elif option == '2':
                print_table()
                multiple = (input("How many data's would you like to add? "))

                if multiple.isdigit() == True and int(multiple) <= 10:
                    multi = int(multiple)
                    for x in range(multi):
                        id = (input('Input new Products_Id: '))
                        if id.isdigit() == False:
                            print_invalid()
                            continue                              
                        else:
                            if checkData_ID() == True:
                                print()
                                print_dataExisted()
                                continue
                            else:
                                newData()   
                else:
                    print_invalid()
                    print("10 Max data's to be added at the same time.")
                
            elif option == '3':
                break

            else:
                print_invalid()

    #================================================
    # UPDATE
    #================================================
    elif userInput == '3':

        while True:
            print('''
                ---------------------------
                        UPDATE MENU
                  
                  1. Update a specific data
                  2. Update multiple data's
                  3. Update per row
                  4. Back to main menu
                  ''')
            
            option = input('Choose option (1-4): ')
            
            if option == '1':
                while True:
                    print_table()
                    id = input('Input Products_Id to update: ')
                    if checkData_ID() == True:
                        show_1Table(id)
                        acc = input('Continue to update this data?(y/n): ').lower()
                        if acc == 'y':               
                            col = input('Input which column in this row to update: ').title()                                                         
                            if check_column() == True:
                                update = input('Input new value: ')
                                if column() > 1 and update.isdigit() == True:
                                    if continue_opt() == True:                  
                                        data[row()][column()] = int(update)
                                        print_table()
                                        print('Data has been succesfully updated')
                                        break
                                    else:
                                        continue
                                elif column() < 2 and update.replace(' ','').isalpha() == True:
                                    update = input('Input new value: ')
                                    if continue_opt() == True:
                                        data[row()][column()] = (update)
                                        print_table()
                                        print('Data has been succesfully updated')
                                        break
                                    else: 
                                        continue
                                else:
                                    print_invalid()
                            else:
                                break

                        elif acc == 'n':
                            break

                        else:
                            print_invalid()
                            continue
                    
                    else: 
                        print_noData()                                                                      
                        break
                
            elif option == '2':
                multiple = (input("How many data's would you like to update? "))

                if multiple.isdigit() == True and int(multiple) <= len(data):
                    multi = int(multiple)
                    for x in range(multi):
                        print_table()
                        id = input('Input Products_Id to update: ')                        
                        if checkData_ID() == True:
                            show_1Table(id)
                            acc = input('Continue to update this data?(y/n): ').lower()

                            if acc == 'y':                                              
                                col = input('Input which column in this row to update: ').title()
                                if check_column() == True: 
                                    update = input('Input new value: ') 
                                    if column() > 1 and update.isdigit() == True:                                                        
                                        data[row()][column()] = int(update)
                                        print_table()
                                        print('Data has been succesfully updated')                                    
                                    elif column() < 2 and update.replace(' ','').isalpha() == True:
                                        data[row()][column()] = int(update)
                                        print_table()
                                        print('Data has been succesfully updated')
                                    else:
                                        print_invalid()
                                else:
                                    continue                           
                            elif acc == 'n':
                                continue
                    
                            else:
                                print_invalid()
                                continue
                
                        else:
                            print_noData()
                            continue
                else:
                    print_invalid()
                    print("Max data to be updated is as many as the data's in the database")
                    continue

            elif option == '3':
                while True:
                    print_table()
                    id = input('Input Products_Id to update: ')
                    if checkData_ID() == True:
                        show_1Table(id)
                        acc = input('Continue to update this data?(y/n): ').lower()
                        if acc == 'y':
                            n_name = input('Please input new Products name: ')
                            if n_name.replace(' ','').isalpha() == True:
                                data[row()][1] = n_name
                            else:
                                print_invalid()
                                break
                            n_stock = input('Please input new Stock: ')
                            if n_stock.isdigit() == True:
                                data[row()][2] = int(n_stock)
                            else:
                                print_invalid()
                                break
                            n_IF = input('Please input new Initial Fund: ')
                            if n_IF.isdigit() == True:
                                data[row()][3] = int(n_IF)
                            else:
                                print_invalid()
                                break
                            n_SP = input('Please input new Sales Price: ')
                            if n_SP.isdigit() == True:
                                data[row()][4] = int(n_SP)
                            else:
                                print_invalid()
                                break
                            n_sales = input('Please input new Sales: ')
                            if n_sales.isdigit() == True:
                                data[row()][5] = int(n_sales)
                            else:
                                print_invalid()
                                break

                            print_table()
                            break

                        else:
                            break
                    else :
                        print_noData()
                        break
                

            elif option == '4':
                break

            else:
                print_invalid()
                continue
#     #==============================================
#     # DELETE
#     #==============================================
    elif userInput == '4':
        while True:
            print("""
            ---------------------------
                    DELETE DATA
                
            1. Delete a specific row
            2. Delete last row
            3. Delete multiple data
            4. Delete all data   
            5. Back to main menu   
                """)
            
            opt = input('Choose option (1-5): ')

            if opt == '1':
                print_table()
                id = input('Input Products_ID to be deleted: ')
                if checkData_ID() == False:
                    print_noData()
                    continue
                elif checkData_ID() == True:
                    delete()

            elif opt == '2':
                print(tabulate(data[-1:], headers=head, numalign='center', tablefmt = 'github'))
                d = input("Are you sure to delete this data?(y/n): ").lower()

                if d == 'y':
                    data.pop()
                    print_table()
                    print()
                    time()
                elif d == 'n':
                    print('Operation Canceled')
                else:
                    print_invalid()

            elif opt == '3':
                multiple = (input("How many data's would you like to delete? "))

                if multiple.isdigit() == True and int(multiple) <= len(data):
                    multi = int(multiple)
                    for x in range(multi):
                        while True:
                            id = (input('Input Products_Id to be deleted: '))
                            if id.isdigit() == True:
                                break
                            else:
                                print_invalid()
                                continue
                        if checkData_ID() == False:
                            print_noData()

                        else:
                            delete()
                else:
                    print_invalid()
                    print("Max data to be deleted is as many as data's in the database")
                    
            elif opt == '4':
                print(tabulate(data, headers=head, numalign='center', tablefmt = 'github'))
                print()
                d = input("Are you sure to delete all data's?(y/n): ").lower()
                
                if d == 'y':
                    data.clear()
                    print_table()
                    print()
                    time()
                    break
                elif d == 'n':
                    print('Operation Canceled.')
                else:
                    print_invalid()
                            
            elif opt == '5':
                break

            else:
                print_invalid()
                continue

#============================
# PROFIT/DEFICIT
#============================
    elif userInput == '5':
        while True:
            print('''
            ------------------------------
                    Profit/Deficit

            1. Per/items
            2. Overall
            3. Back to main menu
                ''')
            ipt = input('Please enter an input (1-3):')
            if ipt == '1':
                print_table()
                id = input('Input Products_id to calculate: ')
                if checkData_ID() == True:
                    expenses = (data[row()][2] * data[row()][3])
                    income = (data[row()][4] * data[row()][5])
                    total = income - expenses

                    if total < 0:
                        print(f'Products : {data[row()][1]}\nExpenses: Rp {expenses:,},00 \nIncome: Rp {income:,},00\nDEFICIT: Rp {total:,},00')
                    else:
                        print(f'Products : {data[row()][1]}\nExpenses: Rp {expenses:,},00 \nIncome: Rp {income:,},00\nPROFIT : Rp {total:,},00')
                    
                else:
                    print_noData()

            elif ipt == '2':
                expenses = 0
                income = 0
                for x in range(len(data)):
                    expenses += (data[x][2]*data[x][3])
                    income += (data[x][4]*data[x][5])
                total = income - expenses
                if total < 0:
                    print(f'DEFICIT \nTotal: Rp {total:,},00')
                else:
                    print(f'PROFIT \nTotal: Rp {total:,},00')

            elif ipt == '3':
                break

            else:
                print_invalid()
                continue
            
#============================
#   DATABASE SIZE
#============================
    elif userInput == '6':
        print(f"""
        Currently there are: 
        {len(head)} column's
        {len(data)} row's 
        on the database
              """)
        time()

    elif userInput == '7':
        exit = (input('Are you sure to exit this program?(y/n): ')).lower()
        if exit == 'y':
            print('Thank You! Program closed.')
            break
        elif exit == 'n':
            continue
        else :
            print_invalid()
    else:
        print_invalid()