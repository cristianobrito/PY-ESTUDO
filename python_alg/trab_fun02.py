def situacao(nota01, nota02, nota03, nota04):
    media = (nota01 + nota02 + nota03 + nota04) / 4
    if media >= 6:
        return print("Aprovado")
    else:
        return print("Reprovado")


situacao(nota03=10, nota02=3, nota01=6, nota04=5)