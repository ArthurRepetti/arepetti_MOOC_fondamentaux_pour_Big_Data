# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Arthur Repetti 18/02/2026

Exercice 2
"""

import numpy as np

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
    
    # Rang de X.T X - I
    rang = np.linalg.matrix_rank( (X.T @ X - I) )
    
    # Affichage
    print("I =\n", I)
    print("\nE =\n", E)
    print("\nX =\n", X)
    print("\ny =\n", y)

    # Affichage rang
    print("\nrang =\n", rang)

