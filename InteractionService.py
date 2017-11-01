from bottle import route, run
import requests


@route('/listInteractions/<rxcui>')
def listInteractions(rxcui):
    url = 'https://rxnav.nlm.nih.gov/REST/interaction/interaction.json?rxcui=153165'
    resp = requests.get(url)
    data = resp.json()
    interactions = []
    for itg in data['interactionTypeGroup']:
        for it in itg['interactionType']:
            for ip in it['interactionPair']:
                for ic in ip["interactionConcept"]:
                    mci = ic['minConceptItem']
                    if mci['tty'] == 'PIN':
                        interactions.append(mci['name'])
    return {"interactions": interactions}

run(host='localhost', port=8080, debug=True, reloader=True)