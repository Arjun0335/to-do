import streamlit as st
import datetime
now = datetime.datetime.now()
custom_css = """<style>
                textarea.stTextArea {
                width: 400px !important;
                height: 400px !important;}
                </style>"""
st.title("To-Do")
st.header("Create your today To-Do")
st.subheader(f"Date: {now.strftime('%Y-%m-%d')}")
st.write(custom_css, unsafe_allow_html=True)
user_input = st.text_area("Type your task here:", " ")
if st.button("Add Task"):
    if user_input:
        st.session_state["task_list"].append(user_input)
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []
if "previous_task" not in st.session_state:
    st.session_state["previous_task"] = []
    
    
for i, t in enumerate (st.session_state["task_list"]):
    if st.checkbox(f" {i + 1}. {t}"):
        st.session_state["task_list"].remove(t)
        st.session_state['previous_task'].append(t)
    if st.button("Remove"):
        st.session_state["task_list"].remove(t)
    
with st.sidebar:
    st.write("Today completed task:")
    for i, t in enumerate (st.session_state["previous_task"]):
        st.write(f" {i + 1}. {t}")
    
if now.strftime('%H:%M:%S') == "00:00:00":
    st.write(f"Your yesterday pending tasks are: {st.session_state["task_list"]}")
    st.session_state["task_list"] = []