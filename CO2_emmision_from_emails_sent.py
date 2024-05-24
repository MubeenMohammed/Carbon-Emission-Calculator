#CO2 emmissions calculator using number of emails sent
print('Welcome to the email CO2e calculator:\nLet\'s start by asking you a few questions about the email:')
email_type = int(input('\tIs this email a spam(type 0 for yes and 1 for no)?' ))
if email_type == 0:
    print('The CO2e emissions for this email is 0.03g')
else:
    email_length = int(input(' \tIs this email a short one(type 0 for yes and 1 for no)? '))
    if email_length == 0:
        device = int(input(' \tIs this email being sent from a phone (type 0 for yes and 1 for no)?'))
        if device == 0:
            print('The CO2e emission for this email is 0.2 g')
        else:
            print('The CO2e emissions for this email is 0.3 g')
    else:
        no_of_recipients = int(input('\tIs this email being sent for only one recipent (type 0 for yes and 1 for no)?'))
        if no_of_recipients == 0:
            print('The CO2 emissions for this email is 17 g')
        else:
            print('The CO2e emissions for this email is 26g')
#Note: we assume that the person running the code will not enter the values other than 0 and 1