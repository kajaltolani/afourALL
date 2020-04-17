
items=['Apples','Bananas','Mangoes','Grapes']
price={'Apples':100,'Bananas':60,'Mangoes':600,'Grapes':250}
quantity={'Apples':20,'Bananas':50,'Mangoes':35,'Grapes':45}

what=input(f'Enter what do you want from {items}? ')
if what in items:
    how_much= float(input(f'Enter how much {what} do you want: '))
    if how_much <= quantity.values():
        print('proceed')
    else:
        print('reduce quantity')
else:
    print('Invalid')

