def allergy(score):




   allergylist = ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish", "peanuts", "eggs"]


   score = list((bin(score)[2:]).zfill(len(allergylist)))


   for i in range(len(allergylist)):


       if score[i] == "1":


           print ("You are allergic to : " + allergylist[i])


allergy(12)

