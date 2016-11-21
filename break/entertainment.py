import media
from goodreads import client
from book import Book
import fresh_tomato


toy_story = media.Movie("Toy Story",
                      "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                      "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                      "http://www.imdb.com/video/imdb/vi2052129305/?ref_=tt_ov_vi")
#toy_story.show_trailer()

key= "jmdxCcybEUGNNMkedliQ"
secret= "snzHwALSA0o8a3MpMlCitiqLDviKpwFNeHhb7fZc"
#url="https://www.goodreads.com/book/isbn?callback=myCallback&format=xml&isbn=0312377320&key=jmdxCcybEUGNNMkedliQ"
#"http://webservices.amazon.com/onca/xml?AWSAccessKeyId=AKIAI56JPQRP57W47VFA&AssociateTag=booksearch0b-21&IdType=ASIN&ItemId=B00004D2XZ&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2CItemIds%2COffers&Service=AWSECommerceService&Timestamp=2015-10-29T12%3A18%3A00.000Z&Signature=4UWuL67KTThAqpyN%2BUC9yz2XDhy2RLPqqfY597S7Qks%3D"
#"http://webservices.amazon.com/onca/xml? Service=AWSECommerceService&AWSAccessKeyId=" + api_key + "&AssociateTag=" + ass_id + "& Operation=ItemSearch&Keywords=Rocket&SearchIndex=Toys&Timestamp=[YYYY-MM-DDThh:mm:ssZ]&Signature=[Request Signature]"
#res = urllib2.urlopen(url)

#data = xmltodict.parse(res)

#res.close

#print(data)
b=[]

gc = client.GoodreadsClient(key, secret)
gc.authenticate(key,secret)
for i in range (1020,1020):
    book = gc.book(i)
    #print(book.title+" by:"+book.authors[0].name+" ")
    #print("DEscription"+book.description)
    au=str(book.authors[0].name);
    #author=gc.find_author(au)
    #print(author.gid+" ")
    #print(book.image_url)
    if(book.small_image_url!=""):
        im=book.small_image_url
    else:
        im=book.mage_url
        
    bo=Book(book.title,book.description,au,im)
    if bo.title!="":
        b.append(bo)
#fresh_tomato.open_books_page(b)
#print (Book.VALID_RATINGS)
print (Book.__doc__)
print (Book.__name__)
print (Book.__module__)