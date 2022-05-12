# Mebook_hub
> A blog website to share your e-book <br>

**Deployed Project :** [MeBook](https://mebook-hub.herokuapp.com/)
<br>
## Lisence 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Inspiration
MeBook aspires to become a place to store milestones in the process of increasing knowledge by allowing users to upload and store their favorite ebooks. Moreover, by sharing useful ebooks with the community, the value of ebooks is also enhanced.

## What it does
* Save and display your book as it on the shelf
* A book community for uploading, searching, rating, and dowloading
* Elevate the importance of ebooks

## How to use MeBook
* **Create an account**
  ![](https://github.com/trinhcaokhoa/Mebook_hub/blob/main/sign-up.png)
* **Uploading** 
  ![](https://github.com/trinhcaokhoa/Mebook_hub/blob/main/addbook.png)
* **Looking for other books**
  ![](https://github.com/trinhcaokhoa/Mebook_hub/blob/main/library.png)
* **Rating others books**
  ![](https://github.com/trinhcaokhoa/Mebook_hub/blob/main/rating.png)

## How MeBook was built
* **Backend: Django, Python**
* **Frontend: HTML, CSS, JS, Crispy-Form, Bootstrap** 
* **Container: Docker**
* **Database: PostGreSQL**
* **Webhosting: Heroku**


## Set up
* Fork and Clone the repo using <br>
`$ git clone https://github.com/trinhcaokhoa/Mebook_hub.git`<br>
`$ cd Mebook_hub`
 * Create and activate virtual environment using pipenv
   <br>
   `$  pipenv shell`
* Use the package manager pip to install all dependencies
  <br>
  `$ pip install -r requirements.txt`
* Or Run the Django server using:
  <br>`$  python manage.py runserver`
* Or Run the Django server on Docker using:
  <br>`$ docker-compose up -d --build`
  <br>`$ docker-compose down`
  <br>`$ docker-compose up`


