def all_thing_is_obj(object: any) -> int:
    type_object = type(object)
    if type_object == str:
        type_name = object + " is in the kitchen"
    else:
        type_name = type_object.__name__

    if (type_object == int):
        print("Type not found")
    else:
        print(type_name, ":", type_object)
    return 42