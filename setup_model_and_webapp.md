# Setup venv
- `py -m venv venv`
- `venv\Scripts\activate`

# Create .flaskenv
    FLASK_ENV=development
    FLASK_APP=main.py

# create application (already done?)
- create `main.py`
- create folder `application`
- create file `__init__.py` in application folder. contains jupyter notebook code. Copy from https://github.com/LinkedInLearning/dsm-bank-model-2870047/blob/main/application/__init__.py

- modify routes.py
- modify templates/index.html

# install requirements
- `pip install gunicorn`
- `pip install python-dotenv`
- `pip install flask`

- create Procfile
    `web: gunicorn application:app`

- create requirements.txt
    `pip freeze >requirements.txt`

# LOCAL DEPLOYMENT  
- `set FLASK_APP=main.py`
- `flask run --port 8082`
- on browers: `http://127.0.0.1:8082`

# HEROKU DEPLOYMENT
- heroku login (use andre email)
- see apps: heroku apps
- see info: heroku info --app climate-change-app-server
- see logs: heroku logs --tail --app climate-change-app-server
- See deployment: https://climate-change-app-server-6c4cbb1cf04f.herokuapp.com/