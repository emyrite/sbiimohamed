# AI-Powered Resume Enhancer

This simple Flask service receives resume information from a webhook (e.g. a
Tally form), rewrites the experience using OpenAI, and returns a PDF version of
the enhanced resume.

## Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key in the environment:

   ```bash
   export OPENAI_API_KEY=YOUR_KEY
   ```

3. Run the server:

   ```bash
   python app.py
   ```

Submit a JSON payload to `/webhook` containing fields such as `First and last name`,
`Past experience`, and `job title/internship target`. The endpoint returns a PDF
with the rewritten content.
