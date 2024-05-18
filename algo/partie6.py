#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 6: Minimisation

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

from algo.partie2 import deterministe, renommage
from algo.partie3 import complet

##########################################


def minimise(auto: dict) -> dict:
    """
    Fonction qui implémente l'algorithme de minimisation de Moore. Un automate déterministe et complet est nécessaire.
    """
    assert deterministe(auto), "L'automate n'est pas déterministe."
    assert complet(auto), "L'automate n'est pas complet."

    # On commence par la classe d'équivalence 0, les états finaux et non finaux
    classe = [[], []]
    for etat in auto["etats"]:
        if etat in auto["F"]:
            classe[0].append(etat)
        else:
            classe[1].append(etat)

    # On va créer une variable qui va retenir la classe d'équivalence précédenter pour savoir si l'on s'arrête
    ancienne_classe = list()

    # On initialise la table de transitions
    table = {etat: [0] * len(auto["alphabet"]) for etat in auto["etats"]}
    table["alphabet"] = auto["alphabet"]
    for transition in auto["transitions"]:
        table[transition[0]][table["alphabet"].index(transition[1])] = transition[2]

    # On boucle désormais jusqu'à ce que l'on trouve deux classes d'équivalence identiques
    while ancienne_classe != classe:
        ancienne_classe = list(classe)
        nouvelle_classe = list()
        deja_classe = set()
        for groupe in classe:
            # Pour chaque état du groupe
            for i in range(len(groupe)):
                if groupe[i] not in deja_classe:
                    deja_classe.add(groupe[i])

                    # On crée la nouvelle classe
                    nouvelle_classe.append([groupe[i]])
                    transition_i = []

                    # On regarde les classes d'équivalences des transitions de l'état
                    for etat in table[groupe[i]]:
                        for k in range(len(classe)):
                            if etat in classe[k]:
                                transition_i.append(k)

                    # On fait de même pour les autres états du groupe
                    for j in range(i + 1, len(groupe)):
                        transition_j = []
                        for etat in table[groupe[j]]:
                            for k in range(len(classe)):
                                if etat in classe[k]:
                                    transition_j.append(k)

                        # Si les transitions sont dans la même classe, alors on les ajoute à la même classe suivante
                        if transition_i == transition_j:
                            deja_classe.add(groupe[j])
                            nouvelle_classe[-1].append(groupe[j])

        classe = list(nouvelle_classe)

    # On crée le nouvel automate
    nouvel_auto = {
        "alphabet": auto["alphabet"],
        "etats": classe,
        "transitions": [],
        "I": [],
        "F": []
    }

    # On cherche le groupe où l'état initial se trouve
    for etat in nouvel_auto["etats"]:
        if auto["I"][0] in etat:
            nouvel_auto["I"] = etat
            break

    # On s'occupe des transitions
    for etat in nouvel_auto["etats"]:
        for i in range(len(table["alphabet"])):
            for groupe in nouvel_auto["etats"]:
                if table[etat[0]][i] in groupe:
                    nouvel_auto["transitions"].append([etat, table["alphabet"][i], groupe])
                    break

    # On cherche les groupes où les états finaux se trouvent
    for etat_final in auto["F"]:
        for etat in nouvel_auto["etats"]:
            if etat_final in etat and etat not in nouvel_auto["F"]:
                nouvel_auto["F"].append(etat)
                break

    return nouvel_auto


def main():
    auto6 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2, 3, 4, 5],
             "transitions": [[0, 'a', 4], [0, 'b', 3], [1, 'a', 5], [1, 'b', 5],
                             [2, 'a', 5], [2, 'b', 2], [3, 'a', 1], [3, 'b', 0], [4, 'a', 1], [4, 'b', 2], [5, 'a', 2],
                             [5, 'b', 5]], "I": [0], "F": [0, 1, 2, 5]}

    minimise(auto6)
    renommage(minimise(auto6))


if __name__ == "__main__":
    main()
