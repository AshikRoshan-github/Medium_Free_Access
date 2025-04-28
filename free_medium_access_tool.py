import streamlit as st

# Function to generate the correct URL based on the chosen option
def generate_url(url, option):
    if option == 'Freedium':
        return f"https://freedium.cfd/{url}"
    elif option == 'ReadMedium':
        return f"https://readmedium.com/{url}"
    elif option == '12ft.io':
        return f"https://12ft.io/{url}"
    elif option == 'Archive.is':
        return f"https://archive.is/{url}"
    else:
        return None

# Streamlit user interface
st.set_page_config(page_title="Free Medium Access Tool", page_icon="🔗", layout="centered")

# Title and description with an icon
st.title("Free Medium Access Tool 🔓")
st.markdown("""
    This tool allows you to access Medium articles for free through various services.
    Simply paste the URL and select a service to bypass paywalls!
""")

# Input field for the user to paste a URL
user_url = st.text_input("Paste your URL here:", key="url", placeholder="Enter Medium article URL")

# Dropdown to select the service (Freedium, ReadMedium, 12ft.io, Archive.is)
option = st.selectbox("Select a service to format your URL:", 
                      ['Freedium', 'ReadMedium', '12ft.io', 'Archive.is'], 
                      help="Choose a service that will format your URL.")

# Show real-time formatted URL without the button
if user_url:
    with st.spinner('Processing URL...'):
        formatted_url = generate_url(user_url, option)

    # Display the formatted URL as a button (styled link)
    if formatted_url:
        st.markdown(f"""
            <a href="{formatted_url}" target="_blank" style="
                display: inline-block;
                padding: 12px 24px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #007bff;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            " onmouseover="this.style.backgroundColor='#0056b3'" onmouseout="this.style.backgroundColor='#007bff'">
                Open your formatted URL
            </a>
        """, unsafe_allow_html=True)

        # JavaScript to auto-click the link and open in a new tab after 1 second
        st.markdown(f"""
            <script>
                setTimeout(function() {{
                    window.open("{formatted_url}", "_blank");
                }}, 1000);
            </script>
        """, unsafe_allow_html=True)
    else:
        st.warning("Invalid URL or service selection. Please check and try again.")
else:
    st.info("Enter a URL to get started!")

# Add helpful information in the sidebar
st.sidebar.title("How to Use")
st.sidebar.markdown("""
1. **Paste any URL** into the input field.
2. **Select the desired service** to format the URL.
3. **Your formatted URL** will appear below and will open automatically in a new tab.
4. If you encounter any issues, recheck the URL or service selection.
""")
