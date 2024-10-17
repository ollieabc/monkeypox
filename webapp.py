from flask import Flask, url_for, render_template, request
from markupsafe import Markup

import json
import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

"""@app.route("/")
def render_main():
    return render_template('file1.html')"""
@app.route("/")
def render_file4():
    cases = get_cases_day()
    return render_template('file4.html', data = cases)

def get_cases_day():
    with open('monkeypox.json') as monkeypox:
        mpoxdata = json.load(monkeypox)
    cases = "["
    for m in mpoxdata:
        if m["Date"]["Month"] == 8:
            if m["Country"]["Full"] == "Spain":
                cases= cases + Markup ("{ x: " + str(m["Date"]["Day"]) + ", y: " +str(m["Data"]["Cases"]["Total"]) + "},") #{x: 8, y: 10}
    cases = cases[:-1] + "]"
    print(cases)
    return cases
    
@app.route("/")
def render_file3():
    deaths = get_deaths_day()
    return render_template('file3.html', data1 = deaths)

def get_deaths_day():
    with open('monkeypox.json') as monkeypox:
        mpoxdata = json.load(monkeypox)
    deaths = "["
    for m in mpoxdata:
        if m["Date"]["Month"] == 8:
            if m["Country"]["Full"] == "Spain":
                deaths= deaths + Markup ("{ x: " + str(m["Date"]["Day"]) + ", y: " +str(m["Deaths"]["New"]) + "},") #{x: 8, y: 10}
    deaths = deaths[:-1] + "]"
    print(deaths)
    return deaths
    
    
     
        
        
        
        
    
    



    
if __name__=="__main__":
    app.run(debug=True)
    

    
    