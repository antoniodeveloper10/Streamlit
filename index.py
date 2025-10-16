import streamlit    as st


pages = {
    "Menu": [
        st.Page("pages/home.py", title="DashBoard"),
    ],
    "Produção": [
        # st.Page("pages/home.py", title="Home"),
        st.Page("pages/Sacarias.py", title="Sacaria"),
        st.Page("pages/testes.py", title="Testes"),
    ]
}

pg = st.navigation(pages)

pg.run()


