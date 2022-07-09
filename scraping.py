{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e18fb30c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "INFO:WDM:====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 102.0.5005\n",
      "INFO:WDM:Current google-chrome version is 102.0.5005\n",
      "[WDM] - Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "INFO:WDM:Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "[WDM] - Driver [C:\\Users\\David\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n",
      "INFO:WDM:Driver [C:\\Users\\David\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Import Splinter, BeautifulSoup, and Pandas\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9483082b",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Initiate headless driver for deployment\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    news_title, news_paragraph = mars_news(browser)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9c4d4ce6",
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with id \"full_image\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\pythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     39\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 40\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     41\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13792/4041481407.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m        \u001b[1;34m\"news_title\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnews_title\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m        \u001b[1;34m\"news_paragraph\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnews_paragraph\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m        \u001b[1;34m\"featured_image\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mfeatured_image\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m        \u001b[1;34m\"facts\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mmars_facts\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m        \u001b[1;34m\"last_modified\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mdt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13792/1159012569.py\u001b[0m in \u001b[0;36mfeatured_image\u001b[1;34m(browser)\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;31m# Find and click the full image button\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mfull_image_elem\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'full_image'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m     \u001b[0mfull_image_elem\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[1;31m# Find the more info button and click that\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\pythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     42\u001b[0m             raise ElementDoesNotExist(\n\u001b[0;32m     43\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[1;32m---> 44\u001b[1;33m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     45\u001b[0m                 )\n\u001b[0;32m     46\u001b[0m             )\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with id \"full_image\""
     ]
    }
   ],
   "source": [
    " # Run all scraping functions and store results in a dictionary\n",
    "data = {\n",
    "        \"news_title\": news_title,\n",
    "        \"news_paragraph\": news_paragraph,\n",
    "        \"featured_image\": featured_image(browser),\n",
    "        \"facts\": mars_facts(),\n",
    "        \"last_modified\": dt.datetime.now(),\n",
    "        \"hemisphere_data\": hemisphere_scrape(browser)\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8d0ba52",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Stop webdriver and return data\n",
    "    browser.quit()\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30fea5cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news(browser):\n",
    "    # Scrape Mars News\n",
    "    # Visit the mars nasa news site\n",
    "    url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)\n",
    "    # Optional delay for loading the page\n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)\n",
    "    # Convert the browser html to a soup object and then quit the browser\n",
    "    html = browser.html\n",
    "    news_soup = soup(html, 'html.parser')\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        slide_elem = news_soup.select_one(\"ul.item_list li.slide\")\n",
    "        # Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "        news_title = slide_elem.find(\"div\", class_=\"content_title\").get_text()\n",
    "        # Use the parent element to find the paragraph text\n",
    "        news_p = slide_elem.find(\"div\", class_=\"article_teaser_body\").get_text()\n",
    "    except AttributeError:\n",
    "        return None, None\n",
    "    return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "573b9141",
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    # Visit URL\n",
    "    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(url)\n",
    "    # Find and click the full image button\n",
    "    full_image_elem = browser.find_by_id('full_image')[0]\n",
    "    full_image_elem.click()\n",
    "    # Find the more info button and click that\n",
    "    browser.is_element_present_by_text('more info', wait_time=1)\n",
    "    more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "    more_info_elem.click()\n",
    "    # Parse the resulting html with soup\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Find the relative image url\n",
    "        img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "    except AttributeError:\n",
    "        return None\n",
    "    # Use the base url to create an absolute url\n",
    "    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "    return img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26f37210",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_facts():\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Use 'read_html' to scrape the facts table into a dataframe\n",
    "        df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "    except BaseException:\n",
    "        return None\n",
    "    # Assign columns and set index of dataframe\n",
    "    df.columns=['Description', 'Mars']\n",
    "    df.set_index('Description', inplace=True)\n",
    "    # Convert dataframe into HTML format, add bootstrap\n",
    "    return df.to_html(classes=\"table table-striped\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d146615",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hemisphere_scrape(browser) :\n",
    "    # 1. Use browser to visit the URL \n",
    "    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    browser.visit(url)\n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)\n",
    "    # 2. Create a list to hold the images and titles.\n",
    "    hemisphere_image_urls = []\n",
    "    # 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "    # Parse the html with beautifulsoup\n",
    "    html = browser.html\n",
    "    hemi_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Get the links for each of the 4 hemispheres\n",
    "    hemi_links = hemi_soup.find_all('h3')\n",
    "    # hemi_links\n",
    "\n",
    "    # loop through each hemisphere link\n",
    "    for hemi in hemi_links:\n",
    "        # Navigate and click the link of the hemisphere\n",
    "        img_page = browser.find_by_text(hemi.text)\n",
    "        img_page.click()\n",
    "        html= browser.html\n",
    "        img_soup = soup(html, 'html.parser')\n",
    "        # Scrape the image link\n",
    "        img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])\n",
    "        # Scrape the title\n",
    "        title = img_soup.find('h2', class_='title').text\n",
    "        # Define and append to the dictionary\n",
    "        hemisphere = {'img_url': img_url,'title': title}\n",
    "        hemisphere_image_urls.append(hemisphere)\n",
    "        browser.back()\n",
    "        # print(hemisphere_image_urls)\n",
    "    return hemisphere_image_urls\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d34d315c",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    # If running as script, print scraped data\n",
    "    print(scrape_all())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bf3137a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
