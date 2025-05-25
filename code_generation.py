# app.py
import streamlit as st
import helper  # helper.py dosyan

# İstemcileri başlat
clients = helper.initialize_clients()

if "messages" not in st.session_state:
    st.session_state.messages = []

def adjust_model_relations():
    st.session_state.messages = []

def send_message(prompt):
    st.chat_message("user").markdown(prompt)

    selected_label = st.session_state.selected_model         # örneğin "LLaMA 3"
    model_key = model_options[selected_label]                # örneğin "llama"
    model_name = clients[model_key]                          # örneğin "llama3"
    
    response = helper.ollama_generate_response(prompt, model_name)

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# SİDEBAR
st.sidebar.header("KONFİGÜRASYON")
st.sidebar.divider()

model_options = {
    "LLaMA 3": "llama",
    "Mistral": "mistral"
}

st.sidebar.selectbox(
    label="Model Seçin:",
    options=list(model_options.keys()),
    key="selected_model",
    index=0,
    on_change=adjust_model_relations
)

st.sidebar.divider()

questions_list = [
    "İki sayının toplamını bulan Python kodunu yaz", 
    "Python Streamlit ile basit giriş ekranı yap", 
    "Eisenhower Matrisi gösteren bir Streamlit uygulaması yaz", 
    "HTML, CSS, JS ile sayı tahmin oyunu kodu yaz", 
    "Manuel Soru Yaz"
]

st.sidebar.selectbox(
    label="Örnek Soru Seçin:",
    options=questions_list,
    key="selected_question",
    index=4
)

st.title("Lokal LLM Kıyaslama: LLaMA vs Mistral")
st.divider()

for message in st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(message["content"])

if st.session_state.selected_question != "Manuel Soru Yaz":
    prompt = st.session_state.selected_question
    send_message(prompt)
elif prompt := st.chat_input("Sorunuzu yazın"):
    send_message(prompt)
