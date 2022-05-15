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
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

* **Backend:** Django, Python
* **Frontend:**  HTML, CSS, JS, Crispy-Form, Bootstrap
* **Container:**  Docker
* **Database:**  PostGreSQL
* **Webhosting:**  Heroku
* **Backend Storage:**  AWS S3


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
* Run the Django server on Docker using:
  <br>`$ docker-compose up -d --build`
  <br>`$ docker-compose down`
  <br>`$ docker-compose up`
  
 ## Note
 The deployed version using S3 as backend storages, which is not public because of security concerns.


