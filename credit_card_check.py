#function to calculate the validation number through the luhn's algorithm:
def validation(number):
  sum_1 = 0
  sum_2 = 0
  #sum the numbers from the last digit skipping one digit:
  for digit_1 in range(len(str(number)),0,-2): #we needed to convert the number to str so that we can find its len.
    number_int = int(str(number)[digit_1-1]) #convert the number to int so that we can sum it.
    sum_1 += number_int
  for digit_2 in range(len(str(number))-1,0,-2): #multiply the remaining numbers by 2 and sum them.
    number_mult = int(str(number)[digit_2-1])*2
    sum_2 += sum(int(digit) for digit in str(number_mult))
  validation_number = sum_1 + sum_2 #obtain the validation number.
  return validation_number
#function to check if the validation number is a valid credit card number:
def check_brand(validation_number):
  if  validation_number % 10 == 0: #check if the validation number represents a valid credit card.
    #if the number is valid then we check to identify what is the brand of the card.
    if len(str(number)) == 15 and (str(number)[:1] == '34' or str(number)[:1] == '37'):
      return 'AMEX'
    elif len(str(number)) == 16 and (str(number)[:1] == '51' or str(number)[:1] == '52' or str(number)[:1] == '53' or str(number)[:1] == '54' or str(number)[:1] == '55'):
      return 'MASTERCARD'
    elif (len(str(number)) == 16 or  len(str(number)) == 13) and str(number)[0] == '4':
      return 'VISA'
  else:
    return 'INVALID'
  
#prompt for the user to type a card number:
number = input('Type a credit card number to check if it is valid, please:') 
#call the functions and return the brand of the card if valid:
validation_number = validation(number)
brand = check_brand(validation_number)
print(brand)




