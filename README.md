

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
This project was initially inspired by a paper version used by a friend [Emma Mills](https://www.linkedin.com/in/emmamipa/), for her clients. It is used in her company [Mi-PA](https://www.mi-pa.co.uk/), to help clients identify the work which can be handed off to the mi-PA.

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
- **Navigation** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Things I need to do** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.
- **Things I've done** - Visible to users not logged in, allows the user to click the button and redirects them to the selected book detail page.
- **Active Priorities** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.
- **Time Tracking** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.

#### Categories - serves as the main page for using the app
- **Add a Category** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Edit a Category** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.
- **Delete a Category** - Visible to users not logged in, allows the user to click the button and redirects them to the selected book detail page.

#### Priorities - serves as the main page for using the app
- **Add a Priority** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Edit a Priority** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.
- **Priority Active Status** - Visible to users not logged in, allows the user to click the button and redirects them to the selected book detail page.
- **Delete a Priority** - Visible to users logged in, clicking this button will add the selected book to shopping cart and redirects the user to cart summary view.

#### Past Actions - serves as the main page for using the app
- **Search** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.
- **Relist Actions** - This section displays 3 of the newest featured books the site has to offer to the user. Images are clickable to allow the user to view more information about the book.

#### Help & Logout - serves as the main page for using the app
- **Help** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.

- **Logout** - The navbar links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Browse', 'Register' and 'Login' links are shown. When the user is logged in, the 'Home', 'Browse', 'Profile' and 'Logout' links are shown.

#### 404 and 500 Error Pages
-  I've included custom 404 and 500 error messages and error handlers to catch these errors. My custom messages allow the user to redirect back to the home page.

### Features Left to Implement
Due to a change in my personal circumstances and with more time and knowledge, I would have liked to implement some additional features to the app:
- **Auto-Relist Actions** - This feature is currently out of the scope of this project. I have added a link to the project to show potential of how it could be used. I feel this is an important feature to have, a user making any purchase online would generally want to be able to track there order.

##### [back to top](#table-of-contents)
---
## Technologies Used
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.

- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to my app.

- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap styles, before adding my custom styles.

- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.

- [**Django**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.

- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the visual icons used in my app.

- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.

- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.

- [**SendGrid API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for my app.

- [**GitPod**](https://code.visualstudio.com/)
    - I've used **Visual Studio Code** as the development environment to write the code for my app.

### Version Control
- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to my project in Visual Studio Code, before pushing to GitHub.

- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

##### [back to top](#table-of-contents)
---

## Testing

### Code Validation
- [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) was used to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate my CSS code.
- [Pep8 Online tool](http://pep8online.com/) was used to validate my Python syntax.

### Automated Testing
The [Coverage](https://pypi.org/project/coverage/) library was used throughout testing to help keep track of how much of my code was covered by the tests. The tests provide an overall coverage of 76%.

To generate your own coverage report install the package using `pip install coverage`
- Run `coverage run manage.py test`
- Then `coverage html` to generate the report
- The report can be viewed in a browser by opening the `index.html` file from inside the `htmlcov` folder.


### Manual User Testing
[Manual testing document](TESTING.md)

### Travis Continuous Integration
In addition to the automated testing files, I used Travis CI for Continuous Integration testing of my code.

### Interesting Bugs Or Problems
- **Stripe Payment** - Has a customized logo at the top of the modal payment form. After deploying the app to Heroku and during testing I realised that image was not displaying correctly due to an error. All image files were uploaded to the AWS bucket, but the image link was broken. The image link was amended in order to fix this bug.
- **Reset Password & Email Confirmation** - Despite allowing less secure apps within my Google Account settings, as instructed by Code Institute's LMS videos, I was still getting an SMTPAuthenticationError when entering the password on the 'Password Reset' screen. This meant that the site was failing to send the password reset email to the user. I resolved this issue by activating the 2-Step Authentication in my Google Account, creating an app password and storing it within my environment variables instead of my standard Gmail password, as instructed by the Django SMTPAuthenticationError article.
- **Order History Tab Page Reload** - The order history is displayed within a multitab view and is paginiated to display a list of 4 items per page. Clicking the pagination to move to the next page makes the page reload. The default tab view is set to the Profile tab so when the page reloads the user is taken back the default Profile view. This meant that the user had to click back onto the History tab in order to view the second page. I resolved this by adding a Javascript to handle the URL request to the selected page, as advised by a [How to get URL parameter using Javascript](https://stackoverflow.com/questions/19491336/how-to-get-url-parameter-using-jquery-or-plain-javascript#:~:text=inArray%20%3A%20http%3A%2F%2Fapi.jquery,.com%2FjQuery.inArray%2F&text=url%20%3D%20%27http%3A%2F%2Fexample.,) artical on StackOverflow.
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