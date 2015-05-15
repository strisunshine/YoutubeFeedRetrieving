import sys

# you must add the right directories to sys.path
# for the following three imports to work
import HTML
import gdata.youtube
import gdata.youtube.service


class YouTubeAPI:

    def __init__(self):
        # Nothing else to do here
        self.yt_service = gdata.youtube.service.YouTubeService()

    def getSearchFeed(self, search_terms):
        # Build the query object here as shown in the documentation
        return feed

    def printVideoFeed(self, feed):
        pass

    def printEntryDetails(self, entry):
        pass


class HTMLWriter:
    
    def __init__(self):
        # Nothing to do here
        pass

    def feed2html(self, feed):
        pass
        return html_string

    def sec2time(self, sec):
        pass
        return hms_string

    def formatViewCount(self, count):
        pass
        return comma_string

    def html2file(self, html, fname):
        pass


if __name__ == "__main__":
    # Do not change these statements, except the qString ='...' statement.
    ytAPI = YouTubeAPI()
    qString = 'riverdance'
    feed = ytAPI.getSearchFeed(qString)
    ytAPI.printVideoFeed(feed)
    
    htmlWriter = HTMLWriter()
    html = htmlWriter.feed2html(feed)
    htmlWriter.html2file(html, 'youtube_'+qString+'.html')
