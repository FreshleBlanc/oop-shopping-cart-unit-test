from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def show(shopping_cart):
    print(text['cart_divider'])
    total = 0
    for key, val in shopping_cart.items():
        item_total = val['quantity'] * val['price']
        total += item_total
        print(text['item_line'].format(key=key.title(), quantity=val['quantity'], item_total=item_total))
        
    print(text['total_line'].format(total=total))    
    
    print(text['cart_divider'])
    
def add(shopping_cart, name, quantity, price):
    if name in shopping_cart:
        while True:
            choice = input(text['add_error'].format(name)).lower()

            if choice == 'y':
                shopping_cart[name]['quantity'] += quantity
                break
            elif choice == 'n':
                print(text['add_cancel'])
                break
            else:
                print(text['invalid_selection'])
    else: 
        shopping_cart[name] = {
            'quantity': quantity,
            'price': price
        }
        print(text['add_success'].format(name=name.title()))

def delete(shopping_cart, name):
    if name in shopping_cart:
        del shopping_cart[name]
    else:
        print(text['delete_error'].format(name))

def main():
    shopping_cart = {}
    
    application_running = True
    while application_running:
        choice = input(text['main_prompt']).lower()
        
        if choice in options['show_options']:
            show(shopping_cart)
        elif choice in options['add_options']:
            name = input(text['add_name']).lower()
            quantity = int(input(text['add_quantity']))
            price = float(input(text['add_price']))
            
            add(shopping_cart, name, quantity, price)
            
        elif choice in options['delete_options']:
            name = input(text['delete_name']).lower()
            
            delete(shopping_cart, name)
            
        elif choice in options['quit_options']:
            print(text['quit_message'])
            show(shopping_cart)
            application_running = False

main()