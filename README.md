# Job Portal — Django Web Application

A full-stack job portal built with Django, featuring role-based authentication, job posting, live search, and an application tracking system with status pipeline management.

## Features

- **Role-based authentication** — separate signup/login flows for Job Seekers, Recruiters, and Admins
- **Recruiter dashboard** — post jobs, view applicants, and manage application status (Applied → Shortlisted → Rejected/Hired)
- **Job Seeker dashboard** — browse jobs, live search/filter (AJAX, no page reload), apply to jobs, and track application status
- **Duplicate-application prevention** — enforced at the database level using a unique constraint
- **Permission-based access control** — recruiters can only view/manage applicants for their own job postings
- **Clean, responsive UI** with custom CSS styling

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS, JavaScript (Fetch API / AJAX)
- **Other:** Django ORM, Django Admin, python-decouple for environment config

## Key Technical Highlights

- Relational database schema with 5 linked models (Profile, Recruiter, JobSeeker, Job, Application)
- Real-time job search implemented with vanilla JavaScript and Django's JsonResponse API
- Secure permission checks using Django's ORM relationship traversal (e.g. `job__recruiter=recruiter`)
- Environment-based configuration (secret key and debug settings kept out of version control)

## Setup Instructions

1. Clone the repository:
```bash
   git clone https://github.com/veerabhadrarao1221-png/job-portal-django.git
   cd job-portal-django
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the project root with:


5. Run migrations:
```bash
   python manage.py migrate
```

6. Create a superuser (for admin access):
```bash
   python manage.py createsuperuser
```

7. Run the development server:
```bash
   python manage.py runserver
```

8. Visit `http://127.0.0.1:8000/accounts/signup/` to create an account.

## Future Improvements

- AJAX-based job applications (currently uses standard form submission)
- Resume upload and parsing
- Email notifications on status changes
- Pagination for job listings
- Deployment with PostgreSQL

## Author

Veerabhadrarao