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
Ensure you have a .env file containing your GROQ_API_KEY.

4. Run the Streamlit app:
   ```bash
   streamlit run app/main.py

## Example Usage
Step 1: Provide the careers page URL in the main input box.
Step 2: Choose between Markdown, HTML, or Plain Text on the sidebar.
Step 3: Select the number of job listings to display.
Step 4: Click "Submit" and watch the magic happen!

## Sample Images
UI of the Website: Shows the main interface where you input a URL and see the generated content.

Different Features (HTML, Markdown, Plain Text): Demonstrates how you can switch output formats easily and shows the sidebar options.

Sample Result: An example of the generated email and listed jobs, illustrating the final output.

## Troubleshooting
If you encounter errors related to large context size, consider reducing the input size by chunking the content or summarizing before extraction.
For issues related to ChromaDB storage or data migration, ensure you’re using a compatible Chroma version and have deleted old vectorstore directories if needed.
Check the Streamlit logs and printed outputs for debugging messages.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for new features, bug fixes, or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
