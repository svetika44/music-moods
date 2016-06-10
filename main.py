#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

from random import randint

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# DEVELOPER_KEY = "AIzaSyBAkQ7GRItzCNbFcU9FkID4_hpsU7LhsNM"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"



def choose_mood (mood): # choose_mood is a function
    # print 'Your mood is ' + mood
    # return 'Here is a song ' + mood_dictionary[mood][1]

    song_count = len(mood_dictionary[mood])

    random_song_number = randint(0, song_count-1)
    return mood_dictionary[mood][random_song_number]

mood_dictionary = {
    "happy" : [
        "Marriage of Figaro by Mozart",
        "Barber of Seville by Rossini",
        "Ruslan and Ludmilla (Overture) - Glinka",
        "Hoe Down - Copland",
        "'Largo al factotum' (from The Barber of Seville) - Rossini",
        "Jupiter the bringer of jollity (The Planets) - Holst",
        "Holberg Suite (Rigaudon) - Grieg"
    ],
    "sad" : [
        "Wolfgang Amadeus Mozart - Requiem Mass in D minor",
        "Samuel Barber - Adagio for Strings",
        "Tomaso Albinoni - Adagio in G minor",
        "Johann Sebastian Bach - Come, Sweet Death",
        "Edward Elgar - 2nd Movement, Serenade for Strings",
        "Henryk Gorecki - Symphony of Sorrowful Songs",
        "Henry Purcell - Dido's Lament",
        "Pyotr Ilyich Tchaikovsky - Symphony No. 6, 4th movement",
        "Giuseppe Verdi - V'ho ingannato"
    ],
    "pensive": [
        "Rachmaninoff's Piano Concerto No. 2",
        "Beethoven's Moonlight Sonata",
        "The Planets by Gustav Holst",
        "J.S. Bach's Cello Suite No. 1"
    ],
    "neutral" : [
        "Johann Pachelbel - Canon in D Major",
        "Fazil Say - Kara Toprak (Black Earth)",
        "Antonio Vivaldi  - Winter (from 'The Four Season')",
        "Johann Sebastian Bach - Suite No.3",
        "Ludovico Einaudi - Divenire",
        "Jon Schmidt - All Of Me",
        "Frederic Chopin - Nocturne in E-flat Major No.2",
        "Ludwig van Beethoven - Appassionata (Piano sonata in F Minor No.23)",
        "Johannes Brahms - Lullaby",
        "Pyotr Tchaikovsky - Concerto for Piano and Orchestra No.1 in B-flat Minor",
        "Claude Debussy - Moonlight",
        "Wolfgang Amadeus Mozart - Piano Concerto No.23, Adagio in F-sharp Minor",
        "Frederic Chopin - Fantaisie-Impromptu in C-sharp Minor Op.66",
        "Johann Strauss II - By the Beautiful Blue Danube",
        "Johann Strauss I - Radetzky March",
        "Handel - Sarabande"
    ]
}

class MainHandler(webapp2.RequestHandler):
  def get(self):

    # youtube = build(
    #     YOUTUBE_API_SERVICE_NAME,
    #     YOUTUBE_API_VERSION,
    #     developerKey=DEVELOPER_KEY)
    # search_response = youtube.search().list(
    #     q="Hello",
    #     part="id,snippet",
    #     maxResults=5
    # ).execute()
    #
    # videos = []
    # channels = []
    # playlists = []
    #
    # for search_result in search_response.get("items", []):
    #     if search_result["id"]["kind"] == "youtube#video":
    #         videos.append("%s (%s)" % (search_result["snippet"]["title"],
    #             search_result["id"]["videoId"]))
    #     elif search_result["id"]["kind"] == "youtube#channel":
    #         channels.append("%s (%s)" % (search_result["snippet"]["title"],
    #             search_result["id"]["channelId"]))
    #     elif search_result["id"]["kind"] == "youtube#playlist":
    #         playlists.append("%s (%s)" % (search_result["snippet"]["title"],
    #             search_result["id"]["playlistId"]))
    #
    # template_values = {
    #     'videos': videos,
    #     'channels': channels,
    #     'playlists': playlists
    # }
    #
    # print(template_values)
    self.response.write("hello")


class OurHandler(webapp2.RequestHandler): # we copied this handler from main one
  
  def get(self): # send get request 
    mood_template = my_env.get_template('templates/form.html')
    self.response.write(mood_template.render())

  def post(self):
    my_result=self.request.get("user_mood") # my_result var stores form value ( form.html)
    print (my_result)

    my_dic = {"song_choise":choose_mood(my_result)} # my dictionary choose_mood is a function
    music_template = my_env.get_template('templates/results.html')
    self.response.write(music_template.render(my_dic))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/asdf', OurHandler)
], debug=True)
