from flask import Flask, url_for, render_template, request
from markupsafe import Markup

import json
import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

"""@app.route("/")
def render_main():
    return render_template('file1.html')"""
@app.route("/f4")
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
    return cases
    









@app.route("/f3")
def render_file3():
    deaths = get_deaths_day()
    return render_template('file3.html', deaths = deaths)

def get_deaths_day():
    with open('monkeypox.json') as monkeypox:
        mpoxdata = json.load(monkeypox)
    deaths = "["
    for m in mpoxdata:
        if m["Date"]["Month"] == 8:
            if m["Country"]["Full"] == "World":
                deaths= deaths + Markup ("{ x: " + str(m["Date"]["Day"]) + ", y: " +str(m["Data"]["Deaths"]["Total"]) + "},") #{x: 8, y: 10}
    deaths = deaths[:-1] + "]"
    return deaths
    





@app.route("/")
def render_file11():
      return render_template('file1.html')
  






@app.route("/f5")
def render_file5():
    fact = get_cases_mill(request.args["day"])
    casesm = get_casesm_day()
    return render_template('file5.html', day_options = casesm, coolFact = fact)
 






@app.route("/f2")
def render_file2():
    casesm = get_casesm_day()
    
    
    
    
    
    
    
    return render_template('file2.html', day_options = casesm)
    
def get_casesm_day():
    with open('monkeypox.json') as monkeypox1:
        mpoxdata1 = json.load(monkeypox1)
    casesm =""
    for m in mpoxdata1: 
        if m["Date"]["Month"] == 8:
            if m["Country"]["Full"] == "World":
                casesm += Markup("<option value=\"" + str(m["Date"]["Day"]) + "\">" + str(m["Date"]["Day"]) + "</option>")
    return casesm

def get_cases_mill(day):
    with open('monkeypox.json') as monkeypox2:
        mpoxdata2 = json.load(monkeypox2)
    fact = ""
    for m in mpoxdata2:
        if (m["Date"]["Month"]) == 8 and int(m["Date"]["Day"]) == int(day):
            if m["Country"]["Full"] == "World":
               fact = "On day " + day + " of august there were a total of " + str(m["Data"]["Cases"]["New"]) + " new cases in the world."
    return fact
























if __name__=="__main__":
    app.run(debug=True)
