def polindrome(word):
        word=list(word)
        if word[0]==word[-1]:
            print('It is polindrome')
        else:
            print('It ia not polindrome')
a=input("Enter word ")
polindrome(a)