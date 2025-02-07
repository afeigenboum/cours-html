import streamlit as st

st.title("Le rappeur EDGE:")

st.write("Edge, stylisé EDGE, est un rappeur français. Il commence à se forger un nom dans le monde du rap français dans le début des années 2020, notamment grâce à ses projets :yellow[Off] et :orange[Off]:green[shore] qu'il réalise respectivement en 2020 et 2021. Il a récemment sorti un projet intitulé :blue[de janvier à janvier] dont vous trouverez le single plus bas :notes:.")

st.title("DERNIERS ALBUMS DE EDGE")


col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-images.dzcdn.net/images/cover/ac83584a300af3fee17c851c052948a3/0x1900-000000-80-0-0.jpg", caption = "Album : Off")

with col3:
    st.image("https://cdn-images.dzcdn.net/images/cover/1a1315b97f058dfdf71bcf431db2c502/500x500.jpg", caption = "Album : :blue[De janvier à janvier]")


with col2:
    st.image("https://cdn-images.dzcdn.net/images/cover/e732022bfaa7c4893d0dd2bf1bcec661/0x1900-000000-80-0-0.jpg", caption = "Album : :orange[Off]:green[shore]")

st.title("Single de l'album :notes: :")

st.video("https://www.youtube.com/watch?v=xD01r-KdF00")

with st.sidebar:
    st.title("Streamez EDGE")
    st.html('<a href="https://open.spotify.com/intl-fr/artist/0ZCX1rGywF2LATUUCq0nOg" style="color:green">Spotify</a>')
    st.html('<a href="https://www.deezer.com/fr/artist/95149082" style="color:purple">Deezer</a>')