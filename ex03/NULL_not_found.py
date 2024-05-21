def NULL_not_found(object: any) -> int:
    type_object = type(object)
    # print(type_object)
    # print(object)
    if type_object == float and object != object:
        print("Cheese: nan", type_object)
    elif object is None:
        print("Nothing: None", type_object)
    elif type_object == int and object == 0:
        print("Zero: 0", type_object)
    elif type_object == str and object == '':
        print("Empty:", type_object)
    elif type_object == bool and object == False:
        print("Fake: False", type_object)
    elif type_object == list and object == []:
        print("List: []", type_object)
    elif type_object == dict and object == {}:
        print("Dict: {}", type_object)
    elif type_object == tuple and object == ():
        print("Tuple: ()", type_object)
    elif type_object == set and object == set():
        print("Set: set()", type_object)
    else:
        print("Type not found")
        return 1
    return 0