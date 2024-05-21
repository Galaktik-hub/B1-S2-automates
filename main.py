#!/usr/bin/python3
"""
Projet SAE 2-02: Exploration algorithmique d’un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Code principal

TELLE Alexis | BUT INF 1 2023-2024
"""
##########################################
#           IMPORTING SECTION            #
##########################################

from algo.partie1 import defauto
from algo.partie2 import deterministe, determinise, renommage
from algo.partie3 import complet, complete, complement
from algo.partie4 import intersection, difference
from algo.partie5 import prefixe, suffixe, facteur, miroir
from algo.partie6 import minimise
from automates import AUTOMATES
from subprocess import run
from platform import platform
import os.path

##########################################


def auto_to_dot(auto: dict, name: str) -> None:
    """
    Converti le graphe en un fichier au format DOT, format permettant la représentation de graphes sous forme de texte.
    """
    try:
        with open("automates_dot/" + name + ".dot", "x") as file:
            # On commence par définir le graphe, avec une lecture de gauche à droite (LR)
            file.write("digraph " + name + "{\n")
            file.write("\trankdir=LR;\n\n")
            file.write(f"\t// States {len(auto['etats'])}\n")

            # On définit le nombre d'états initiaux
            for i in auto["I"]:
                file.write(f"\tnode [shape = point]; __Qi{i}__; // Etat initial \n")

            # On définit les états et les états finaux
            for etat in auto["etats"]:
                if etat in auto["F"]:
                    file.write(f"\tnode [shape = doublecircle]; Q{etat}[label={etat}];\n")
                else:
                    file.write(f"\tnode [shape = circle]; Q{etat}[label={etat}];\n")

            file.write("\n\t// Transitions\n\n\t// Etats initiaux\n")
            # On fait la liaison entre les états initiaux et leurs points de départ
            for i in auto["I"]:
                file.write(f"\t__Qi{i}__ -> Q{i}\n")

            # On écrit toutes les transitions
            for transition in auto["transitions"]:
                file.write(f"\tQ{transition[0]} -> Q{transition[2]} [label={transition[1]}];\n")

            file.write("}")

        print(f"Le fichier a bien été enregistré sous le nom {name}.dot")

    except FileExistsError:
        print(f"Le fichier existe déjà et est enregistré sous le nom {name}.dot")


def dot_to_png(file, name: str = "automate") -> None:
    """
    Converti un fichier au format DOT sous forme d'une image au format png
    """
    print("ATTENTION")
    print("Si vous êtes sous Linux, vous avez besoin d'avoir installé Graphviz pour convertir le fichier en png (sudo"
          " apt install graphviz)")
    choix = input("Voulez-vous continuer ? (o/n) ")
    if choix == "o":
        if platform().startswith("Windows"):
            dot_path = r"Graphviz\bin\dot.exe"
            file_path = os.path.abspath("automates_dot/" + file + ".dot")
            png_path = os.path.abspath("automates_png/" + name + ".png")
            run(f"\"{dot_path}\" -Tpng {file_path} -o {png_path}", shell=True)
            print("Conversion en png effectuée.")
        else:
            run(f"dot -Tpng automates_dot/{file}.png -o automates_png/{name}", shell=True)
            print("Conversion en png effectuée.")


def voir_auto() -> None:
    print("Affichage des automates disponibles:")
    for nom, auto in AUTOMATES:
        print(f"{nom}: {auto}")


def enregistrer_auto() -> None:
    nom = input("Veuillez donner un nom à votre automate: ")
    auto = defauto()
    _enregistrer_fichier_(nom, auto)
    print("Votre automate a bien été enregistré.")


def _enregistrer_fichier_(nom: str, auto: dict) -> None:
    AUTOMATES.append((nom, auto))
    with open("automates.py", "a") as file:
        file.write(nom + " = {\n")
        file.write(f"\t\"alphabet\": {auto['alphabet']},\n")
        file.write(f"\t\"etats\": {auto['etats']},\n")
        file.write(f"\t\"transitions\": {auto['transitions']},\n")
        file.write(f"\t\"I\": {auto['I']},\n")
        file.write(f"\t\"F\": {auto['F']}\n")
        file.write("}\n")
        file.write(f"AUTOMATES.append((\"{nom}\", {nom}))\n\n")


def choisir_auto() -> tuple:
    voir_auto()
    nom_auto = input("Veuillez rentrer le nom de l'automate sur lequel appliquer un algorithme: ")
    correct = False
    auto = None
    while not correct:
        for i in range(len(AUTOMATES)):
            if AUTOMATES[i][0] == nom_auto:
                auto = AUTOMATES[i][1]
                correct = True
                break
        else:
            voir_auto()
            nom_auto = input("L'automate voulu que vous avez choisi est introuvable, veuillez en choisir un parmi ceux "
                             "disponibles ci-dessus: ")

    return nom_auto, auto


def appliquer_algo() -> None:
    nom_auto, auto = choisir_auto()

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
    algo = input(f"{nom_auto} a bien été choisi. Faites un choix d'algorithme à appliquer : ")

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
            nom_auto2, auto2 = choisir_auto()
            nouvel_auto = intersection(auto, auto2)
            futur_name = "intersection_avec_" + nom_auto2
            print(f"L'intersection des deux automates est {nouvel_auto}")
        case "7":
            nom_auto2, auto2 = choisir_auto()
            nouvel_auto = difference(auto, auto2)
            futur_name = "difference_avec_" + nom_auto2
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
            return
        case _:
            print("L'option choisie n'existe pas.")
            return

    if algo != "1" and algo != "3":
        choix = input("Voulez-vous sauvegarder le résultat obtenu ? (o/n) ")
        if choix == "o":
            choix = input("Voulez-vous renommer les états de l'automate ? (o/n) ")
            if choix == "o":
                _enregistrer_fichier_(f"{nom_auto}_{futur_name}", renommage(nouvel_auto))
            else:
                _enregistrer_fichier_(f"{nom_auto}_{futur_name}", nouvel_auto)


def main():
    while True:
        print("#" * 20)
        print("Menu des automates")
        print("#" * 20)
        print("1. Voir mes automates")
        print("2. Enregistrer mon automate")
        print("3. Appliquer un algorithme sur un automate")
        print("4. Convertir un automate en .dot")
        print("5. Convertir un fichier .dot en .png")
        print("9. Quitter le programme")
        print("#" * 20)
        option = input("Veuillez sélectionner une option: ")
        print("#" * 20)
        match option:
            case "1":
                voir_auto()
            case "2":
                enregistrer_auto()
            case "3":
                appliquer_algo()
            case "4":
                nom_auto, auto = choisir_auto()
                print(f"{nom_auto} a bien été choisi. Conversion en cours...")
                auto_to_dot(auto, nom_auto)
            case "5":
                file = input("Veuillez rentrer le nom du fichier .dot, se trouvant dans le dossier automates_dot, "
                             "à convertir: ")
                name = input("Veuillez rentrer le nom de l'image .png à créer: ")
                dot_to_png(file, name)
            case "9":
                break
            case _:
                print("L'option choisie n'existe pas.")


if __name__ == "__main__":
    main()
