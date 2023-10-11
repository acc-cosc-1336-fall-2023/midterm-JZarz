#write functions here, don't add input('') statements here!

def get_assesment_vaule(value):
    assement_value = value * .60 
    return assement_value

def get_tax_assesed(assment_value):
    tax_value = assment_value // 100 * .72

    return round(tax_value,2)

def get_property_value():
    value = int(input("input property value you'd like to assess: \n"))
    assement_value = get_assesment_vaule(value)
    tax_value = get_tax_assesed(assement_value)
    print (f'Your land assement value is: {assement_value} \nYour tax assement is {tax_value}')

    cont()

def cont():
    result = input ("Would you like to assess another property?\n Type 'Y' for yes \n Type 'N' for no:\n")

    while result.upper() != "N":
        if result.upper() == 'Y':
            get_property_value()
            
        else:
            while result.upper() != 'Y' and result.upper() != 'N':
                result = input("Please choose 'Y' or 'N': ")
    print("program exited")
    exit()