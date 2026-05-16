import streamlit as st
from api import buscar_cotacao
from utils import formatar_valor


# Configuração da página
st.set_page_config(
    page_title='currency converter',
    page_icon='💱'
)


# Titulo
st.header('Currency Converter')
st.write('Converta valores entre diferentes moedas com cotações em tempo real.')


# Lista de moedas disponíveis
MOEDAS = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWG']


# Formulario de conversão
st.divider()
st.subheader('Dados')

col1, col2 = st.columns([1,1])
# Seleção de moedas
with col1:
    moeda_origem = st.selectbox(
        'Moeda Origem',
        MOEDAS)
with col2:
    moeda_destino = st.selectbox(
        'Moeda Destino',
        MOEDAS)


col1, col2 = st.columns([1,1])
with col1:
    # Campo de valor
    valor = st.number_input('Valor a ser convertido', min_value=0.00)

# Botão de conversão
converter = st.button('Converter')


# Processamento e exibição do resultado
if converter:
    taxa = buscar_cotacao(moeda_origem, moeda_destino)
    resultado = valor * taxa
    
    # Resultado
    st.divider()
    st.subheader('Resultado')
    st.metric(
        label=f'{moeda_origem} → {moeda_destino}',
        value=f'{moeda_destino} {formatar_valor(resultado)}'
    )