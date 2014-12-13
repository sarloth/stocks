import urllib2, urllib, json

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from yahoo.finance.quote where symbol='COF'"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&env=http%3A%2F%2Fdatatables.org%2Falltables.env" + "&format=json"
print yql_url
result = urllib2.urlopen(yql_url).read()
data=json.loads(result)

print data['query']['results']
