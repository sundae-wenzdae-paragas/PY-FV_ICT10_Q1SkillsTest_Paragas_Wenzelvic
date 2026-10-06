 from pyscript import display, document

def checkout(e): #I put def "checkout" to let pyscript know that I want it to connect to the id (id= "checkout") in my Place Order button. So, when I click the Place Order button, this will function.

    document.getElementById("output").innerHTML = ""
    
    price1 = 420
    price2 = 420
    price3 = 435
    price4 = 435
    price5 = 500
    price6 = 475
#These are the prices of each item that I will connect to the respective orders

    item1 = document.getElementById("order1").checked * price1

    item2 = document.getElementById("order2").checked * price2

    item3 = document.getElementById("order3").checked * price3

    item4 = document.getElementById("order4").checked * price4

    item5 = document.getElementById("order5").checked * price5

    item6 = document.getElementById("order6").checked * price6

    subtotal = item1 + item2 + item3 + item4 + item5 + item6

    vat = subtotal * 0.12 #this calculates for the value added tax given 12% from the guidelines which is equal to 0.12

    total = subtotal + vat #this formulates the total price

    display("Subtotal:", float(subtotal), target="output") #this one displays the subtotal amount of the items. I used float to add the decimal points in the calculation

    display("Value Added Tax:", float(vat), target="output") #this displays the value added tax


    display("Total Amount:", float(total), target="output")
    #this one displays the total amount