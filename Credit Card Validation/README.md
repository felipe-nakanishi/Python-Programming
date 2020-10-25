# Credit Card Validation using Luhns's Algorithm

This is a program that checks if a credit card number is valid or not and returns it's brand. It is based on Harvard's CS50 problem set 'Credit'.

**Luhn’s Algorithm**

Most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:
 1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
 2. Add the sum to the sum of the digits that weren’t multiplied by 2.
 3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
 
**Credit Card Brands**

According to Harvard's CS50 problem set: 
 1. All American Express numbers start with 34 or 37; 
 2. most MasterCard numbers start with 51, 52, 53, 54, or 55; 
 3. All Visa numbers start with 4. 
