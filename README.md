# Take a hike

Take a hike is a fully responsive full-stack website that I have built using the Django Full Stack framework for my Portfolio Project 4. I created this website to promote an adventure style of life and to give users the opportunity to explore local areas and mountains with us.
  
![Am i responsive image](readme_img/responsive/responsive.png)  

[Click Here To Visit Live Site](https://blog-hike.herokuapp.com/)  

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Post page](#post-page)
    * [Single post page](#single-post-page)
    * [Profile page](#profile-page)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)

3. [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Libraries](#libraries-used)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## Design & Planning:

### User Stories
#### First time visitor
- As a first-time visitor, I want to understand the purpose of the website and easily navigate through
- As a first-time visitor, I want to be able to view the posts so that I would get quick access to relevant information and get a better understanding of the content
- As a first-time visitor, I want to be able to see likes and comments for the posts to get some feedback from other users
- As a first-time visitor, I want to be able to register an account to have more access to the website
- As a first-time visitor, I want to be able to search posts by title name so I could get quick access to the relevant one
- As a first-time visitor, I want to be able to subscribe to the blog so I could get relevant information about future blog posts
#### Registred user
- As a registered user I want to be able to leave comments for posts so that I can engage with other users and, leave feedback about certain posts
- As a registered user I want to be able to like/unlike posts so that I can support certain posts without providing comment
- As a registered user I want to be able to update my profile information so that I could change my first name, last name, email and password and add a profile picture, bio
#### Site owner
- As a site owner, I want to be able to create, update and delete posts so that I can control my website content
- As a site owner, I want to be able to approve or delete comments so that I can filter out objectionable comments
-As a site owner, I want to be able to access all subscribed emails so that I could send new information related to my website
- As a site owner, I want to be able to delete users so that I can receive several benefits such as: manage my data, reduce liability & resource optimization 


### Wireframes
Below are the wireframes for the site that I created using balsamiq. 
#### Desktop
<details><summary>Home page</summary>
<img src="readme_img/wireframes/bals_home.png">
</details>

<details><summary>Post page</summary>
<img src="readme_img/wireframes/bals_post.png">
</details>

<details><summary>Single post page</summary>
<img src="readme_img/wireframes/bals_single.png">
</details>

<details><summary>Profile page</summary>
<img src="readme_img/wireframes/bals_profile.png">
</details>

<details><summary>Signup page</summary>
<img src="readme_img/wireframes/bals_sign.png">
</details>

#### Mobile
<details><summary>Home page</summary>
<img src="readme_img/wireframes/bals_m_home.png">
</details>

<details><summary>Posts page</summary>
<img src="readme_img/wireframes/bals_m_post.png">
</details>

<details><summary>Single post page & navigation menu</summary>
<img src="readme_img/wireframes/bals_m_single.png">
</details>

<details><summary>Profile</summary>
<img src="readme_img/wireframes/bals_m_profile.png">
</details>

<details><summary>Sign up</summary>
<img src="readme_img/wireframes/bals_m_signup.png">
</details>

  
### Agile Methodology
The Agile Methodology was used to plan this project. I found it hard for me to work parallel on agile and on my coding as I was team of 1 and was aware of the changes and progress I made, so I had to add a few things at the end of my project. I did learn more towards the end of the project about the use of the agile develepment. I implemented it through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections: 

* To-Do- (All the User stories were initially entered in the 'To Do' column)
* In Progress- (then during development story they were moved into the 'In Progress' column)
* Done- (and then finally they get moved into 'Done' once the development completes)

<details><summary>Project board</summary>
<img src="readme_img/user_stories.png">
</details>

<details><summary>Milestones</summary>
<img src="readme_img/milestones.png">
</details>

<details><summary>Milestone detail</summary>
<img src="readme_img/milestone.png">
</details>

<details><summary>Issues board</summary>
<img src="readme_img/issues.png">
</details>

<details><summary>User story detail</summary>
<img src="readme_img/user_story.png">
</details>

### Typography


### Colour Scheme
For this site, I decide to keep the main color scheme very simple, with the text either being white or black with background of certain cards and the footer beeing orange while the rest of the background is white.
I did also have some buttons like the login, signup, logout, delete and update  which were colored according to the standards
  
<!-- ![colour scheme](readme-docs/images/color-scheme.jpg)  
- - -  -->

### DataBase Diagram
Below is the database diagram that I created using LucidCharts.

<details><summary>DataBase diagram</summary>
<img src="readme_img/database.jpeg">
</details>

## Features:

### Navigation Bar
- The Navigation bar sits at the very top of each page, and it's sticky navbar which means when page is longer and user has to scroll down the navbar will stay on top of the page all the time! The logo is at the left side and the navigation links are in the middle with login/signup buttons on the right.
- When logged in new link is displayed to the user "Profile" and login/signup button is replaced with Logout button. Also user name is displayed next to the logo.
- The Navbar background is black with opacity set to 75%.
- On large to xx-large screens the navigation bar is in the center of the page and is sized by the bootstrap class.
- The active page (page that the user is currently on) is displayed in bold text, this makes it stand out much more and is clear to the user which page they are on.
- When on medium to small screens the navigation menu changes to burger menu which shows all the nav links when clicked on.
  
<details><summary>Navbar</summary>
<img src="readme_img/navbar.png">
</details>

<details><summary>Navbar Logged in</summary>
<img src="readme_img/navbar_login.png">
</details>

<details><summary>Navbar mobile</summary>
<img src="readme_img/navbar_mobile.png">
</details>


### Footer
- The footer is found at the bottom of every page and is responsive for tablet and mobile too.
- It displays the logo in the left corner, social links (Youtube, Facebook, Twitter & Youtube) are in the middle of the footer and, the Subscription field is on the right side of the footer.
- When any of the icons are clicked the social media site opens on a separate tab, this way the user still has the main website open, also by clicking on thelogo the user is redirected to the home page.
  
<details><summary>Footer</summary>
<img src="readme_img/footer.png">
</details>

### Home Page
- The home page has a dark hero image with text gradually displaying and deleting indicating site purpose
- Bellow hero image there are two sections which describe the owner of the page and his reach to the community with icons and numbers

<details><summary>Home page</summary>
<img src="readme_img/home_page.png">
</details>


### Posts page
-  Posts are displayed in 2 columns with 3 posts per row, each post contains of: image, author, date, indicator of likes and comments and title and brief description which are clickable and will direct the user to another page about that post
- All posts are scaling up as the user hovers over them which makes it more attractive for the user

<details><summary>Posts page</summary>
<img src="readme_img/posts.png">
</details>

  
### Single post page
- On this page, the user can have a brief description of the certain post that he clicked on and get all relevant information about it
- Bellow post section user can either like that post or read/leave comments
- After the user posts his comment he will be prompted with the message that "comment is waiting for approval"
 
<details><summary>Single post page</summary>
<img src="readme_img/single_post.png">
</details>

<details><summary>Comments section</summary>
<img src="readme_img/comments.png">
</details>

### Profile page
- Profile page has 2 sections
<details><summary>Profile page</summary>
<img src="readme_img/profile.png">
</details>

- The first section displays current information about the user.
- The second section is a standard django form which allows the user to change information about him
- Bellow the form there is a link to reset/change his password. When a user clicks on it he will be directed to the page with further instructions.

<details><summary>Password change email input page</summary>
<img src="readme_img/password1.png">
</details>

<details><summary>Check email page</summary>
<img src="readme_img/password2.png">
</details>

<details><summary>Input new password page</summary>
<img src="readme_img/password3.png">
</details>

<details><summary>Password change confirmation page</summary>
<img src="readme_img/password4.png">
</details>
  - Bellow reset/change passwords there are 2 buttons to either "Update" or " Delete" the user account, if a user clicks on the delete button separate model will pop out for the user to confirm deleting his account. 

<details><summary>Delete account</summary>
<img src="readme_img/delete_account.png">
</details>

### Search page
- This page will either display a post that user has searched or it will provide a user with message that there is no post under that search
- Page behaves just like post page where user can open searched posts with click on the title of the post


### Login page
- Login page is a basic django allauth form that has 2 input fields for username and password with sign in the button below it
- A User also have description links to either signup for the website or to reset his password which will redirect a user to the "Password change page"
<details><summary>Login page</summary>
<img src="readme_img/login.png">
</details>

### Signup page
- The signup page is also a standard django form with all required fields for a user to input. After inputting all the fields and pressing sign-up button user will be automatically logged in and redirected to the home page.
<details><summary>Sign up page</summary>
<img src="readme_img/signup.png">
</details>


## Future Features
<details><summary>Future features</summary>
<img src="readme_img/page_screen/future.png">
</details>
- There are 3 features that I would like to implement in the next iteration that would improve user experience and attract more traffic to my website
- Create a gallery page
- Allow users to create their posts (CRUD)
- Create a booking system for adventures


## Technologies Used
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) was used to create the wireframes.
- [LucidChart](https://www.lucidchart.com/pages/) was used to design the database schema.
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Gitpod](https://www.gitpod.io/about) was used to create this site and then push everything to github.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [Cloudinary](https://cloudinary.com/) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.
- [Grammarly](https://app.grammarly.com/) was used to check typography.
- - -

## Libraries
- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
- cloudinary - A Python package allowing integration between the application and Cloudinary.
- coverage - is a third-party package that helps developers measure code coverage in their Python codebase.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- Django - A python package for the Django framework.
- django-active-link - A Django package used to highlight an active link in the site navigation bars.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-summernote - is a third-party package that provides a rich text editor widget for Django web applications.
- django-crispy-forms - A Django package that provides tags and filters to control the rendering behaviour of Django forms. 
- gunicorn - A Python WSGI HTTP Server for UNIX.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- psycopg2 - A PostgreSQL database adapter for Python.
- PyJWT - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
- python3-openid - A set of Python packages to support use of the OpenID decentralized identity system.
- pytz - A Python package for world timezone definitions, modern and historical.
- Pillow - A Python Imaging Library adds image processing capabilities
- requests-oauthlib - A Python package for OAuthlib authentication support for Requests.
- sqlparse - A non-validating SQL parser for Python.
## Testing
The testing section can be found [here](TESTING.md).

## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |
| On home page hero image was not loading| Created new file path directly to Cloudinary |
| Post page was not displaying| Change path in urls.py to post/ |
| Admin page have no style | Set DEBUG to True|
| Locally reset password email not working| Implemented if else statemEnt for DEVELOPMENT in settings.py for email part|
| No css style on Heroku | Before every deployment set debug to false and run "python3 manage.py collectstatic" |
| Deployment issue on Heroku multiple times error "etag" & error collectstatic | Deleted all Cloudinary files and pushed code again |
| Password reset & password confirm templates not rendering, displayed django templates | Renamed templates from django documentation |
| After signing up user was not logged in automatically | Changed registration function and added extra code to store data from user and use it to login automatically |
| Profile model information was not updating with the user model on the profile page| Combined 2 forms into 1 function |
| The user image was not uploading| Added code in the form = 'enctype="multipart/form-data"'|
| No css styles on heroku| Add ',' in settings.py 'STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]'|
| No css styles on heroku| Deleted all static files in Cloduinary|
| No searched posts displayed on search page | replaced {% if post in posts %} with {% if posts %} statemant and placed it outside div |


## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
- - -

## Credits
- [Stack Overflow](https://stackoverflow.com/) is probably a developer's best resource, this provided me with many answers to my questions.
  Examples of code I found on slack that helped me with coding:
    'def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in ["username", "email", "password1", "password2"]:
            self.fields[field].help_text = None'
  Also found similar solution on how to combine 2 forms into 1 (in my case User & Profile form)
- [W3schools](https://www.w3schools.com/) this was great for looking up forgotten **CSS** syntax and how to use it.
- [Unsplash](https://unsplash.com/) all images were taken from Unsplash.
- [CodeInstitute](https://learn.codeinstitute.net/) for their walkthrough project 'I think I can blog', which guided me with website build especially for publishing posts and comments section which I code along with the video with few adjustments
- [AllTrails](https://www.alltrails.com/) for providing me some text and useful information for my posts
- [youtube](https://www.youtube.com/) videos from **codemy**, **netninja** and **veryacademy** for guidance and examples on how to create blog and improve of the website
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) for their documentation which was helpfull in creating user authentication
- [Logoapp](https://logo.com/) for providing me with tools to easier generate my idea and create logo


## Acknowledgements:
- I would like to thank my mentor Narander Singh for all his help throughout the project and guidance in general
- I would like to thank Code Institutes Slack Community, and tutor support as this helped me so much when I got stuck on part of my project
- I would also like to thank our cohort facilitator Irene Neville, for answering any course-related questions I asked and for providing us with weekly guidance information about the project

[Back to the top](#take-a-hike)