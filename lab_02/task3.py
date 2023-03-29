questions = ["Jak masz na imię oraz nazwisko? ",
             "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
             "W jakich okolicznościach czytasz książki najczęściej? ",
             "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? "]
answers = []

i = 0
for question in questions:
    answers.append(input(question))
    i = i + 1

i = 0
for question in questions:
    print("Pytanie: " + question)
    print("Odpowiedz: " + answers[i])
    i = i + 1