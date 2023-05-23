import streamlit as st
import itertools

def apriori(recetas, min_support):
    ingredientes_frecuentes = {}
    for receta in recetas:
        for ingrediente in receta:
            if ingrediente in ingredientes_frecuentes:
                ingredientes_frecuentes[ingrediente] += 1
            else:
                ingredientes_frecuentes[ingrediente] = 1

    ingredientes_frecuentes = {
        ingrediente: frecuencia
        for ingrediente, frecuencia in ingredientes_frecuentes.items()
        if frecuencia >= min_support
    }

    conjuntos_frecuentes = []
    for r in range(1, len(ingredientes_frecuentes) + 1):
        combinaciones = itertools.combinations(ingredientes_frecuentes, r)
        conjuntos_frecuentes.extend(list(combinaciones))

    return conjuntos_frecuentes

def main():
    st.title("Análisis de recetas de comida con Apriori")

    # Generar recetas ficticias
    recetas = [
        ['pollo', 'cebolla', 'ajo', 'sal'],
        ['pasta', 'tomate', 'queso'],
        ['arroz', 'pollo', 'cebolla', 'pimiento'],
        ['pasta', 'tomate', 'cebolla', 'aceite'],
        ['pollo', 'sal', 'pimienta', 'limón'],
        ['arroz', 'pollo', 'aceite', 'sal'],
        ['pasta', 'queso', 'aceite', 'sal'],
        ['pasta', 'tomate', 'queso', 'cebolla'],
        ['pollo', 'pimiento', 'cebolla', 'sal'],
        ['pasta', 'tomate', 'queso', 'aceite'],
        ['pollo', 'cebolla', 'aceite', 'sal'],
        ['pasta', 'tomate', 'queso', 'ajo'],
        ['arroz', 'pollo', 'cebolla', 'sal'],
        ['pasta', 'tomate', 'aceite', 'sal'],
        ['pollo', 'cebolla', 'ajo', 'limón'],
        ['arroz', 'pollo', 'cebolla', 'ajo'],
        ['pasta', 'tomate', 'queso', 'sal'],
        ['pollo', 'pimiento', 'cebolla', 'ajo'],
        ['pasta', 'tomate', 'cebolla', 'sal'],
        ['pollo', 'cebolla', 'aceite', 'ajo']
    ]

    # Parámetros
    min_support = 5

    # Ejecutar el algoritmo de Apriori
    conjuntos_frecuentes = apriori(recetas, min_support)

    # Mostrar los conjuntos de ingredientes frecuentes
    st.subheader("Conjuntos de ingredientes frecuentes:")
    for conjunto in conjuntos_frecuentes:
        st.write(conjunto)

if __name__ == '__main__':
    main()
