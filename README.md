##### e_com_system
## Product and Category Management API

This repository contains a Django REST API for managing products and categories. The API allows authenticated users to create, read, update, and delete product and category records, with prices encrypted for security.

### Features

- User authentication using JWT
- CRUD operations for products and categories
- Price encryption using the `cryptography` library
- Pagination for product listing
- Custom exception handling

### Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Cryptography
- JWT Authentication

### Installation

1. Clone the repository:
  
    ```
    git clone https://github.com/varshamohan08/e_com_system.git
    cd e_com_system
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

4. Set up your PostgreSQL database and configure the settings in settings.py.
    Apply migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```

6. Run the server:
    ```
    python manage.py runserver
    ```

### API Endpoints
Listed in [api_endpoints.md](https://github.com/varshamohan08/e_com_system/blob/main/api_endpoints.md) inside project folder.
