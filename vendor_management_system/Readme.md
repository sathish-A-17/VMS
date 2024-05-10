Vendor Management System
This is a vendor management system built using Django and Django REST Framework. It provides an interface to manage vendors, purchase orders, and historical performance data. Users can perform CRUD operations on these models using the web interface created with Bootstrap for a responsive design.

Features
Vendor Management: Add, edit, view, and delete vendor details, including contact information and performance metrics.
Purchase Order Management: Add, edit, view, and delete purchase orders, including acknowledgment and quality rating.
Historical Performance Tracking: Record and track historical performance data for vendors, including on-time delivery rate, quality rating, and other metrics.
Dashboard: View a summary of vendors, purchase orders, and historical performance data on a central dashboard.
Technologies Used
Django: Web framework for building web applications.
Django REST Framework: Framework for building RESTful APIs in Django.
Bootstrap: CSS framework for responsive design.
SQLite: Default database used by Django (you may choose to use another database for production).

Installation
Clone the repository:
git clone <repository_url>

Navigate to the project directory:
cd project/

Create a virtual environment (optional but recommended):
python3 -m venv venv

Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Create a superuser (optional, but recommended for access to the Django admin panel):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

The application should now be running locally at http://127.0.0.1:8000/.

Usage
Vendors: Navigate to /vendors/ to manage vendors.
Purchase Orders: Navigate to /purchase_orders/ to manage purchase orders.
Historical Performance: Navigate to /historical_performance/ to manage historical performance data.
API: The API is available at /api/.
You can also access the Django admin panel at /admin/ using the superuser credentials you created.

Future Improvements
Add authentication and permissions to secure access to the application.
Improve error handling and validation.
Implement additional performance optimization as needed.


Acknowledgments
Thanks to the Django and Django REST Framework communities for their amazing frameworks.
Special thanks to Bootstrap for providing a responsive design foundation.
