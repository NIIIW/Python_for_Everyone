money=float(input("Insert your money(baht) : "))
style=str(input("Insert your style : "))

stylecheck=["Thai","Japanese","Korean","Chinese"]

car_brand={"red":100,"blue":200,"green":300}

if money>1500 and style in stylecheck:
    print("You can come in restaurant.")
    

def checkyourstyle(style,money):
    stylecheck=["Thai","Japanese","Korean","Chinese"]
    if money>1500 and style in stylecheck:
        print("You can come in restaurant.")
    else:
        print("You can not come in restaurant.")
        
print("---------end---------")