import streamlit as st
import openai

# Chave da API GPT-3
openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50  # Limitando a resposta a 50 tokens (~100 palavras)
    )
    return response.choices[0].text.strip()

def main():
    st.title("Crazy Jung - Psicólogo Virtual")
    user_input = st.text_input("Digite sua pergunta:")
    submit_button = st.button("Enviar")

    if submit_button and user_input:
        st.text("Crazy Jung: Analisando...")
        prompt = f"Usuário: {user_input}\nCrazy Jung:"
        response = generate_response(prompt)
        st.text("Crazy Jung: " + response)

if __name__ == "__main__":
    main()

