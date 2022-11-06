from bs4 import BeautifulSoup
import requests
# <editor-fold desc="local website">
# with open("website.html", encoding="utf8") as website:
#     content = website.read()
#
# soup = BeautifulSoup(content, parser='html.parser', features="lxml")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.a) #first a element
# # list = soup.find_all(name="a")
# # for tag in list:
# #     # print(tag.getText())#give text
# #     # tag.get("href") #give links
# #print(list)
#
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# </editor-fold>
# <editor-fold desc="news on ycombinator">
# response = requests.get("https://news.ycombinator.com/news")
# yc_webpage = response.text

# soup = BeautifulSoup(yc_webpage, "html.parser")
# articles = soup.find_all(name="a", class_="titlelink")

# article_text = ['How “latency numbers everybody should know” decreased from 1990–2020', 'Alex Honnold: The Soloist VR', 'Fire at Ukrainian nuclear plant outside perimeter', 'The Miseducation of Maria Montessori', 'Duck DNS – free dynamic DNS hosted on AWS', 'iPhone 11 Emulated on QEMU', 'Cybercriminals who breached Nvidia issue one of the most unusual demands ever', 'CSS-Checker: Find and Reduce Similar and Duplicated CSS Scripts', 'Meticulous (YC S21) Is Hiring #2 Founding Engineer in London', 'Chimpanzees observed applying and giving medicine', 'Treatment for Tinnitus with Stimulation of Auditory and Non-Auditory Nerves', 'DocBook 5.1: The Definitive Guide (2020)', 'How I See Numbers', 'Who Says C is Simple?', 'Harold Hering', 'How the weak can win – A primer on protracted war', 'USDA Pomological Watercolor Collection', 'Rules of Card Games: I Doubt It (1998)', 'New York Times tech workers vote to certify union', "Let's Build a Network Video Recorder in Python", 'Launch HN: Requestly (YC W22) – Network debugging proxy for web and mobile', 'Launch HN: Slai (YC W22) – Build ML models quickly and deploy them as apps', 'Elephant seals have a map sense', 'Better visibility into Linux packet-dropping decisions', 'CPython, C standards, and IEEE 754', 'New UCIe Chiplet Standard Supported by Intel, AMD, and Arm', "Speeding up Go's built-in JSON encoder for large arrays of objects", 'Protein tweak makes CRISPR gene editing 4k times less error-prone', 'Universal Chiplet Interconnect Express UCIe 1.0 Launched', 'Brave Talk: Unlimited, private video calls, in browser']
# article_links = ['https://colin-scott.github.io/personal_website/research/interactive_latency.html', 'https://thesoloist-vr.com/', 'https://www.reuters.com/markets/europe/top-wrap-1-europes-largest-nuclear-power-plant-fire-after-russian-attack-mayor-2022-03-04/', 'https://www.newyorker.com/books/under-review/the-miseducation-of-maria-montessori', 'https://www.duckdns.org/', 'https://github.com/TrungNguyen1909/qemu-t8030', 'https://arstechnica.com/information-technology/2022/03/cybercriminals-who-breached-nvidia-issue-one-of-the-most-unusual-demands-ever/', 'https://github.com/ruilisi/css-checker', 'item?id=30551541', 'https://www.sapiens.org/biology/chimpanzees-self-medication-wound/', 'https://www.frontiersin.org/articles/10.3389/fnins.2022.758575/full', 'https://tdg.docbook.org/tdg/5.1/', 'https://www.csun.io/2022/03/03/how-i-see-numbers.html', 'https://people.eecs.berkeley.edu/~necula/cil/cil016.html', 'https://en.wikipedia.org/wiki/Harold_Hering', 'https://acoup.blog/2022/03/03/collections-how-the-weak-can-win-a-primer-on-protracted-war/', 'https://naldc.nal.usda.gov/usda_pomological_watercolor?q=&search_field=all_fields', 'https://www.pagat.com/beating/doubt.html', 'https://www.nytimes.com/2022/03/03/business/media/new-york-times-tech-union.html', 'https://eternityforest.com/doku/doku.php?id=tech:nvr', 'item?id=30540735', 'item?id=30543228', 'https://www.cell.com/current-biology/fulltext/S0960-9822(22)00042-2', 'https://lwn.net/SubscriberLink/885729/c495a793abeee387/', 'https://lwn.net/SubscriberLink/886516/d835ee6026544345/', 'https://www.tomshardware.com/news/new-ucie-chiplet-standard-supported-by-intel-amd-and-arm', 'https://datastation.multiprocess.io/blog/2022-03-03-improving-go-json-encoding-performance-for-large-arrays-of-objects.html', 'https://newatlas.com/science/crispr-gene-editing-error-correction-protein/', 'https://www.servethehome.com/universal-chiplet-interconnect-express-ucie-1-0-launched/', 'https://brave.com/talk/']
# article_upvotes = ['494 points', '101 points', '762 points', '81 points', '26 points', '301 points', '141 points', '15 points', '100 points', '75 points', '37 points', '252 points', '11 points', '94 points', '208 points', '97 points', '77 points', '234 points', '33 points', '164 points', '117 points', '17 points', '122 points', '106 points', '31 points', '103 points', '18 points', '83 points', '175 points']
# # for article_tag in articles:
# #     article_text.append(article_tag.getText())
# #     article_links.append(article_tag.get("href"))
# #
# # article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# article_upvotes = [int(score.split()[0]) for score in article_upvotes]
# max_score_index = article_upvotes.index(max(article_upvotes))
# print(article_text[max_score_index])
# print(article_links[max_score_index])
# </editor-fold>
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(URL)
# webpage_html = response.text
with open("The 100 Greatest Movies _ Movies _ Empire.htm", encoding="utf8") as website:
    content = website.read()
soup = BeautifulSoup(content, parser="html.parser", features="lxml")
articles = [film.getText().split(") ")[1] for film in soup.find_all(name="h3", class_="jsx-4245974604")]
# articles.reverse()
year_list = [int(year.getText()) for year in soup.select("p strong") if year.getText() != "READ MORE:"]
# 27 74 in reverse trainspotting - no year
# 52 49 in reverse Point Break - no year
# 20 81 in reverse the matix - no year
# 3 98 in reverse the godfather- no year
year_list.insert(94, 1972)
year_list.insert(78, 1977)
year_list.insert(47, 1991)
year_list.insert(26, 1996)
# year_list.reverse()
# print(year_list)

with open("movies.txt", "w") as movies_file:
    for i in range(len(year_list)):
        if i < 9:
            count = f"00{i + 1}"
        elif 9 < i < 99:
            count = f"0{i + 1}"
        else:
            count = i + 1
        movies_file.write(f"{count}). {articles[i]}  ({year_list[i]})\n")
        