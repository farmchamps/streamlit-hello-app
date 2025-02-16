# import streamlit as st
# from openai import OpenAI

# # Show title and description.
# st.title("💬 Chatbot")
# st.write(
#     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# )

# # Ask user for their OpenAI API key via `st.text_input`.
# # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})

# from flask import Flask, render_template, request, redirect, session
 
# app = Flask(__name__)

# @app.route('/handle_post', methods=['POST'])
# def handle_post():
#     if request.method == 'POST':
#         return '<h1>Welcome!!!</h1>'
#     else:
#         return "not a post"
 
# if __name__ == '__main__':
#     app.run()


import streamlit as st
from flask import Flask, jsonify
import threading

# Create a Flask app
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def api_data():
    return jsonify({"message": "Hello from Flask API!"})

# Run Flask in a separate thread
def run_flask():
    app.run(port=5001, debug=False, use_reloader=False)

threading.Thread(target=run_flask, daemon=True).start()

# Streamlit UI
st.title("Streamlit App with API")
st.write("Flask API is running at: [http://localhost:5001/api/data](http://localhost:5001/api/data)")