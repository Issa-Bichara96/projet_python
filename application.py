# 📦 Packages nécessaires
import streamlit as st
import pandas as pd
import pickle
import datetime as dt

# 🔄 Chargement des données
data = pd.read_csv("stress_detection.csv")
data.columns = data.columns.str.strip()

# 🧹 Nettoyage
colonnes_a_supprimer = [
    'Gender', 'Occupation', 'Marital_Status',
    'Sleep_Quality', 'Bed_Time', 'Wake_Up_Time',
    'Blood_Pressure', 'Cholesterol_Level', 'Blood_Sugar_Level'
]
data = data.drop(columns=[col for col in colonnes_a_supprimer if col in data.columns])
data[['Smoking_Habit', 'Meditation_Practice']] = data[['Smoking_Habit', 'Meditation_Practice']].replace({'Yes': 1, 'No': 0})

# 🧠 Mapping des labels de stress
stress_map = {"Low": 0, "Medium": 1, "High": 2}
data["Stress_Level"] = data["Stress_Detection"].map(stress_map)

# ✅ Charger le modèle de classification
model = pickle.load(open("stress_classifier.pkl", "rb"))

st.image("MoodMetric.png", width=150)


if 'page' not in st.session_state:
    st.session_state.page = "Accueil"


st.sidebar.title("Aller à")
page = st.sidebar.radio("", ["Accueil", "À propos", "Contact"])

# Affichage dynamique en fonction du choix


if page == "Accueil":
# 🎨 Interface utilisateur
    st.title("MoodMetric : votre prédicteur de Stress 🌡️")
    st.write("Entrez vos habitudes de vie pour évaluer votre niveau de stress :")

    st.title("Bienvenue dans mon application")
    st.write("Ceci est la page d'accueil.")

    
    # 🎛️ Saisie utilisateur
    age = st.number_input("Votre âge", min_value=10, max_value=100, value=30)
    #st.caption("**Recommandation :** 18 à 65 ans. En dehors de cette tranche d'âge, le stress peut être plus difficile à évaluer.")
    sleep = st.slider("Heures de sommeil par nuit", 0.0, 12.0, 7.0, step=1.0)
    #st.caption("**Recommandation :** 7 à 9 heures pour un adulte. Moins de 6h peut augmenter le stress.")
    activity = st.slider("Activité physique (heures/semaine)", 0.0, 20.0, 5.0, step=1.0)
    #st.caption("**Recommandation :** 150 minutes d'activité modérée par semaine. Plus de 300 minutes est idéal.")
    screen = st.slider("Temps d'écran par jour (heures)", 0.0, 16.0, 5.0, step=1.0)
    #st.caption("**Recommandation :** Moins de 6 heures par jour. Plus de 8 heures peut augmenter le stress.")
    caffeine = st.slider("Caféine consommée (tasses/jour)", 0, 10, 1)
    #st.caption("**Recommandation :** 1 à 2 tasses par jour. Plus de 4 tasses peut perturber le sommeil.")
    alcohol_intake = st.slider("Consommation d'alcool (verres/jour)", 0, 10, 1)
    #st.caption("**Recommandation :** 1 verre par jour pour les femmes, 2 pour les hommes. Plus de 3 verres peut nuire au sommeil.")
    work_hours = st.slider("Heures de travail par jour", 0, 24, 8)
    #st.caption("**Recommandation :** 8 heures par jour. Plus de 10 heures peut augmenter le stress.")
    travel_time = st.slider("Temps de trajet (minutes)", 0, 120, 30)
    #st.caption("**Recommandation :** Moins de 30 minutes. Plus de 60 minutes peut augmenter le stress.")
    social_interactions = st.slider("Interactions sociales (par jour)", 0, 10, 5)
    #st.caption("**Recommandation :** 5 à 10 interactions par jour. Moins de 3 peut augmenter le stress.")
    meditation_practice = st.selectbox("Pratique de la méditation", ("Oui", "Non"))
    #st.caption("**Recommandation :** 10 à 20 minutes par jour. La méditation peut réduire le stress.")
    smoking_habit = st.selectbox("Habitude de fumer", ("Oui", "Non"))
    #st.caption("**Recommandation :** Ne pas fumer. Fumer peut augmenter le stress et nuire à la santé.")

    # 🧾 Construction du DataFrame utilisateur
    input_data = pd.DataFrame([{
        "Age": age,
        "Sleep_Duration": float(sleep),
        "Physical_Activity": float(activity),
        "Screen_Time": float(screen),
        "Caffeine_Intake": int(caffeine),
        "Alcohol_Intake": int(alcohol_intake),
        "Smoking_Habit": 1 if smoking_habit == "Oui" else 0,
        "Work_Hours": int(work_hours),
        "Travel_Time": float(travel_time),
        "Social_Interactions": int(social_interactions),
        "Meditation_Practice": 1 if meditation_practice == "Oui" else 0
    }])

    # 🧠 Prédiction
    if st.button("Analyser mon stress"):
        prediction_class = model.predict(input_data)[0]
        stress_map_inverse = {0: "Low", 1: "Medium", 2: "High"}
        resultat_final = stress_map_inverse[prediction_class]

        st.subheader("Niveau de stress prédit :")
        st.write(f"🧠 **{resultat_final}**")

        if prediction_class == 2:
            st.error("⚠️ Votre niveau de stress est élevé. Pensez à consulter un professionnel.")
        elif prediction_class == 1:
            st.warning("😐 Stress modéré. Prenez du temps pour vous relaxer.")
        else:
            st.success("😊 Faible stress. Continuez à prendre soin de vous !")
    
elif page == "À propos":
    st.title("L'application MoodMetric")
    st.write("MoodMetric est une application conçue pour aider les utilisateurs à évaluer leur niveau de stress en fonction de leurs habitudes de vie." \
        "Elle permet de mieux comprendre les facteurs qui influencent le stress et d'adopter des comportements plus sains.")

    st.title("Comment ça marche ?")
    st.write("Cette application utilise un modèle de classification pour prédire le niveau de stress en fonction de vos habitudes de vie." \
        "Le modèle a été entraîné sur des données d'auto-évaluation et utilise des algorithmes d'apprentissage automatique pour fournir une estimation du niveau de stress.")
    

    st.title("Pourquoi le mesurer ?")
    st.write("S'il n'est pas traité correctement, vous pouvez alors vous retrouver dans une phase de stress chronique." \
        "Une situation de stress prolongé peut nuire aux activités quotidiennes, entraînant dans certains cas un burn-out, des insomnies et de l'anxiété, voire une dépression."\
        "De nombreuses maladies mentales y sont associées, c'est pourquoi il est essentiel de faire appel à un médecin si vous n'arrivez pas à le gérer au quotidien.")
    
    st.title("Mots de l'équipe")
    st.write("Issa BICHARA: Cette application a été developpée dans le cadre de notre projet du DU Data Analyics de l'Université de Paris 1."\
        "Nous avons voulu créer un outil qui puisse aider les gens à mieux comprendre et gérer leur stress." \
        "En utilisant des techniques d'apprentissage automatique afin développer un modèle de classification qui prédit le niveau de stress en fonction de divers facteurs de style de vie." \
        "Nous avons également veillé à ce que l'application soit facile à utiliser, afin que tout le monde puisse en bénéficier." \
        "A travers cette application nous tenons à sensibiliser les utilisateurs à l'importance de la gestion du stress et des habitudes de vie saines." \
        "Nous espérons qu'elle vous sera utile dans votre quotidien.")
    
    st.write("Naya MAOUDANA KARE: En participant à ce projet, j'ai pu mettre en pratique mes compétences en analyse de données et en développement d'applications interactives." \
    " J'ai contribué à la comprehension des facteurs influencant le stress et à l'intégration du modèle de prédiction dans une interface conviviale." \
    "En rendant vidible ce qui est souvent ignoré, cette application encoyrage à adopter des comportement plus sain pour réduire le stress au quotidien." \
    "Nous espérons qu'elle pourra contribuer à une meilleure hygiène de vie, notamment chez les étudiants, les professionnels ou toute personne soumise à des rythmes de vie intenses.")

elif page == "Contact":
    st.title("Contact")
    st.write("Pour toute question, contactez-nous à : contact@monapp.com")

