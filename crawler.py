import requests
import sys
from urllib.parse import urlparse
import re
from page import Page

all_links = []


def get_list_of_links_for_domain(url, domain, proto, content, level, depth):
    links = []
    parsed_url = urlparse(url)
    for line in content.splitlines():
        get_links_from_content_line(line, "href", links, parsed_url, domain, proto, level, depth)
        get_links_from_content_line(line, "src", links, parsed_url, domain, proto, level, depth)
    return links


def get_links_from_content_line(line, type, links, parsed_url, domain, proto, level, depth):
    for part in re.split(type, line):
        if part.startswith("=\"") and len(part.replace("=", "").split("\"")) > 0:
            link = part.replace("=", "").split("\"")[1]
            # if Page.is_absolute(link) and domain in link or not Page.is_absolute(link):
            page = Page(link, type, parsed_url.netloc, proto, level)
            if page not in all_links:
                links.append(page)
                all_links.append(page)
                if level < depth and type == "href" and \
                        (Page.is_absolute(link) and domain in link or not Page.is_absolute(link)):
                    try:
                        print("GET " + page.absolute_url)
                        r = requests.get(page.absolute_url)
                        if r.status_code == 200 and "text/html" in r.headers['Content-Type'] \
                                and domain in page.absolute_url:
                            page.sublinks = get_list_of_links_for_domain(page.absolute_url,
                                                                         domain,
                                                                         proto,
                                                                         r.text,
                                                                         level + 1,
                                                                         depth)
                    except Exception as e:
                        print("ERROR " + str(e) + "while trying to GET " + page.absolute_url)


def parse_html_page(url, depth):
    try:
        print("GET " + url)
        r = requests.get(url)
        if r.status_code == 200:
            if "text/html" in r.headers['Content-Type']:
                return get_list_of_links_for_domain(url,
                                                    urlparse(url).netloc,
                                                    urlparse(url).scheme,
                                                    r.text,
                                                    0,
                                                    depth)
            else:
                return "Incorrect content type " + r.headers['Content-Type'] + " in response instead of text/html"
        else:
            return "Could not parse " + url + ", because of receiving HTTP status code " + str(r.status_code)
    except requests.exceptions.ConnectionError:
        return "Failed to establish a new connection with url " + url
    except requests.exceptions.MissingSchema:
        return "Invalid url " + url


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Please run program with 1 or 2 arguments using following command: \npython crawler.py URL DEPTH")
    else:
        depth = 3
        if len(sys.argv) == 3:
            depth = int(sys.argv[2])

        print("Starting to crawling on page " + sys.argv[1] + " with depth " + str(depth) + "\n")
        parsed_data = parse_html_page(sys.argv[1], depth)
        if type(parsed_data) is list:
            print("\nSimple structured site map for " + sys.argv[1] + ":\n")
            for page in parsed_data:
                print(page)
        else:
            print(parsed_data)
