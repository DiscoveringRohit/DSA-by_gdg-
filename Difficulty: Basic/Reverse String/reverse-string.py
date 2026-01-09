def reverseString(s):
    #code here revers=[]

    revers=[]
    for i in range(len(s)-1,-1,-1):
           revers.append(s[i])
    revers= "".join(revers)
    return revers
