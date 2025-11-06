from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def extract_page(url:str)->dict:
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response=requests.get(url,headers=header,timeout=15)
    response.raise_for_status()
    soup=BeautifulSoup(response.text,"html.parser")

    ## EXTRACTING THE TITLE OF THE PAGE
    title=soup.title.string.strip() if soup.title else urlparse(url).netloc
    #---> net loc--> www.google.com part of an url

    '''
    --------------------------------------------------------------------------
    '''
    ## EXTRACTING THE MAIN TEXT OF THAT PAGE
    paragraphs=[
        p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip())>0
    ]
    cleaned_text="\n\n".join(paragraphs)

    '''
       --------------------------------------------------------------------------
    '''

    ## EXTRACTING THE META DATA FROM THE WEBPAGE
    meta_desc=soup.find("meta",attrs={"name":"description"})
    meta_desc=meta_desc["content"].strip() if meta_desc and meta_desc.get("content")else ""


    '''
       --------------------------------------------------------------------------
    '''

    ## RETURNING THE FULL DATA THAT WE HAVE SCRAPPED
    return{
        "url":url,
        "title":title,
        "description":meta_desc,
        "word_count": len(cleaned_text.split()),     # Word count of extracted text
        "cleaned_text": cleaned_text[:5000]
    } ## we are returning a dictionary



'''
       --------------------------------------------------------------------------
'''
## THIS PART IS ONLY FOR THE LOCAL TESTING PURPOSE
if __name__=="__main__":
    url=""
    test = extract_page(url)
    print(test["title"])
    print(test["description"])
    print(test["cleaned_text"][:400])

