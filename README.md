# Soundscape API

Soundscape API is built using Django REST Framework to support a web application. This application serves as a dynamic platform that facilitates the sharing of acoustic environment sound recordings. Moreover, it allows users to download and make compositions using these recordings. Soundscape API enables efficient and secure communication between the web application frontend and backend services by leveraging the powerful features of the Django REST Framework.

## Table of Content

- [Features](#features)
- [User Stories](#user-stories)
- [Data Models](#data-models)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Features

- Users can register, log in,log out and authenticate, ensuring secure access to personalized features and data.

- Users can view and update their profiles, including preferences, settings, and other relevant information.

- Users can upload their acoustic environment recordings, while others can access and download these recordings.

    *All the features are explained in detail in the [API Endpoints](#api-endpoints) section.*

## User Stories

1. As a application developer, I want to retrieve a list of registered profiles through the API so that I can display them in the user interface of the application.
2. As a application developer, I want to to retrieve profile details through the API so that I can display it in the user interface of the application.
3. As a application developer, I want to to retrieve a profile through the API so that I can edit/delete the profile.
4. As a application developer, I want to retrieve list of posts through the API so that I can display them in the user interface of the application.
5. As a application developer, I want to to retrieve a post through the API so that I can edit/delete the post.
6. As a application developer, I want to retrieve list of likes through the API so that I can display them in the user interface of the application.
7. As a application developer, I want to to retrieve a like through the API so that I can delete/unlike it.
8. As a application developer, I want to retrieve list of followers through the API so that I can display them in the user interface of the application.
9. As a application developer, I want to retrieve a follower details through the API so that I can display it in the user interface of the application.
10. As a application developer, I want to retrieve list of comments through the API so that I can display them in the user interface of the application.
11. As a application developer, I want to retrieve a comment details through the API so that I can display it in the user interface of the application for editing/deleting.

## Data Models

The following models were created to represent the database model structure of the application:

![Entity Relationship Diagram](../soundscape-backend/docs/soundscape_data_models.png)

### User Model

Django's default User model. The user identifier is the username.

- One-to-one relation with the Profile model
- ForeignKey relation with the Post model
- ForeignKey relation with the Comment model
- ForeignKey relation with the Like model
- ForeignKey relation with the Follower model

### Profile Model

It is created automatically upon user registration.

- One-to-one relation with the User model

### Post Model

- ForeignKey relation with the Like model
- ForeignKey relation with the Comment model

### Comment Model

- ForeignKey relation with the User model
- ForeignKey relation with the Post model

### Like Model

- ForeignKey relation with the User model
- ForeignKey relation with the Post model

### Follower Model

- ForeignKey relation with the User model

## API Endpoints

| HTTP | URI | Status Code | CRUD Operation | View Name |
|---|---|---|---|---|
| GET | soundscape/api/profiles/| 200 (OK) | READ (list all profiles) | ProfileList |
| GET | soundscape/api/profiles/:id| 200 (OK) | READ (retrieve a profile by id) | ProfileDetail |
| PUT | soundscape/api/profiles/:id | 200 (OK) | UPDATE (update a profile by id) | ProfileDetail |
| GET | soundscape/api/posts/| 200 (OK) | READ (list all posts) | PostList |
| GET | soundscape/api/posts/:id| 200 (OK) | READ (retrieve a post by id) | PostDetail |
| PUT | soundscape/api/posts/:id | 200 (OK) | UPDATE (update a post by id) | PostDetail |
| DELETE | soundscape/api/posts/:id | 200 (OK) | DELETE (delete a post by id) | PostDetail |
| GET | soundscape/api/likes/| 200 (OK) | READ (list all likes) | LikeList |
| GET | soundscape/api/likes/:id| 200 (OK) | READ (retrieve a like by id) | LikeDetail |
| DELETE | soundscape/api/likes/:id| 200 (OK) | DELETE (undo a like by id) | LikeDetail |
| GET | soundscape/api/comments/| 200 (OK) | READ (list all comments) | CommentList |
| GET | soundscape/api/comments/:id| 200 (OK) | READ (retrieve a comment by id) | CommentDetail |
| DELETE | soundscape/api/comments/:id| 200 (OK) | DELETE (delete a comment by id) | CommentDetail |
| GET | soundscape/api/followers/| 200 (OK) | READ (list all followers) | FollowerList |
| GET | soundscape/api/followers/:id| 200 (OK) | READ (retrieve a follower by id) | FollowerDetail |
| DELETE | soundscape/api/followers/:id| 200 (OK) | DELETE (undoe following a user by id) | FollowerDetail |

## Technologies Used

### Languages and Frameworks

- Python
- Django
- Django REST Framework

### Libraries, Tools and Packages

- [django-allauth](https://pypi.org/project/django-allauth/)
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [psycopg](https://www.psycopg.org/)
- [Pillow](https://pypi.org/project/pillow/)
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/)
- [cloudinary](https://pypi.org/project/cloudinary/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [django-filter](https://pypi.org/project/django-filter/)
- [coverage](https://pypi.org/project/coverage/)

### Development Tools and Platforms

- GitHub (Version Control)
- Git (Version Control System)
- Heroku (Cloud Platform for Deployment)
- Cloudinary (Cloud-based Media Management)

### Project Management and Collaboration

- GitHub Issues (Issue Tracking)
- GitHub Projects (Project Management)

## Testing

### Automated Tests

Tests have been written for most of the code written for the project. Tests have not been written for serializers. Coverage test report is as follows.

<details>
<summary>Show coverage report</summary>
<img src="../soundscape-backend/docs/coverage_report.png">
</details>

### User Stories Testing

All user stories have been manually tested with the following results

For user stories => [User Stories](#user-stories)

| Stories | Action | Expected Result | Test Result |
| -------- | ------------------- | ------------------- | ----------------- |
| 1/2/3 | Create, update & delete user profile | A user profile can be created, edited or deleted | Passed |
| 4/5 | Create, update & delete | A post can be created, edited or deleted | Passed |
| 6/7 | Create & delete | A like can be created or deleted (like / unlike post) | Passed |
| 8/9 | Create & delete | Follow or unfollow user | Passed |
| 10/11 | Create, update & delete | A comment can be created, edited or deleted | Passed |

### PEP-8 Testing

The Python code has passed PEP-8 testing using the [Python Linter](https://pep8ci.herokuapp.com/) provided by the Code Institute.

## Deployment

The following steps were taken to deploy the project:

1. Clone or fork the project repo.
    <details>
    <summary>Image</summary>
    <img src="../soundscape-backend/docs/deployment_images/clone_or_fork.png">
    </details>
2. Create a [cloudinary](https://cloudinary.com) account and get your cloudinary url from your account dashboard.
    <details>
    <summary>Image</summary>
    <img src="../soundscape-backend/docs/deployment_images/cloudinary_url.png">
    </details>
3. Create a database. Since the database URL was sent via e-mail by Code Institute, no image is provided for it. You can find free database storage providers and get your database URL from the providers. For details see the documentation [PostgreSQL connection settings](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
4. Create a [Heroku](https://www.heroku.com) account and start your app. Go to the app settings and click the `Reveal Config Vars`. Add the following configuration variables.

        SECRET_KEY
        CLOUDINARY_URL
        DATABASE_URL
        ALLOWED_HOSTS
        CLIENT_ORIGIN_DEV
        CLIENT_ORIGIN
        DISABLE_COLLECTSTATIC
5. After adding the configuration variables go to the `Deploy` tab and connect the GitHub repository with the Heroku.
    <details>
    <summary>Image</summary>
    <img src="../soundscape-backend/docs/deployment_images/heroku_github_repo.png">
    </details>
6. Now scroll to the `Manual deploy` section and click the `Deploy Branch` button.
    <details>
    <summary>Image</summary>
    <img src="../soundscape-backend/docs/deployment_images/deploy_branch.png">
    </details>
7. After the deployment is completed, you can open the deployed app by clicking `View`.

## Credits
