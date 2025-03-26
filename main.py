import streamlit as st
import requests
from frontend.home import show_home

if "user" in st.session_state and st.session_state.user == "user":
    show_home()
    st.stop()  # Stops further execution



if "user" not in st.session_state:
    st.session_state.user = None



USER = [None, "New", "old","user"]

USER = st.session_state.user

def set_user_user():
    st.session_state.user="user"
def set_old_user():
    st.session_state.user = "old"

def set_NEW_user():
    st.session_state.user = "New"

if USER=="old":
    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://t3.ftcdn.net/jpg/05/99/17/30/360_F_599173089_foA2mPZ2Ija1z25NWjHWQwB4Ujpezdii.jpg");
                background-size: cover;
                background-position: center;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Login")
    user_email = st.text_input("Email")
    hashed_password = st.text_input("password")
    if st.button("Login"):
        response = requests.post("http://127.0.0.1:5000/login", json={"email": user_email, "password": hashed_password})

        if response.status_code == 200:
            st.success("✅ Logged in Succesfully")
            st.session_state.user = "user"
            if st.session_state.user == "user":
                st.rerun()


        else:
            st.error("❌ Login request failed!")

elif USER=="New":
    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://t3.ftcdn.net/jpg/05/99/17/30/360_F_599173089_foA2mPZ2Ija1z25NWjHWQwB4Ujpezdii.jpg");
                background-size: cover;
                background-position: center;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Register")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    phone = st.text_input("Phone Number")
    user_email = st.text_input("Email Id")
    hashed_password = st.text_input("Password")
    if st.button("Register"):
         response1 = requests.post("http://127.0.0.1:5000/register",json={"first_name":first_name,"last_name":last_name,"phone":phone,"email":user_email,"hashed_password":hashed_password})

         if response1.status_code == 201:
             st.info("Registration succesful")
             st.button("Login Now", on_click=set_old_user)

         else:
             st.error("❌ Register request failed!")


else:
    st.markdown(
        "<h1 style='text-align: center; color: white;'>🎧 Welcome to <span style='color:#ffcc33'>Suno</span></h1>"
        "<h2 style='text-align: center; color: white;'>Experience the future of music streaming 🎼🔥</h2>",
        unsafe_allow_html=True)


    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://t3.ftcdn.net/jpg/05/99/17/30/360_F_599173089_foA2mPZ2Ija1z25NWjHWQwB4Ujpezdii.jpg");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }
            .main {
                background: rgba(0, 0, 0, 0.6);
                padding: 20px;
                border-radius: 15px;
            }
            h1 {
                color: white !important;
                text-align: center;
                font-size: 50px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎵Register", use_container_width=True,on_click=set_NEW_user):
            st.session_state.user = "New"

    with col2:
        if st.button("🎤 Login 🎶", use_container_width=True,on_click=set_old_user):
            st.session_state.user = "old"

    st.write("## 🎵 Popular Artists")

    # Creating a 2-row grid with 3 columns each
    rows = [
        ["https://i.scdn.co/image/ab6761610000e5ebcb6926f44f620555ba444fca", "Pritam"],
        ["https://i.pinimg.com/736x/e8/d0/9d/e8d09dc7491d9801c8edb409a40186c7.jpg", "Arijit Singh"],
        ["https://images.firstpost.com/wp-content/uploads/2018/02/atif-aslam-825.jpg", "Atif Aslam"],
        ["https://m.media-amazon.com/images/M/MV5BODA4MjM2ODk4OF5BMl5BanBnXkFtZTcwNDgzODk1OQ@@._V1_FMjpg_UX1000_.jpg","poster"],
        ["https://i.scdn.co/image/ab67616d00001e026404721c1943d5069f0805f3","poster"],
        ["https://m.media-amazon.com/images/M/MV5BNjU5ZTljMDEtNzg5Ny00OTliLWI3NmYtOTE1ZDg3NTNkMDM0XkEyXkFqcGc@._V1_.jpg","poster"]
    ]

    for i in range(0, len(rows), 3):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(rows[i][0], caption=rows[i][1], use_container_width=True)
        with col2:
            if i + 1 < len(rows):
                st.image(rows[i + 1][0], caption=rows[i + 1][1], use_container_width=True)
        with col3:
            if i + 2 < len(rows):
                st.image(rows[i + 2][0], caption=rows[i + 2][1], use_container_width=True)
