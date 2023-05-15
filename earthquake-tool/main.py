import urllib.request
import urllib.parse
import json
import re

from bs4 import BeautifulSoup

MASTODON_URL = "https://unnerv.jp"
MASTODON_API_PREFIX = f"{MASTODON_URL}/api/v1/"
MASTODON_NERV_ACCOUNT = { "id": "2", "username": "EEW" } # @EEW@unnerv.jp

def fetch() -> list[dict]:

    query = { "tagged": "#神奈川県" }
    query_string = urllib.parse.urlencode(query).encode("utf-8"),

    url = f"{MASTODON_API_PREFIX}/accounts/{MASTODON_NERV_ACCOUNT['id']}/statuses?{query_string}"
    req = urllib.request.Request(
        url, method="GET",
    )

    result = ""
    with urllib.request.urlopen(req) as res:
        result = res.read().decode("utf-8")

    return json.loads(result)


def filter(data: list[dict], location: str = "") -> list[tuple]:

    filtered_data = []
    for d in data:
        if location == "":
            filtered_data.append(gen_content_and_link_by_responsed_data(d))
        elif check_contain_tag(d, location):
            filtered_data.append(gen_content_and_link_by_responsed_data(d))

    return filtered_data


def gen_content_and_link_by_responsed_data(data: dict) -> tuple[str, str]:

    content = data["reblog"]["content"]
    link = f"{MASTODON_URL}/@{MASTODON_NERV_ACCOUNT['username']}/{data['id']}"

    return content, link


def gen_eathquake_info_by_content(content: str) -> dict:
    """
    sample: content = '<p>【緊急地震速報 第6報 2023年5月11日】<br '
                      '/>12時11分頃、トカラ列島近海を震源とする地震がありました。地震の規模はM5.6程度、最大震度4程度と推定されています。この情報は気象庁の予報に基づく推定です。情報は誤差を含む場合があります。<br '
                      '/><a '
                      'href="https://unnerv.jp/tags/%E9%B9%BF%E5%85%90%E5%B3%B6%E7%9C%8C" '
                      'class="mention hashtag" '
                      'rel="tag">#<span>鹿児島県</span></a>（奄美地方除く） <a '
                      'href="https://unnerv.jp/tags/%E7%B7%8A%E6%80%A5%E5%9C%B0%E9%9C%87%E9%80%9F%E5%A0%B1" '
                      'class="mention hashtag" '
                      'rel="tag">#<span>緊急地震速報</span></a></p>',
    """

    soup = BeautifulSoup(content, "html.parser")
    content_text = soup.p.text
    print(content_text)

    m = re.search(r"M([0-9.]+).*震度([0-9]+)", content_text)
    result = {
        "マグニチュード": float(m.group(1)),
        "震度": int(m.group(2))
    }

    return result
    

def check_contain_tag(status: dict, tag: str) -> bool:

    tags = status["reblog"]["tags"]
    for t in tags:
        if t["name"] == tag:
            return True

    return False

def main():

    responsed_data = fetch()

    import pprint
    #  pprint.pprint(responsed_data)
    pprint.pprint(filter(responsed_data, ""))

    #  content = '<p>【緊急地震速報 第6報 2023年5月11日】<br ' \
              #  '/>12時11分頃、トカラ列島近海を震源とする地震がありました。地震の規模はM5.6程度、最大震度4程度と推定されています。この情報は気象庁の予報に基づく推定です。情報は誤差を含む場合があります。<br ' \
              #  '/><a ' \
              #  'href="https://unnerv.jp/tags/%E9%B9%BF%E5%85%90%E5%B3%B6%E7%9C%8C" '  \
#  'class="mention hashtag" ' \
              #  'rel="tag">#<span>鹿児島県</span></a>（奄美地方除く） <a ' \
              #  'href="https://unnerv.jp/tags/%E7%B7%8A%E6%80%A5%E5%9C%B0%E9%9C%87%E9%80%9F%E5%A0%B1" ' \
              #  'class="mention hashtag" ' \
              #  'rel="tag">#<span>緊急地震速報</span></a></p>'

    #  print(content)
    #  print(gen_eathquake_info_by_content(content))

    # print(json.dumps(responsed_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
