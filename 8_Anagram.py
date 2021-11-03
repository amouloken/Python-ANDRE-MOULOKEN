def anagram(check):




   alist = ["enlists", "google", "inlets", "banana"]


   for i in check:


       for j in alist:


           if (i in j) and check.count(i) == j.count(i):


               continue


           else:


               alist.remove(j)


               print (j + " is not an anagram")


   if alist:


       print (*alist, " is an anagram of " + check)







anagram("listen")

