
import streamlit as st

# Page configuration
st.set_page_config(page_title="The Preston – Guest Portal", page_icon="💧", layout="centered")

# Import Google Fonts and set background
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Lato:wght@300;400&display=swap" rel="stylesheet">
<style>
body {
    font-family: 'Lato', sans-serif;
    background-image: url('https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #F4C8A6;
    text-align: center;
}
h1 {
    font-family: 'Playfair Display', serif;
    color: #D4AF37;
    font-size: 3.2em;
    margin-bottom: 0.2em;
}
h3 {
    font-style: italic;
    font-size: 1.2em;
    margin-top: 0;
    margin-bottom: 2em;
}
.card {
    background-color: rgba(47, 47, 47, 0.85);
    border: 1px solid #D4AF37;
    padding: 1.5rem;
    margin: 1rem auto;
    border-radius: 16px;
    max-width: 480px;
    transition: 0.3s;
    backdrop-filter: blur(4px);
}
.card:hover {
    background-color: rgba(70, 70, 70, 0.9);
    box-shadow: 0 0 12px #D4AF37;
}
a {
    text-decoration: none;
    color: #6FB7C5;
    font-weight: bold;
}
hr {
    border: 1px solid #D4AF37;
    margin: 2rem auto;
    width: 60%;
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
st.markdown("""<h1>THE PRESTON</h1><h3>Private Guest Access<br><em>...you know you want to.</em></h3><hr>""", unsafe_allow_html=True)

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
