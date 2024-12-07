# Cold Email Generator 📧

Welcome to the **Cold Email Generator**, an interactive Streamlit application that takes a careers page URL, extracts job postings, and generates a highly customized cold email. This tool leverages AI to parse job descriptions, highlight your company's capabilities, and produce compelling outreach emails.

## Features

- **Input:** Provide any careers page URL from which the app will scrape job postings.
- **Multiple Output Formats:** Choose between Markdown, HTML, or Plain Text for the generated cold emails.
- **Limit Displayed Jobs:** Control how many job listings to display and include in the email.
- **Auto-Fetched Portfolio Links:** Automatically query a portfolio (stored locally) to match job skills with relevant portfolio examples.

## How It Works

1. **Enter a URL:** Input a careers URL into the text field.
2. **Select Format & Number of Jobs:** Use the sidebar to choose your email format and how many jobs to highlight.
3. **Generate Email:** Click "Submit" to process the URL, extract job data, and produce your customized cold email.

## Under the Hood

- **Data Extraction:** Utilizes `WebBaseLoader` to scrape and clean content from the given URL.
- **LLM-Powered Analysis:** Uses a large language model (via the Groq API) to parse job descriptions and format the output.
- **ChromaDB Integration:** Links skills to related portfolio items stored in ChromaDB, showcasing relevant past work and capabilities.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Cold_Email_Generator.git
   
2. Navigate into the project directory:
   ```bash
   cd Cold_Email_Generator
   
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
- Ensure you have a .env file containing your GROQ_API_KEY.

4. Run the Streamlit app:
   ```bash
   streamlit run app/main.py

5. Open the app in your browser:

- After running the above command, Streamlit will provide a local URL (e.g., http://localhost:8501). Open this URL in your browser to start using the app.

## Usage
- **Open the App:** Launch the app by visiting the provided URL after running streamlit run app/main.py.
- **Input URL:** Paste a careers page URL into the input field on the main page.
- **Customize Settings:** Use the sidebar to:
-- Select the email format (Markdown, HTML, Plain Text).
-- Adjust the number of job listings to display.
- **Submit and View Results:** Click "Submit" to fetch and process job data. Review the generated cold email, job listings, and linked portfolio items.

## Screenshots
- UI of the Website
<img src="./images/ui_example.png" alt="UI Example" width="300"/>

- Different Features (HTML, Markdown, Plain Text)
<img src="./images/format_features.png" alt="Format Features" width="300"/>

- Sample Result
<img src="./images/sample_result.png" alt="Sample Result" width="300"/>

## Technologies
- **Streamlit:** For building interactive web UIs with Python.
- **Chromadb:** For vector-based storage and portfolio link retrieval.
- **LangChain / LLM:** For AI-driven parsing and email generation.
- **Python:** The main language for server-side logic and data handling.
- **Groq API:** Accessing a large language model for intelligent text analysis.

## Troubleshooting
- **Context Too Big:** If you encounter a "Context too big" error, consider breaking the input text into chunks before processing.
- **SQLite Issues:** If encountering SQLite errors with ChromaDB, ensure you’re using a supported version or switch to the DuckDB-based persistence.
- **Check Logs:** For debugging, print out raw LLM output and inspect Streamlit logs.


## License
This project is licensed under the MIT License. See the LICENSE file for details.
