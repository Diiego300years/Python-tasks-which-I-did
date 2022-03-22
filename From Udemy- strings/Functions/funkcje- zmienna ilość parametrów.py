def DoAction(action, *parameter):   #  *sprawia że robi sie tupla i można wpisać więcej elementów
    print("action: ", action)
    print("parameter: ", parameter)
    return

DoAction("kup", "buty", "skarpetki")



def DoAction2(action, what, **parameter):   #  **sprawia że robi sie dictionary i można wpisać więcej elementów
    print("action: ", action)
    print("what: ", what)
    print("parameter: ", parameter)
    for element in parameter:
        print(element, "=", parameter[element])  #żeby ładne wyprintowało
    return

DoAction2("buy, ", "shoes, ", size=45, color="red", type="sport")

