def uvod():
    print("Vítejte v naší originální aplikaci!")
    print("Rádi bychom zjistili něco víc o vás. Zodpovězte prosím následující otázky.")

def zeptej_se_na_jmeno():
    jmeno = input("Jaké je vaše jméno? ")
    print(f"Děkuji, {jmeno}!")

def zeptej_se_na_vek():
    while True:
        vek = input("Kolik vám je let? ")
        if vek.isdigit():
            vek = int(vek)
            if 0 < vek < 100:
                print(f"Děkuji, že jste mi sdělili, že vám je {vek} let.")
                break
            else:
                print("Toto nevypadá na správný věk, zkuste to znovu.")
        else:
            print("Toto není platné číslo, zkuste to znovu.")

def zeptej_se_na_hobby():
    hobby = input("Jaké je vaše oblíbené koníček nebo hobby? ")
    print(f"Skvělé! {hobby} je skvělý způsob, jak trávit volný čas.")

def ukonceni():
    print("Děkuji za odpovědi! Na základě vašich odpovědí vám mohu říct, že jste skvělý člověk!")

if __name__ == "__main__":
    uvod()
    zeptej_se_na_jmeno()
    zeptej_se_na_vek()
    zeptej_se_na_hobby()
    ukonceni()