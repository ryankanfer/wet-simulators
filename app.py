import streamlit as st

# Page configuration
st.set_page_config(page_title="The Preston – Guest Portal", page_icon="💧", layout="centered")

# Custom CSS for luxury branding
st.markdown("""
<style>
body {
    background-color: #2F2F2F;
    color: #F4C8A6;
    font-family: 'Lato', sans-serif;
}
h1 {
    font-family: 'Playfair Display', serif;
    color: #D4AF37;
    text-align: center;
    font-size: 3em;
    margin-bottom: 0.2em;
}
h3 {
    text-align: center;
    font-style: italic;
    font-size: 1.25em;
    margin-top: 0;
    margin-bottom: 2em;
}
.card {
    background-color: #2F2F2F;
    border: 1px solid #D4AF37;
    padding: 1.5rem;
    margin: 1rem auto;
    border-radius: 12px;
    max-width: 500px;
    text-align: center;
    transition: 0.3s;
}
.card:hover {
    background-color: #3a3a3a;
    box-shadow: 0 0 10px #D4AF37;
}
a {
    text-decoration: none;
    color: #6FB7C5;
    font-weight: bold;
}
hr {
    border: 1px solid #D4AF37;
    margin-bottom: 2rem;
}
.footer {
    text-align: center;
    font-size: 0.85em;
    color: #aaa;
    margin-top: 4rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1>THE PRESTON</h1>
<h3>Private Guest Access<br><em>...you know you want to.</em></h3>
<hr>
""", unsafe_allow_html=True)

# Episode card(s)
st.markdown("""
<div class='card'>
    <h2>💧 Orientation Chaos</h2>
    <p>Episode 3 · Charlie’s First Shift</p>
    <a href="episode3/app.py">ENTER SUITE</a>
</div>

<div class='card'>
    <h2>🔒 Guest List Discretion</h2>
    <p>Episode 4 · Coming Soon</p>
    <span style='color:#777;'>[ MEMBERS ONLY ]</span>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""<div class='footer'>
© The Preston Hotel · Confidential Guest Portal · @WETseries
</div>""", unsafe_allow_html=True)