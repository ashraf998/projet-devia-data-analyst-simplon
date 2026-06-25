import plotly.express as px
import pandas as pd

def generer():

    données = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
    )

    # Calcul du chiffre d'affaires
    données['chiffre_affaires'] = données['prix'] * données['qte']

    # Regroupement par produit
    ca_par_produit = (
        données.groupby('produit', as_index=False)['chiffre_affaires']
        .sum()
    )

    figure = px.bar(
    ca_par_produit,
    x='produit',
    y='chiffre_affaires',
    text='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={
        'produit': 'Produit',
        'chiffre_affaires': "Chiffre d'affaires (€)"
    }
    )

    figure.update_traces(textposition='outside')

    figure.write_html('chiffre-affaires-par-produit.html')

    print('chiffre-affaires-par-produit.html généré avec succès !')