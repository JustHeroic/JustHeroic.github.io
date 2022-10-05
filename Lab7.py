def newfunction():
    keylist = ["print","print","print","and","and","break","break","break","global","while","in","in","in","continue","def","elif","elif","or","for","for","return","global"]
    mydict = {}
    for i in keylist:
        if i in mydict.keys():
            mydict[i] = mydict[i] + 1
        else:
           value = 1
           mydict[i] = value

    print('keyword_name\tcount')
    mydict = {k: v for k, v in sorted(mydict.items(), key=lambda y: y[1], reverse=True)}
    for key,value in mydict.items():
       X = key.ljust(17)
       print(X,value)







newfunction()
