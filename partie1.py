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
def pref(u: str) -> list:   # 1.1.1
    """Retourne une liste de tous les préfixes du mot u."""
    return [u[:i] for i in range(len(u) + 1)]   # Utilisation de la création de liste par compréhension et des slices


@dec.timer
def suf(u: str) -> list:    # 1.1.2
    """Retourne une liste de tous les suffixes du mot u."""
    return [u[i:] for i in range(len(u) + 1)]  # Utilisation de la création de liste par compréhension et des slices


@dec.timer
def fact2(u: str) -> list:   # 1.1.3
    """Retourne une liste sans doublons de tous les facteurs du mot u."""
    res = {u[i:j] for i in range(len(u)) for j in range(i, len(u) + 1)} # Ici, un set est utilisé pour éviter les doublons et ainsi optimiser les performances
    return sorted(list(res))    # On renvoit la liste triée pour une meilleur lisibilité de la réponse, mais ce n'est pas obligatoire et peut être retiré pour optimiser les performances


@dec.timer
def miroir(u: str) -> str:   # 1.1.4
    """Retourne le mot miroir de u."""
    return u[::-1]  # Simple utilisation des slices pour effecture le miroir du mot

################# 1.2 ####################

@dec.timer
def concatene(l1: list[str], l2: list[str]) -> list:    # 1.2.1
    """Retourne une liste de tous les mots obtenus en copncaténant les mots de l1 avec les mots de l2."""
    res = {f'{u}{v}' for u in l1 for v in l2} # Ici, un set est utilisé pour éviter les doublons et ainsi optimiser les performances
    return sorted(list(res))    # On renvoit la liste triée pour une meilleur lisibilité de la réponse, mais ce n'est pas obligatoire et peut être retiré pour optimiser les performances


@dec.timer
def puis(l: list[str], n: int) -> list:
    if n == 0:
        return ['']
    if n == 1:
        return l
    res = set() # Ici, un set est utilisé pour éviter les doublons et ainsi optimiser les performances

    return sorted(list(res))   # On renvoit la liste triée pour une meilleur lisibilité de la réponse, mais ce n'est pas obligatoire et peut être retiré pour optimiser les performances

def main() -> None: # Cellule de test

    def part1() -> None:
        pref("coucou")
        suf("coucou")
        fact2("coucou")
        miroir("coucou")

    def part2() -> None:
        l1=['aa','ab','ba','bb']
        l2=['a', 'b', '']
        concatene(l1, l2)
    
    #part1()
    part2()


if __name__ == "__main__":
    main()