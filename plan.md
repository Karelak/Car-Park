# Car Park Management System Plan

## System Overview

A PyQt5-based application to manage and monitor car parking permits for a college, allowing staff to track valid permits, visitors, and manage permit data.

## Core Requirements

### Functionality

1. Search parking permits
2. View all cars with valid permits
3. View daily visitors
4. View expired permits
5. Read-only access for basic users

### Extension Features

1. Add new permits (students/staff)
2. Look up individual permits
3. Edit car details
4. Generate printable/emailable permits

## Technical Implementation

### Database Design

1. Tables needed:

   - Permits (id, permit_number, issue_date, expiry_date, status)
   - Vehicles (id, registration, make, model, color)
   - People (id, name, type[student/staff], contact_info)
   - Visitors (id, vehicle_id, visit_date, purpose)

   - Permit list view
   - Visitor list view
   - Status indicators
   - Filter options

### Technology Stack

- Frontend: PyQt5
- Database: SQLite
- Additional libraries:
  - reportlab (for permit generation)
  - smtplib (for email functionality)

## Implementation Phases

### Phase 1: Core Setup

1. Set up project structure
2. Create database schema
3. Implement basic UI layout

### Phase 2: Basic Functionality

1. Implement database connections
2. Create search functionality
3. Display permit data
4. Show visitor information

### Phase 3: Extensions

1. Add permit management features
2. Implement editing capabilities
3. Create permit generation system
4. Add email functionality

## UI Design Notes

- Color scheme: Collyers colors
- High contrast for readability
- Clear separation of functions
- Intuitive navigation
- Input validation for all forms

## Security Considerations

- Read-only access for basic users
- Input sanitization
- Data validation
- User authentication system

### UI Components

1. Main window with:
   - Search functionality
