# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Arthur Repetti 18/02/2026

Exercice 1
"""

import numpy as np

def estimateur_moindres_carres(X: np.ndarray, y: np.ndarray):
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    return beta

def somme_estimateurs_mc(beta):
    somme = np.sum(beta)
    return somme


if __name__ == '__main__':
    # Matrice I
    I = np.eye(8, dtype=int)
    
    # Matrice E
    E = np.zeros((8, 8), dtype=int)
    E[0, 7] = 1
    
    # Matrice X
    X = I + E
    
    # Vecteur y
    y = np.ones((8, 1), dtype=int)
    
    # Affichage
    print("I =\n", I)
    print("\nE =\n", E)
    print("\nX =\n", X)
    print("\ny =\n", y)

    # Calcule somme des βi
    beta = estimateur_moindres_carres(X, y)
    somme_betas = somme_estimateurs_mc(beta)
    print("\nsomme des Bi =\n", somme_betas)
    