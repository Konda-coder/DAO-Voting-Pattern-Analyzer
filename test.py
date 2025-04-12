import streamlit as st
import streamlit.components.v1 as components

# Set up your OpenAI API key securely using environment variables or Streamlit secrets management.
# openai.api_key = st.secrets["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"]

# Custom CSS for modern styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }

    .header-style {
        color: #FA4032;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        padding: 20px 0;
    }

    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .iframe-container {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    .problem-statement {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-top: 30px;
    }

    .problem-statement h3 {
        color: #4CAF50;
        font-size: 1.8rem;
        font-weight: bold;
    }

    .problem-statement p {
        font-size: 1rem;
        color: #555;
        line-height: 1.6;
    }

    .input-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
    }

    .input-box textarea {
        width: 100%;
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        font-size: 1rem;
        background-color: #f9f9f9;
        resize: vertical;
    }

    .chat-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    .message-container {
        margin-bottom: 20px;
    }

    .message-user {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }

    .message-assistant {
        background-color: #f1f1f1;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }

    .sidebar-header {
        font-size: 1.25rem;
        color: #333;
        font-weight: bold;
        padding-bottom: 10px;
    }

    .stSlider {
        margin-top: 15px;
    }

    .stButton {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.header("Navigation", anchor="navigation")
page_selection = st.sidebar.radio("Go to:", ("Problem Statement", "Dashboard", "Chat with GPT-3.5"))

if page_selection == "Problem Statement":
    # Problem Statement Page
    st.markdown("<h2 class='header-style'>Project Title: GDP and Productivity of Indian Cities</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='problem-statement'>
            <h3>Project Statement:</h3>
            <p>The <strong>'GDP and Productivity of Indian Cities'</strong> project aims to develop an interactive Power BI dashboard that visualizes the Gross Domestic Product (GDP) and productivity metrics of various Indian cities. This project involves collecting, preprocessing, and structuring data on city-specific GDP, productivity indicators, and other relevant economic factors.</p>
            <p>The dashboard will provide insights into economic performance, regional comparisons, and trends over time, making complex data accessible and understandable for policymakers, business leaders, and researchers as they develop strategic plans.</p>
        </div>
    """, unsafe_allow_html=True)

elif page_selection == "Dashboard":
    # Dashboard Page
    st.markdown("<h1 class='header-style'>Power BI Dashboard Integration</h1>", unsafe_allow_html=True)

    # Sidebar for user interactions
    st.sidebar.header("Dashboard Controls")
    dashboard_height = st.sidebar.slider("Select dashboard height:", 400, 1000, 600, step=50)

    # Embed the Power BI dashboard using an iframe with custom styling
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=169458a4-3afa-4591-8f0d-14b214c49eb1&autoAuth=true&ctid=dbc112df-c598-4c12-9d48-faa8dfce15f0"  # Replace with your actual Power BI embed URL

    components.html(
        f"""
        <div class="iframe-container">
            <iframe 
                title="Power BI Dashboard" 
                width="100%" 
                height="{dashboard_height}" 
                src="{power_bi_url}" 
                frameborder="0">
            </iframe>
        </div>
        """,
        height=dashboard_height + 50  # Slightly more to include padding
    )

elif page_selection == "Chat with GPT-3.5":
    st.markdown("<h1 class='header-style'>Ask me:</h1>", unsafe_allow_html=True)

    # Chat interface
    if "history" not in st.session_state:
        st.session_state["history"] = []

    # User input
    user_input = st.text_input("You:", placeholder="Type your message here...")

    if user_input:
        # Call the OpenAI API for GPT-3.5 response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ 
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state["history"],
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        st.session_state["history"].append({"role": "user", "content": user_input})
        st.session_state["history"].append({"role": "assistant", "content": answer})

        # Display the chat interface
        st.text_area("GPT-3.5:", value=answer, height=200, max_chars=None, key=None)

    # Display the chat history in a more structured way
    for message in st.session_state["history"]:
        if message["role"] == "user":
            st.markdown(f"<div class='message-container'><div class='message-user'>{message['content']}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='message-container'><div class='message-assistant'>{message['content']}</div></div>", unsafe_allow_html=True)
