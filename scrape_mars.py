
# coding: utf-8

# In[30]:


#dependencies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time


# In[2]:


get_ipython().system('which chromedriver')


# In[3]:


#directory where chromedriver exists
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


#NASA Mars News
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[5]:


#scrape
html = browser.html
soup = bs(html,"html.parser")


# In[6]:


#latest news title and paragraph text
news_title = soup.find("div",class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text
print(news_title)
print(news_p)


# In[7]:


#JPL Mars url
url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_2)


# In[13]:


#locate image
featured_image_list = []

for image in soup.find_all('div',class_="img"):
    featured_image_list.append(image.find('img').get('src'))


# In[15]:


feature_image = featured_image_list[0]

feature_image_url = "https://www.jpl.nasa.gov/" + feature_image

feature_image_dict = {"image": feature_image_url}
 
#print feature image
print("Feature Image URL:", feature_image_url)


# In[46]:


#Latest Mars weather tweet
url_3 = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_3)


# In[17]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[47]:


#Mars facts
url_4 = "https://space-facts.com/mars/"
browser.visit(url_4)


# In[53]:


mars_facts_df = pd.read_html("https://space-facts.com/mars/")

mars_facts_df = mars_facts_df[0]

mars_facts_df.rename({0:"Parameters", 1:"Values"},axis=1, inplace=True)

mars_facts_df


# In[55]:


#convert table to HMTL
mars_facts_table_df = mars_facts_df.to_html("mars_facts_table_df.html",index=False)

mars_facts_dict_df = {"mars_facts_df": mars_facts_table_df}


# In[56]:


#Mars hemispheres 
url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_5)
html = browser.html
soup = bs(html, 'html.parser')


# In[36]:


hemis_title=[]

for img_title in soup.find_all('div',class_="description"):
    hemis_title.append(img_title.find('h3').text)


# In[38]:


hemis_image = []

for image in soup.find_all('div',class_="item"):
    
    url = "https://astrogeology.usgs.gov/"
    
    hemis_image.append(url + image.find('img').get('src'))
    
hemis_image


# In[41]:


full_image_url = []

for each_url in hemis_image:
    
    split_url = each_url.split(".tif_thumb.png")[0]
    
    image_url = split_url + ".tif/full.jpg"
    
    full_image_url.append(image_url)
    
full_image_url


# In[42]:


hemis_title


# In[57]:


hemis_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": full_image_url[3]},
    {"title": "Cerberus Hemisphere", "img_url": full_image_url[0]},
    {"title": "Schiaparelli Hemisphere", "img_url": full_image_url[1]},
    {"title": "Syrtis Major Hemisphere", "img_url": full_image_url[2]},
]

