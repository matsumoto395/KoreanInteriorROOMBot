import streamlit as st, glob, os

st.title("Reels 自動生成ログ")
for p in sorted(glob.glob("/tmp/*.mp4"), reverse=True)[:10]:
    st.video(p)
    st.text(os.path.basename(p))
st.info("ここから手動再生成するには CLI `python app/main.py` を実行してください。")
