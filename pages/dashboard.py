import streamlit as st

tab1, tab2 ,tab3= st.tabs(["dahsboard","createbot","profile"])

with tab1:
   st.subheader(":blue[bots]")
   row1 = st.columns(3)
   row2 = st.columns(3)

   for col in row1 + row2:
       tile = col.container(height=150)
       tile.title("💬")


with tab2:
    st.header(":blue[create bot]")
    one,two = st.columns([0.7, 0.3])
    with one:
        name = st.text_input('name',placeholder="enter your name")
        icon = st.file_uploader("icon")
        voice= st.write("Voice")
        T_to_S = st.checkbox('Text To Speech')
        S_to_T = st.checkbox('Speech To Text')
        voice_select = st.selectbox(
            'Voice',
            ('Google Bahasa Indonesia', 'Google Deutsch', 'Google español (es-ES)','Google español de Estados Unidos (es-US)'
             ,'Google français (fr-FR)','Google italiano (it-IT)','Google Nederlands (nl-NL)','Google polski (pl-PL)',
             'Google português do Brasil','Google UK English Female','Google UK English Male','Google US English'
             ,'Google русский','Google हिन्दी','Google 國語'))
        color = st.color_picker('Pick A Color', '#00f900')
        st.subheader("Data&Security")
        dataSource = st.file_uploader("data Source")
        st.write("-----------------------  or ------------------------   ")
        url = st.text_input("Upload url")
        simillarQuestions = st.checkbox('Generate Simillar Questions ')
        st.button("create bot", type="secondary")

with tab3:

    st.image('vector-business-men-icon.jpg',width=100)
    st.subheader('rakesh narlagiri')
    st.write('Email : rakeshnarlagiri@gmail.com')
    st.markdown("[help](#section-1)")
    st.markdown("[settings](#section-1)")
    st.link_button('signout',"#section-1")
