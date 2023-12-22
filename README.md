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
[   git clone https://github.com/your_username/online-bookstore.git](https://github.com/dipin736/Book-Store-Management-Django.git)

   cd online-bookstore
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   
### Creating-superuser
  python manage.py createsuperuser-for Admin

### Setting Up Razorpay
Sign up on the  [Razorpay website](https://razorpay.com/) and create an account.

Find your API key and secret in the Razorpay Dashboard.

Add the Razorpay API key and secret to your Django settings in settings.py:

RAZORPAY_API_KEY = 'your_razorpay_api_key'


### Usage
Visit http://localhost:8000/ in your web browser to access the application. Explore the various features provided by the online bookstore, including the Razorpay payment option.

### Separate HTML for Admin(Use Createsuperuser)
The admin side has its own set of HTML templates, providing a dedicated and customized interface for managing books and users. The HTML templates for the admin can be found in the admin_templates directory.

### Screenshot
1.Home Page
![Screenshot 2023-12-21 121603](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/1f07da8c-650e-4086-b0f0-ad0681255797)
2.About
![Screenshot 2023-12-21 121805](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/0d859711-18ec-45a4-88c4-6c863e5fa44d)
3.Contact
![Screenshot 2023-12-21 121825](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/49a44f83-019b-4071-a399-b2a985a25900)
4.Login Form
![Screenshot 2023-12-21 121625](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/8598d1db-3334-43a5-a3b8-d55f97dd96e4)
5.Registration Form
![Screenshot 2023-12-21 121652](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/2cf431cf-72ff-45eb-8220-7ac18d6c1389)
  ## Admin
  1.Admin View
  ![Screenshot 2023-12-21 121847](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/bc7c188b-0bf5-49ad-a2b2-5d92ad4a18b0)
  2.Category
  ![Screenshot 2023-12-21 122005](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/b43f5143-d36e-46ed-9a53-7f2a10772e4c)
  3.Product
  ![Screenshot 2023-12-21 122022](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/367b0b7c-b970-4678-abae-426088716d0f)
  4.Admin view order
  ![Screenshot 2023-12-21 122038](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/613df017-8b4c-4843-813f-29cb12238ec8)
  
  ## User
  1.User View
  ![Screenshot 2023-12-21 122332](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/23086c21-01d2-4b29-b422-de4c6066f4dd)
  2.View book details
  ![Screenshot 2023-12-21 122352](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/994f04e6-b14d-4f1d-a8fd-a4b64c8c81bd)
  3.Cart
  ![Screenshot 2023-12-21 122423](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/c38cc30f-ec6c-4177-8dfc-165ed9b9963c)
  4.Wishlist
  ![Screenshot 2023-12-21 122436](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/1d417f94-245b-43fe-a321-812c0203712c)Place order
  5.Place order
  ![Screenshot 2023-12-21 122549](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/5e8e9dde-61f8-4ae2-b666-bea4ba8593f4)
  6.Razor Pay
  ![Screenshot 2023-12-21 122605](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/09ee3b75-d39f-46a7-850d-a988d1acce64)
  7.User order
  ![Screenshot 2023-12-21 122452](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/73eb551c-6543-41be-8891-c30775c39761)
  8.Order view
  ![Screenshot 2023-12-21 122504](https://github.com/dipin736/Book-Store-Management-Django/assets/114206930/db61eec5-25a4-468b-9cdd-a91b0687c0ea)
  
