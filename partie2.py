#!/usr/bin/python3
'''
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 2: Déterminisation

TELLE Alexis | BUT INF 1 2023-2024
'''
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec
import automates

##########################################

@dec.timer
def deterministe(auto: dict) -> bool :
    if len(auto["I"]) != 1:
        return False
    for etat in auto["etats"]:
        dejaVu = set()  # Pour les états qui auraient plusieurs transitions avec une même lettre
        for transition in auto["transitions"]: #TODO: A optimiser avec un filter
            if transition[0] == etat:
                if transition[1] not in dejaVu:
                    dejaVu.add(transition[1])
                else:
                    return False
    return True


@dec.timer
def determinise(auto: dict) -> dict:
    if deterministe(auto):
        return auto

    alphabet = auto["alphabet"]
    etats = auto["etats"]
    transitions = auto["transition"]
    i = auto["I"]
    f = auto["F"]

    # On initialise la 1er ligne du tableau de transitions avec les étiquettes états et celles de l'alphabet
    tableTransitions = [{"etats": list()}] + [{lettre: list()} for lettre in alphabet] 

    # On place sur la 1er ligne en première colonne l'ensemble des états de départ
    tableTransitions["etats"].append(i)

    while True:
        # Tant qu'au moins une case du tableau n'est pas remplie
        lenEtats = len(tableTransitions["etats"])
        for colonne in tableTransitions:
            if len(colonne) != lenEtats:
                # Il reste des cases à remplir
                break
        else:
            # Dans le cas où toutes les cases du tableau sont remplies
            break
        
        # On choisit une case à remplir

        # Si aucune ligne n'est associé à cette valeur, commencer une nouvelle ligne étiquetée par cette valeur

    return dict()


@dec.timer
def renommage(auto: dict) -> dict:
    etats = list()
    transitions = list()
    i = list()
    f = list()
    
    return automates.defauto(auto["alphabet"], etats, transitions, i, f)


def main(): # Cellule de test
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3], "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    auto1 ={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto2={"alphabet":['a','b'],"etats": [0,1], "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

    deterministe(auto0)
    deterministe(auto2)


if __name__ == "__main__":
    main()
