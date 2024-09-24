dictionary = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

"""Hur skulle du identifiera vilket projekt Erik har spenderat mest tid på?"""

def projekt_med_flest_timmar(projekt, namn): # Denna funktion berättar vilket projekt som en person har spenderat mest tid på
    
    timmar = [0]
    for i in projekt:
        for j in projekt[i]:
            if namn in j:
                timmar.append(projekt[i][j])
    else:
        if timmar == [0]:
            print("Personen finns ej med i några projekt")
        else:    
            for i in projekt:
                for j in projekt[i]:
                    if namn in j and projekt[i][j] == max(timmar):
                        return print(i)
    
projekt_med_flest_timmar(dictionary, "Erik")



"""Hur skulle du skapa en ny dictionary som bara innehåller projekten där Lina har arbetat mer än 30 timmar?"""

def uppdaterad_dictionary(projekt, namn): # Denna funktion skapar en ny dictionary beroende på om personen har arbetat mer en 30 timmar i något projekt
    
    ny_projekt = {}
    for i in projekt:
            for j in projekt[i]:
                if namn in j and projekt[i][j] > 30:
                    ny_projekt.update({i: projekt[i]})
    else:
        if ny_projekt == {}:
           print("Personen finns ej med i några projekt")
        else:
            return print(ny_projekt)

uppdaterad_dictionary(dictionary, "Lina")
                





