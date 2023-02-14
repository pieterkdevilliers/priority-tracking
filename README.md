

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
I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, 
I used the following steps:

1. Created the app using a unique name in Heroku.

2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.

3. Selected the free **Hobby** level.

4. Updated the `env.py` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.

5. Ran the `python manage.py makemigrations`, `python manage.py migrate`, `python manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.

6. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.

7. Copied and pasted all of the `env.py` default variables into Heroku's Config Vars settings.

KEY | VALUE
--- | -----
DATABASE_URL | link to db |
AWS_ACCESS_KEY_ID | aws access key |
AWS_SECRET_ACCESS_KEY | aws secret key |
AWS_STORAGE_BUCKET_NAME | aws bucket name |
SECRET_KEY | site secret key |
STRIPE_PUBLISHABLE_KEY | stripe key |
STRIPE_SECRET_KEY | stripe secret key |

8. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.

9. Went to the **Developers** section in Stripe and clicked on **API Keys**.

10. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE_KEY` and `STRIPE_SECRET_KEY` environment variables in the `env.py` file within my local workspace. These were also added to the Heroku's Config Vars settings.

11. Updated the `settings.py` with the new Stripe environment variables.

12. Went to the **S3** section of AWS and created a new S3 bucket.

13. Within the relevant bucket's permissions, changed the **CORS Configuration** to the following:
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

14. Still in the **S3** section, changed the **Bucket Policy** to the following:
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<my-bucket-name>/*"
            }
        ]
    }
    ```
15. Replaced the `<my-bucket-name>` in the `Resource` line with my S3 bucket's name instead.

16. Went to the **IAM** section of AWS, created a 'New Group' and attached my S3 bucket to it.

17. Still in the **IAM** section, created a 'New Policy' and a 'New User' and attached these to the newly created group.

18. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    ```

19. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.

20. Updated the `settings.py` file with the relevant configuration for static and media file storage.

21. Ran the `python manage.py collectstatic` command to push the static files to my S3 bucket.

22. Created a requirements.txt file using the following command in the terminal window:
    ```pip3 freeze --local > requirements.txt```

23. Created a Procfile using the following command in the terminal window:
    ```echo web: gunicorn bookstore.wsgi:application > Procfile```

24. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Repository Link

Click the link below to visit my project's GitHub repository:

[Bookstore Repository](https://github.com/pramcistudent/bookstore-milestone-four)

### Running Code Locally

To run my code locally, users can download a copy of my code to their desktop by completing the following steps:

1. Go to my [GitHub repository](https://github.com/pramcistudent/bookstore-milestone-four)

2. Click on 'Clone or download' under the repository name.

3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.

4. Open 'Git Bash' in your local IDE.

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type `git clone`, then paste the URL you copied in Step 
    
    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and clone the repository.

8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Create a `env.py` file with your own credentials and import this into the `settings.py` file

9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.

12. Run the following commands to migrate the database models and create a super user:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

##### [back to top](#table-of-contents)
---

## Credits
#### Content
- The Author content was sourced using [Google](https://www.google.com) search and by researching each individual Author.
- Information about each book was sourced using the online [Waterstones](https://www.waterstones.com/) E-commerce site.

#### Media
- The site Logo was created using [Free Logo Design](https://www.freelogodesign.org/) site.
- I found the Favicon image on Google, and I used the [Favicon.io](https://favicon.io/) converter to convert the image to a Favicon.
- Carousel images were sourced from the [Google](https://www.google.com/search?q=book+images&tbm=isch&ved=2ahUKEwinuaq1zqnqAhUF0oUKHU2XAVYQ2-cCegQIABAA&oq=book+images&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCsJ1jGM2C1NWgBcAB4AIABiAGIAcAFkgEDNi4ymAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=zDn7XqejBoWklwTNroawBQ&bih=625&biw=1024&safe=active&hl=en) images pages.
- Images for each book were sourced by using the online [Waterstones](https://www.waterstones.com/) E-commerce site.
- Images were converted from PNG files to JPG files by using [PNG2JPG](https://png2jpg.com/) site and re-seized by using [Pixlr](https://pixlr.com/x/) site.

#### Acknowledgements
- I would like to thank my mentor [Guido Cecilio](https://github.com/guidocecilio) for his feedback on my project's scope, design and functionality.
- Thanks to the Slack community for their feedback and help on how to debug my Python code.

### Disclaimer
This project is for educational purposes only.

##### [back to top](#table-of-contents)
---