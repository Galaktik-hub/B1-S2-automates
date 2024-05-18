#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 5: Propriétés de fermeture

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec

##########################################


def emonde(auto: dict) -> bool:
    """
    Fonction auxiliaire pour vérifier qu'un automate est bien émondé
    """
    #TODO: Faire la fonction
    return True


@dec.timer
def prefixe(auto: dict) -> dict:
    """
    Fonction qui retourne l'automate acceptant l’ensemble des préfixes des mots de l'automate
    """
    assert emonde(auto), "L'automate n'est pas émondé"
    return {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["I"]),
        "F": list(auto["etats"])
    }


@dec.timer
def suffixe(auto: dict) -> dict:
    """
    Fonction qui retourne l'automate acceptant l’ensemble des suffixes des mots de l'automate
    """
    assert emonde(auto), "L'automate n'est pas émondé"
    return {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["etats"]),
        "F": list(auto["F"])
    }


@dec.timer
def facteur(auto: dict) -> dict:
    """
    Fonction qui retourne l'automate acceptant l’ensemble des facteurs des mots de l'automate
    """
    assert emonde(auto), "L'automate n'est pas émondé"
    return {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": list(auto["transitions"]),
        "I": list(auto["etats"]),
        "F": list(auto["etats"])
    }


@dec.timer
def miroir(auto: dict) -> dict:
    """
    Fonction qui retourne l'automate acceptant l’ensemble des mots miroirs de l'automate
    """
    assert emonde(auto), "L'automate n'est pas émondé"
    return {
        "alphabet": list(auto["alphabet"]),
        "etats": list(auto["etats"]),
        "transitions": [transition[::-1] for transition in auto["transitions"]],
        "I": list(auto["F"]),
        "F": list(auto["I"])
    }


def main():
    auto4 = {"alphabet": ['a', 'b'], "etats": [0, 1, 2, ],
             "transitions": [[0, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 2]], "I": [0], "F": [2]}

    prefixe(auto4)
    suffixe(auto4)
    facteur(auto4)
    miroir(auto4)


if __name__ == "__main__":
    main()
