#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 4: Automate produit

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec
from partie2 import deterministe, renommage
from partie3 import complete

##########################################


def produit(auto1: dict, auto2: dict) -> dict:
    """
    Fonction intermédiaire faisant le produit de deux automates, les transitions finales ne sont pas traitées.
    """
    assert auto1["alphabet"] == auto2["alphabet"], "Les automates n'ont pas le même alphabet."
    assert deterministe(auto1) and deterministe(auto2), "Les automates ne sont pas déterministes."

    nouvel_auto = {
        "alphabet": auto1["alphabet"],
        "etats": [],
        "transitions": [],
        "I": [(auto1["I"][0], auto2["I"][0])],
        "F": []
    }

    # On initialise mes états à traiter et ceux visités
    etats_a_traiter = [nouvel_auto["I"][0]]
    etats_visites = []

    while etats_a_traiter:
        (etat1, etat2) = etats_a_traiter.pop()
        nouvel_etat = (etat1, etat2)

        if nouvel_etat not in etats_visites:
            etats_visites.append(nouvel_etat)
            nouvel_auto["etats"].append(nouvel_etat)

            # On regarde les transitions possibles pour chaque lettre de l'alphabet
            for lettre in nouvel_auto["alphabet"]:

                # On vérifie si une transition existe dans l'automate 1
                for transition in auto1["transitions"]:
                    if transition[0] == etat1 and transition[1] == lettre:
                        new_etat1 = transition[2]
                        break
                else:
                    new_etat1 = False

                # On vérifie si une transition existe dans l'automate 2
                for transition in auto2["transitions"]:
                    if transition[0] == etat2 and transition[1] == lettre:
                        new_etat2 = transition[2]
                        break
                else:
                    new_etat2 = False

                if type(new_etat1) is int and type(new_etat2) is int:
                    nouvel_auto["transitions"].append([(etat1, etat2), lettre, (new_etat1, new_etat2)])
                    if (new_etat1, new_etat2) not in etats_visites:
                        etats_a_traiter.append((new_etat1, new_etat2))

    return nouvel_auto


@dec.timer
def intersection(auto1: dict, auto2: dict) -> dict:
    """
    Fonction qui, étant donnée deux automates déterministes, retourne l'automate produit qui accepte l'intersection des
    ces deux automates.
    """
    nouvel_auto = produit(auto1, auto2)
    for (etat1, etat2) in nouvel_auto["etats"]:
        if etat1 in auto1["F"] and etat2 in auto2["F"] and (etat1, etat2) not in nouvel_auto["F"]:
            nouvel_auto["F"].append((etat1, etat2))
    return nouvel_auto


@dec.timer
def difference(auto1: dict, auto2: dict) -> dict:
    """
    Fonction qui, étant donnée deux automates déterministes, retourne l'automate produit qui accepte la différence de
    auto1 par auto2.
    """
    nouvel_auto = produit(complete(auto1), complete(auto2))
    for (etat1, etat2) in nouvel_auto["etats"]:
        if etat1 in auto1["F"] and etat2 not in auto2["F"] and (etat1, etat2) not in nouvel_auto["F"]:
            nouvel_auto["F"].append((etat1, etat2))
    return nouvel_auto


def main():  # Cellule de test
    auto4 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2, ],
             "transitions": [[0, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 2]], "I": [0], "F": [2]}
    auto5 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2],
             "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 0]], "I": [0],
             "F": [0, 1]}

    intersection(auto4, auto5)
    renommage(intersection(auto4, auto5))
    renommage(difference(auto4, auto5))


if __name__ == "__main__":
    main()
