import argparse
import os

from modules.fetch import search_mail_by_query
from modules.notice import post_by_incoming_webhook


WEBHOOK_ENDPOINT = os.environ.get('WEBHOOK')


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query')

    args = parser.parse_args()
    if not args.query:
        return

    mails = search_mail_by_query(args.query)
    for mail in mails:
        print(mail)
        post_by_incoming_webhook(
            mail.base_of_json_for_slack(), WEBHOOK_ENDPOINT,
        )


if __name__ == '__main__':
    main()
