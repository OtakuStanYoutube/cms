# OtakuStan CMS

<div align="center">
    <h1>Welcome to OtakuStan CMS Repository</h1>
</div>

## About
This is an Central Content Management system for Otakustan to power all our dynamic content like blogs, articles, news feed, guest feed, etc for our website and podcasts. This made for OtakuStan's internal use only. The main user website is made using Django and Django rest framework.

### 🏗️ Built With

<div>

[<img src="https://img.shields.io/badge/-Python-306998?style=for-the-badge&labelColor=black&logo=python&logoColor=4b8bbe" >](https://www.python.org/)

[<img src="https://img.shields.io/badge/-Django-092e20?style=for-the-badge&labelColor=black&logo=Django&logoColor=092e20" >](https://www.djangoproject.com/)

[<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&labelColor=black&logo=sqlite&logoColor=white" >](https://www.sqlite.org/index.html)


</div>

## Features

* [ ] Create Blogs
* [ ] Create Articles
* [ ] Create News Feed
* [ ] Create Guest Feed
* [ ] One Api for all our websites
* [ ] Manage Content
* [ ] Live Update

## Install and Run

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.

To contribute, please follow the [guidelines](https://github.com/divanov11/mumbleapi/blob/master/Contributing.md) process.

1. Clone the repository using the following command

```bash
git clone git@github.com:OtakuStanYoutube/cms.git
# After cloning, move into the directory having the project files using the change directory command
cd mumbleapi
```
2. Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
3. Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

4. Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```


5. Run the development server

```bash
# run django development server
python manage.py runserver
```

## 🔐 License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details

## Suggestions and Bug Reports
Since this is an open source project all suggestions, requests and bug reports are always welcomed. If you have any don't forget to leave them in the issues section. But we recommend creating an issue or replying in a comment to let us know what you are working on first that way we don't overwrite each other.

Don't forget to checkout the [CONTRIBUTING.md](CONTRIBUTING.md) for more info on how to contribute to this project.

## Branches

- staging -> pr this branch for everything
- prod -> don't even think of touching it, this is what's running in prod

<br>
<h2 id="credits">Credits</h2>
This was built by the following individuals.<br><br>
<ul>
    <li>Sudeep Deysarker (<a target="_blank" href="https://github.com/Lunaticsatoshi">@Lunaticsatoshi</a>)</li>
</ul>
