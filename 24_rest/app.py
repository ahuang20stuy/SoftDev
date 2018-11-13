'''
Addison Huang 
SoftDev1 pd6
K 

'''

from flask import Flask, render_template
import urllib, json

app=Flask(__name__)

@app.route("/")
def root():
    urlData = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    dic = json.loads(data.decode(encoding))
    print(dic)
    print (dic['url'])
    return render_template(pic = dic['url'], "index.html")
    
    
    
if __name__ == "__main__":
    app.debug = True
    app.run()


