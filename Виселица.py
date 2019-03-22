import random
 
vocabulary = ["поезд","машина","самолет","корабль","вертолет",
              "кактус","хризантема","дерево","тюльпан","смородина",
              "телефон","компьютер","телевизор","микроволновка","клавиатура",]
word = random.choice(vocabulary)
len_w = len(word)
len_w = len_w - 1
HP = 10
s = word[1:]
if word == "поезд" or word ==  "машина" or word ==  "самолет" or word == "корабль" or word ==  "вертолет":
    print("Тема: транспорт")
if word == "кактус" or word ==  "хризантема" or word ==  "дерево" or word == "тюльпан" or word ==  "смородина":
    print("Тема: растения")
if word == "телефон" or word ==  "компьютер" or word ==  "телевизор" or word == "микроволновка" or word ==  "клавиатура":
    print("Тема: техника")    
k = 0
used_let = " "
winw = [word[0]]
print("Угадай слово из " , len_w + 1 , "букв, " , "первая буква: " , word[0] )
for i in range(len_w):
    winw += "*"
for i in s:
    if word[0] == i:
        len_w = len_w + 1
while  HP != 0 and len_w != 0:
    T = False
    while True:
        let = input("Введите букву: ")
        let = let.lower()        
        if len(let) > 1:            
            if let == word:
                k = k + 1
            if let != word:
                k = k + 2
        print()
        if let in used_let:
            print("Вы ввели букву , которая уже была")
            print()
        else:
            used_let += let
            break
    count = 0
    for i in word:
        if let in i:
            len_w = len_w -  1
            T = True
            winw[count] = let
        count += 1 
    if k == 1:
        len_w = len_w * 0
        T = True
    if k == 2:
        HP = HP * 0
        print("НЕВЕРНО")
    else:
        if not T:
            HP = HP - 1
            print("Неверно")
            print()
        else:
            print("Верно")
            print()
            print(winw) 
            print()
        print("Ваше здоровье = ", HP) 
        print()
if(len_w == 0):
    print("ПОБЕДА Вы угадали слово: ", word.upper())
else:
    print("ВЫ ПРОИГРАЛИ ")



