# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Arthur Repetti 18/02/2026

Exercice 4
"""

import numpy as np


def standardisation_des_var(Z: np.ndarray):
    moyennes = np.mean(Z, axis=0)
    ecarts_type = np.nanstd(Z, axis=0)
    X = Z - moyennes
    X = X / ecarts_type
    return X
        

def estimateur_moindres_carres(X: np.ndarray, y: np.ndarray):
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    return beta

def val_residus_obtenus(X: np.ndarray, beta, y: np.ndarray):
    residus = np.sum( np.square( (X @ beta) - (y) ) )
    return residus

if __name__ == '__main__':
    # Matrice Z contenant les données
    Z = np.genfromtxt('data/data.csv', delimiter=';', skip_header=1)
    
    y = Z[:, 11]    # y prend la 12ème colonne
    Z = Z[:, :11]   # on retire la 12 ème colonne à Z
    
    # Matrice X
    X = standardisation_des_var(Z)
    
    # Affichage des résultats pour chaque colonnes (moyenne et variance)
    for i in range(11): 
        moy_col = np.mean(X[:, i])
        ecarts_col = np.var(X[:, i])
        print(f"\nMoyenne de la colonne {i} = {moy_col}")
        print(f"Variance de la colonne {i} = {ecarts_col}")
    
    # Calcule de β (pour X)
    beta = estimateur_moindres_carres(X, y)
    # Calcule des residus (pour X)
    residus = val_residus_obtenus(X, beta, y)
    
    # Affichage
    print("\nβ =\n", beta)
    print("\nresidus =\n", residus)
    

