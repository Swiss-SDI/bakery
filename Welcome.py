# coding=utf-8
""" """
# Copyright 2023, Swiss Statistical Design & Innovation Sàrl

import streamlit as st
from utils import render_swiss_sdi_footer

st.set_page_config(
    page_title="Bienvenue",
)

st.title("Projet guidé de data science")

st.markdown("""
Dans cette page web interactive, vous avez la possibilité de jouer le rôle de data scientist à travers un exemple guidé.

Votre mission du jour est de **prévoir les ventes d'une boulangerie en France**.

Vous découvrirez les  étapes clés d'un projet de data science et apprendrez quelques points d'attention à ne pas rater lors d'une analyse.""")

st.image("assets/bakery.jpg")

st.markdown("""
En particulier, pour mener à bien votre mission, vous traverserez les pas suivants:
1. **Data Cleaning**: Charger l'ensemble des données et éliminer les incohérences.
2. **Data Analysis**: Comprendre les données en les examinants.
3. **Forecasting**: Essayer différents modèles d'apprentissage automatique et différentes caractéristiques pour trouver le meilleur modèle possible.

Curieux de vous lancer dans votre première mission de data scientist ?

Dirigiez-vous sans attendre vers la première étape! 
""")


if st.button('Aller vers 🧹 Data Cleaning', type='primary', use_container_width=True):
    st.switch_page('pages/1_🧹_Data_Cleaning.py')

# Render the Swiss-SDI footer
render_swiss_sdi_footer()
