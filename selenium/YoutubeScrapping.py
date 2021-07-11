{
 "metadata": {
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
   "version": "3.7.4"
  },
  "orig_nbformat": 4,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.4 64-bit"
  },
  "interpreter": {
   "hash": "4cd7ab41f5fca4b9b44701077e38c5ffd31fe66a6cab21e0214b68d958d0e462"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Driver [/Users/sweicharles/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver] found in cache\n",
      "                                                title       views       posted\n",
      "0                       1. Introduction to Algorithms    2M views  3 years ago\n",
      "1   5.1 Graph Traversals - BFS & DFS -Breadth Firs...  1.5M views  3 years ago\n",
      "2   3.6 Dijkstra Algorithm - Single Source Shortes...  1.5M views  3 years ago\n",
      "3                           2.8.1 QuickSort Algorithm  1.5M views  3 years ago\n",
      "4   3.5 Prims and Kruskals Algorithms - Greedy Method  1.2M views  3 years ago\n",
      "5   4.5 0/1 Knapsack - Two Methods - Dynamic Progr...    1M views  3 years ago\n",
      "6                3.1 Knapsack Problem - Greedy Method    1M views  3 years ago\n",
      "7   4.2 All Pairs Shortest Path (Floyd-Warshall) -...  981K views  3 years ago\n",
      "8                            1.5.1 Time Complexity #1  897K views  3 years ago\n",
      "9   2.6.3 Heap - Heap Sort - Heapify - Priority Qu...  820K views  2 years ago\n",
      "10                        2.7.2. Merge Sort Algorithm  758K views  3 years ago\n",
      "11  4.4 Bellman Ford Algorithm - Single Source Sho...  756K views  3 years ago\n",
      "12                8. NP-Hard and NP-Complete Problems  752K views  3 years ago\n",
      "13  1.8.1 Asymptotic Notations Big Oh - Omega - Th...  746K views  3 years ago\n",
      "14            6.1 N Queens Problem using Backtracking  740K views  3 years ago\n",
      "15    2.1.1 Recurrence Relation (T(n)= T(n-1) + 1) #1  700K views  3 years ago\n",
      "16  7.3 Traveling Salesman Problem - Branch and Bound  686K views  3 years ago\n",
      "17  4.3 Matrix Chain Multiplication - Dynamic Prog...  682K views  3 years ago\n",
      "18                 3.4 Huffman Coding - Greedy Method  673K views  3 years ago\n",
      "19  4.7 Traveling Salesperson Problem - Dynamic Pr...  664K views  3 years ago\n",
      "20                    3. Greedy Method - Introduction  654K views  3 years ago\n",
      "21  10.2 B Trees and B+ Trees. How they are useful...  613K views  3 years ago\n",
      "22  9.1 Knuth-Morris-Pratt KMP String Matching Alg...  593K views  3 years ago\n",
      "23  3.2 Job Sequencing with Deadlines - Greedy Method  560K views  3 years ago\n",
      "24                   1.5.2 Time Complexity Example #2  552K views  3 years ago\n",
      "25          6.2 Sum Of Subsets Problem - Backtracking  532K views  3 years ago\n",
      "26  6 Introduction to Backtracking - Brute Force A...  512K views  3 years ago\n",
      "27            10.1 AVL Tree - Insertion and Rotations  511K views  3 years ago\n",
      "28  4 Principle of Optimality - Dynamic Programmin...  497K views  3 years ago\n",
      "29  2.4.1 Masters Theorem in Algorithms for Dividi...  469K views  3 years ago\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver \n",
    "import pandas as pd\n",
    "\n",
    "# Get a url from a Youtube channel host\n",
    "# go to video in the profile and sort by popular\n",
    "url = \"https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw/videos?view=0&sort=p&flow=grid\"\n",
    "\n",
    "# Assign driver\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install())\n",
    "driver.get(url)\n",
    "\n",
    "# Get all videos by classname by Finding the best charaters of the video\n",
    "# class=\"style-scope yt-horizontal-list-renderer\"\n",
    "# title path -> //*[@id=\"video-title\"]\n",
    "# views -> //*[@id=\"metadata-line\"]/span[1]\n",
    "# dates -> //*[@id=\"metadata-line\"]/span[2]\n",
    "\n",
    "videos = driver.find_elements_by_css_selector(\"#items > ytd-grid-video-renderer\")\n",
    "\n",
    "\n",
    "# Create an empty list \n",
    "video_list = []\n",
    "\n",
    "# extract informaiton from videos\n",
    "for video in videos:\n",
    "    # put a . in front of the xpath so that we can search everythong inside of the element\n",
    "    # Then use .text to get the text instead of object\n",
    "    title = video.find_element_by_xpath('.//*[@id=\"video-title\"]').text\n",
    "    views = video.find_element_by_xpath('.//*[@id=\"metadata-line\"]/span[1]').text\n",
    "    posted = video.find_element_by_xpath('.//*[@id=\"metadata-line\"]/span[2]').text\n",
    "    \n",
    "    # print(\"Title: {0}\\nViews: {1}\\nDate:{2}\\n\".format(title, view, date))\n",
    "\n",
    "    # Make use of information and make it as a dictionary\n",
    "    vid_item = {\n",
    "        'title': title,\n",
    "        'views': views,\n",
    "        'posted': posted\n",
    "    }\n",
    "\n",
    "    # Add the dictionary of the video item in a list\n",
    "    video_list.append(vid_item)\n",
    "\n",
    "# Convert the list into a pandas dataframe\n",
    "df = pd.DataFrame(video_list)\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}