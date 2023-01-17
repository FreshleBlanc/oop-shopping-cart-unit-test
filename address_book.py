
# step 2
address_book = {}

# step 1
def store_user_info(name, address):
    # Add a try and except, that handles the case
    # where the name is already in the address book
    try:
        if name in address_book:
            raise Exception(f"{name} is already in your address book.")
        else:
            address_book[name] = address
    except Exception as error:
        print(error)
    
def remove_user_info(name):
    # Add a try and except to handle the key error
    try:
        del address_book[name]
    except:
        print(f'{name} is not in your address book.')
        
def main():
    # step 3
    while True:
        # step 4
        name = input("Person's Name: ")
        address = input("Person's Address: ")
        
        # step 6
        store_user_info(name, address)
        
        cont = input("Would you like to continue (y/n)? ")
        
        # step 5
        if cont == 'n':
            # step 5b
            break
            
    # step 5a
    print(address_book)