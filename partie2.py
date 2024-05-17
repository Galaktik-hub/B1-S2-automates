#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 2: Déterminisation

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec

##########################################

@dec.timer
def deterministe(auto: dict) -> bool:
    if len(auto["I"]) != 1:
        return False
    for etat in auto["etats"]:
        deja_vu = set()  # Pour les états qui auraient plusieurs transitions avec une même lettre
        #TODO: A optimiser avec un filter
        for transition in auto["transitions"]:
            if transition[0] == etat:
                if transition[1] not in deja_vu:
                    deja_vu.add(transition[1])
                else:
                    return False
    return True


@dec.timer
def determinise(auto: dict) -> dict:
    """
    Définir une fonction determinise qui déterminise l’automate passé en paramètre
    """
    if deterministe(auto):
        return auto

    nouvel_auto = {
        "alphabet": auto["alphabet"],
        "etats": [],
        "transitions": [],
        "I": auto["I"],
        "F": []
    }

    # On commence à déterminiser par les états initiaux
    etats_a_traiter = [auto["I"]]
    etats_visites = []

    while etats_a_traiter:
        etat_courant = etats_a_traiter.pop(0)

        # Pour éviter les boucles infinies
        if etat_courant not in etats_visites:
            etats_visites.append(etat_courant)
            # Désormais cet état fait partie du nouvel automate
            nouvel_auto["etats"].append(etat_courant)

            for lettre in auto["alphabet"]:
                nouvel_etat = set()
                # Si jamais il y a plusieurs états de l'ancien automate
                for sous_etat in etat_courant:
                    for transition in auto["transitions"]:
                        if transition[0] == sous_etat and transition[1] == lettre:
                            nouvel_etat.add(transition[2])

                # Si le nouvel état possède des transitions possibles
                if nouvel_etat:
                    nouvel_etat = sorted(nouvel_etat)
                    nouvel_auto["transitions"].append([etat_courant, lettre, nouvel_etat])
                    if nouvel_etat not in etats_visites and nouvel_etat not in etats_a_traiter:
                        etats_a_traiter.append(nouvel_etat)

                    # Si jamais le nouvel état posséde un état qui était final, on le rend final
                    if any(etat in auto["F"] for etat in nouvel_etat):
                        if nouvel_etat not in nouvel_auto["F"]:
                            nouvel_auto["F"].append(nouvel_etat)

    return nouvel_auto


@dec.timer
def renommage(auto: dict) -> dict:
    nouvel_auto = {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["I"]),
        "F": list(auto["F"])
    }

    compteur = 0
    for i in range(len(nouvel_auto["etats"])):
        etat = nouvel_auto["etats"][i]

        for j in range(len(nouvel_auto["etats"])):
            if nouvel_auto["etats"][j] == etat:
                nouvel_auto["etats"][j] = compteur

        for j in range(len(nouvel_auto["transitions"])):
            if nouvel_auto["transitions"][j][0] == etat:
                nouvel_auto["transitions"][j][0] = compteur
            if nouvel_auto["transitions"][j][2] == etat:
                nouvel_auto["transitions"][j][2] = compteur

        for j in range(len(nouvel_auto["I"])):
            if nouvel_auto["I"][j] == etat:
                nouvel_auto["I"][j] = compteur

        for j in range(len(nouvel_auto["F"])):
            if nouvel_auto["F"][j] == etat:
                nouvel_auto["F"][j] = compteur

        compteur += 1

    return nouvel_auto


def main():  # Cellule de test
    auto0 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2, 3],
             "transitions": [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3]], "I": [0], "F": [3]}
    auto2 = {"alphabet": ['a', 'b'], "etats": [0, 1],
             "transitions": [[0, 'a', 0], [0, 'a', 1], [1, 'b', 1], [1, 'a', 1]], "I": [0], "F": [1]}

    deterministe(auto0)
    deterministe(auto2)

    renommage(determinise(auto2))


if __name__ == "__main__":
    main()
