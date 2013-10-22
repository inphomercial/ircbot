def rottentomatoes(query, apikey):
    """
    Searches urbandictionary.com for a definition to the query given
    @return response dictionary 
    """
    import requests
    import json

    # send the request and get the data
    r = requests.get('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=%s&q=%s&page_limits=1' % (apikey, query))
    data = json.loads(r.text)

    
    if data['movies']:
        response = {
        	'critics_score' : data['movies'][0]['ratings']['critics_score'],
    		'audience_score' : data['movies'][0]['ratings']['audience_score'],
    		'link' : data['movies'][0]['links']['alternate']
        }
    else:
        response = None

    return response
        

if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    print rottentomatoes(query, 'nbf4u2eczdtrc2dtcn4gkzj8')