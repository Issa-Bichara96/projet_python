import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# 📄 Charger les données
data = pd.read_csv("stress_detection.csv")
data.columns = data.columns.str.strip()

# 🧹 Supprimer les colonnes inutiles
colonnes_a_supprimer = [
    'Gender', 'Occupation', 'Marital_Status',
    'Sleep_Quality', 'Bed_Time', 'Wake_Up_Time',
    'Blood_Pressure', 'Cholesterol_Level', 'Blood_Sugar_Level',
    'Exercise_Type'  # 👈 suppression ici
]
data = data.drop(columns=[col for col in colonnes_a_supprimer if col in data.columns])

# 🧼 Nettoyer les valeurs texte (enlever espaces autour)
data = data.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

# 🔄 Convertir les colonnes binaires "Yes"/"No" en 1/0
colonnes_binaires = ['Smoking_Habit', 'Meditation_Practice']
data[colonnes_binaires] = data[colonnes_binaires].replace({'Yes': 1, 'No': 0})

# 🎯 Mapping du niveau de stress
stress_map = {"Low": 0, "Medium": 1, "High": 2}
data["Stress_Level"] = data["Stress_Detection"].map(stress_map)

# ✅ Séparer X et y
X = data.drop(columns=["Stress_Detection", "Stress_Level"])
y = data["Stress_Level"]

# 🧪 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🧠 Entraîner le modèle
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 💾 Sauvegarder dans un fichier .pkl (nom personnalisé si besoin)
with open("stress_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modèle entraîné et sauvegardé sous 'stress_classifier.pkl'")
