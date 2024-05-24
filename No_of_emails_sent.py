#Writing a python program that calculates the number of long emails sent
co2e_emissions = float(input('What is the amount of CO2e emissions (in grams)?'))
a = int(co2e_emissions//26)
b = co2e_emissions%26
c = int(b//17)
d = round(b%17,2)
print(co2e_emissions,'g of CO2e corresponds to:')
print(a,'Long emails sent to many recipients')
if b > 17:
    print('and',c,'Long emails sent to one recipient')
if d > 0:
    print('with a remaining',d,'g left')
#All the above variables:
#a = no of long emails sent to many recipients
#b = remainder of CO2e left after sending certain no of long emails
#c = no of long emails sent to one recipient
#d = remainder of CO2e left after sending emails to many recipients and one recipient collectively
#Finally we suppose that user will always input a valid positive number higher than 26