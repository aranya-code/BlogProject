# 📝 Django BlogProject

A simple blog application built using **Django**, created to understand how Django handles
**URLs, views, templates, static files, and dynamic routing using slugs**.

This project uses **dummy in-memory data** (no database models yet) and focuses on learning
core Django concepts correctly.

---

## 🚀 Features

- Home page
- List of all blog posts
- Individual post detail pages using **slug-based URLs**
- Navigation bar shared across pages
- Template inheritance using `base.html`
- Static images loaded using `{% static %}`
- Clean and readable project structure

---

## 🧩 Project Structure

BlogProject/
│
├── BlogPost/ # Main Django app
│ ├── templates/BlogPost/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── all-posts.html
│ │ └── post-detail.html
│ ├── views.py
│ ├── urls.py
│ └── ...
│
├── BlogProject/ # Project configuration
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── static/
│ └── BlogPost/
│ ├── mountain.jpg
│ ├── coding.jpg
│ └── woods.jpg
│
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md



---

## 🛠 Tech Stack

- **Python 3**
- **Django**
- HTML & CSS
- Django Template Language

---


