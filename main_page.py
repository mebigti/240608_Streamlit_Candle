import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
# st.image('umbro.png', caption='sunrise') 왜 이미지가 로딩되지 않는지 알기 어려움 일단은 마크다운 방식의 경로 및 링크 생성이 동일한 기능을 수행하므로 이를 따르도록 함
st.title("CAT")
st.markdown("[![Click me](./static/umboy.png)](http://localhost:8501/#cat)")
