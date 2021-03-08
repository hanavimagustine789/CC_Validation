# Credit Card Validation
# Provided a List containing Dictionary (ccNasabah), This list contains data on the credit card number of a bank customer, which has not been verified the validity of the credit card. Create a python file (.py)that has a Return Function and 1 Argument,the function will separate between the customer with a valid & invalid credit card number, then save the result in a separate Dictionary (ccValid and ccInvalid).

# The criteria for a valid credit card number are as follows:

# It starts with the numbers 4, 5 or 6.
# It consists of exactly 16 digits of numbers.
# Only contains numbers 0-9.
# Can be written as a group of 4 digits separated by a hyphen "-"
# There should not be 1 number repeated >3x & written in a row, for example: 3333.
# Example:
# ✅ Validcredit card number :

# 4253 -6258-7961 - 5781
# 4424424424442442
# 5122-2368-7954-3213
# 4123456789123454
# 5123-4567-8912-3455
# 4123356789123456


try:
   input1 = input("Masukan Credit Card Number: ")
   cc_split = input1.split("-")
   index_cc = cc_index[0]
   for i in cc_split:
       if i.isdigit() == False:
           print("Hanya menerima Digit")
           for i in index_cc != '4' or index_cc != '5' or index_cc != '6':
               print("Hanya menerima angka 4, 5, dan 6")
               if len(CreditCardNumber) != 16:
                   print("Bukan Merupakan CreditCardNumber")
               elif len(cc_split) != 3:
                   print("Bukan merupakan CreditCard Number")
               else:
                   Index = cc_split[0].split("-")
                   index1 = cc_split[1].split("-")
                   index2 = cc_split[2].split("-")
                   index3 = cc_split[3].split("-")
                   if len(index) and len(index1) and len(index2) and len(index3) != 4:
                       print("Bukan Merupakan Credit Card Number")
                   else:
                       if len(index) != 4 or len(index1) !=4 or len(index2) != 4 or len(index3) != 4: 
                           print("Bukan merupakan cc")
                       else:
                           for i in input1:
                                if not i.isdigit():
                                   print("Bukan merupakan cc")
                                else:
                                    if i in input1 > 9 or input1 < 0:
                                        print("Hanya menerima angka 0 - 9")
except:
    "Tidak Menerima Alphabet"
                        
                 


print(ccValidation())