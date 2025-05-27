import streamlit as st
from PIL import Image
import base64
import os

st.set_page_config(page_title="MangiAmore Restaurant", layout="wide")

# ----------- base64 Function -----------
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ----------- Custom CSS -----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: black !important;
        color: white !important;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    input, textarea {
        color: white !important;
        background-color: #222 !important;
        border: 1px solid white !important;
        border-radius: 5px !important;
    }

    label {
        color: white !important;
    }

    ::placeholder {
        color: #ccc !important;
    }

    div.stButton > button {
        color: black !important;
        background-color: white !important;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        color: red !important;
        background-color: #f2f2f2 !important;
    }

    button[kind="formSubmit"] {
        color: black !important;
        background-color: white !important;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
        border: 2px solid black !important;
        transition: 0.3s ease-in-out;
    }

    button[kind="formSubmit"]:hover {
        color: red !important;
        background-color: #f2f2f2 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------- Menu Items -----------
menu_items = {
    "Pizza Margherita": {"price": 750, "image": "images/food1.jpg"},
    "Bulgogi-Stuffed Arancini": {"price": 280, "image": "images/food3.jpg"},
    "Spaghetti Carbonara": {"price": 350, "image": "images/Spaghetti Carbonara.jpg"},
    "Chorizo Mozzarella Gnocchi Bake": {"price": 500, "image": "images/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg"},
    "Lasagna": {"price": 400, "image": "images/food7.jpg"},
    "Tiramisu": {"price": 250, "image": "images/food9.jpg"},
    "Ravioli": {"price": 600, "image": "images/food2.jpg"},
    "Vanilla Panna Cotta with Raspberry Coulis": {"price": 200, "image": "images/food10.jpg"},
    "Focaccia": {"price": 300, "image": "images/food12.jpg"},
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# ----------- Sidebar Navigation -----------
st.sidebar.title("🍴 Restaurant Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Menu", "Add to Cart", "Contact"])

# ----------- Home Page -----------
if page == "Home":
    st.markdown("""
        <h1 style='text-align: center; font-size: 60px; color: white; margin-top: -40px;'>
          MangiAmore Restaurant
        </h1>
    """, unsafe_allow_html=True)

    st.subheader("Taste the Love of Italy ")
    st.write("""
    Welcome to MangiAmore! Choose your favorite meals and add them to your cart.
    We serve authentic Italian cuisine crafted with passion and the freshest ingredients.
    """)

    cols = st.columns(3)
    for i, (item, details) in enumerate(menu_items.items()):
        with cols[i % 3]:
            image_path = details["image"]
            if os.path.exists(image_path):
                st.image(image_path, caption=item, use_container_width=True)
            else:
                st.error(f"⚠️ Image not found: {image_path}")
            st.write(f"**Price: {details['price']} PKR**")
            if st.button(f"Add {item}", key=f"home_{item}"):
                st.session_state.cart.append((item, details["price"]))
                st.success(f"{item} added to cart!")

# ----------- About Us Page -----------
elif page == "About Us":
    img_base64 = get_base64_of_image("images/foodback.jpg")

    st.markdown(
        f"""
        <style>
        .about-container {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 60px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 0 15px rgba(0,0,0,0.6);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="about-container">
            <h1>👨‍🍳 About Us</h1>
            <p style="font-size: 20px;">
            Welcome to <strong>MangiAmore Restaurant</strong> — where flavor meets passion.<br><br>
            We believe food is not just about taste, it's about experience. Our chefs craft every dish with fresh ingredients and love, bringing comfort and creativity to your plate.<br><br>
            From sizzling starters to mouth-watering mains and dreamy desserts, we have something for every craving.<br><br>
            Whether you're dining in or ordering out, we serve a culinary experience you won't forget.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------- Menu Page -----------
elif page == "Menu":
    st.title("📋 Our Menu")

    for item, details in menu_items.items():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            image_path = details["image"]
            if os.path.exists(image_path):
                st.image(image_path, width=150)
            else:
                st.error(f"⚠️ Image not found: {image_path}")
        with col2:
            st.write(f"**{item}**")
            st.write(f"Price: {details['price']} PKR")
        with col3:
            if st.button(f"Add", key=f"menu_{item}"):
                st.session_state.cart.append((item, details["price"]))
                st.success(f"{item} added to cart!")

# ----------- Add to Cart Page -----------
elif page == "Add to Cart":
    st.title("🛒 Your Cart")
    if st.session_state.cart:
        total = 0
        for i, (item, price) in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {item} - {price} PKR")
            total += price
        st.write(f"**Total: {total} PKR**")
    else:
        st.info("Your cart is empty. Add some items from the menu.")

# ----------- Contact Page -----------
elif page == "Contact":
    st.title("📬 Contact Us")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send")

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all fields before submitting.")
            else:
                st.success(f"Thank you, {name}! Your message has been received.")