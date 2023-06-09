import data
import streamlit as st
import matplotlib.pyplot as plt

# Fréquentations par ligne :

query="SELECT l.nom AS ligne, SUM(f.nombre_passagers) AS total_passagers FROM frequentation f INNER JOIN horaires h ON f.horaire = h.id INNER JOIN lignes l ON h.ligne = l.id GROUP BY l.nom"
dataframe=data.get_data(query)
st.title("Fréquentations par ligne :")

fig=plt.figure(figsize=[20,8])
plt.barh(dataframe['ligne'], dataframe['total_passagers'])
plt.ylabel('Ligne')
plt.xlabel('Nombre de passagers')
plt.title('Histogramme des fréquentations par lignes')
plt.xticks(rotation=45)

for i, v in enumerate(dataframe['total_passagers']):
    plt.text(v, i, str(v), color='black', va='center')

plt.show()
st.pyplot(fig)

# Fréquentations par heure :

query = "SELECT heure,sum(nombre_passagers) as total_passagers FROM frequentation f LEFT JOIN horaires h ON f.horaire=h.id GROUP BY heure ORDER BY heure ASC"
dataframe=data.format_heure(data.get_data(query))
st.title("Fréquentations par heure :")

fig = plt.figure(figsize=[20, 8])
plt.plot(dataframe['heure'], dataframe['total_passagers'], marker='o')
plt.ylabel('Nombre de passagers')
plt.xlabel('Heure')
plt.title('Graphique des fréquentations par heure')
plt.xticks(rotation=45)

for i, v in enumerate(dataframe['total_passagers']):
    plt.text(dataframe['heure'].iloc[i], v, str(v), color='black', ha='center')

plt.grid(True)
plt.show()
st.pyplot(fig)

# Fréquentation par jour
st.title("Fréquentation par jour")

query = "SELECT jour,sum(nombre_passagers) as total_passagers FROM frequentation f GROUP BY jour"
dataframe=data.get_data(query)

fig, ax = plt.subplots()
ax.pie(dataframe['total_passagers'],labels=dataframe["jour"], autopct='%2d%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)