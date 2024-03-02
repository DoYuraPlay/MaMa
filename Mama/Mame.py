from PIL import Image
print("1.Вы готовы?")
oto=input("2.")
if oto=="Да":
    print("1.Точно?")
    rot=input("2.")
    if rot=="Да":
        print("1.Точно Точно?")
        una=input("2.")
        if una=="Да":
            print("1.Хорошо:")
            image = Image.open('S8Marta.jpg')
            image.show()
        elif una=="Нет":
            print("1.Ну ладно")
        else:
            print("1.Не понемаю")
    elif rot=="Нет":
        print("1.Окей")
    else:
        print("1.Не очень понел")
elif oto=="Нет":
    print("1.Хорошо")
elif oto=="ДА":
    print("1.Не кричите хорошо")
    image = Image.open('S8Marta.jpg')
    image.show()
else:
    print("1.Не очень понел")