prijzenkast = ("een knuffelbeer", "een gameconsole", "een fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")
welkeDoos = int(input("welke doos kies je? (typ alleen het nummer van de doos) "))
if welkeDoos == 1:
    print("je hebt " + prijzenkast[0] +" gekregen uit doos 1! gefeliciteerd!")
elif welkeDoos == 2:
    print("je hebt " + prijzenkast[1] +" gekregen uit doos 2! gefeliciteerd!")
elif welkeDoos == 3:
    print("je hebt " + prijzenkast[2] +" gekregen uit doos 3! gefeliciteerd!")
else:
    print("oei! Deze doos heb ik niet! probeer het opnieuw!")