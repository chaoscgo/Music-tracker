i# READING LIST

![Music Tracker landing page-1](https://github.com/user-attachments/assets/7f1fb6b5-6cbb-4c57-989c-d63691212470)


## Description of Project

The project was to build a Django/PostgreSQL application with full CRUD that manages or tracks things of personal interest to us.  Once completed, we were to present our application to the class.  This was the fourth project we completed in this course.

## Brief

The type of application to build was entirely up to us and we were encouraged to choose something of personal interest to us.  The following minimum requirements were to be met:

* The app must utilize Django templates to render templates to users.

* PostgreSQL must be used for the database management system.

* The app must use Django's built-in session-based authentication.

* The app must have at least one data entity in addition to the User model and at least one entity must have a relationship with the User model.  

* The app must have full CRUD functionality.

* Authorization must be implemented in the app.  Guests who are not signed in must not be able to create, update or delete data or access functionality allowing those actions.

* The app must be deployed online.

## Timeframe & Working Team

We worked in a group of three on this project.  We had one week to complete and present.

## Getting Started/Code Installation

The code for this project can be found in our public GitHub repository [here](https://github.com/chaoscgo/music-tracker.git).

# How to use Music Tracker

The Music Tracker is an app designed for people who love music.  It is a way to keep track of your favorite songs.

Anytime you hear a song that you really love, you can enter it into the Music Tracker for future reference.

You can sign up for a free account and start your song list by entering the name of the song, the genre of music, the date the song was published and the length of the song. Once on a song's detail page, you can also add artists associated with this song.

You are able to manage your songs by adding new songs, editing information about songs already in the list and deleting any songs you no longer wish to keep in your list.

## Deployment Link

https://reading-list-app-6bcea523d230.herokuapp.com/

## Planning Materials

We started planning this project on Trello.  We created the User Stories first and then sketched out the ERD for the data entities. We also sketched out wireframes of how we wanted certain pages to look.  Our planning materials can be accessed [here](https://trello.com/b/FIyQ3OaT/music-tracker).

We also created todos on Trello to keep us on track with this project.  Then we started coding!

## Build/Code Process

First we installed Django and the virtual environment (pipenv shell).  Then we started a new Django project within the virtual environment.  We then created and registered the main-app.

We started defining routes in the urls.py files as well as implementing both view functions and Django's class based views.  We used Django's DTL to set up our HTML templates and used template inheritance to extend the main HTML language from the base.html file.

We set up a static directory to hold our css files and all images.  

We set up our class method (Song) and created the musictracker database.  We configured Django to use PostgreSQL for our database maintenance.  We then migrated the model so the database could store data for the model.

We created a superuser account so that we could perform admin on the site and registered our Song model with the admin portal.

We then implemented CRUD functionality for our app using Class Based Views.

We created a one-to-many relationship between the songs and their artists and migrated the new model.

Lastly, we implemented authorization and authentication using Django's built-in functionality and added some CSS styling and images.

We used GitHub feature branches so that we could all work independently and still keep track of all updates and changes.

## Challenges

We found it initially challenging to work with GitHub's feature branches since it was something new for us.  Once we got the hang of it, it became easier.

## Wins

We were happy to be able to get the CRUD functionality working without too much error handling or backtracking.

We also played around with using a Back button and got that working well.

![Song List](https://github.com/user-attachments/assets/f0c0ace4-cd9e-43d8-ac96-784cbb0f5a08)


## Key Learnings/Takeaways

We have learned that using GitHub collaboration can be very efficient if you're familar with it and have plenty of communication.  Group projects can be challenging because everyone is on a different time schedule, but good communication can make it easier.

## Attributions

All of our images were taken from the pexels.com website and were free to use without attribution.

## Technologies used:

Django, PostgreSQL, Python, HTML, CSS, Markdown, GitHub.

## Future plans/improvements

* Add the actual audio so that users can play their songs from the app.
* Have artist links that would redirect to a page where they could purchase the album.
* Display lyrics for each song.
* The ability to have a community space where users can share notes on songs.
* The ability to have a community space where users can share notes on songs.
