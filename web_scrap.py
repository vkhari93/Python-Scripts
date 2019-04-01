from bs4 import BeautifulSoup as bs
import urllib3
import urllib.request

# Google image search terms
query = ['BarrackObama', 'AlbertEinstein']
for item in query:
    link = "https://www.google.com/search?tbm=isch&source=hp&biw=1366&bih=654&ei=eg1LXLeAH8mEvQS43pMw&q=" + item + \
           "+&gs_l=img.3.0.0l10.2992.4338..5691...0.0..0.183.1130.0j7......0....1..gws-wiz-img.....0.ui7-obDA6L4"
    http = urllib3.PoolManager()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    webpage = http.request('GET', link)
    soup = bs(webpage.data.decode('utf-8'), features="html.parser")
    links = soup.findAll('img')
    for link in links:
        # save source links in a text document
        with open("src.txt", "a+") as src_file:
            src_file.write(str(link['src'])+"\n")
        # save jpg image
        urllib.request.urlretrieve(link['src'], "image_"+item+"_"+str(links.index(link))+".jpg")
