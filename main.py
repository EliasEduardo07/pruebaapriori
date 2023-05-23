import streamlit as st
import itertools
import pandas as pd
import matplotlib.pyplot as plt

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
    min_support = st.slider("Soporte mínimo", min_value=1, max_value=10, value=5)
    min_confidence = st.slider("Confianza mínima (%)", min_value=1, max_value=100, value=50)

    # Ejecutar el algoritmo de Apriori
    conjuntos_frecuentes = apriori(recetas, min_support)

    # Obtener las reglas de asociación
    reglas_asociacion = []
    for conjunto in conjuntos_frecuentes:
        if len(conjunto) > 1:
            for i in range(1, len(conjunto)):
                for combinacion in itertools.combinations(conjunto, i):
                    conjunto_A = set(combinacion)
                    conjunto_B = set(conjunto) - conjunto_A
                    soporte_A = sum(1 for receta in recetas if conjunto_A.issubset(receta))
                    soporte_B = sum(1 for receta in recetas if conjunto_B.issubset(receta))
                    confidence = (soporte_B / soporte_A) * 100
                    if confidence >= min_confidence:
                        reglas_asociacion.append((conjunto_A, conjunto_B, soporte_A, soporte_B, confidence))

    # Crear DataFrame con los resultados ordenados por confianza
    df_resultados = pd.DataFrame(reglas_asociacion, columns=["A", "B", "Soporte A", "Soporte B", "Confianza"])
    df_resultados = df_resultados.sort_values("Confianza", ascending=False)

    # Mostrar gráfico de barras con las confianzas
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(range(len(df_resultados)), df_resultados["Confianza"], color="skyblue")
    ax.set_yticks(range(len(df_resultados)))
    ax.set_yticklabels(["{} -> {}".format(list(row["A"]), list(row["B"])) for _, row in df_resultados.iterrows()])
    ax.invert_yaxis()
    ax.set_xlabel("Confianza (%)")
    ax.set_title("Reglas de Asociación")
    st.pyplot(fig)

    # Mostrar tabla con los resultados
    st.subheader("Reglas de Asociación ordenadas por confianza:")
    st.dataframe(df_resultados)

if __name__ == '__main__':
    main()
