# Inventory Management System

A simple and efficient inventory management web application built with Flask. It allows administrators to manage product records, track stock information, and handle login and authentication securely.

## Project Overview

This project is designed to help businesses and stores keep track of their inventory in one place. The application provides a web interface for managing product data such as product details, categories, and related records while ensuring that only authenticated admins can access the management features.

## Features

- Admin sign up and login
- Secure session-based authentication
- Product listing and searching
- Product lookup by ID and type
- Add new products
- Update existing product details
- Delete product entries
- Clean Flask blueprint-based architecture

## Tech Stack

- Python
- Flask
- Jinja2
- SQLite database
- HTML, CSS, JavaScript

## Project Structure

- `app/` – main Flask application setup and templates
- `routes/` – API and page routes for admin and product management
- `controllers/` – business logic for admin and product operations
- `services/` – service-layer logic for application features
- `db/` – database-related files
- `middelwares/` – authentication and request guarding
- `main.py` – application entry point

## Getting Started

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

5. Open the app in your browser at:

```text
http://localhost:5000
```

## License

This project is open for educational and personal use.
