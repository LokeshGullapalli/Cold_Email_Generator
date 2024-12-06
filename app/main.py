import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from resource.chains import Chain
from resource.portfolio import Portfolio
from resource.utils import clean_text

import sqlite3
import streamlit as st

st.write(f"SQLite version: {sqlite3.sqlite_version}")

# Set page configuration at the top
st.set_page_config(
    layout="wide",
    page_title="Cold Email Generator",
    page_icon="📧"
)

# Inject custom CSS for a creative dark theme
st.markdown(
    """
    <style>
    /* Target the text input widget */
    div[data-testid="stTextInput"] input {
        width: 100% !important;
        max-width: 400px !important; /* Adjust this value as needed */
        box-sizing: border-box;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar configuration
st.sidebar.title("🌌 **Creative Cold Email Generator**")
st.sidebar.write("Generate personalized, professional, and visually stunning emails with ease.")

username = st.sidebar.text_input("Your Name (optional):", value="Guest")

st.sidebar.markdown("""
**How to Use:**
1. Enter a careers URL.
2. Choose email format & number of jobs.
3. Click Submit and enjoy the show!
""")

format_option = st.sidebar.radio(
    "Select Email Format:",
    ("Markdown", "HTML", "Plain Text")
)

max_jobs = st.sidebar.slider("Max Number of Jobs to Display:", min_value=1, max_value=10, value=5)


def create_streamlit_app(llm, portfolio, clean_text):
    # Titles and subtitles
    st.markdown("<h1 class='title'>📧 Cold Email Generator</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='subtitle'>Welcome {username}! Unlock new business opportunities with a creative flair.</h2>",
                unsafe_allow_html=True)

    # Use a container to center content and add spacing
    with st.container():
        st.write("")  # Optional spacing
        # Create equal-width columns
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Enter a Careers URL 👇")
            url_input = st.text_input("", value="https://www.atlassian.com/company/careers/details/16968")
            submit_button = st.button("Submit")

        with col2:
            st.markdown("### About This Tool 🌱")
            st.write("This application fetches job postings from a provided careers page, "
                     "and crafts a captivating cold email showcasing your company's capabilities.")
            st.write("Customize your experience using the sidebar, adjust the email format "
                     "and number of jobs, then watch as the results come alive!")

    if submit_button:
        with st.spinner('🔄 Fetching and processing job data...'):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                if not all(isinstance(job, dict) for job in jobs):
                    st.error("❌ The LLM did not return a list of job dictionaries.")
                else:
                    displayed_jobs = jobs[:max_jobs]
                    if displayed_jobs:
                        st.success("✅ Jobs retrieved successfully!")
                        progress_bar = st.progress(0)

                        for i, job in enumerate(displayed_jobs):
                            with st.expander(job.get('role', 'Unknown Role'), expanded=True):
                                st.markdown(f"**Experience:** {job.get('experience', 'N/A')}")
                                st.markdown("**Skills:**")
                                for skill in job.get('skills', []):
                                    st.write(f"- {skill}")
                                st.markdown("**Description:**")
                                st.write(job.get('description', 'N/A'))

                                skills = job.get('skills', [])
                                links = portfolio.query_links(skills)
                                email = llm.write_mail(job, links)

                                st.markdown("### Generated Email:")
                                if format_option == "Markdown":
                                    st.code(email, language='markdown')
                                elif format_option == "HTML":
                                    st.markdown(email, unsafe_allow_html=True)
                                else:  # Plain Text
                                    st.text(email)

                            progress_bar.progress(int((i + 1) / len(displayed_jobs) * 100))
                    else:
                        st.warning("⚠️ No jobs found at the provided URL.")
            except Exception as e:
                st.error(f"An Error Occurred: {e}")



if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
