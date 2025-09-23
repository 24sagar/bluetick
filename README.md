# Bluetick

A Django-based website for **Bluetick Software Private Limited**, designed to showcase company information, services, and contact details.  
This project demonstrates a simple but scalable Django application with multiple apps, templates, and static file handling.

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Project Structure](#project-structure)  
5. [Getting Started](#getting-started)  
6. [Configuration](#configuration)  
7. [Usage](#usage)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact](#contact)

---

## 📖 Project Overview

Bluetick is a company portfolio website developed using **Django**.  
It includes pages like **About Us**, **Services**, and **Contact**, making it useful for organizations to present their details and allow users to connect with them.

The project is structured with multiple Django apps, each handling a specific section of the website.

---

## ✨ Features

- Informational pages (*About Us, Services, Contact*)  
- Django templating system with reusable templates  
- Static file and media file management  
- Organized Django apps for modularity  
- Basic database integration with **SQLite**  
- Clean frontend using HTML, CSS/SCSS  

---

## 🛠 Tech Stack

- **Backend**: Python (Django Framework)  
- **Frontend**: HTML, CSS, SCSS, JavaScript  
- **Database**: SQLite (development)  
- **Other Tools**: Django ORM, Django Admin, Virtual Environment  

---

## 📂 Project Structure

bluetick/
│── aboutus/ # About Us app
│── contact/ # Contact app
│── services/ # Services app
│── media/ # Media files (images, uploads)
│── static/ # Static assets (CSS, JS, SCSS)
│── templates/ # HTML templates
│── db.sqlite3 # Development database
│── manage.py # Django management script
│── requirements.txt # Python dependencies



---

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/24sagar/bluetick.git
cd bluetick
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Apply migrations
bash
Copy code
python manage.py migrate
5. Run the server
bash
Copy code
python manage.py runserver
6. Open in browser
Visit: http://127.0.0.1:8000/

⚙️ Configuration
Update settings.py:

DEBUG, ALLOWED_HOSTS for production

DATABASES if switching from SQLite to PostgreSQL/MySQL

STATIC_URL and MEDIA_URL for deployment

Use environment variables for sensitive data (SECRET_KEY, DB credentials).

💻 Usage
Navigate to the About Us page to learn about the company

Explore Services to check offerings

Use the Contact page for inquiries

Admins can manage content through the Django Admin Panel

🤝 Contributing
Contributions are welcome!

Fork this repository

Create a new branch: git checkout -b feature-name

Commit changes: git commit -m "Added new feature"

Push to branch: git push origin feature-name

Open a Pull Request

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
