
import argparse
import json

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
KEY_FILE_LOCATION = '../client_secrets.json'


def initialize():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
        An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    webmasters = build('webmasters', 'v3', credentials=credentials)

    return webmasters


def get(webmasters, start, end, limit):
    return webmasters.searchanalytics().query(
        siteUrl='https://memo.laughk.org/',
        body={
            'startDate': '2019-12-01',
            'endDate': '2019-12-14',
            'dimensions': ['query'],
            'rowLimit': limit,
        },
    ).execute()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', default='2019-12-07')
    parser.add_argument('-e', '--end', default='2019-12-14')
    parser.add_argument('-l', '--limit', default=10)
    args = parser.parse_args()

    wb = initialize()
    rows = get(wb, args.start, args.end, args.limit)['rows']
    # print(json.dumps(rows, indent=2))

    print(f'# 検索キーワード上位10 (期間: {args.start} - {args.end})')
    print('')
    for row in rows:
        print(f'word: {row["keys"]} (click: {row["clicks"]})')


if __name__ == '__main__':
    main()
