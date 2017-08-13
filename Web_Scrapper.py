
import bs4
from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq



my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards"



#opening the connection
uClient = uReq(my_url)


#put into a variable
page_html = uClient.read()



#close the connection
uClient.close()



#html_parsing
page_soup = soup(page_html, "html.parser")



#Print the header 
print page_soup.h1



print page_soup.p



containers = page_soup.find_all("div", {"class": "item-container"})


filename = "product.csv"
f = open(filename , 'w')



f.write("brand, name , shipping\n")



for container in containers:
    
   if len(container.div.find_all("div", {"class": "item-branding"}))> 0:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"}) 
    product_name =  title_container[0].text 
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    print("\n")
    print("brand :" + brand)
    print("product_name :" + product_name)
    print("shipping :" + shipping)
    
        #f.write(brand + "," + product_name.replace(",","|") +"," + shipping +"\n")
#==============================================================================
#     try:                                      
#     
#     except IOError:
#         print('An error occured trying to read the file.')
#     
#     except ValueError:
#         print('Non-numeric data found in the file.')
# 
#     except ImportError:
#         print "NO module found"
#     
#     except EOFError:
#         print('Why did you do an EOF on me?')
# 
#     except KeyboardInterrupt:
#         print('You cancelled the operation.')
# 
#     except:
#         print('An error occured.')   
#         brand = ""
#         product_name = container.div.a.text
#         shipping = " "
#==============================================================================
    
    f.write(brand + "," + product_name.replace(",","|") +"," + shipping +"\n")                                


f.close()


print ("Excel Generated Successfully")







