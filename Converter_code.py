import json


data = json.load(open("conv_json.json"))

def convert(unittype, oldvalue, oldunit, newunit):
    conv = data[unittype]
    # print(conv)
    for i in conv:
        for k,v in i.items():
            if k == oldunit:
                sourceUnit = v
            if k == newunit:
                desUnit = v

    newValue = (float(oldvalue) * (sourceUnit)) / (desUnit)
    print("Value in "+newunit,newValue)

def userInputSwitch(arg):
    switcher = {
        1:"MassConv",
        2:"LengthConv",
        3:"ForceConv"
    }
    return switcher.get(arg,"nothing")

def main():
    userInp = int(input("Choose:\n"
                 "1:Mass\n"
                 "2:Length\n"
                 "3:Force\n"))

    userChoiceUnitType = (userInputSwitch(userInp))
    print("-------Available source units-------")
    for k in data[userChoiceUnitType]:
        for i in k.keys():
            print(i)
    print("------------------------------------")
    userSourceUnit = input("Type source unit from above options:")
    userNewUnit = input("Type desired unit:")
    userSourceValue = input("Enter source value:")
    convert(userChoiceUnitType,userSourceValue,userSourceUnit,userNewUnit)

if __name__ == '__main__':
    main()