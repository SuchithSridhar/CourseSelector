import requests
import bs4
import json
from pprint import PrettyPrinter
pprint = PrettyPrinter().pprint

URL = "https://www.unb.ca/academics/calendar/undergraduate/current/frederictoncourses/computer-science/index.html"

HEAD_CONTENTS = ["Course Number", "Course Title", "Course Credits"] 
BODY_CONTENTS = ["Course Description", "Pre-requisites", "Co-requisites"]

def getData(url):
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.content, 'html.parser')
    soup = soup.findAll("table", "ugradcal")
    return soup; 
def stringParser(string):
    '''
    bracketItems = []
    count = 0
    while "(" in string:
        firstBracket = string.find("(")
        secondBracket = string.find(")")
        bracketItems.append(string[firstBracket+1:secondBracket])
        string = string[:firstBracket] + " #prt" + str( count ) +" " + string[secondBracket+1:]
        string = string.lstrip()
        count += 1

    string = string.split(" and ")
    temp = []
    for i in string:
        if "," in i:
            temp.extend(i.split(","))

    string = []
    for i in temp:
        if " or " in i:
            string.append(["##or##"] + i.split(" or "))
        else:
            string.append(i)

    '''
    return string



reqs = []

def generateJson(tables):
    data = {}
    prereq = ""
    coreq = ""
    for table in tables:
        headings = table.findAll("th")
        for i, head in enumerate(headings):
            data[HEAD_CONTENTS[i]] = head.string

        # data[BODY_CONTENTS[0]] = table.findAll("course_description")[0].get_text()
        prereq = table.findAll("course_prereq")[0].get_text()
        coreq = table.findAll("course_coreq")[0].get_text()

        prereq = prereq.replace("\xa0", " ")[prereq.find(":")+1:].strip().rstrip(".").replace("  "," ")
        coreq = coreq.replace("\xa0", " ")[coreq.find(":")+1:].strip().rstrip(".").replace("  "," ")

        reqs.append(prereq)
        reqs.append(coreq)

        data[BODY_CONTENTS[1]] = stringParser(prereq)
        data[BODY_CONTENTS[2]] = stringParser(coreq)



generateJson(getData(URL))
with open ("data.json", 'w') as f:
    json.dump(reqs, f)

