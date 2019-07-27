# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:10:47 2019

@author: arnou
"""

from flask import Flask, render_template, request
app = Flask(__name__)

posts = [
            {
                'author':'Corey Arnouts',
                'title': 'Blog Post 1',
                'content':'First post content',
                'date_posted':'April 7, 2019'
                
                
                },
                                {
                'author':'Jane Doe',
                'title': 'Blog Post 2',
                'content':'Second post content',
                'date_posted':'April 21, 2019'
                
                
                }
        ]





@app.route('/') #this is known as a decorator 
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

## Youtube Python Flask Tutorial 
  
@app.route('/about') #this is known as a decorator 
def about():
    return render_template('about.html', title ='About')

@app.route('/main') #this is known as a decorator 
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)