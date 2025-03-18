import streamlit as st
import functions as fc

todos = fc.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    fc.write_todos(todos)
    st.session_state.new_todo = ""


st.title("My To-Do App")
st.subheader("This is my first web app")
st.write("Be productive by adding your to-dos in here")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add a todo", label_visibility="hidden",
              placeholder="Add a new to-do",
              on_change=add_todo, key="new_todo")
