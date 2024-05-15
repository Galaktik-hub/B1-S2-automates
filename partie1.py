#!/usr/bin/python3
'''
Projet SAE 2-02: Exploration algorithmique d'un problème

Les décorateurs ont pour but de tester les fonctions définies dans cette partie avec un aperçu des performances.

Partie 1: Mots, langages et automates...

TELLE Alexis | BUT INF 1 2023-2024
'''
##########################################
#           IMPORTING SECTION            #
##########################################

import decorators as dec

##########################################

################# 1.1 ####################

@dec.timer
def pref(u: str) -> list[str]:  # 1.1.1
    """Retourne une liste de tous les préfixes du mot u."""
    return [u[:i] for i in range(len(u) + 1)]  # Utilisation de la création de liste par compréhension et des slices


@dec.timer
def suf(u: str) -> list[str]:  # 1.1.2
    """Retourne une liste de tous les suffixes du mot u."""
    return [u[i:] for i in range(len(u) + 1)]  # Utilisation de la création de liste par compréhension et des slices


@dec.timer
def fact(u: str) -> list[str]:  # 1.1.3
    """Retourne une liste sans doublons de tous les facteurs du mot u."""
    res: set[str] = {u[i:j] for i in range(len(u)) for j in range(i,
                                                                  len(u) + 1)}  # Ici, un set est utilisé pour éviter les doublons et ainsi optimiser les performances
    return sorted(list(
        res))  # On renvoie la liste triée pour une meilleure lisibilité de la réponse, mais ce n'est pas obligatoire et peut être retiré pour optimiser les performances


@dec.timer
def miroir(u: str) -> str:  # 1.1.4
    """Retourne le mot miroir de u."""
    return u[::-1]  # Simple utilisation des slices pour effectuer le miroir du mot


################# 1.2 ####################

@dec.timer
def concatene(l1: list[str], l2: list[str]) -> list[str]:  # 1.2.1
    """Retourne une liste de tous les mots obtenus en copncaténant les mots de l1 avec les mots de l2."""
    res: set[str] = {f'{u}{v}' for u in l1 for v in
                     l2}  # Ici, un set est utilisé pour éviter les doublons et ainsi optimiser les performances
    return sorted(list(
        res))  # On renvoie la liste triée pour une meilleure lisibilité de la réponse, mais ce n'est pas obligatoire et peut être retiré pour optimiser les performances


@dec.timer
def puis(l: list[str], n: int) -> list[str]:  # 1.2.2
    """Retourne une liste de tous les mots du langage l puissance n."""
    res: set[str] = ['']  # Initialisation de la liste de mots avec le mot vide
    for _ in range(n):
        res = [u + v for u in l for v in res]  # On concatène chaque mot de l avec chaque mot de res n fois
    return res


# 1.2.3
# Il n'est pas possible d'implémenter la fonction permettant de calculer l'étoile d'un langage pour la simple et 
#bonne raison que l'étoile d'un langage est possiblement infinie et que (pour le moment, peut-être) les technologies ont des ressources limitées


@dec.timer
def tousmots(a: list[str], n: int) -> list[str]:  # 1.2.4
    """Retourne une liste de tous les mots du langage a* de longueur inférieure n."""
    res: list[str] = list()
    for i in range(n + 1):
        for u in puis(a, i):  # On ajoute tous les mots de a^i à la liste
            res.append(u)
    return res


################# 1.3 ####################

@dec.timer
def defauto(alphabet: list[str], etats: list, transitions: list[list], i: list[int], f: list[int]) -> dict:  # 1.3.1
    """Retourne un automate sous forme d'un dictionnaire."""
    return {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": i,
        "F": f
    }


@dec.timer
def lirelettre(t: list[list], e: list[int], a: str) -> list[int]:  # 1.3.2
    """Retourne la liste des états dans lesquels on peut arriver en partant d'un état de E et en lisant la lettre a."""
    res: set[int] = set()
    for i in range(len(t)):
        if t[i][1] == a and t[i][0] in e:
            res.add(t[i][2])
    return list(res)


@dec.timer
def liremot(t: list[list], e: list[int], m: str) -> list[int]:  # 1.3.3
    """Renvoie la liste des états dans lesquels on peut arriver en partant d'un état de E et en lisant le mot m."""
    if len(m) == 0:  # Si le mot est vide, on renvoie la liste de tous les états de E
        return e
    res: set[int] = set()
    for i in range(len(t)):
        if t[i][1] == m[0] and t[i][0] in e:  # Si on peut lire le premier caractère du mot
            if len(m) == 1:  # Si on a lu le dernier caractère du mot (Cas de base)
                res.add(t[i][2])
            else:  # Sinon, on continue la lecture du mot (Appels récursifs)
                suiteMot: list[int] = liremot(t, [t[i][2]], m[1:])
                res.update(suiteMot)  # On met à jour la liste des états atteignables pour former le mot
    return list(res)


@dec.timer
def accepte(automate: dict, m: str) -> bool:  # 1.3.4
    """Renvoie True si le mot m est accepté par l'automate, False sinon."""
    return len(liremot(automate["transitions"], automate["etats"], m)) > 0


@dec.timer
def langage_accepte(automate: dict, n: int) -> list[str]:  # 1.3.5
    """Renvoie la liste des mots de longueur inférieure à n acceptés par l'automate."""
    res: set[str] = tousmots(automate["alphabet"], n)  # On récupère tous les mots de longueur inférieure à n
    for m in res:  # On itére sur chaque mot trouvé pour savoir si il est accepté ou non par l'automate
        if not accepte(automate, m):
            res.remove(m)  # On supprime les mots non acceptés par l'automate
    return list(res)


# 1.3.6
# Il est impossible d'implémenter une fonction qui renvoie le langage accepté par un automate car un automate peut potentiellement 
# accepter une infinité de mots et que, pour la même raison que pour l'étoile d'un langage, les ressources sont limitées


def main() -> None:  # Cellule de test

    def part1() -> None:
        pref("coucou")
        suf("coucou")
        fact("coucou")
        miroir("coucou")

    def part2() -> None:
        l1 = ['aa', 'ab', 'ba', 'bb']
        l2 = ['a', 'b', '']
        concatene(l1, l2)
        puis(l1, 2)
        tousmots(['a', 'b'], 3)

    def part3() -> None:
        auto1 = defauto(['a', 'b'], [1, 2, 3, 4], [[1, 'a', 2], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4]], [1], [4])
        lirelettre(auto1["transitions"], auto1["etats"], 'a')
        liremot(auto1["transitions"], auto1["etats"], 'aba')
        accepte(auto1, 'aba')
        accepte(auto1, 'abbbba')
        langage_accepte(auto1, 3)

    #part1()
    #part2()
    #part3()


if __name__ == "__main__":
    main()
