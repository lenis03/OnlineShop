# OnlineShop

## Introduction
This Django project serves as an online shop featuring bilingual support, user authentication, product management, cart functionality, order processing, and payment integration using ZarinPal.

## Features
- **User Authentication:** Implemented with Django Allauth for user registration, login, and account management.
- **Bilingual Support:** Utilizes Django's i18n and l10n for bilingual (Persian and English) functionality.
- **Product Management:** Includes product listing, detailed views, and search capability.
- **Cart Management:** Enables users to add/remove products from the cart and proceed to checkout.
- **Order Management:** Facilitates seamless order placement with a streamlined checkout process.
- **Payment Integration:** Integrated ZarinPal API ensures secure payment processing in both live and sandbox environments.

## Requirements
- Python 3.9
- Django 3.x
- PostgreSQL 14
- Docker and Docker Compose (for containerized deployment)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lenis03/OnlineShop.git
   cd OnlineShop
2.Install dependencies:
```bash
pip install -r requirements.txt
```
3.Set up environment variables:
Create a .env file in the root directory and define the following variables:
```makefile
DJANGO_SECRET_KEY=your_django_secret_key
DJANGO_DEBUG=True
DJANGO_ZARINPAL_MERCHANT_ID=your_zarinpal_merchant_id
```
4.Apply database migrations:
```bash
python manage.py migrate
```
5.Run the development server:
```bash
python manage.py runserver
```
6.Access the application at http://localhost:8000.
## Docker Deployment
For containerized deployment, use the provided Dockerfile and Docker Compose configuration (docker-compose.yml):
```
```bash
docker-compose up --build
```

## Usage
Admin Panel: Manage products, orders, and users at http://localhost:8000/admin/.
Customer Views: Access product listings (/), cart management (/cart/), and order processing (/order/).
Additional Notes
Customize frontend templates and styles to meet project requirements.
Ensure PostgreSQL is properly configured for production deployments.
Securely manage environment variables, especially sensitive information such as API keys and merchant IDs.
Credits
Developed by FardinTorkamand. Built with Python and Django.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to utilize this updated content for your project! Let me know if you require further assistance. 😊
