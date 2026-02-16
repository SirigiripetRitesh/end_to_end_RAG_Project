from youtubesearchpython import VideosSearch
import pprint

def get_yt_video_link(query):
    Videos_search = VideosSearch(query=query, limit = 3)
    result = Videos_search.result()
    video_titles = [video["title"] for video in result['result']]
    video_link = [video["link"] for video in result['result']]
    return video_titles, video_link
    
    # return result


user_query = "what is Machine Learning"
title,link = get_yt_video_link(user_query)
print(title, link)
