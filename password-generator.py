# import streamlit as st  # Import Streamlit for creating the web-based UI
# import random  # Import random for generating random choices
# import string  # Import string to use predefined character sets




# # Function to generate a random password
# def generate_password(length, use_digits, use_special):
#     characters = string.ascii_letters  # Includes uppercase and lowercase letters

#     if use_digits:
#         characters += string.digits  # Adds numbers (0-9) if selected

#     if use_special:
#         characters += (
#             string.punctuation
#         )  # Adds special characters (!@#$%^&* etc.) if selected

#     # Generate a password by randomly selecting characters based on the length provided
#     return "".join(random.choice(characters) for _ in range(length))


# # Streamlit UI setup
# st.title("🔏Simple Password Generator")  # Display the app title on the web page

# # User input: password length (slider to select length between 6 and 32 characters)
# length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# # Checkbox options for including numbers and special characters in the password
# use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
# use_special = st.checkbox(
#     "Include special characters"
# )  # Checkbox for special characters (!@#$%^&*)

# # Button to generate password
# if st.button("Generate Password"):
#     password = generate_password(
#         length, use_digits, use_special
#     )  # Call the password generation function
#     st.write(f"Generated Password: `{password}`")  # Display the generated password

#     st.write("--------------------------------------------------------------------")
#     st.write("Made by 💞[Tayyaba Ajaz]")


import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
st.title("🔏 Custom Password Generator")  # Display the app title on the web page

# Create session state for storing entered password
if "user_password" not in st.session_state:
    st.session_state.user_password = None

# Input field for user's password
user_password = st.text_input("Enter any password:", type="password")

# Button to confirm password input
if st.button("Enter"):
    if user_password:
        st.session_state.user_password = user_password
        st.success("Password saved! Now you can generate a new one.")
    else:
        st.error("Please enter a password before proceeding.")

# If a password has been entered, allow generating a new one
if st.session_state.user_password:
    st.write(f"Your entered password: `{st.session_state.user_password}`")

    # User input: password length (slider to select length between 6 and 32 characters)
    length = st.slider("Select new password length:", min_value=6, max_value=32, value=12)

    # Checkbox options for including numbers and special characters in the new password
    use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
    use_special = st.checkbox("Include special characters")  # Checkbox for special characters (!@#$%^&*)

    # Button to generate a new password
    if st.button("Generate New Password"):
        new_password = generate_password(length, use_digits, use_special)  # Generate new password
        st.write(f"Generated Password: `{new_password}`")  # Display the generated password

        st.write("--------------------------------------------------------------------")
        st.write("Made by 💞[Tayyaba Ajaz]")
        
