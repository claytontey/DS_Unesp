import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os

# Carregar o modelo e o encoder
model = joblib.load("\\Users\\Yuki\\Desktop\\github\\DS_Unesp\\Work_Git\\lucas_yuki\\WorkGit\\Aula12\\best_random_forest_model.pkl")
encoder = joblib.load("\\Users\\Yuki\\Desktop\\github\\DS_Unesp\\Work_Git\\lucas_yuki\\WorkGit\\Aula12\\label_encoder.pkl")

# Carregar a lista de sintomas
symptoms_list = list(pd.read_csv("\\Users\\Yuki\\Desktop\\github\\DS_Unesp\\Work_Git\\lucas_yuki\\WorkGit\\Aula12\\Testing.csv").columns[:-1])

# Traduções de sintomas
sintomas_traduzidos = {
    "itching": "Coceira",
    "skin_rash": "Erupção cutânea",
    "nodal_skin_eruptions": "Erupções cutâneas nodulares",
    "continuous_sneezing": "Espirros contínuos",
    "shivering": "Tremores",
    "chills": "Calafrios",
    "joint_pain": "Dor nas articulações",
    "stomach_pain": "Dor de estômago",
    "acidity": "Acidez",
    "ulcers_on_tongue": "Úlceras na língua",
    "muscle_wasting": "Perda de massa muscular",
    "vomiting": "Vômito",
    "burning_micturition": "Micção dolorosa",
    "spotting_urination": "Urina com sangue",
    "fatigue": "Fadiga",
    "weight_gain": "Ganho de peso",
    "anxiety": "Ansiedade",
    "cold_hands_and_feet": "Mãos e pés frios",
    "mood_swings": "Mudanças de humor",
    "weight_loss": "Perda de peso",
    "restlessness": "Inquietação",
    "lethargy": "Letargia",
    "patches_in_throat": "Manchas na garganta",
    "irregular_sugar_level": "Nível irregular de açúcar",
    "cough": "Tosse",
    "high_fever": "Febre alta",
    "sunken_eyes": "Olhos fundos",
    "breathlessness": "Falta de ar",
    "sweating": "Sudorese",
    "dehydration": "Desidratação",
    "indigestion": "Indigestão",
    "headache": "Dor de cabeça",
    "yellowish_skin": "Pele amarelada",
    "dark_urine": "Urina escura",
    "nausea": "Náusea",
    "loss_of_appetite": "Perda de apetite",
    "pain_behind_the_eyes": "Dor atrás dos olhos",
    "back_pain": "Dor nas costas",
    "constipation": "Constipação",
    "abdominal_pain": "Dor abdominal",
    "diarrhoea": "Diarreia",
    "mild_fever": "Febre leve",
    "yellow_urine": "Urina amarela",
    "yellowing_of_eyes": "Amarelamento dos olhos",
    "acute_liver_failure": "Falência hepática aguda",
    "fluid_overload": "Sobrecarga de fluidos",
    "swelling_of_stomach": "Inchaço do estômago",
    "swelled_lymph_nodes": "Linfonodos inchados",
    "malaise": "Mal-estar",
    "blurred_and_distorted_vision": "Visão embaçada e distorcida",
    "phlegm": "Fleuma",
    "throat_irritation": "Irritação na garganta",
    "redness_of_eyes": "Vermelhidão dos olhos",
    "sinus_pressure": "Pressão sinusal",
    "runny_nose": "Coriza",
    "congestion": "Congestão",
    "chest_pain": "Dor no peito",
    "weakness_in_limbs": "Fraqueza nos membros",
    "fast_heart_rate": "Frequência cardíaca rápida",
    "pain_during_bowel_movements": "Dor durante movimentos intestinais",
    "pain_in_anal_region": "Dor na região anal",
    "bloody_stool": "Fezes com sangue",
    "irritation_in_anus": "Irritação no ânus",
    "neck_pain": "Dor no pescoço",
    "dizziness": "Tontura",
    "cramps": "Cãibras",
    "bruising": "Hematomas",
    "obesity": "Obesidade",
    "swollen_legs": "Pernas inchadas",
    "swollen_blood_vessels": "Vasos sanguíneos inchados",
    "puffy_face_and_eyes": "Rosto e olhos inchados",
    "enlarged_thyroid": "Tireoide aumentada",
    "brittle_nails": "Unhas frágeis",
    "swollen_extremeties": "Extremidades inchadas",
    "excessive_hunger": "Fome excessiva",
    "extra_marital_contacts": "Contatos extraconjugais",
    "drying_and_tingling_lips": "Secura e formigamento nos lábios",
    "slurred_speech": "Fala arrastada",
    "knee_pain": "Dor no joelho",
    "hip_joint_pain": "Dor na articulação do quadril",
    "muscle_weakness": "Fraqueza muscular",
    "stiff_neck": "Pescoço rígido",
    "swelling_joints": "Articulações inchadas",
    "movement_stiffness": "Rigidez de movimento",
    "spinning_movements": "Movimentos giratórios",
    "loss_of_balance": "Perda de equilíbrio",
    "unsteadiness": "Instabilidade",
    "weakness_of_one_body_side": "Fraqueza em um lado do corpo",
    "loss_of_smell": "Perda de olfato",
    "bladder_discomfort": "Desconforto na bexiga",
    "foul_smell_of_urine": "Cheiro ruim de urina",
    "continuous_feel_of_urine": "Sensação contínua de urinar",
    "passage_of_gases": "Passagem de gases",
    "internal_itching": "Coceira interna",
    "toxic_look_(typhos)": "Aparência tóxica (tifo)",
    "depression": "Depressão",
    "irritability": "Irritabilidade",
    "muscle_pain": "Dor muscular",
    "altered_sensorium": "Sensorium alterado",
    "red_spots_over_body": "Manchas vermelhas pelo corpo",
    "belly_pain": "Dor abdominal",
    "abnormal_menstruation": "Menstruação anormal",
    "dischromic_patches": "Manchas discrômicas",
    "watering_from_eyes": "Lacrimejamento dos olhos",
    "increased_appetite": "Aumento do apetite",
    "polyuria": "Poliúria",
    "family_history": "Histórico familiar",
    "mucoid_sputum": "Escarro mucoso",
    "rusty_sputum": "Escarro enferrujado",
    "lack_of_concentration": "Falta de concentração",
    "visual_disturbances": "Distúrbios visuais",
    "receiving_blood_transfusion": "Recebimento de transfusão de sangue",
    "receiving_unsterile_injections": "Recebimento de injeções não esterilizadas",
    "coma": "Coma",
    "stomach_bleeding": "Sangramento estomacal",
    "distention_of_abdomen": "Distensão abdominal",
    "history_of_alcohol_consumption": "Histórico de consumo de álcool",
    "blood_in_sputum": "Sangue no escarro",
    "prominent_veins_on_calf": "Veias proeminentes na panturrilha",
    "palpitations": "Palpitações",
    "painful_walking": "Caminhada dolorosa",
    "pus_filled_pimples": "Pústulas",
    "blackheads": "Cravos",
    "scurring": "Escoriações",
    "skin_peeling": "Descamação da pele",
    "silver_like_dusting": "Poeira prateada",
    "small_dents_in_nails": "Pequenas depressões nas unhas",
    "inflammatory_nails": "Unhas inflamadas",
    "blister": "Bolha",
    "red_sore_around_nose": "Ferida vermelha ao redor do nariz",
    "yellow_crust_ooze": "Exsudação de crosta amarela"
}

doencas_traduzidas = {
    "(vertigo) Paroymsal  Positional Vertigo": "Vertigem Posicional Paroxística",
    "AIDS": "AIDS",
    "Acne": "Acne",
    "Alcoholic hepatitis": "Hepatite Alcoólica",
    "Allergy": "Alergia",
    "Arthritis": "Artrite",
    "Bronchial Asthma": "Asma Brônquica",
    "Cervical spondylosis": "Espondilose Cervical",
    "Chicken pox": "Catapora",
    "Chronic cholestasis": "Colestase Crônica",
    "Common Cold": "Resfriado Comum",
    "Dengue": "Dengue",
    "Diabetes ": "Diabetes",
    "Dimorphic hemmorhoids(piles)": "Hemorroidas Dimórficas",
    "Drug Reaction": "Reação a Medicamentos",
    "Fungal infection": "Infecção Fúngica",
    "GERD": "DRGE (Doença do Refluxo Gastroesofágico)",
    "Gastroenteritis": "Gastroenterite",
    "Heart attack": "Infarto",
    "Hepatitis B": "Hepatite B",
    "Hepatitis C": "Hepatite C",
    "Hepatitis D": "Hepatite D",
    "Hepatitis E": "Hepatite E",
    "Hypertension ": "Hipertensão",
    "Hyperthyroidism": "Hipertireoidismo",
    "Hypoglycemia": "Hipoglicemia",
    "Hypothyroidism": "Hipotireoidismo",
    "Impetigo": "Impetigo",
    "Jaundice": "Icterícia",
    "Malaria": "Malária",
    "Migraine": "Enxaqueca",
    "Osteoarthristis": "Osteoartrite",
    "Paralysis (brain hemorrhage)": "Paralisia (hemorragia cerebral)",
    "Peptic ulcer diseae": "Doença de Úlcera Péptica",
    "Pneumonia": "Pneumonia",
    "Psoriasis": "Psoríase",
    "Tuberculosis": "Tuberculose",
    "Typhoid": "Tifo",
    "Urinary tract infection": "Infecção do Trato Urinário",
    "Varicose veins": "Varizes",
    "hepatitis A": "Hepatite A"
}

# Função para prever a doença e registrar o diagnóstico
def predict_disease(symptoms):
    input_data = np.array([symptoms])
    prediction_proba = model.predict_proba(input_data)[0]
    prediction = model.predict(input_data)[0]
    predicted_disease = encoder.inverse_transform([prediction])[0]
    predicted_disease_translated = doencas_traduzidas.get(predicted_disease, "Doença não traduzida")

    # Registrar o diagnóstico
    #record_diagnosis(predicted_disease_translated, prediction_proba)

    return predicted_disease_translated, prediction_proba

# Título do app
st.title('Diagnóstico de Doença com Base em Sintomas')

# Seleção de sintomas via multiselect
translated_symptoms = [sintomas_traduzidos.get(symptom, "Sem tradução") for symptom in symptoms_list]
selected_symptoms_translated = st.multiselect("Selecione os sintomas:", options=translated_symptoms)

# Converter sintomas selecionados de volta para o formato original
selected_symptoms = [symptom for symptom, translation in sintomas_traduzidos.items() if translation in selected_symptoms_translated]

# Preparar a entrada para o modelo
symptoms_input = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]

# Botão para diagnosticar
if st.button('Diagnosticar'):
    if any(symptoms_input):  # Verifica se algum sintoma foi selecionado
        diagnosis, probabilities = predict_disease(symptoms_input)
        st.write(f"A doença prevista é: {diagnosis}")

        # Ordenar probabilidades e pegar os índices das maiores probabilidades
        sorted_indices = np.argsort(probabilities)[::-1]
        top_indices = sorted_indices[:5]  # Suponha que você quer mostrar os top 5
        probabilities_sorted = probabilities[top_indices]

        # Traduzir doenças para os rótulos
        diseases = [doencas_traduzidas.get(encoder.inverse_transform([index])[0], "Doença não traduzida") for index in top_indices]

        # Criar gráfico de setores das probabilidades
        fig, ax = plt.subplots()
        ax.pie(probabilities_sorted, labels=diseases, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Garante que a torta seja desenhada como um círculo.
        st.pyplot(fig)
    else:
        st.error("Por favor, selecione pelo menos um sintoma.")
