#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 3: Complémentation

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec
from partie2 import determinise, renommage

##########################################


@dec.timer
def complet(auto: dict) -> bool:
    for etat in auto["etats"]:
        deja_vu = set()
        for transition in auto["transitions"]:  #TODO: A optimiser avec un filter
            if transition[0] == etat:
                deja_vu.add(transition[1])
        if len(deja_vu) != len(auto["alphabet"]):
            return False
    return True


@dec.timer
def complete(auto: dict) -> dict:
    if complet(auto):
        return auto

    nouvel_auto = {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["I"]),
        "F": list(auto["F"])
    }

    # On récupère l'état avec le numéro le plus grand et on lui ajoute 1, c'est notre état puit
    etat_puits = sorted(auto["etats"])[len(auto["etats"]) - 1] + 1
    nouvel_auto["etats"].append(etat_puits)

    for etat in nouvel_auto["etats"]:
        deja_vu = set()
        for transition in nouvel_auto["transitions"]:
            if transition[0] == etat:
                deja_vu.add(transition[1])

        for lettre in nouvel_auto["alphabet"]:
            if lettre not in deja_vu:
                nouvel_auto["transitions"].append([etat, lettre, etat_puits])

    return nouvel_auto


@dec.timer
def complement(auto: dict) -> dict:
    nouvel_auto = determinise(auto)
    nouvel_auto = renommage(auto)
    nouvel_auto = complete(nouvel_auto)
    nouvel_auto["F"] = [etat for etat in nouvel_auto["etats"] if etat not in nouvel_auto["F"]]
    return nouvel_auto


def main():  # Cellule de test
    auto0 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2, 3],
             "transitions": [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3]], "I": [0], "F": [3]}
    auto1 = {"alphabet": ['a', 'b'], "etats": [0, 1],
             "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'b', 1], [1, 'a', 1]], "I": [0], "F": [1]}
    auto3 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2],
             "transitions": [[0, 'a', 1], [0, 'a', 0], [1, 'b', 2], [1, 'b', 1]], "I": [0], "F": [2]}

    complet(auto0)
    complet(auto1)

    complete(auto0)

    complement(auto3)


if __name__ == "__main__":
    main()
