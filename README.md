# Gmail-PDF-downloader.

  Download specific PDFs from your Gmail inbox and sent messages. You will specify a keyword that each PDF file will contain in the document title.

# Gmail Invoice Downloader

  Gmail Invoice Downloader is a Python script that searches your Gmail sent messages for PDF and Word documents with "Invoice" in their filename, downloads   them, and saves them to a local folder.

## Prerequisites

Before you begin, ensure you have met the following requirements:

  * You have a Google account with Gmail enabled.
  * You have a basic understanding of Python programming.
  * You have Python 3.x installed on your machine. You can download it from [Python.org](https://www.python.org/downloads/).

## Setup and Installation

1. Clone this repository to your local machine:

  git clone https://github.com/Andy-Chase/Gmail-Invoice-Downloader.git

2. Change into the project directory:

  cd Gmail-Invoice-Downloader

3. Install the required Python packages:

  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

4. Visit the [Google Cloud Console](https://console.developers.google.com/).

5. Create a new project.

6. Enable the Gmail API:

  * Click on "Enable APIs and Services".
  * Search for "Gmail".
  * Select "Gmail API".
  * Click on "Enable".

7. Create credentials:

  * Go to "Credentials" in the APIs & Services section.
  * Click on "Create credentials".
  * Select "OAuth client ID".
  * Set the Application type to "Desktop app".
  * Enter a name for your OAuth client ID (e.g., "Gmail Invoice Downloader").
  * Click "Create" and download the `credentials.json` file.
  * Move the `credentials.json` file into the project directory.

## Adding Yourself as a Tester

  If you receive an error message that says the app has not completed the Google verification process, you can add yourself as a tester for the Gmail       Invoice Downloader by following these steps:

  1. Go to the [Google Cloud Console](https://console.developers.google.com/).

  2. Select your project from the project dropdown menu.

  3. Click on "OAuth consent screen" in the APIs & Services section.

  4. In the "Test users" section, click "Add Users".

  5. Enter your Google email address and click "Add".

  Now you should be able to authenticate and use the Gmail Invoice Downloader without encountering the error.

## Usage

To use Gmail Invoice Downloader, follow these steps:

1. Open the `gmail_invoice_downloader.py` script with a text editor.

2. Locate the following line:

   ```python
   if file_extension in ["pdf", "doc", "docx"] and "Keyword" in filename:
   
   Replace "Keyword" with the keyword you'd like to search for in the document filenames. Save the changes and close the text editor.

3. Open a terminal or command prompt.

4. Change to the project directory:

  cd path/to/Gmail-Invoice-Downloader

5. Run the script:

  python3 gmail_invoice_downloader.py

5. Follow the instructions in the terminal to authenticate the script with your Google account.

6. The script will search your sent messages for PDF and Word attachments with "Your-Keyword" in their filename and download them to a folder named "documents" in the project directory.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

