import streamlit as st
from util.db import save_one, get_by_uid, check_username
def login():
    uid = check_username(st.session_state['username-login'])
    st.session_state['uid-session'] = uid
    return True


def register():
    user = {
        'username': st.session_state['username-register'],
        'password': st.session_state['password-register'],
        'fullname': st.session_state['fullname-register'],
        'dob': st.session_state['dob-register'],
        'gender': st.session_state['gender-register'],
    }
    res = save_one(user)
    print(res._id)


def logout():
    st.session_state['username-session'] = None
    st.session_state['password-session'] = None


def logged():
    return 'uid' in st.session_state and st.session_state['uid'] is not None    


def check_dup(username):
    st.session_state['duplicate-user'] = False
    # if check_username(username):
    #     st.session_state['duplicate-user'] = True
    # else:
    #     st.session_state['duplicate-user'] = False