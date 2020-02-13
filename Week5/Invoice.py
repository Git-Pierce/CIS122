print("Program 3: Welcome to the Invoice program")

custType = input("Enter customer type (r/w): ")
invoiceTotal = int(input("Enter invoice total: "))

if custType.lower() == "r":
    if (invoiceTotal > 0 and invoiceTotal < 100):
        discount = 0
    elif (invoiceTotal >= 100 and invoiceTotal < 250):
        discount = .1
    elif (invoiceTotal >= 250 and invoiceTotal < 500):
        discount = .1
    elif (invoiceTotal >= 500):
        discount = .25
elif custType.lower() == "w":
    if (invoiceTotal > 0 and invoiceTotal < 500):
        discount = .4
    elif (invoiceTotal >= 500):
        discount = .5
else:
    discount = 0

discountAmount = invoiceTotal * discount;
newDiscountTotal = invoiceTotal - discountAmount;

print("Discounted Amount: ${}".format(discountAmount))
print("New Total after discount: ${}".format(newDiscountTotal))
