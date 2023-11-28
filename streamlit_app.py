import streamlit as st
import requests
from streamlit import secrets

API_KEY = '260cee54-6d54-48ba-92e8-bf641b5f4805'  # Agrega tu API key aquí

def generate_contract(changes_to_make, contract_file):
    url = 'https://api.respell.ai/v1/run'
    headers = {
        'authorization': f'Bearer {API_KEY}',
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    data = {
        'spellId': 'Q9cMo4SZQo7OFFnnq9l9L',
        'spellVersionId': 'hF1xYtgWU-TNr-HFZMpfw',
        'inputs': {
            'changes_to_make': changes_to_make,
            'similar_contract_pdf': contract_file.read()
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        # Aquí puedes guardar el archivo PDF generado o mostrarlo en Streamlit
        st.write('Contrato generado correctamente')
        st.write(response.json())
    else:
        st.write('Error al generar el contrato')

def main():
    st.title('Generador de Contratos')
    st.write('Ingrese los datos necesarios para generar el contrato')
    
    # Campo de texto para ingresar los cambios a realizar en el contrato
    changes_to_make = st.text_area('Cambios a realizar en el contrato', height=200)
    
    # Campo de carga de archivo para cargar el contrato original
    contract_file = st.file_uploader('Cargar Contrato Original', type=['pdf'])
    
    if st.button('Generar Contrato') and contract_file is not None:
        generate_contract(changes_to_make, contract_file)

if __name__ == '__main__':
    main()
