import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def download_documents(service):
    def download_attachments(parts, msg_id):
        for part in parts:
            filename = part.get("filename")
            file_extension = filename.split(".")[-1].lower()

            # Replace "Keyword" with your desired keyword.
            if file_extension in ["pdf", "doc", "docx"] and "Keyword" in filename:
                attachment = service.users().messages().attachments().get(
                    userId='me', messageId=msg_id, id=part['body']['attachmentId']).execute()
                file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))

                with open(os.path.join("documents", filename), "wb") as file:
                    file.write(file_data)
                    print(f"Downloaded: {filename}")

            if "parts" in part:
                download_attachments(part["parts"], msg_id)

    query = 'has:attachment (filename:pdf OR filename:doc OR filename:docx) in:sent'
    results = service.users().messages().list(userId="me", q=query).execute()
    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
    else:
        print("Messages with PDF or Word attachments containing your keyword:")
        for message in messages:
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()

            if "parts" in msg["payload"]:
                download_attachments(msg["payload"]["parts"], message["id"])

def main():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    if not os.path.exists("documents"):
        os.makedirs("documents")

    download_documents(service)

if __name__ == '__main__':
    main()
