# Box Selection System

## Overview

The Box Selection System is a Django-based web application developed as part of a Python/Django hiring assignment.

The system simulates an e-commerce warehouse workflow where, after a customer places an order, the application automatically recommends the most suitable shipping box based on:

* Product dimensions
* Product weight
* Quantity ordered
* Available shipping boxes
* Shipping box cost

The recommendation engine selects the **lowest-cost box** that satisfies both the weight and volume requirements of the order.

---

# Features

* Product Management
* Automatic Order Creation
* Quantity Support
* Shipping Box Recommendation
* Cost Optimization
* Django REST Framework APIs
* Bootstrap-based User Interface
* Automated Unit Tests
* Default Shipping Box Seeder

---

# Tech Stack

| Technology            | Purpose          |
| --------------------- | ---------------- |
| Python                | Backend Language |
| Django                | Web Framework    |
| Django REST Framework | REST APIs        |
| SQLite                | Database         |
| Bootstrap 5           | User Interface   |

---

# Project Structure

```text
box_selector/
│
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
│
├── box_selector/
│
└── shipping/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── forms.py
    ├── urls.py
    ├── tests.py
    │
    ├── services/
    │   └── box_selector.py
    │
    ├── management/
    │   └── commands/
    │       └── seed_boxes.py
    │
    └── templates/
        └── shipping/
            └── home.html
```

---

# Database Models

## Product

Stores product information.

Attributes:

* Name
* Length (cm)
* Width (cm)
* Height (cm)
* Weight (kg)

---

## Box

Stores available shipping boxes.

Attributes:

* Name
* Length (cm)
* Width (cm)
* Height (cm)
* Maximum Weight (kg)
* Cost

---

## Order

Represents a customer order.
Automatically created when a product is submitted through the web interface.

---

## OrderItem

Connects products with orders.

Stores:

* Product
* Quantity

---

# Recommendation Algorithm

The recommendation engine follows these steps:

1. Calculate total order weight.

```
Total Weight = Product Weight × Quantity
```

2. Calculate total order volume.

```
Total Volume = (Length × Width × Height) × Quantity
```

3. Retrieve all available shipping boxes.

4. Filter boxes that satisfy:

* Weight Capacity
* Volume Capacity

5. If multiple boxes are eligible:

* Select the box with the lowest shipping cost.
* If costs are equal, choose the smaller box.

6. Return the recommended shipping box.

---

# Application Workflow

```
User enters product details
            │
            ▼
Product is saved
            │
            ▼
Order is created automatically
            │
            ▼
OrderItem is created with selected quantity
            │
            ▼
Recommendation engine evaluates boxes
            │
            ▼
Best shipping box is displayed
```

---

# API Endpoints

| Method     | Endpoint            | Description            |
| ---------- | ------------------- | ---------------------- |
| GET / POST | /api/products/      | Manage Products        |
| GET / POST | /api/boxes/         | Manage Boxes           |
| GET / POST | /api/orders/        | Manage Orders          |
| POST       | /api/recommend-box/ | Get Box Recommendation |

---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>
cd box_selector
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Seed Default Shipping Boxes

```bash
python manage.py seed_boxes
```

This command inserts predefined shipping boxes used by the recommendation engine.

---

## Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# Running Tests

Execute:

```bash
python manage.py test
```

Current Test Coverage:

* Cheapest eligible box selected
* No suitable box available
* Weight limit exceeded
* Equal-cost tie-breaking

---

# Business Assumptions

* Products are rectangular.
* All dimensions are entered in centimeters.
* Weight is entered in kilograms.
* Only one product type is added per order through the web interface.
* Quantity determines the total weight and volume.
* Shipping cost is associated with each box.
* The cheapest valid shipping box is always preferred.

---

# Future Improvements

Potential enhancements include:

* Multiple products in a single order
* Dimension-based fit validation (not just volume)
* Product catalog with searchable inventory
* Warehouse stock management
* Shipping carrier integration
* Packing optimization for multiple box selection
* User authentication and order history

---

# AI Usage

Artificial Intelligence was used as a development assistant during this project for:

* Requirement clarification
* Django best practices
* Code review
* Debugging
* Unit testing suggestions
* Documentation improvements

All business logic, project structure, testing, and validation were manually reviewed and verified before inclusion.

---

# Author
Viraj Patel
