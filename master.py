# variables of benefit categories containing dictionaries of available benefits for each card we have

from re import X


dining = {'amex': '4x points', 'chase freedom': '3% cash back', 'chase sapphire preferred': '3x points'}
grocery = {'amex': '4x points', 'bonvoy': '3x points'}
everything_else = {'amex': '1x points', 'bonvoy': '2x points'}
gas_station = {'bonvoy': '3x points'}
drug_store = {'chase freedom': '3% cash back'}
online_grocery = {'chase sapphire preferred': '3x points'}
streaming_service = {'chase sapphire preferred': '3x points'}
categories = {'dining', 'grocery', 'gas station', 'drug store', 'online grocery', 'streaming service'}

print( 'Hi! Here are your current benefit categories:')
for category in categories:
   print(category)

def purchase_type():
    is_category = input('Is your purchase in one of these categories?: ')
    is_category = is_category.lower()
    if is_category == 'no':
        print('you can use the: ') 
        for x,y in everything_else.items():
	        print(x + ' for ' + y) 
    else:
        purchase_type = input('Which category is it?: ')
        purchase_type = purchase_type.lower()
        purchase_type = purchase_type.replace(' ','_')
        for category in categories:
            if purchase_type == category:
                print('you can use the: ') 
                for x,y in category.items():
	                print(x + ' for ' + y) 
        
        #print('that is not one of your categories.')
         #       try_again = input('Would you like to try again? y/n: ')
          #      try_again = try_again.lower()
           #     if try_again == 'n':
            #        print('thank you, have  a great day!')
             #   else:
              #      purchase_type()

purchase_type()