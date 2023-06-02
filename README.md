# CualiVy-BE

**Make sure python already installed on your computer.**

**Install required libraries**

```pip install mysql-connector-python```

**Activate Virtual Env**

You can activate virtual env either using

- ```env\Scripts\activate``` (for windows) or using
- ```source env/bin/activate``` (for macOS or Linux)

**Run the application**

You can run the app by

- ```python app.py```
  and CTRL + C to stop it

**Endpoints**

You can access the app on

- **GET** http://127.0.0.1:5000 (for checking)
- **GET SAMPLE 10 Jobs** http://127.0.0.1:5000/jobs
- **POST Search Jobs <http://127.0.0.1:5000/searchjobs>**
  - Body ```x-www-form-urlencoded```
    - image => {base64image}
