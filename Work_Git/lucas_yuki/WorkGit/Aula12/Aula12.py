import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import numpy as np
import os

# Carregar dados de treinamento
data_train_path = 'C:\\Users\\Yuki\\Desktop\\github\\DS_Unesp\\Work_Git\\lucas_yuki\\WorkGit\\Aula12\\Training.csv'
data_train = pd.read_csv(data_train_path)

# Remover a coluna 'Unnamed: 133' se ela for desnecessária
if 'Unnamed: 133' in data_train.columns:
    data_train.drop(columns=['Unnamed: 133'], inplace=True)

# Preparar os dados de treinamento
encoder = LabelEncoder()
data_train['prognosis'] = encoder.fit_transform(data_train['prognosis'])

X_train = data_train.drop('prognosis', axis=1)
y_train = data_train['prognosis']

# Visualizar a frequência de cada sintoma
symptom_counts = X_train.sum(axis=0).sort_values(ascending=False)
plt.figure(figsize=(12, 8))
plt.title('Frequency of Symptoms')
symptom_counts.plot(kind='bar')
plt.xlabel('Symptoms')
plt.ylabel('Frequency')
plt.show()

# Carregar dados de teste
data_test_path = 'C:\\Users\\Yuki\\Desktop\\github\\DS_Unesp\\Work_Git\\lucas_yuki\\WorkGit\\Aula12\\Testing.csv'
data_test = pd.read_csv(data_test_path)
X_test = data_test.drop('prognosis', axis=1, errors='ignore')

# Definir o modelo
model = RandomForestClassifier(random_state=42)

# Definir a grade de parâmetros para testar
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Configurar o GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Melhores parâmetros e melhor modelo
best_model = grid_search.best_estimator_
print("Melhores Parâmetros Encontrados:", grid_search.best_params_)

# Avaliação no conjunto de teste
if 'prognosis' in data_test.columns:
    y_test = encoder.transform(data_test['prognosis'])  # Garantir que as etiquetas estão codificadas da mesma forma
    y_pred = best_model.predict(X_test)
    print("Acurácia no Teste:", accuracy_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

    # Calcular a matriz de confusão
    cm = confusion_matrix(y_test, y_pred)

    # Visualizar a matriz de confusão
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
    plt.title('Matriz de Confusão')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

# Visualizar a importância dos recursos
feature_importances = best_model.feature_importances_
sorted_indices = np.argsort(feature_importances)[::-1]

plt.figure(figsize=(12, 8))
plt.title('Feature Importances')
plt.bar(range(X_train.shape[1]), feature_importances[sorted_indices], align='center')
plt.xticks(range(X_train.shape[1]), X_train.columns[sorted_indices], rotation=90)
plt.tight_layout()
plt.show()

# Salvar o modelo e o encoder
joblib.dump(best_model, 'best_random_forest_model.pkl')
joblib.dump(encoder, 'label_encoder.pkl')