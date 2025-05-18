# Projet : 🧠 Détection du Stress - Application Web avec Streamlit

<p align="center">
  <img src="MoodMetric.png" alt="Logo de l'application" width="200"/>
</p>

## Bienvenue chez MoodMetric

Ce projet académique a été réalisé dans le cadre d’un travail pratique visant à concevoir une application web capable d’évaluer le niveau de stress d’un individu. Grâce à une interface intuitive développée avec **Streamlit** et à un modèle de **machine learning (Random Forest)**, l’application prédit si une personne a un **niveau de stress faible**, **moyen** ou **élevé**, en fonction de ses habitudes de vie.

## 👥 Auteurs

- NAYA MAOUDANA KARE
- Issa BICHARA 

## 🔍 Nos données

Les données proviennent d’un jeu de données disponible sur **Kaggle**. Pour cette application, apres le nettoyage de la base, les variables suivantes ont été sélectionnées dans le modele:

- Âge
- Heures de sommeil par nuit
- Heures d'activité physique par semaine
- Temps d'écran par jour
- Nombre de tasses de café par jour
- Nombre de verres d’alcool par jour
- Fumeur ou non
- Heures de travail par jour
- Temps de trajet quotidien pour aller au travail
- Nombre d’interactions sociales hors travail
- Pratique de la méditation ou non

## 🤖 Modèle de prédiction

Le modèle utilisé est un **Random Forest Classifier**, entraîné pour classer les individus selon trois niveaux de stress :

- **Faible**
- **Moyen**
- **Élevé**

En fonction du résultat, un **conseil personnalisé** est affiché pour aider l’utilisateur à mieux gérer son stress.

## 🖥️ Interface utilisateur

L’utilisateur interagit avec l’application à l’aide de **sliders** pour ajuster ses habitudes de vie, puis clique sur un bouton **“Prédire”**. Le niveau de stress est alors affiché instantanément.

Aucune visualisation graphique n'est incluse, l'objectif étant de maintenir une interface simple et directe.

## 📁 Arborescence du projet

📦 stress-detector
├── application.py
├── model.pkl
├── requirements.txt
├── README.md
└── data/
