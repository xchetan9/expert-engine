import requests
from bs4 import BeautifulSoup
import json

def animekayo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    post_content = soup.find("div", class_="post-body entry-content")
    return post_content



def tmdbSearch(x):
    try:
        reqUrl = "https://api.themoviedb.org/3/search/tv?api_key=b93049a713559ad90b95537da68308fe&query="+x
        headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

        payload = ""

        response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
        response= response.json()
        return response
    except Exception as e:
        return f"Sorry Something is Wrong !!! {e}"
    

def MAL(p,quality,language,credit):
    reqUrl = f"https://api.jikan.moe/v4/anime/{p}/full"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList).json()
    main = ''''''

    titlesYs = ''''''
    for i in response['data']['titles'] :
        x = f'''<p><b>{i['type']} : </b>{i['title']}</p><br />'''
        titlesYs = titlesYs + x

    genress = ''''''
    for i in response['data']['genres'] :
        x = f'''<a href='/category/{i['name']}'>{i['name']} </a>'''
        genress = genress + x

    xyx = response['data']
    titlesection = f'''<h2><b>Title : </b>{xyx['title']}</h2><h2><b>English Title : </b>{xyx['title_english']}</h2>'''
    info = f'''
    <h3 class='infoH3'>Series Info</h3>
    <ul class='infoul'>
        <li><b>Type : </b>{xyx['type']}</li>
        <li><b>Source : </b>{xyx['source']}</li>
        <li><b>Status : </b>{xyx['status']}</li>
        <li><b>Episodes : </b>{xyx['episodes']}</li>
        <li><b>RunTime : </b>{xyx['duration']}</li>
        <li><b>Rating : </b>{xyx['rating']}</li>
        <li><b>Original Year : </b>{xyx['year']}</li>
        <li><b>Stars : </b>{xyx['score']}</li>
        <li><b>Quality : </b>{quality}</li>
        <li><b>Language : {language}</b></li>
        <li><b>Genres : </b> {genress}</li>
        <li><b>Encoder : </b> HindiToons</li>
        <li><b>Credits : {credit}</b></li>
    </ul>'''

    backg = f'''<h3>Background : </h3><p>{xyx['background']}</p>'''
    symp = f'''<h3>Plot : {xyx['title_english']}</h3><p>{xyx['synopsis']}</p>'''
    image1 = f'''{xyx['images']['webp']['large_image_url']}'''
    image2 = f'''<img src='{xyx['trailer']['images']['image_url']}' alt='image' loading='lazy'></img>'''
    trailerYT = f'''<iframe src='{xyx['trailer']['embed_url']}' title='{xyx['title_english']}' frameborder='0'></iframe>'''

    tags = f'''<p class='httags'> {xyx['title_english']} {language} | {xyx['title_english']} {language} Free Download | {xyx['title_english']} Download HD | {xyx['title_english']} HindiToons.in | {xyx['title_english']} {language} Free Download | {xyx['title_english']} {quality} | {xyx['title_english']} {language} {quality} | {xyx['title_english']} {language} Direct Links | {xyx['title_english']} {language} Episodes | {xyx['title_english']} {language} Episodes free Download</p>'''

    dwnsec = f'''<h2 class='htdl'>{xyx['title_english']} Download {language}</h2>'''

    main = image1 + tags + backg +titlesection + genress + info + symp + dwnsec 
    return main