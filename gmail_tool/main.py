import base64
import pickle
import os.path
import typing as t
from dataclasses import dataclass
from datetime import datetime

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


@dataclass
class GmailMessage:
    from_: str
    to: str
    date: datetime
    subject: str
    body: str
    snippet: str

    def detail(self):
        fmt = f'from: {self.from_}\n' \
              f'to: {self.to}\n' \
              f'date: {self.date}\n' \
              f'subject: {self.subject}\n' \
              f'body:\n{self.body}'
        return fmt


def get_creds():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def convert_dict_list_to_dict(
    src_dict_list: t.List[t.Dict],
) -> t.Dict:

    return {
        i['name']: i['value'] for i in src_dict_list
    }


def get_headers_by_message_detail(
    message_detail: list
) -> t.Dict:
    return convert_dict_list_to_dict(message_detail['payload']['headers'])


def get_mail_body_by_message_detail(
    message_detail_payload: t.Dict
) -> str:

    body_resource = message_detail_payload['body']
    if not body_resource.get('data'):
        return get_mail_body_by_message_detail(
            message_detail_payload['parts'][0],
        )
    else:
        body_data = body_resource['data']

    body_64decoded = base64.urlsafe_b64decode(body_data)
    return bytes(body_64decoded).decode()


def search_mail_by_query(query: str = '') -> t.List[GmailMessage]:

    creds = get_creds()
    service = build('gmail', 'v1', credentials=creds)
    results = []

    # Call the Gmail API
    message_id_dict = service.users()\
        .messages()\
        .list(userId='me', q=query)\
        .execute()

    count = 0
    for msg in message_id_dict['messages']:

        # Call the Gmail API
        message_detail = service.users()\
            .messages()\
            .get(userId='me', id=msg['id'])\
            .execute()

        headers = get_headers_by_message_detail(message_detail)

        results.append(
            GmailMessage(
                from_=headers['From'],
                to=headers['To'],
                date=datetime.strptime(
                    headers['Date'], '%a, %d %b %Y %H:%M:%S %z'
                ),
                subject=headers['Subject'],
                snippet=message_detail.get("snippet"),
                body=get_mail_body_by_message_detail(
                    message_detail['payload']
                ),
            )
        )

        if count > 1:
            break
        count += 1

    return results


def main():

    #mails = search_mail_by_query('(第100回)Python mini Hack-a-thon')
    #mails = search_mail_by_query('From: connpass')
    mails = search_mail_by_query('From: sebn_support@shoeisha.co.jp')

    for mail in mails:
        print('---------------------------')
        print(mail.detail())


if __name__ == '__main__':
    main()
