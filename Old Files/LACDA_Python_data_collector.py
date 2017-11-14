"""Before use, pip-install requests library for Python.
Documentation: http://docs.python-requests.org/en/master/ """

import requests

# LOK Page access token, obtained from: https://developers.facebook.com/tools/explorer/
LOK_TOKEN = 'EAABlwgSoQBkBAJ3RU02zyvxEuuG6CdelTMEmTdzvZAGYkWnKFBgyonZAM6W5TRzASz6wIW009R0B1tz8CZCQHhiHqtWBigZC8ZCJG3sZAOPZAHcVtFnVrnFXZAuGSMB1F4YJP1UUOWXfng0SRxoRfwZCDuft1aLf6qXmFmfDVwQxIGwZDZD'
LOK_PAGE_ID = '1553363564876294'


def req_facebook(req):
    """Pass a request to Fb using GET. Return json as dict"""
    r_json = requests.get('https://graph.facebook.com/v2.10/'+req, {'access_token' : LOK_TOKEN})
    r = r_json.json()
    if ('error') in r.keys():
        print 'Likely need to get a new token from: https://developers.facebook.com/tools/explorer/'
        print r
    return r

def recursively_get_ids(r):
    """As long as there is still a 'next' in the response dict, keep (recursively)
    collecting ids (of videos, likers, etc.), parse all ids into a list"""
    id_list = [] #empty collector list
    
    while ('next' in r['paging'].keys()) == True:
    #see structure of JSON response to understand the boolean better
        for item in r['data']:
        #iterate through all users in the response
            item_id = item['id']
            id_list.append(item_id)
        r = requests.get(r['paging']['next']).json()
        #get the link to go to next 25 likers
        return id_list + recursively_get_ids(r)
    return id_list #break recursion if 'next' is not there anymore

def get_videos_list(page_id):
    """Get a list of all videos of a page"""
    req = page_id + '/videos'
    r = req_facebook(req)
    video_list = recursively_get_ids(r)
    print len(video_list)
    return video_list

def get_posts_list(page_id):
    """Get a list of all posts of a page"""
    req = page_id + '/posts'
    r = req_facebook(req)
    post_list = recursively_get_ids(r)
    return post_list
    
def get_video_insight(video_id,insight):
    """Get a specified insight from a specified video"""
    req = LOK_PAGE_ID +'_'+ video_id + '/insights/' + insight
    # manually parse a post id from video id
    r = req_facebook(req)
    data = r['data'] #see result's raw JSON for more details
    value = data[0]['values'] #same as above
    return value
    
print (get_video_insight('1926485160897464','post_video_complete_views_organic'))




