price=None
quantity=3

if price and not quantity: #if price is availabe and quantity is not availabel
    print("Execute Price Query")
elif not price and quantity:#if price is not availabe and quantity is availabel
    print("Execute Quantity Query")
elif not price and not quantity:#if both are not availabel
    print("Both Are Empty")
elif price and quantity:#if both are  availabel
    print("Execute Both Query")