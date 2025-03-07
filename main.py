import streamlit as st


home_page = st.page(
    page="views/home.py",
    title="Home",
    icon=":material/security:",
    default=True,
)

blog_page= st.page(
    page="views/blog.py",
    title="Blog",
    icon=":material/security:",
)

pg = st.navigation(pages=[home_page, blog_page])

pg.run()