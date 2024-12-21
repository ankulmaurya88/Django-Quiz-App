step to run----

pip install -r requirements.txt
sudo apt install sqlite3


python manage.py makemigrations
python manage.py migrate
python manage.py dbshell


INSERT INTO quiz_question (id, question_text, option_a, option_b, option_c, option_d, correct_option)
VALUES 
(1, 'What is the capital of India?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'A'),
(2, 'Who is known as the Father of the Indian Nation?', 'Subhash Chandra Bose', 'Mahatma Gandhi', 'Jawaharlal Nehru', 'Dr. B.R. Ambedkar', 'B'),
(3, 'Which is the longest river in India?', 'Ganga', 'Brahmaputra', 'Yamuna', 'Godavari', 'A'),
(4, 'Which Indian city is known as the Silicon Valley of India?', 'Mumbai', 'Hyderabad', 'Bangalore', 'Pune', 'C'),
(5, 'What is the national animal of India?', 'Tiger', 'Peacock', 'Lion', 'Elephant', 'A');

python manage.py runserver