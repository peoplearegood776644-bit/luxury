import streamlit as st

# Page Configuration for a clean, professional look
st.set_page_config(page_title="LuxeLife Concierge", page_icon="💎", layout="wide")

# Custom CSS for a luxury aesthetic (Gold and Dark themes)
st.markdown("""
    <style>
    .main { background-color: #0c0c0c; color: #d4af37; }
    .stButton>button { background-color: #d4af37; color: #0c0c0c; border-radius: 5px; border: none; font-weight: bold; }
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# App Header
st.title("💎 LuxeLife Concierge")
st.subheader("Your exclusive portal to global refinement.")

# Sidebar Navigation
menu = ["Dashboard", "Curated Stays", "Private Charters", "VIP Events"]
choice = st.sidebar.radio("Select Category", menu)

if choice == "Dashboard":
    st.write("### Welcome back, Member #7001.")
    st.info("Today's Curated Highlight: Private viewing at the Louvre.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Exclusive Invites", value="3 Pending")
    with col2:
        st.metric(label="Concierge Status", value="Active")

elif choice == "Curated Stays":
    st.header("Handpicked Estates")
    st.write("Explore villas and private homes in the world's most desirable destinations.")
    # Example luxury listings
    st.image("https://unsplash.com", caption="Amalfi Coast Villa")
    if st.button("Request Booking"):
        st.success("Your personal attaché has been notified.")

elif choice == "Private Charters":
    st.header("Elite Travel")
    vehicle_type = st.selectbox("Preferred Mode", ["Gulfstream G650", "Super Yacht", "Luxury Helicopter"])
    st.write(f"Inquiring about {vehicle_type} availability...")
    st.button("Search Routes")

elif choice == "VIP Events":
    st.header("Exclusive Access")
    st.write("Early access to limited collections and fashion releases.")
    st.checkbox("Paris Fashion Week Front Row")
    st.checkbox("Monaco Grand Prix Yacht Access")
    st.button("Request Invitations")
