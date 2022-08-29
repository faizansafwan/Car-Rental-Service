

vehicle = []
v_id = []
v_model = []
v_no = []
v_type = []
v_quantity = []
job_assign = []
car_id = []
van_id = []
wheel_id = []
lorry_id = []
truck_id = []

while True:
    title = 'Welcome to Cab service.'
    print(title)

    choose_user_type = input(
        "Enter 'a' if you want to start as admin, if not enter 'c' to continue as hire vehicle: \n").lower()

    if choose_user_type == 'a':
        print('You selected as admin')

        vehicle_type = " Car = 'c'\n Van = 'v'\n 3 wheel = 'tw'\n Lorry = 'l'\n Truck = 'tr' "
        print(vehicle_type)

        select_vehicle_type = input("Enter 'c' or 'v' or 'tw' or 'l' or 'tr': ")
        if select_vehicle_type == 'c':
            next_step = input("Enter 'add' to add car to system or Enter 'del' to remove car from system"
                             " or Enter 'menu' to go back or Enter 'ct' get vehicle detail: ").lower()

            if next_step == 'add':
                Id = input("ID(xxxx): ")
                model = input("Model(eg- Benz): ")
                num = input("Vehicle Number(eg- LN-xxxx): ")
                Type = input("Vehicle Type(A-AC OR N-NON AC): ").upper()
                quantity = input("number of seats- '3' or '4': ")
                if len(Id) == 4 and len(model) > 1 and (len(num) == 7 or len(num) == 8) and \
                        (quantity == '3' or quantity == '4') and len(Type) == 1:
                    v_id.append("c"+Id)
                    v_model.append(model)
                    v_no.append(num)
                    v_quantity.append(quantity)
                    if Type == 'A':
                        v_type.append('AC')
                    elif Type == 'N':
                        v_type.append('NON AC')
                    vehicle.append('Car')
                    print("you have successfully inserted vehicle to the system")
                else:
                    print("wrong Input, Enter correct format")

            elif next_step == 'ct':
                for l in v_id:
                    if 'c' in l and l not in car_id:
                        car_id.append(l)
                for n in v_id:
                    print("Car ID's: ", car_id)
                    print("Vehicle ID's: ", v_id)
                    search_id = input("Input your ID: ")
                    if search_id in v_id:
                        a = v_id.index(search_id)
                        print(f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                              f" Quantity- {v_quantity[a]}  ")
                        just = input("If you want to go main menu- 'c', or Enter any key to continue")
                        if just == 'c':
                            break

            elif next_step == 'del':
                for n in v_id:
                    print("Vehicle ID's: ", v_id)
                    del_user = input("Enter vehicle ID to delete data: ")
                    a = v_id.index(del_user)
                    b = f"Vehicle ID - {v_id.pop(a)}  Model- {v_model.pop(a)}  Number- {v_no.pop(a)}  Type- {v_type.pop(a)} "
                    print(f"you have deleted: {b} ")
                    if del_user in car_id:
                        car_id.remove(del_user)
                    just = input("If you want to go main menu- 'c', or Enter any key to continue")
                    if just == 'c':
                        break


        elif select_vehicle_type == 'v':
            next_step = input("Enter 'add' to add van to system or Enter 'del' to remove van from system"
                             " or Enter 'menu' to go back or Enter 'ct' get vehicle detail: ").lower()

            if next_step == 'add':
                Id = input("ID: ")
                model = input("Model(eg- Benz): ")
                num = input("Vehicle Number(eg- LN-xxxx): ")
                Type = input("Vehicle Type(A-AC OR N-NON AC): ").upper()
                quantity = input("number of seats- '6' or '8': ")
                if len(Id) == 4 and len(model) > 1 and (len(num) == 7 or len(num) == 8) and \
                        (quantity == '6' or quantity == '8') and len(Type) == 1:
                    v_id.append('v'+Id)
                    v_model.append(model)
                    v_no.append(num)
                    v_quantity.append(quantity)
                    if Type == 'A':
                        v_type.append('AC')
                    elif Type == 'N':
                        v_type.append('NON AC')
                    vehicle.append('Van')
                    print("you have successfully inserted vehicle to the system")
                else:
                    print("wrong Input, Enter correct format")

            elif next_step == 'ct':
                for l in v_id:
                    if 'v' in l and l not in van_id:
                        van_id.append(l)
                for n in v_id:
                    print("Van ID's:", van_id)
                    print("Vehicle ID's:",  v_id)
                    search_id = input("Input your ID: ")
                    if search_id in v_id:
                        a = v_id.index(search_id)
                        print(f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                              f" Quatity- {v_quantity[a]}  ")
                        just = input("If you want to go main menu- 'c', or Enter any key to continue")
                        if just == 'c':
                            break

            elif next_step == 'del':
                for n in v_id:
                    print("Vehicle ID's: ", v_id)
                    del_user = input("Enter vehicle ID to delete data: ")
                    a = v_id.index(del_user)
                    b = f"Vehicle ID- {v_id.pop(a)}  Model- {v_model.pop(a)}  Number- {v_no.pop(a)}   Type- {v_type.pop(a)}"
                    print(f"you hav deleted: {b}")
                    if del_user in van_id:
                        van_id.remove(del_user)
                    just = input("If you want to go main menu- 'c', or Enter any key to continue")
                    if just == 'c':
                        break

        elif select_vehicle_type == 'tw':
            next_step = input("Enter 'add' to add van to system or Enter 'del' to remove van from system"
                              " or Enter 'menu' to go back or Enter 'ct' get vehicle detail: ").lower()

            if next_step == 'add':
                Id = input("ID: ")
                model = input("Model(eg- Benz): ")
                num = input("Vehicle Number(eg- LN-xxxx): ")
                Type = 'None'
                if len(Id) == 4 and len(model) > 1 and (len(num) == 7 or len(num) == 8):
                    v_id.append('tw'+Id)
                    v_model.append(model)
                    v_no.append(num)
                    v_type.append(Type)
                    v_quantity.append(3)
                    vehicle.append('Three Wheel')
                    print("you have successfully inserted vehicle to the system")
                else:
                    print("wrong Input, Enter correct format")

            elif next_step == 'ct':
                for l in v_id:
                    if 'tw' in l and l not in wheel_id:
                        wheel_id.append(l)
                for n in v_id:
                    print("Van ID's:", wheel_id)
                    print("Vehicle ID's: ", v_id)
                    search_id = input("Input your ID: ")
                    if search_id in v_id:
                        a = v_id.index(search_id)
                        print(f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                              f"Quantity- {v_quantity[a]} seats  ")
                        just = input("If you want to go main menu- 'c', or Enter any key to continue")
                        if just == 'c':
                            break

            elif next_step == 'del':
                for n in v_id:
                    print("Vehicle ID's: ", v_id)
                    del_user = input("Enter vehicle ID to delete data: ")
                    a = v_id.index(del_user)
                    b = f"Vehicle ID- {v_id.pop(a)}  Model- {v_model.pop(a)}  Number- {v_no.pop(a)}   Type- {v_type.pop(a)}"
                    print(f"you hav deleted: {b}")
                    if del_user in wheel_id:
                        wheel_id.remove(del_user)
                    just = input("If you want to go main menu- 'c', or Enter any key to continue")
                    if just == 'c':
                        break

        elif select_vehicle_type == 'l':
            next_step = input("Enter 'add' to add Lorry to system or Enter 'del' to remove Lorry from system"
                              " or Enter 'menu' to go back or Enter 'ct' get vehicle detail: ").lower()

            if next_step == 'add':
                Id = input("ID: ")
                model = input("Model(eg- Benz): ")
                num = input("Vehicle Number(eg- LN-xxxx): ")
                quantity = input("Size- '7' or '12': ")
                if len(Id) == 4 and len(model) > 1 and (len(num) == 7 or len(num) == 8) and \
                        (quantity == '7' or quantity == '12'):
                    v_id.append("l" + Id)
                    v_model.append(model)
                    v_no.append(num)
                    v_quantity.append(quantity + 'ft')
                    v_type.append('None')
                    vehicle.append('Lorry')
                    print("you have successfully inserted vehicle to the system")
                else:
                    print("wrong Input, Enter correct format")

            elif next_step == 'ct':
                for l in v_id:
                    if 'l' in l and l not in lorry_id:
                        lorry_id.append(l)
                for n in v_id:
                    print("Van ID's:", lorry_id)
                    print("Vehicle ID's: ", v_id)
                    search_id = input("Input your ID: ")
                    if search_id in v_id:
                        a = v_id.index(search_id)
                        print(
                            f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                            f" Quantity- {v_quantity[a]}  ")
                        just = input("If you want to go main menu- 'c', or Enter any key to continue")
                        if just == 'c':
                            break

            elif next_step == 'del':
                for n in v_id:
                    print("Vehicle ID's: ", v_id)
                    del_user = input("Enter vehicle ID to delete data: ")
                    a = v_id.index(del_user)
                    b = f"Vehicle ID - {v_id.pop(a)}  Model- {v_model.pop(a)}  Number- {v_no.pop(a)}  Type- {v_type.pop(a)} "
                    print(f"you have deleted: {b} ")
                    if del_user in lorry_id:
                        lorry_id.remove(del_user)
                    just = input("If you want to go main menu- 'c', or Enter any key to continue")
                    if just == 'c':
                        break


        elif select_vehicle_type == 'tr':
            next_step = input("Enter 'add' to add Truck to system or Enter 'del' to remove Truck from system"
                              " or Enter 'menu' to go back or Enter 'ct' get vehicle detail: ").lower()

            if next_step == 'add':
                Id = input("ID: ")
                model = input("Model(eg- Benz): ")
                num = input("Vehicle Number(eg- LN-xxxx): ")
                quantity = input("Max load and size(kg)- '2500' or '3500': ")
                if len(Id) == 4 and len(model) > 1 and (len(num) == 7 or len(num) == 8) and \
                        (quantity == '2500' or quantity == '3500'):
                    v_id.append("tr" + Id)
                    v_model.append(model)
                    v_no.append(num)
                    v_quantity.append(quantity + 'kg')
                    v_type.append('None')
                    vehicle.append('Truck')
                    print("you have successfully inserted vehicle to the system")
                else:
                    print("wrong Input, Enter correct format")

            elif next_step == 'ct':
                for l in v_id:
                    if 'tr' in l and l not in truck_id:
                        truck_id.append(l)
                for n in v_id:
                    print("Truck ID's:", truck_id)
                    print("Vehicle ID's: ", v_id)
                    search_id = input("Input your ID: ")
                    if search_id in v_id:
                        a = v_id.index(search_id)
                        print(
                            f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                            f" Quantity- {v_quantity[a]}  ")
                        just = input("If you want to go main menu- 'c', or Enter any key to continue")
                        if just == 'c':
                            break

            elif next_step == 'del':
                for n in v_id:
                    print("Vehicle ID's: ", v_id)
                    del_user = input("Enter vehicle ID to delete data: ")
                    a = v_id.index(del_user)
                    b = f"Vehicle ID - {v_id.pop(a)}  Model- {v_model.pop(a)}  Number- {v_no.pop(a)}  Type- {v_type.pop(a)} "
                    print(f"you have deleted: {b} ")
                    if del_user in truck_id:
                        truck_id.remove(del_user)
                    just = input("If you want to go main menu- 'c', or Enter any key to continue")
                    if just == 'c':
                        break


    elif choose_user_type == "c":
        print("you have selected to hire a vehicle")

        print(v_id)
        print("Available Vehicle list")
        for n in v_id:
            a =v_id.index(n)
            print(
                f"{vehicle[a]}: ID- {v_id[a]},  Model- {v_model[a]}, Number- {v_no[a]}, Type- {v_type[a]},"
                f" Quantity- {v_quantity[a]}  ")

        hire_vehicle = input('Enter Vehicle ID to hire: ')

        x = v_id.index(hire_vehicle)
        print(x)

        v_id_assign = v_id.pop(x)
        v_model_assign = v_model.pop(x)
        v_no_assign = v_no.pop(x)
        v_type_assign = v_type.pop(x)
        v_quantity_assign = v_quantity.pop(x)
        vehicle_assign = vehicle.pop(x)
        b = {
            "Vehicle": vehicle_assign,
            "ID": v_id_assign,
            "Model": v_model_assign,
            "NO.": v_no_assign,
            "Type": v_type_assign,
            "Quantity": v_quantity_assign
        }
        job_assign.append(b)
        print(job_assign)
        q = f"Vehicle - {vehicle_assign} Vehicle ID - {v_id_assign}  Model- {v_model_assign}  " \
            f"Number- {v_no_assign}  Type- {v_type_assign}  Quantity- {v_quantity_assign} "
        print(f"you have hired: {q} ")

    else:
        exit()





