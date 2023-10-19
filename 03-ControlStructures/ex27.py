fb = False
twt = True
ig = True

if fb == True and twt == True and ig == True:
    print("A person can be a good influencer!")
elif fb == True and twt == True and ig == False:
    print("A person can be a good influencer!")
elif fb == True and twt == False and ig == True:
    print("A person can be a good influencer!")
elif fb == False and twt == True and ig == True:
    print("A person can be a good influencer!")
else:
    print("A person CAN'T be a good influencer!")