import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")
st.title(":blue[Calculator]", text_alignment="center")


if "calc_value" not in st.session_state:
    st.session_state.calc_value = ""

if "input_value" not in st.session_state:
    st.session_state.input_value = ""


def add_number(num):
    st.session_state.calc_value += str(num)
    st.session_state.input_value = st.session_state.calc_value

def clear():
    st.session_state.calc_value = ""
    st.session_state.input_value = ""

def backspace():
    st.session_state.calc_value = st.session_state.calc_value[:-1]
    st.session_state.input_value = st.session_state.calc_value

def calculate():
    try:
        expression = st.session_state.calc_value.replace("%", "/100")
        result = eval(expression)
        st.session_state.calc_value = str(result)
        st.session_state.input_value = str(result)
    except:
        st.session_state.calc_value = "Error"
        st.session_state.input_value = "Error"


st.markdown("""
<style>
.stApp { 
    background-color: #F5F5F5; 
}
.block-container {
    max-width: 400px;
    margin: auto;
}
.stTextInput input {
    text-align: right;
    font-size: 45px;
    background-color: #1C1C1C;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
}

div.stButton > button {
    height: 65px;
    width: 65px;
    border-radius: 50%;
    font-size: 24px;
    margin: 6px;
    border: none;
    background-color: #2F2F2F;
    color: white;
    box-shadow: 0px 3px 6px rgba(0,0,0,0.2);
}

div.stButton > button:hover {
    background-color: darkblue;
}
</style>
""", unsafe_allow_html=True)


st.text_input(
    "Enter expression",
    key="input_value",
    on_change=lambda: st.session_state.update({"calc_value": st.session_state.input_value}) or calculate()
)


# Row 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("AC", on_click=clear)
with col2:
    st.button("C", on_click=backspace)
with col3:
    st.button("%", on_click=add_number, args=("%",))
with col4:
    st.button("÷", on_click=add_number, args=("/"))

# Row 2
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("7", on_click=add_number, args=("7",))
with col2:
    st.button("8", on_click=add_number, args=("8",))
with col3:
    st.button("9", on_click=add_number, args=("9",))
with col4:
    st.button("×", on_click=add_number, args=("*",))

# Row 3
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("4", on_click=add_number, args=("4",))
with col2:
    st.button("5", on_click=add_number, args=("5",))
with col3:
    st.button("6", on_click=add_number, args=("6",))
with col4:
    st.button("−", on_click=add_number, args=("-",))

# Row 4
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("1", on_click=add_number, args=("1",))
with col2:
    st.button("2", on_click=add_number, args=("2",))
with col3:
    st.button("3", on_click=add_number, args=("3",))
with col4:
    st.button("➕", on_click=add_number, args=("+",))

# Row 5
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("0", on_click=add_number, args=("0",))
with col2:
    st.button(".", on_click=add_number, args=(".",))
with col3:
    st.button("⌫", on_click=backspace)
with col4:
    st.button("=", on_click=calculate)