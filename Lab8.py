def getStringInfo(*args):
    for i in range(0,len(args)):
        print('{:30}-{:13}'.format("#of words", len(args[i].split())))
        numberofcharacterswhitespace(args[i])
        numberofcharacters(args[i])
        numberofletters(args[i])
        numberofdigits(args[i])
        numberofpunctuation(args[i])
        l = args[i]
        x =l.isdigit()
        print(('{:30}-{:13}'.format("is number",x)))
        numberofuppercase(args[i])
        numberoflowercase(args[i])
        uppercasestring(args[i])
        lowercasestring(args[i])
        swapcasestring(args[i])
        nospacestring(args[i])
        tittlestring(args[i])
        reversestring(args[i])
        print("****************************************************************")


    return

def numberofcharacterswhitespace(p):

    return print(('{:30}-{:13}'.format("# of characters", len([x for x in p if
                                                                            x.isalpha() or x.isdigit() or x.isspace() or not x.isalpha() and not x.isdigit() and not x.isspace()])
                 )))


def numberofcharacters(p):
    return print(('{:30}-{:13}'.format("# of characters (Excl. w/s)", len([x for x in p if
                                                             x.isalpha() or x.isdigit() or not x.isalpha() and not x.isdigit() and not x.isspace()])
                 )))

def numberofletters(p):

    return  print(('{:30}-{:13}'.format("# of letters",len([x for x in p if x.isalpha()]))))

def numberofdigits(p):

    return  print(('{:30}-{:13}'.format("# of digits",len([x for x in p if x.isdigit()]))))

def numberofpunctuation(p):

    return  print(('{:30}-{:13}'.format("# of punctuation",len([x for x in p if not x.isalpha() and not x.isdigit() and not x.isspace()])
    )))

def numberofuppercase(p):

    return  print(('{:30}-{:13}'.format("# of uppercase chars",len([x for x in p if x.isupper()]))))

def numberoflowercase(p):

    return  print(('{:30}-{:13}'.format("# of lowercase chars",len([x for x in p if x.islower()]))))

def uppercasestring(p):

    count = p.upper()
    return print(('{:30}-{:20}'.format("uppercase",count)))

def lowercasestring(p):


    count = p.lower()
    return print(('{:30}-{:20}'.format("lowercase",count)))

def swapcasestring(p):

   count = p.swapcase()
   return print(('{:30}-{:20}'.format("reversed",count)))

def nospacestring(p):

    count = p.replace(" ", "")
    return print(('{:30}-{:20}'.format("no space ",count)))


def tittlestring(p):

    count = p.title()
    return print(('{:30}-{:30}'.format("title",count)))

def reversestring(p):

    count = p[::-1]
    return print(('{:30}-{:40}'.format("reverse",count)))

getStringInfo("HeLlO wOrLd!!11", "Did you hear about the one-eyed  one-horned Flying Purple People Eater?")




