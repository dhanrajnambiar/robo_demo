To run the project follow steps.
1) Clone the git repo.
    "git clone https://github.com/dhanrajnambiar/robo_demo.git ."
2) For this have python3 and virtualenv in system.
    "python3 -m venv robo_env"
    "source robo_env/bin/activate"
    "pip3 install -r requirements.txt"
3) Change to directory
    "cd toy_robo"
4) Create DB schema and write to DB.This project uses simple sqlite db
    "python3 manage.py makemigrations"
    "python3 manage.py migrate"
4) Run the Django Server in defualt port 8000
    "python3 manage.py runserver"
5) Access the home page of project with link
    "127.0.0.1:8000/robo/home"
    Follow the instructions in the page.
