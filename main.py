#jose, rebeca, katherine 


paragraph = "I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all"
list_1 = paragraph.lower()
ask1= input("Choose 1 letter from the Alphabet:   ")
ask2= input("Choose 1 letter from the Alphabet:   ")
ask3= input("Choose 1 letter from the Alphabet:   ")



print(input("The letters you chose were: " + ask1 +ask2 + ask3))

letters= []
letters.append(ask1)
letters.append(ask2)
letters.append(ask3)
print(letters)



print(ask1 + " appears:  " )
print(paragraph.count(ask1)) 
print(ask2 +" appears:  " )
print(paragraph.count(ask2))
print(ask3 +" appears:  " )
print(paragraph.count(ask3))


list = list_1.split(" ")
print(list)

len_list=len(list)
print(len_list)

print("The first letter of this paragraph is " + paragraph[0])
print("The lasta letter of this paragraph is " + paragraph[-1])



paragraph= "I", "pledge", "allegiance", "to", "the", "Flag", "of", "the", "United", "States", "of", "America", "and", "to", "the", "Republic", "for", "which","it", "stands", "one" ,"Nation","under", "God", "indivisible", "with", "liberty", "and", "justice", "for", "all"

print(paragraph[::-1])

print(' '.join(paragraph))
my_bool = paragraph
my_bool = ("python")
