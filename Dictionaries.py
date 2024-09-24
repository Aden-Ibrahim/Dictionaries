dictionary = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

"""Hur skulle du identifiera vilket projekt Erik har spenderat mest tid på?"""

def projekt_med_flest_timmar(projekt_lista, anställd): # Denna funktion berättar vilket projekt som en person har spenderat mest tid på

    timmar = [0]
    
    for projekt in projekt_lista:
        for projekt_anställd in projekt_lista[projekt]:
            if anställd == projekt_anställd:
                timmar.append(projekt_lista[projekt][projekt_anställd])

    if timmar == [0]:
        print("Personen finns ej med i några projekt")

    else:    
        for projekt in projekt_lista:
            for projekt_anställd in projekt_lista[projekt]:
                if anställd == projekt_anställd and projekt_lista[projekt][projekt_anställd] == max(timmar):
                    return print(projekt)
    
projekt_med_flest_timmar(dictionary, "Erik")


"""Hur skulle du skapa en ny dictionary som bara innehåller projekten där Lina har arbetat mer än 30 timmar?"""

def uppdaterad_dictionary(projekt_lista, anställd): # Denna funktion skapar en ny dictionary beroende på om personen har arbetat mer en 30 timmar i något projekt
    
    ny_projekt = {}

    for projekt in projekt_lista:
        for projekt_anställd in projekt_lista[projekt]:
            if anställd == projekt_anställd and projekt_lista[projekt][projekt_anställd] > 30:
                ny_projekt.update({projekt: projekt_lista[projekt]})
    
    if ny_projekt == {}:
        print("Personen finns ej med i några projekt i mer än 30 timmar")

    else:
        return print(ny_projekt)

uppdaterad_dictionary(dictionary, "Lina")