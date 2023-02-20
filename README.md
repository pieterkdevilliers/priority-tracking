

[Link to deployed site](https://ci-priority-tracker.herokuapp.com/)

**Project Overview - What are we aiming for?**

A priority tracking app, allowing the user to specify their top 3 priorities, and then track their time on tasks. This will allow the user to see how much of their time is spent on priority and how much is spent off priority.

[![Wireframe Overview](/assets/images/wire_frame_screenshot.png)](https://www.loom.com/share/14b672c3510a4650bfed82f3297aa880)

**Where does your time go?**

It is easy to be busy, and still feel as if you don't get anything done. This often happens when you don't know where your time goes. What are you really busy with? With this Priority Tracking App you'll see clearly how much of your time is spent on what is really important, and what is wasted away.

---
## Table of Contents
1. [**Why This Project**](#why-this-project) 
2. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Database Schema**](#database-schema)
3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
4. [**Technologies Used**](#technologies-used)
    - [**Version Control**](#version-control)
    - [**Hosting**](#hosting)
5. [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
    - [**Automated Testing**](#automated-testing)
    - [**Manual User Testing**](#manual-user-testing)
    - [**Travis Continuous Integration**](#travis-continuous-integration)
    - [**Interesting Bugs Or Problems**](#interesting-bugs-or-problems)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)
---
### Why This Project?
This project was initially inspired by a paper version used by a friend, [Emma Mills](https://www.linkedin.com/in/emmamipa/), for her clients. It is used in her company [Mi-PA](https://www.mi-pa.co.uk/), to help clients identify the work which can be handed off to the Mi-PA team.

For the front-end I used HTML, CSS and JavaScript. For the back-end I used Python, Django, SQLite3 and PostgreSQL.

## UX
This is a simple Priority Tracker, focussed on tracking the work you are actually doing, and not as a task-list manager for work you intend to do.

Users can register/login and create their own Work Categories, Active Priorities and Actions, in a simple uncluttered interface.

### User Stories
"**_As a user, I would like to_** _____"
- reister for a new account
- log into my existing account
- create my own work categories
- list my own key priorities
- list my actions within priorities and categories
- track time for each action
- see the total time tracked
- see what percentage of time is spent on-priority and off-priority
- relist an incomplete action for today
- mark actions as complete
- undo a completed action
- delete actions not required
- have the ability to reset my password if I forget it

"**_As a product owner, I would like to_** _____"
- send new registered users an automated welcome email
- assist users with resetting their passwords, in an automated fashion
- have full test coverage for Models, Views and Forms


### Wireframes
I used Balsamiq to create the wireframes and mock-up of the app. The links to the files are below:
- [Registration](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/registration_page.png)
- [Login](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/login_page.png)
- [Basic Actions](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/basic_actions_page.png)
- [Multi-Actions](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/multi_actions_apge.png)
- [Full App Screen](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/full_app_page.png)

### Database Schema
At the start of the project I created a Database Schema using [dbdiagram.io](https://dbdiagram.io) The link to the file is below:
- [Database Schema](https://github.com/pieterkdevilliers/priority-tracking/blob/assets/images/priority_tracker_schema.png)

##### [back to top](#table-of-contents)
---

## Features
### Existing Features

#### Actions - serves as the main page for using the app
- **Navigation** - Simple navigation to access the Actions, Categories, Priorities, Past Actions and Help sections. This is visible on all pages in the app.
- **Things I need to do** - This lists the existing actions being worked on and the ability to add new actions. For each action there is also controls to start/stop the timer, mark an actions as done, edit an action or delete an action.
Each action displays information on the Title, Related Priority, Related Category the time tracked and the action date.
- **Things I've done** - This simply lists the Completed Actions, with the ability to undo an Action, which moves it back into the "Things I need to do" section.
- **Active Priorities** - This section shows the Active Priorities, with their Title, Description and related Category.
- **Time Tracking** - Here a user can see their tracking details.
Time - Today: Displays the number of Actions, Completed Actions, Open Actions and Total Time Tracked for the day.
Focus - Today: Displays the percentage and time split between on-priority and off-priority tracking, for today. This area has a red border when the On-Priority Percentage is below 70%.
Averages: Displays the on-priority and off-priority percentages for all time. This area has a red border when the On-Priority Percentage is below 70%.

#### Categories - management of all Categories
- **Add a Category** - Allows the user to add a work Category, which is then used to categorise Priorities and Actions.
- **Edit a Category** - Allows the user to amend an existing Category.
- **Delete a Category** - Allows the user to delete an existing Category.

#### Priorities - management of all Priorities
- **Add a Priority** - Allows the user to add Priorities, which can be nested under Categories, and used to link Actions to their related Priorities.
- **Edit a Priority** - Allows the user to edit an existing Priority.
- **Priority Active Status** - Only Active Priorities are shown on the Actions Overview. Actions can only be assigned under Active Priorities. Users control the Active/Inactvie status of Priorities with a tiggle.
- **Delete a Priority** - Allows users to delete existing Priorities. Only Inactive Priorities can be deleted.

#### Past Actions - ability to access past Actions and their details
- **Search** - Users have the ability to select a date to filter past Actions by. The result shows Actions with an Action Date matching the search query.
- **Relist Actions** - In addition to the standard Action Controls as listed in the Things I need to do section, users here have the option to "relist" an action, which moves it from the Past Actions results into today's active Actions list.

#### Help & Logout - simple help and logout
- **Help** - A simple overview to help new users get to know the Priority Tracker and the available functions.

- **Logout** - Users can log out of their account and they will be redirected to the login page.

#### Error Pages
-  Included are custom error handlers for 400, 403, 404 and 500 errors, with the option to navigate back to the desired section of the app. 

### Features Left to Implement
- **Auto-Relist Actions** - At some stage I would like to add an automated sevice which will automatically relist yesterdays uncompleted Actions to today, to save the user time in having to review the previous day's uncompleted Actions.

##### [back to top](#table-of-contents)
---
## Technologies Used
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the pages and content of the app.

- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to the app.

- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework for the majority of the layout and styling.

- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language applied using the Django Framework.

- [**Django**](https://www.djangoproject.com/)
    - **Django** was used for all aspects of creating the app. 

- [**Font Awesome**](https://fontawesome.com/)
    - **Font Awesome** is used for the icons for the Actions, Priorities and Categories.

- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the Database when running the project locally.

- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database for the deployed version of the app.

- [**SendGrid API**](https://stripe.com/gb)
    - **SendGrid** is used to send the new user Welcome email as well as the emails related to the Password Reset process.

- [**GitPod**](https://gitpod.io/)
    - I've used **GitPod** as the development environment when writing the code for the app.

### Version Control
- [**Git**](https://git-scm.com/)
    - **Git** is used as a version control system throughout the building of this app.

- [**GitHub**](https://github.com/)
    - I use **GitHub** as a remote repository linked to Heroku when committing and pushing updates and changes.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - The deployed vertion of the app is hosted on **Heroku**.

##### [back to top](#table-of-contents)
---

## Testing

### Code Validation
- [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) was used to validate all HTML code.
    - As W3C doesn't validate the Django Template HTML correctly, the validator remains showing some errors, but these are specific to the W3C compatibility with Django Templates. All standard HTML validates successfully.
- [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate all CSS code, excluding Bootstrap.
- [Pep8 Online tool](http://pep8online.com/) was used to validate my Python syntax.

### Automated Testing
The [Coverage](https://pypi.org/project/coverage/) library was used throughout testing to help keep track of how much of my code was covered by the tests. The tests provide an overall coverage of 82% when including all files including files generated by Django.

You can generate a coverage report by installing the package using `pip3 install coverage`
- Run `coverage run manage.py test`
- Then `coverage html` to generate the report
- The report can be viewed in a browser by opening the `index.html` file from inside the `htmlcov` folder.


### Interesting Bugs Or Problems
- **Repeating Past Action Query** - When a user performs a Past Actions query the app displays the Actions for the queried date. The trick here was to ensure that when the user marks a Past Action as Done, Undone or Relisting a Past Action, that the page relaods, including the most recently user Query Date. This is so that the user does not need to keep running the query manaully when updating multiple Actions from a Past Actions query. The solution here was to store the Query Date as a cookie, in order to fetch it upon page reload, combined with `click` event listeners.

- **Past Action Query Reload Loop** - I ran into an issue where once the Past Actions page was cleared of either all Done Actions or Active Actions, the page would go into a looping reload. This was solved by using a cookie for the reload_required_status in order to only reload the query page when required.

##### [back to top](#table-of-contents)
---

## Deployment
Using GitHub for version control and Heroku as the host for the deployed version of the site, I deployed to Heroku following these steps:

1. Create an app in Heroku using a unique name.

2. Under the **Resources** tab in Heroku, search for **Heroku Postgres** in the 'Add-Ons' section.

3. Selected the **Heroku Mini** level.

4. Updated the `env.py` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.

5. Ran the `python manage.py makemigrations`, `python manage.py migrate`, `python manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.

6. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.

7. Add the required SendGrid and Database URL values as required.

KEY | VALUE
--- | -----
DATABASE_URL | link to db |
SENDGRID_API_KEY | sendgrid API Key |

8. On the **Deploy** tab in Heroku, connect the Heroku App to the GitHub repository and select **Enable Automatic Deployment** as the deployment method.

11. Ensure `settings.py` references the correct Environment Variables for the Database Connections.


12. Update the `settings.py` file with the relevant configuration for static and media file storage.

13. Update the `settings.py` file with the required SendGrid email settings.

14. Confirm the correct API values in the `sendgrid.env` file.

15. Confirm that `sendgrid.env` is included in `.gitignore`

13. Run the `python manage.py collectstatic` command to push the static files to Heroku.

14. Created a requirements.txt file using the following command in the terminal window:
    ```pip3 freeze --local > requirements.txt```

15. Create a Procfile using the following command in the terminal window:
    ```echo web: gunicorn priority_tracker.wsgi:application > Procfile```

16. Ensure that the Heroku App has an associated Dyno for running the App

16. Run the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app should be successfully deployed to Heroku.

### Repository Link

Visit the project's GitHub repository:

[GitHub Repository](https://github.com/pieterkdevilliers/priority-tracking)

### Running Code Locally

To run the code locally, you can follow these steps:

1. Go to my [GitHub repository](https://github.com/pieterkdevilliers/priority-tracking)

2. Select Clone from the 'Code' dropdown.

3. Copy the clone URL for the repository under the HTTPs tab.

4. Open 'Git Bash' in your local IDE.

5. Select the directory you want to use for the clone.

6. Use `git clone`, and paste the URL from step 3 above. 
    
    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the clone process.

9. Install `requirements.txt` using the following command in your Terminal:

    ```pip3 install -r requirements.txt```

10. Run the following command in your Terminal:

    ```python manage.py runserver```

11. Click the `http://` link  or the `Open In Browser` button from the pop-up,to load the project.

12. Migrate the database models and create a super user:

    `python manage.py makemigrations`
    `python manage.py migrate`
    `python manage.py createsuperuser`


This will migrate the models and create your SuperUser account. You should now be able to run the site locally.

 To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

##### [back to top](#table-of-contents)
---

## Credits
#### Helpful Resources
These creators and teachers were all helpful through there content at different steps in this project.
- [Tech With Tim - YouTube ](https://www.youtube.com/@TechWithTim) 
- [Dennis Ivy - YouTube ](https://www.youtube.com/@DennisIvy)
- [Codemy.com - YouTube ](https://www.youtube.com/@Codemycom)
- [TylerPottsDev - GitHub ](https://github.com/TylerPottsDev/yt-js-stopwatch)
- [WhiteNoise - Django Library ](https://whitenoise.evans.io/en/latest/)
- [StudyGyaan - YouTube ](https://www.youtube.com/watch?v=VIx3HD2gRWQ)
- [Did Coding - YouTube ](https://www.youtube.com/@DidCoding)
- [Master Code Online - YouTube ](https://www.youtube.com/@LearnpythontutorialFree)

I also found a lot of examples and suggested solution to questions on Stack Overflow for specific issues I got stuck on.
- [Stack Overflow ](https://stackoverflow.com/)


#### Acknowledgements
- I would like to thank both my mentors [Guido Cecilio](https://github.com/guidocecilio) for their feedback and suggestions.
- Thanks to the CI Slack community for help with the odd question.

##### [back to top](#table-of-contents)
---