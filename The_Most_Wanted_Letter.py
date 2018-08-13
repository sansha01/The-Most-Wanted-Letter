def checkio(str):
    str=str.lower()
    result=None
    dict = {'a': 0, 'b': 0, 'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'g': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,
            'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    for letter in str:
        if ord(letter)>=97 and ord(letter)<=122:
           for k in dict.keys():
                if k==letter:
                    dict[k]=dict[k]+1

    newdict=sorted(dict.items(), key=lambda x: x[1], reverse=True)
    list=[]
    list.append(newdict[0][0])
    for i in range(1,len(newdict)):
        if newdict[i][1]==newdict[0][1]:
            list.append(newdict[i][0])
    print(list)
    for letter in str:
        for k in list:


            if letter==k:
                result=letter

            break
    return result


    

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
