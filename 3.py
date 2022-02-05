import random

while True:
    a = int(input("შეიყვანეთ შუალედის საწყისი ელემენტი: "))
    b = int(input("შეიყვანეთ შუალედის საბოლოო ელემენტი: "))
    n = int(input("შეიყვანეთ ნატურალური რიცხვების რაოდენობა: "))
    user_input= input("შეიყვანეთ უნიკალური რიცხვები(თითოეული რიცხვი გამოყავით მძიმით): ")
    numbers = set((i for i in user_input))

    computer = set(random.sample(range(a,b), k = n))
    intersection = numbers.intersection(computer)
    print(f'მომხმარებლის კოლექცია:{numbers}')
    print(f'კომპიუტერის კოლექცია: {computer}')
    print(f'მომხმარებელმა გამოიცნო {len(intersection)}:{intersection}')
    question = input("გსურთ თუ არა პროგრამის ხელახლა გაშვება? კი/არა")
    if question != "კი":
        break