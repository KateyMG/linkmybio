#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml 

class enlaces():
    def __init__(self, name, enable, link, description):
        self.name = name
        self.enable= enable
        self.link = link
        self.description= description

app = Flask(__name__)


links =yaml.load(open('links.yaml')) 

#print(links)
socialMediaLinks = links.get("links")
#print(socialMediaLinks)
social = []
name = []

for data in range(len(socialMediaLinks)):
    name = socialMediaLinks[data].get(data).get("name")
    enable = socialMediaLinks[data].get(data).get("enable")
    link = socialMediaLinks[data].get(data).get("link")
    description = socialMediaLinks[data].get(data).get("description")

    enlacesobj = enlaces(name, enable, link, description)
    social.append(enlacesobj)
    


link_list = links.get("enable")
 
print (social[0].description)  

environment=os.getenv("ENVIRONMENT","development")

@app.route("/")
def api_students():
    return render_template("index.html", links=links, social = social)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)