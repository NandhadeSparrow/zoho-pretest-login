import streamlit as st
from util import auth


def check_dup():
    if auth.check_dup(st.session_state['username-register']):
        st.session_state['duplicate-user'] = True


def register():
    st.markdown('## Register')
    st.text_input('FullName', value="", key='fullname-register')
    st.text_input('Date of Birth', value="", key='dob-register')
    st.text_input('Gender', value="", key='gender-register')   


    st.text_input('Username', value="", on_change=check_dup, key='username-register')
    if 'duplicate-user' in st.session_state and st.session_state['duplicate-user']:
        st.warning('Username already exists')
    
    
    st.text_input('Password', value="", key='password-register')



    if not st.session_state['duplicate-user'] \
        and st.session_state['fullname-register'] \
        and st.session_state['username-register'] \
        and st.session_state['password-register']:
        if st.button('Register', key='register',type="secondary"):
            reg = auth.register()
            if reg:
                st.switch_page("pages/profile.py")



if __name__ == '__main__':
    register()