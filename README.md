# Online Bookstore

An online bookstore project built with Django, providing functionalities for book management, user authentication, and more.

## Table of Contents

- [About the Project](#about-the-project)
  - [Features](#features)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Creating Superuser](#creating-superuser)
  - [Setting Up Razorpay](#setting-up-razorpay)
- [Usage](#usage)
  - [Separate HTML for Admin](#separate-html-for-admin)


## About the Project

The Online Bookstore is a web application built with Django, offering features such as book management, user authentication, cart functionality, order processing, wishlists, and Razorpay payment integration.

### Features

- Admin dashboard for book and user management
- User authentication and profile management
- Browse books by category
- Add books to the cart and wishlist
- View and manage the shopping cart
- Place orders and view order history
- Request books
- Razorpay payment integration

### Built With

- Django
- HTML, CSS, JavaScript
- Bootstrap
- Razorpay

## Getting Started

To run the project locally, follow the instructions below.

### Prerequisites

Make sure you have the following installed:

- Python
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/online-bookstore.git

   cd online-bookstore
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   
### Creating-superuser
  python manage.py createsuperuser

### Setting Up Razorpay
Sign up on the  [Razorpay website](https://razorpay.com/) and create an account.

Find your API key and secret in the Razorpay Dashboard.

Add the Razorpay API key and secret to your Django settings in settings.py:

RAZORPAY_API_KEY = 'your_razorpay_api_key'


### Usage
Visit http://localhost:8000/ in your web browser to access the application. Explore the various features provided by the online bookstore, including the Razorpay payment option.

### Separate HTML for Admin
The admin side has its own set of HTML templates, providing a dedicated and customized interface for managing books and users. The HTML templates for the admin can be found in the admin_templates directory.
