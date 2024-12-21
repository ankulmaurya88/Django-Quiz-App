# Django Quiz App

This is a web-based quiz application built with Django. It allows users to take quizzes, answer questions, view their scores, and explore various quizzes available on the platform.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)


## Features

- **Quiz List**: Displays all available quizzes.
- **Quiz Details**: Shows questions for a selected quiz.
- **Quiz Submission**: Users can submit answers and get their score.
- **Dynamic Questions**: Questions are fetched dynamically from the database.
- **Result Display**: Displays the score after submitting the quiz.
  
## Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS (for UI styling)
- **Database**: SQLite (default in Django for development)
- **Version Control**: Git
- **Others**: Python 3, Django 4+

## Installation

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.10
- pip (Python package installer)

### Steps to Install

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ankulmaurya88/Django-Quiz-App.git
   cd Django-Quiz-App  ```
---
   ```
   pip install -r requirements.txt
   ```
---
```
sudo apt install sqlite3
```
---
```
python manage.py makemigrations
python manage.py migrate
python manage.py dbshell
 
```
---
```
INSERT INTO quiz_question (id, question_text, option_a, option_b, option_c, option_d, correct_option)
VALUES 
(1, 'What is the capital of India?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'A'),
(2, 'Who is known as the Father of the Indian Nation?', 'Subhash Chandra Bose', 'Mahatma Gandhi', 'Jawaharlal Nehru', 'Dr. B.R. Ambedkar', 'B'),
(3, 'Which is the longest river in India?', 'Ganga', 'Brahmaputra', 'Yamuna', 'Godavari', 'A'),
(4, 'Which Indian city is known as the Silicon Valley of India?', 'Mumbai', 'Hyderabad', 'Bangalore', 'Pune', 'C'),
(5, 'What is the national animal of India?', 'Tiger', 'Peacock', 'Lion', 'Elephant', 'A');
```
---
```
python manage.py runserver

```
---

