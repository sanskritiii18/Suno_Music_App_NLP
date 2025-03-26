import streamlit as st

def show_home():
    st.title("🎶 Welcome to Suno!")
    st.write("Explore and listen to unlimited music.")
    st.title("Welcome to Suno 🎵")
    st.write("Enjoy unlimited music streaming!")
    st.sidebar.header("Navigation")
    st.sidebar.write("🎵 Home")
    st.sidebar.write("🎶 Your Playlists")
    st.sidebar.write("🔍 Search Songs")
    st.sidebar.write("⚙️ Settings")

    # Sample songs grid
    songs = [
        ["https://i.scdn.co/image/ab67616d0000b273a76f17cb5b0f04c8a1ab9b3c", "Song 1"],
        ["https://i.scdn.co/image/ab67616d0000b273fca98e70b43bff51a0cf0f8b", "Song 2"],
        ["https://i.scdn.co/image/ab67616d0000b273b0cb0b5b0b489ec6b3ea4d2d", "Song 3"],
        ["https://i.scdn.co/image/ab67616d0000b273c24bfb9237a8425e9338a489", "Song 4"]
    ]

    cols = st.columns(4)
    for i, (img, title) in enumerate(songs):
        with cols[i % 4]:  # Display 4 per row
            st.image(img, caption=title, use_container_width =True)
            st.button(f"🎵 Play {title}", key=f"play_{i}")  # Play button

# 🔥 Prevent automatic execution when imported into `main.py`
if __name__ == "__main__":
    show_home()
