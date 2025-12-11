def calc_component2_amount():
    try:
        avg_salt1 = float(input("MEASURED SALT%: "))
        amount1 = float(input("BATCH KG: "))
        salt_target = float(input("DESIRED SALT%: "))
        salt2 = float(input("COMPONENT SALT%: "))

        if amount1 == 0:
            print(f"COMPONENT KG: IMPOSIBLE ")
            print(f"NEW BATCH KG: IMPOSIBLE")
        elif salt_target ==avg_salt1:
            print(f"COMPONENT KG: 0")
            print(f"NEW BATCH KG: {amount1:.2f}")

        elif avg_salt1 == salt2 or amount1 == 0 :
            print(f"COMPONENT KG: IMPOSIBLE ")
            print(f"NEW BATCH KG: IMPOSIBLE")

        if salt_target ==avg_salt1:
            print(f"COMPONENT KG: 0.0")
            print(f"NEW BATCH KG: {amount1:.2f}")
         
        
        elif salt_target > avg_salt1 and salt2 <= salt_target:
            print(f"COMPONENT KG: IMPOSIBLE ")
            print(f"NEW BATCH KG: IMPOSIBLE")

        elif salt_target < avg_salt1 and salt2 >= salt_target:
            print(f"COMPONENT KG: IMPOSIBLE ")
            print(f"NEW BATCH KG: IMPOSIBLE")
            


        else:
            # Quotient számítás
            quotient1 = (salt_target - salt2) / (avg_salt1 - salt2)
            quotient2 = 1 - quotient1

            amount2 = amount1 * (quotient2 / quotient1)

        

            print(f"COMPONENT KG: {amount2:.2f}")
            print(f"NEW BATCH KG: {amount2 + amount1:.2f}")

    except Exception as e:
        print(f"ERROR: {str(e)}")




def reversed_calculation():
    try:
        avg_salt1 = float(input("MEASURED SALT%: "))

        salt2 = float(input("COMPONENT SALT%: "))
        amount1 = float(input("BATCH KG: "))
        amount2 = float(input("COMPONENT KG: "))

        salt_backw = ((amount1*avg_salt1)+(amount2*salt2))/ (amount1+amount2)

        print(f"MEASURED SALT%: {salt_backw:.2f}")
        print(f"NEW BATCH KG: {amount1+amount2:.2f}")

    except Exception as e:
        print(f"ERROR: {str(e)}")


def starting():
    print("CHOSE MODE: a-NORMAL CALC. b-BACKWARD CALC.")
    mode = str(input("MODE: "))

    if mode =="a":
        calc_component2_amount()
    elif mode =="b":
        reversed_calculation()
    else:
        print("INVALID MODE")

starting()






