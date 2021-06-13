# Napisati program koji za uneti pozitivan cetvorocifreni broj racuna njegove cifre jedinica, desetica i stotina, 
# a potom ispisati najvecu cifru.
# Program takodje treba ispisati gresku ukoliko uneti broj nije cetvorocifren.

trazeni_broj = int(input("Unesite neki cetvorocifreni broj: "))

jedinica = trazeni_broj%10

desetica = trazeni_broj//10%10

stotina = trazeni_broj//100%10

hiljada = trazeni_broj//1000
# Konvertujemo varijablu najveci_broj u string, i trazimo najvecu vrednost.
najveci_broj = max(str(trazeni_broj))

if trazeni_broj>999 and trazeni_broj<9999:
    print(f"Uneti broj sadrzi: hiljada {hiljada}, stotina {stotina}, desetica {desetica}, jedinica {jedinica} i najveci broj je {najveci_broj}!")

else:
    print("Uneti broj nije cetvorocifren!")