import sys
sys.path.append('C:\Python27\HTML.py-0.04')
sys.path.append('C:\Python27\gdata-2.0.18\src')

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
         yt_service = gdata.youtube.service.YouTubeService()
         query = gdata.youtube.service.YouTubeVideoQuery()
         query.vq = search_terms
         query.orderby = 'viewCount'
         query.racy = 'include'
         feed = yt_service.YouTubeQuery(query)
         return feed

    def printVideoFeed(self, feed):
        for entry in feed.entry:
          self.printEntryDetails(entry)

    def printEntryDetails(self, entry):
        print 'Video title: %s' % entry.media.title.text
        print 'Video published on: %s ' % entry.published.text
        print 'Video description: %s' % entry.media.description.text
        print 'Video category: %s' % entry.media.category[0].text
        print 'Video tags: %s' % entry.media.keywords.text
        print 'Video watch page: %s' % entry.media.player.url
        print 'Video flash player URL: %s' % entry.GetSwfUrl()
        print 'Video duration: %s' % entry.media.duration.seconds

        # non entry.media attributes

        print 'Video view count: %s' % entry.statistics.view_count
        print 'Video rating: %s' % entry.rating.average

        # show alternate formats
        for alternate_format in entry.media.content:
           if 'isDefault' not in alternate_format.extension_attributes:
              print 'Alternate format: %s | url: %s ' % (alternate_format.type, alternate_format.url)

        # show thumbnails
        for thumbnail in entry.media.thumbnail:
           print 'Thumbnail url: %s' % thumbnail.url


class HTMLWriter:
    
    def __init__(self):
        # Nothing to do here
        pass

    def feed2html(self, feed):
        table_data = []
        entrylist = []
        
        for entry in feed.entry:
           entrylist = [ HTML.link(entry.media.title.text,entry.media.player.url), entry.published.text[:10], entry.media.category[0].text, self.sec2time(entry.media.duration.seconds), self.formatViewCount(entry.statistics.view_count), '%.2f'%float(entry.rating.average)]
           table_data.append(entrylist)
        html_string = HTML.table(table_data, header_row=['Video title','Video published on','Video category','Video duration','Video view count','Video rating'])
        return html_string

    def sec2time(self, sec):
        m, s = divmod(int(sec),60)
        h, m = divmod(m, 60)
        if(h==0):
               hms_string = "%d:%02d" %(m,s)
        else:
               hms_string = "%d:%2d:%02d" %(h,m,s)
        return hms_string

    def formatViewCount(self, count):
        comma_string = format(int(count), ',d')
        return comma_string

    def html2file(self, html, fname):
        outFile = open( fname, 'w')
        outFile.write(html)
        outFile.close


if __name__ == "__main__":
    # Do not change these statements, except the qString ='...' statement.
    ytAPI = YouTubeAPI()
    qString = 'riverdance'
    feed = ytAPI.getSearchFeed(qString)
    ytAPI.printVideoFeed(feed)
    
    htmlWriter = HTMLWriter()
    html = htmlWriter.feed2html(feed)
    htmlWriter.html2file(html, 'youtube_'+qString+'.html')
