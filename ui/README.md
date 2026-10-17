# UI 

The UI will provide a simple and user-friendly interface for interacting with the application.

# Tech Stack

## Frontend

- Vue.js 3 + TypeScript
- Vite (Build Tool)
- Pinia (State Management)
- Element Plus (Component Library)
- Tailwind CSS (Styling)
- TanStack Table (Data Tables)

## Backend

- FastAPI + Uvicorn + Python
- SQLAlchemy + Asyncpg (Database)
- Pydantic (Validation)
- Alembic (Migrations)
- JWT Authentication

## Infrastructure

- Docker + Docker Compose
- GitHub Actions (CI/CD)
- PostgreSQL 16

# UI Overview

## 1. Login Page

- URL: `/`
- Features:
  - Username and password fields
  - Login button
  - Validation messages
- Keyboard shortcuts:
  - Enter: Submit form
  - Esc: Close dialogs

## 2. Home Dashboard

- URL: `/dashboard`
- Features:
  - Welcome message
  - Quick navigation buttons
  - System status indicators

## 3. User Management Page

- URL: `/users`
- Features:
  - Table of all users
  - User details
  - Add/edit/delete operations

## 4. Authentication Pages

- Register: `/register`
- Password Reset: `/reset-password`
- Change Password: `/change-password`
