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
import webapp2
import os
import jinja2

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def choose_mood (mood): # choose_mood is a function 
    print 'Your mood is ' +mood  
    return 'Here is a song ' +mood_dictionary["happy"][1]

mood_dictionary={"happy":["joy by Vivaldi", "Marriage of Figaro by Mozart", "Barber of Seville by Rossini"], "sad":"grief by Mozart"}

class MainHandler(webapp2.RequestHandler):
  def get(self):
      self.response.write('Hello world!')
  

class OurHandler(webapp2.RequestHandler): # we copied this handler from main one
  
  def get(self):
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
