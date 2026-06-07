# app.py

import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import time

from graph_logic2 import create_graph, shortest_path
from data2 import halte

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="DSS Trans Metro Dewata",
    page_icon="🚌",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp{
    background:linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e293b
    );
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#38bdf8;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

.card{
    background:rgba(30,41,59,0.8);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,.1);
}

.metric{
    color:#38bdf8;
    font-size:22px;
    font-weight:bold;
    margin-top:10px;
}

.stButton>button{
    width:100%;
    background:#0ea5e9;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GRAPH
# =========================
G = create_graph()

# =========================
# HEADER
# =========================
st.markdown("""
<div class='main-title'>
🚌 TRANS METRO DEWATA
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Sistem Pendukung Keputusan Rute Bus Trans Metro Dewata
Menggunakan Algoritma Dijkstra dan Graph
</div>
""", unsafe_allow_html=True)

# =========================
# LAYOUT
# =========================
left,right = st.columns([1,2])

# =========================
# PANEL KIRI
# =========================
with left:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🚏 Pilih Halte")

    nodes = list(G.nodes())

    start = st.selectbox(
        "Halte Asal",
        nodes
    )

    end = st.selectbox(
        "Halte Tujuan",
        nodes
    )

    cari = st.button(
        "🚌 Cari Rute"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PANEL KANAN
# =========================
with right:

    if cari:

        with st.spinner(
            "🔍 Menghitung rute terbaik..."
        ):
            time.sleep(1)

        try:

            path, distance = shortest_path(
                G,
                start,
                end
            )

            st.markdown(
                "<div class='card'>",
                unsafe_allow_html=True
            )

            st.success(
                "Rute berhasil ditemukan"
            )

            st.markdown(
                "<div class='metric'>🚏 Rute Halte</div>",
                unsafe_allow_html=True
            )

            st.write(
                " ➜ ".join(path)
            )

            st.markdown(
                f"<div class='metric'>🛣️ Total Jarak : {distance} KM</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='metric'>📍 Jumlah Halte : {len(path)-1}</div>",
                unsafe_allow_html=True
            )

            st.info(f"""
Halte Asal : {start}

Halte Tujuan : {end}

Jumlah Halte Dilewati : {len(path)}

Total Jarak : {distance} KM
""")

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

            fig, ax = plt.subplots(
                figsize=(12,8)
            )

            fig.patch.set_facecolor(
                '#020617'
            )

            ax.set_facecolor(
                '#020617'
            )

            pos = nx.spring_layout(
                G,
                seed=42
            )

            nx.draw_networkx_nodes(
                G,
                pos,
                node_color="#06b6d4",
                node_size=2500
            )

            nx.draw_networkx_labels(
                G,
                pos,
                font_color="white",
                font_size=9
            )

            nx.draw_networkx_edges(
                G,
                pos,
                edge_color="white",
                width=2
            )

            edge_labels = nx.get_edge_attributes(
                G,
                'weight'
            )

            nx.draw_networkx_edge_labels(
                G,
                pos,
                edge_labels=edge_labels,
                font_color="yellow"
            )

            path_edges = list(
                zip(
                    path,
                    path[1:]
                )
            )

            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=path_edges,
                edge_color="red",
                width=5
            )

            st.markdown(
                "<div class='card'>",
                unsafe_allow_html=True
            )

            st.subheader(
                "🗺️ Visualisasi Rute Bus"
            )

            st.pyplot(fig)

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        except:
            st.error(
                "Rute tidak ditemukan"
            )

# =========================
# DATA HALTE
# =========================
st.write("")
st.write("")

st.markdown("""
<h2 style='text-align:center;color:#38bdf8'>
📋 Data Halte Trans Metro Dewata
</h2>
""", unsafe_allow_html=True)

cols = st.columns(3)

i = 0

for asal in halte:

    with cols[i % 3]:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"### 🚏 {asal}"
        )

        for tujuan, jarak in halte[asal].items():

            st.write(
                f"➡️ {tujuan} — {jarak} KM"
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    i += 1