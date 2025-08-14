from setuptools import setup, find_packages

setup(
    name="quiz_project",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django==4.2.2",
        "pymysql",
        "psycopg2>=2.9,<3.0",
        "gunicorn>=20.1,<21.0",
        "django-environ>=0.9,<1.0",
        "djangorestframework>=3.12,<4.0",
        "celery>=5.0,<6.0",
        "python-dotenv>=0.19,<1.0",
        "django-cors-headers>=3.7,<4.0"
    ],
)
