#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Code principal

TELLE Alexis | BUT INF 1 2023-2024
"""
from subprocess import call

##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec
from partie1 import defauto
from partie2 import deterministe, determinise
from partie3 import complet, complete, complement
from partie4 import intersection, difference
from partie5 import prefixe, suffixe, facteur, miroir
from partie6 import minimise


##########################################


def to_dot(dfa, name="Graph"):
    """ Returns a string corresponding to the specified DFA in DOT format.
        @param dfa  the DFA to be converted in DOT format.
        @param name the name of the automaton for the DOT file ("Graph")
            by default.
        @returns the automaton in DOT format."""
    ret = "digraph " + name + " {\n    rankdir=\"LR\";\n\n"
    ret += "    // States (" + str(len(dfa.states)) + ")\n"

    state_name = lambda s: "Q_" + str(dfa.states.index(s))

    # States
    ret += "    node [shape = point ];     __Qi__ // Initial state\n"  # Initial state
    for state in dfa.states:
        ret += "    "
        if state in dfa.finals:
            ret += "node [shape=doublecircle]; "
        else:
            ret += "node [shape=circle];       "
        ret += state_name(state) + " [label=" + state + "];\n"

    # Transitions
    ret += "\n    // Transitions\n"
    ret += "    __Qi__ -> " + state_name(dfa.init) + "; // Initial state arrow\n"
    for state in dfa.states:
        for (symbol, dst_state) in dfa.transitions[state]:
            ret += "    " + state_name(state) + " -> " + state_name(dst_state) + " [label=" + symbol + "];\n"
    return ret + "}\n"


def to_png(dfa, filename=None, name="Graph"):
    """ Create the PNG image corresponding to the representation of the
        specified DFA in a file.
        The automaton is converted in DOT format and the command dot is called
        in order to generate the PNG.
        @param dfa      the DFA to be converted in PNG.
        @param name     the name of the graph.
        @param filename the name of the PNG file, use the name of the graph if
            not specified. """

    if filename is None:
        filename = name + ".png"

    tmp_file = filename + ".tmp"
    with open(tmp_file, "w") as file:
        file.write(to_dot(dfa, name))

    call(("dot -Tpng " + tmp_file + " -o " + filename).split(" "))
    call(("rm " + tmp_file).split(" "))


def voir_auto(automates: list) -> None:
    if len(automates) == 0:
        print("Vous n'avez aucun automate d'enregistré.")
    for nom, auto in automates:
        print(f"{nom}: {auto}")


def enregistrer_auto() -> tuple:
    nom = input("Veuillez donner un nom à votre automate: ")
    auto = defauto()
    return nom, auto


def appliquer_algo(automates: list) -> None:
    voir_auto(automates)
    nom_auto = input("Veuillez rentrer le nom de l'automate sur lequel appliquer un algorithme: ")
    while nom_auto not in automates:
        voir_auto(automates)
        nom_auto = input("L'automate voulu que vous avez choisi est introuvable, veuillez en choisir un parmi ceux "
                         "disponibles ci-dessus")
    auto = automates[automates.index(nom_auto)]
    algo = input(f"{nom_auto} a bien été choisi. Faites un choix d'algorithme à appliquer :")
    print("1. Savoir si l'automate est déterministe")
    print("2. Déterminiser l'automate")
    print("3. Savoir si l'automate est complet")
    print("4. Compléter l'automate")
    print("5. Obtenir le complément de l'automate")
    print("6. Obtenir l'intersection avec un autre automate")
    print("7. Obtenir la différence avec un autre automate")
    print("8. Obtenir l'automate acceptant l’ensemble des préfixes des mots de l'automate")
    print("9. Obtenir l'automate acceptant l’ensemble des suffixes des mots de l'automate")
    print("10. Obtenir l'automate acceptant l’ensemble des facteurs des mots de l'automate")
    print("11. Obtenir l'automate acceptant l’ensemble des mots miroirs de l'automate")
    print("12. Minimiser l'automate grâce à l'algorithme de Moore")
    print("13. Annuler")

    match algo:
        case "1":
            nouvel_auto = deterministe(auto)
            futur_name = "inconnu"
            print("L'automate est déterministe." if nouvel_auto else "L'automate n'est pas déterministe.")
        case "2":
            nouvel_auto = determinise(auto)
            futur_name = "deterministe"
            print(f"L'automate déterminisé est {nouvel_auto}")
        case "3":
            nouvel_auto = complet(auto)
            futur_name = "inconnu"
            print("L'automate est complet." if nouvel_auto else "L'automate n'est pas complet.")
        case "4":
            nouvel_auto = complete(auto)
            futur_name = "complet"
            print(f"L'automate complété est {nouvel_auto}")
        case "5":
            nouvel_auto = complement(auto)
            futur_name = "complement"
            print(f"L'automate complémenté est {nouvel_auto}")
        case "6":
            voir_auto(automates)
            nom_auto2 = input("Veuillez rentrer le nom de l'automate avec lequel vous voulez faire l'intersection: ")
            auto2 = automates[automates.index(nom_auto2)]
            nouvel_auto = intersection(auto, auto2)
            futur_name = "intersection"
            print(f"L'intersection des deux automates est {nouvel_auto}")
        case "7":
            voir_auto(automates)
            nom_auto2 = input("Veuillez rentrer le nom de l'automate avec lequel vous voulez faire la différence: ")
            auto2 = automates[automates.index(nom_auto2)]
            nouvel_auto = difference(auto, auto2)
            futur_name = "difference"
            print(f"La différence des deux automates est {nouvel_auto}")
        case "8":
            nouvel_auto = prefixe(auto)
            futur_name = "prefixe"
            print(f"L'automate des préfixes est {nouvel_auto}")
        case "9":
            nouvel_auto = suffixe(auto)
            futur_name = "suffixe"
            print(f"L'automate des suffixes est {nouvel_auto}")
        case "10":
            nouvel_auto = facteur(auto)
            futur_name = "facteur"
            print(f"L'automate des facteurs est {nouvel_auto}")
        case "11":
            nouvel_auto = miroir(auto)
            futur_name = "miroir"
            print(f"L'automate miroir est {nouvel_auto}")
        case "12":
            nouvel_auto = minimise(auto)
            futur_name = "minimaliste"
            print(f"L'automate minimisé est {nouvel_auto}")
        case "13":
            futur_name = "inconnu"
            return
        case _:
            print("L'option choisie n'existe pas.")
            return

    if algo != "1" or algo != "3":
        choix = input("Voulez-vous sauvegarder le résultat obtenu ? (O/N)")
        if choix:
            choix = input("Voulez-vous écraser l'automate existant ? (O/N)")
            if choix:
                automates[automates.index(nom_auto)] = nouvel_auto
            else:
                automates.append((f"{nom_auto}_{futur_name}", nouvel_auto))


def convertir_auto(automates: list):
    return


def main():
    automates_enregistres: list[tuple] = list()
    while True:
        print("#" * 20)
        print("Menu des automates")
        print("#" * 20)
        print("1. Voir mes automates")
        print("2. Enregistrer mon automate")
        print("3. Appliquer un algorithme sur un automate")
        print("4. Convertir un automate en .png")
        print("9. Quitter le programme")
        print("#" * 20)
        option = input("Veuillez sélectionner une option: ")
        print("#" * 20)
        match option:
            case "1":
                voir_auto(automates_enregistres)
            case "2":
                nom, auto = enregistrer_auto()
                automates_enregistres.append((nom, auto))
            case "3":
                appliquer_algo(automates_enregistres)
            case "4":
                convertir_auto(automates_enregistres)
            case "9":
                break
            case _:
                print("L'option choisie n'existe pas.")


if __name__ == "__main__":
    main()
