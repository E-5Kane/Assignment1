a = """
E1: miles to KM
E2: KM to miles
E3: KG to pounds
E4: pounds to KG
E5: liters to quarts
E6: quarts to liters
E7: mph To KMS
E8: gallons to Liters
E9: water state 
E10: compound interest
E11: model growth
"""
print(a)
print("user pick a conversion")


while True :
    choose = input("choose an option")
    #milesToKM = float(input("how many miles"))
    #KMTomiles = float(input("how many kilometers"))
    #KGTopounds = float(input("how many kilograms"))
    #PoundsToKG = float(input("how many kilograms"))
    #litersToQuarts = float(input("how many liters"))
    #QuartsToliters = float(input("how many quarts"))
    #mphToKMS = float(input("how many mph"))
    #gallonsToLiters = float(input("how many gallons"))


    #miles = milesToKM * 1.60934
    #km = milesToKM * 1.609344
    #KG = PoundsToKG * 2.205
    #pounds = KGTopounds / 2.205
    #liters = literToQuaerts * 1.05669
    #quarts = QuartsToliters / 1.05669
    #KMS = mphToKMS * 0.00044704
    #Liters = gallonsToLiters * 8.34 / 2.204623

    if choose == "E1" :
        milesToKM = float(input("how many miles"))
        km = milesToKM * 1.60934
        print(km)


    if choose == "E2" :
        KMTomiles = float(input("how many kilometers"))
        miles = KMTomiles * 0.621371
        print(miles)


    if choose == "E3" :
        KGTopounds = float(input("how many kilograms"))
        pounds = KGTopounds / 2.205
        print(pounds)


    if choose == "E4" :
        PoundsToKG = float(input("how many pounds"))
        KG = PoundsToKG * 2.205
        print(KG)


    if choose == "E5" :
        litersToQuarts = float(input("how many liters"))
        quarts = litersToQuarts * 1.05669
        print(quarts)


    if choose == "E6" :
        QuartsToliters = float(input("how many quarts"))
        liters = QuartsToliters / 1.05669
        print(liters)

    if choose == "E7" :
        mphToKMS = float(input("how many miles per hour"))
        KMS = mphToKMS * 0.00044704
        print(KMS)

    if choose == "E8" :
        gallonsToLiters = float(input("how many gallons"))
        Liters = gallonsToLiters * 8.34 / 2.204623
        print(Liters)

    if choose == "E9" :
        temperature = float(input("what is the temperature"))
        if temperature < 0 :
            print("ICE")
        elif temperature >= 0 and temperature < 100 :
            print("LIQUID")
        elif temperature >= 100 :
            print("STEAM")

    if choose == "E10" :
        p = float(input("what is the inital investment"))
        a = p*(1 + 0.05 / 12) ** 12 * 1
        print(round(a,2))

    if choose == "E11" :
        p = float(input("what is the inital investment"))
        for i in range(1,11) :
            a = p * (1 + 0.08 / 12) ** i * 1
            print(round(a,2))

    Runagain = input("would you like to convert again?")
    if Runagain == "yes":
        continue

    elif Runagain == "no":
        break
