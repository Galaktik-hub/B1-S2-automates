#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d'un problème

Ce fichier est un groupement de plusieurs automates vus en cours
De plus, il contient les automates enregistrés dans par l'utilisateur

NE RIEN SUPPRIMER AU DESSUS DE LA LIGNE DE SÉPARATION

TELLE Alexis | BUT INF 1 2023-2024
"""

AUTOMATES = list()

td2exo3autoi = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, "b", 2], [1, "b", 4], [2, "a", 3], [2, "b", 3], [3, "a", 2], [3, "b", 2], [3, "b", 4],
                    [5, "a", 5], [5, "b", 5], [5, "a", 4]],
    "I": [1, 5],
    "F": [4]
}
AUTOMATES.append(("td2exo3autoi", td2exo3autoi))

####################################################

test = {
	"alphabet": ['a', 'b'],
	"etats": [0, 1],
	"transitions": [[0, 'a', 1], [1, 'a', 1], [1, 'b', 1]],
	"I": [0],
	"F": [1]
}
AUTOMATES.append(("test", test))
