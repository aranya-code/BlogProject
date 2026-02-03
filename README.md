# 📘 BlogProject

A simple Django blog application that allows users to read posts, add comments, and save posts to read later using session storage.

---

## 🚀 Features

- View all blog posts
- View individual post detail pages
- Display post images
- Add comments to posts
- Save posts to a **Read Later** list
- Remove posts from **Read Later**
- View saved posts on a separate page

---

## 🛠 Built With

- Python 3
- Django 6.0.1
- SQLite (development database)
- HTML & CSS

---

## 📁 Project Structure

BlogProject/
├── BlogPost/                # Main blog app
│   ├── migrations/          # Database migrations
│   ├── templates/BlogPost/  # HTML templates
│   │   ├── all-posts.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── post-detail.html
│   │   └── stored-posts.html
│   ├── admin.py
│   ├── forms.py             # Comment form
│   ├── models.py            # Post & Comment models
│   ├── urls.py              # App URLs
│   └── views.py             # Views for posts & read later
├── BlogProject/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                   # Uploaded images
├── db.sqlite3               # Database
├── manage.py
└── requirements.txt


🛠 Tech Stack
- Python 3
- Django
- HTML & CSS
- Django Template Language