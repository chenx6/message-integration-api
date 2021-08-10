from re import compile
from random import randint
from datetime import datetime

from requests import Session
from bs4 import BeautifulSoup

from schemas.item import Item

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}
SOGOU_URL = "https://weixin.sogou.com/"
SEARCH_PATH = "weixin?type=1&query="
var_re = compile(r'var[ ]+(\w+)[ ]?=[ ]?"(.+)"')
json_re = compile(r'"(.+)"[ ]+: "(.+)"')
approve_re = compile(r"src = ('.+')")
real_url_re = compile(r"url \+= '(.+)';")
grab_time_re = compile(r"document.write\(timeConvert\('(\d+)'\)\)")


def calc_href(href: str) -> str:
    """
    计算 href 链接
    """
    b = randint(0, 100) + 1
    a = href.index("url=")
    # c = href.index("&k=")
    if a != -1:
        sub_begin = a + 4 + 21 + b
        h = href[sub_begin : sub_begin + 1]
        href += f"&k={b}&h={h}"
    return href


def concat_approve(splited: str) -> str:
    """
    将 approve 链接提取并合并
    """
    return "".join(filter(lambda x: len(x) != 0 and x != " + ", splited.split("'")))


def parse_sogou(session: Session, url: str):
    """
    处理搜狗搜索页面，获取跳转链接
    """
    response = session.get(url)
    content = response.text
    # 解析出页面变量和 JSON
    var_dic = dict(var_re.findall(content))
    json_dic = dict(json_re.findall(content))
    # 发起 approve 请求
    session.get(
        f"{SOGOU_URL}/approve",
        params={
            "uuid": var_dic["uuid"],
            "token": var_dic["ssToken"],
            "from": "outer",
            "channel": json_dic["channel"],
        },
    )
    # 选择并计算跳转链接
    soup = BeautifulSoup(content, features="html.parser")
    selected = soup.select_one("a[uigs=account_article_0]")
    publish_time_s = selected.next_sibling.script.string  # type: ignore
    publish_time = grab_time_re.findall(publish_time_s)[0]
    href: str = selected["href"]  # type: ignore
    print(f"[*] Origin href: {href}")
    href = calc_href(href)
    print(f"[+] Calculated href: {href}")
    return f"{SOGOU_URL}{href}", selected.text, int(publish_time)  # type: ignore


def parse_jump_page(session: Session, jump_url: str) -> str:
    """
    获取并解析跳转数据
    """
    jump_response = session.get(jump_url)
    jump_content = jump_response.text
    # 获取并拼接 approve 链接
    approve_url = approve_re.findall(jump_content)[0]
    approve_url = concat_approve(approve_url)
    print(f"[+] Approve url: {approve_url}")
    session.get(approve_url)
    # 拼接文章 URL
    urls = real_url_re.findall(jump_content)
    url = "".join(urls).replace("@", "")
    print(f"[+] Article url: {url}")
    return url


def parse_page(session: Session, article_url: str):
    """
    处理文章页面
    """
    article_response = session.get(article_url)
    article_text = article_response.text
    soup = BeautifulSoup(article_text, features="html.parser")
    paras = soup.select("#js_content > p")
    return "\n".join(i.text for i in paras)  # type: ignore


def parse_weixin(public_name: str):
    search_url = SOGOU_URL + SEARCH_PATH + public_name
    session = Session()
    session.headers.update(HEADER)
    jump_url, _, _ = parse_sogou(session, search_url)
    real_url = parse_jump_page(session, jump_url)
    text = parse_page(session, real_url)
    return text


def weixin_public(public_name: str, zone_id: int):
    """
    获取微信公众号发文
    """
    search_url = SOGOU_URL + SEARCH_PATH + public_name
    session = Session()
    session.headers.update(HEADER)
    jump_url, article_title, publish_time = parse_sogou(session, search_url)
    real_url = parse_jump_page(session, jump_url)
    return Item(
        title=article_title,
        message="",
        update_time=datetime.fromtimestamp(publish_time),
        fetch_time=datetime.now(),
        url=real_url,
        zone_id=zone_id,
    )
