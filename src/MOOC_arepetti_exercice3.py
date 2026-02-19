# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Arthur Repetti 18/02/2026

Exercice 3
"""

import numpy as np

def estimateur_moindres_carres(X: np.ndarray, y: np.ndarray):
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    return beta

def val_residus_obtenus(Z: np.ndarray, beta, y: np.ndarray):
    residus = np.sum( np.square( (Z @ beta) - (y) ) )
    return residus

if __name__ == '__main__':
    # Matrice Z contenant les données
    Z = np.genfromtxt('data/data.csv', delimiter=';', skip_header=1)
    
    y = Z[:, 11]    # y prend la 12ème colonne
    Z = Z[:, :11]   # on retire la 12 ème colonne à Z
    
    # Calcule de β (pour Z)
    beta = estimateur_moindres_carres(Z, y)
    # Calcule des residus (pour Z)
    residus = val_residus_obtenus(Z, beta, y)
    
    
