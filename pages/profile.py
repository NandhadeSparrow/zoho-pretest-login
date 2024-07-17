import streamlit as st
from util.db import get_by_uid
from util.auth import logout


def profile():
    st.markdown('## Profile')

    if 'uid-session' in st.session_state and st.session_state['username-session']:
        user = get_by_uid(st.session_state['uid-session'])
                    # process user
        st.write('Full Name: ', user['fullname'])
        st.write('Date of Birth: ', user['dob'])
        st.write('Gender: ', user['gender'])
    else:
        return 'login'

    if st.button('Logout', key='logout', on_click=logout, type="secondary"):
        # redirect
        pass
if __name__ == '__main__':
    profile()