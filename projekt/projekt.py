import os
import sqlite3
from tkinter import ttk

import pandas as pd
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class_mapping = ["Barolo", "Grignolino", "Barbera"]
column_names = [
    "Class", "Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium",
    "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins",
    "Color_intensity", "Hue", "OD280/OD315_of_diluted_wines", "Proline"
]

database_name = "projekt.db"


def first_train():
    global data, X, y, X_train, X_test, y_train, y_test, model
    print("First start! Training!")
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

    data = pd.read_csv(url, header=None, names=column_names)

    X = data.drop("Class", axis=1)
    y = data["Class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)


def load_data():
    global data, X, y, X_train, X_test, y_train, y_test, model
    print("Loading data from database!")

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    select_query = """
        SELECT * FROM wine_data
        """
    cursor.execute(select_query)

    data = pd.DataFrame(cursor.fetchall(), columns=column_names)
    X = data.drop("Class", axis=1)
    y = data["Class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    connection.close()


if os.path.isfile(database_name):
    load_data()
else:
    first_train()


def save_data():
    print("Saving data")

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS wine_data (
        alcohol REAL,
        malic_acid REAL,
        ash REAL,
        alcalinity REAL,
        magnesium REAL,
        total_phenols REAL,
        flavanoids REAL,
        nonflavanoid_phenols REAL,
        proanthocyanins REAL,
        color_intensity REAL,
        hue REAL,
        od280_od315 REAL,
        proline REAL,
        class INTEGER
    );
    """
    cursor.execute(create_table_query)

    insert_query = "INSERT INTO wine_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    for index, row in data.iterrows():
        cursor.execute(insert_query, tuple(row))

    connection.commit()
    connection.close()


def train_model():
    global model, class_mapping
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    result_label.config(text="Dokładność modelu: {:.2f}%".format(accuracy * 100))
    class_mapping = {i: class_name for i, class_name in enumerate(model.classes_)}


def predict_data():
    new_data = pd.DataFrame([[
        float(entry_alcohol.get()),
        float(entry_malic_acid.get()),
        float(entry_ash.get()),
        float(entry_alcalinity.get()),
        float(entry_magnesium.get()),
        float(entry_total_phenols.get()),
        float(entry_flavanoids.get()),
        float(entry_nonflavanoid.get()),
        float(entry_proanthocyanins.get()),
        float(entry_color_intensity.get()),
        float(entry_hue.get()),
        float(entry_od280.get()),
        float(entry_proline.get())]],
        columns=X.columns)

    prediction = model.predict(new_data)
    class_name = class_mapping[int(prediction[0])]
    result_label.config("Predykcja klasy: {}".format(class_name))


def rebuild_model():
    global model
    model = RandomForestClassifier()
    result_label.config(text="Przebudowano model")


window = tk.Tk()
window.title("Projekt python")

data_frame = ttk.Frame(window)
data_frame.grid(row=0, column=0, padx=10, pady=10)

tree = ttk.Treeview(data_frame, columns=column_names, show="headings", height=5)
for column in column_names:
    tree.heading(column, text=column)
    tree.column(column, width=50)
tree.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

for index, row in data.iterrows():
    row_list = row.tolist()
    row_list[0] = class_mapping[int(row_list[0] - 1)]
    tree.insert("", "end", values=row_list)


predict_label = tk.Label(window, text="Predykcja nowych danych")
predict_label.grid(row=1, column=0, columnspan=2, pady=10)

entry_alcohol = tk.Entry(window)
entry_alcohol.insert(0, "Alcohol")
entry_alcohol.grid(row=2, column=0)

entry_malic_acid = tk.Entry(window)
entry_malic_acid.insert(0, "Malic Acid")
entry_malic_acid.grid(row=3, column=0)

entry_ash = tk.Entry(window)
entry_ash.insert(0, "Ash")
entry_ash.grid(row=4, column=0)

entry_alcalinity = tk.Entry(window)
entry_alcalinity.insert(0, "Alcalinity of Ash")
entry_alcalinity.grid(row=5, column=0)

entry_magnesium = tk.Entry(window)
entry_magnesium.insert(0, "Magnesium")
entry_magnesium.grid(row=6, column=0)

entry_total_phenols = tk.Entry(window)
entry_total_phenols.insert(0, "Total Phenols")
entry_total_phenols.grid(row=7, column=0)

entry_flavanoids = tk.Entry(window)
entry_flavanoids.insert(0, "Flavanoids")
entry_flavanoids.grid(row=8, column=0)

entry_nonflavanoid = tk.Entry(window)
entry_nonflavanoid.insert(0, "Nonflavanoid Phenols")
entry_nonflavanoid.grid(row=9, column=0)

entry_proanthocyanins = tk.Entry(window)
entry_proanthocyanins.insert(0, "Proanthocyanins")
entry_proanthocyanins.grid(row=10, column=0)

entry_color_intensity = tk.Entry(window)
entry_color_intensity.insert(0, "Color Intensity")
entry_color_intensity.grid(row=11, column=0)

entry_hue = tk.Entry(window)
entry_hue.insert(0, "Hue")
entry_hue.grid(row=12, column=0)

entry_od280 = tk.Entry(window)
entry_od280.insert(0, "OD280/OD315 of Diluted Wines")
entry_od280.grid(row=13, column=00)

entry_proline = tk.Entry(window)
entry_proline.insert(0, "Proline")
entry_proline.grid(row=14, column=0)

predict_button = tk.Button(window, text="Przewiduj", command=predict_data)
predict_button.grid(row=15, column=0)

result_label = tk.Label(window, text="")
result_label.grid(row=16, column=0)

train_button = tk.Button(window, text="Trenuj model", command=train_model)
train_button.grid(row=17, column=0, pady=10)

rebuild_button = tk.Button(window, text="Ponowne zbudowanie modelu", command=rebuild_model)
rebuild_button.grid(row=18, column=00, pady=10)

window.mainloop()

save_data()
