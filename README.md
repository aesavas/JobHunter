![Showcase](./Resources/images/JobHunter.png)

JobHunter is a web app that organizes your job search. Also, you can store your resumes on this platform. JobHunter developed with Django.

> If you want to see small showcase you can watch the video from this [link](https://www.youtube.com/watch?v=-R_1qSQOH-4)

### 🎯 Features

- Create - Update Profile
- Add - Update - Delete Job Post
- Add - Update - Delete Resume
- Add - Delete Skills
- Simple Dashboard
- Show Stats
- Forgetten Password (Reset Password)


## 🚀 Installation

To install the application you need to run these commands.
```bash
  git clone https://github.com/aesavas/JobHunter.git
  cd JobHunter
  python -m venv env
  ===================================================
  -- For Linux --
  source env/Scripts/activate
  -- For Windows --
  .\env\Scripts\activate
  ===================================================
  pip install -r requirements.txt
```


## 🛠 Environment Variables

- After install part, you need to configure your .env file. I share example of .env file as a .env.example
- .env file must be in same folder with settings.py
- You need to create random key for application. There are two way to create key.
    - First way : [Djecrety](https://djecrety.ir/)
    - Second way : You need to run on terminal

    ```bash
    python manage.py shell
    ```
    After that, you can create key with this command and paste to .env file.
    ```python
    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()
    ```

- .env Example:
```
SECRET_KEY=your_secret_key
DEBUG=1 or 0
EMAIL_HOST=your_host
EMAIL_PORT=your_port
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_username
EMAIL_HOST_PASSWORD=your_password
```

## Usage

```bash
python manage.py runserver
```

After run the server, please open the browser and visit http://127.0.0.1:8000

Create a profile and login.

## 📫 Feedback

If you have any feedback, I will be very happy to hear them. Please reach me from contact@aliemresavas.com

