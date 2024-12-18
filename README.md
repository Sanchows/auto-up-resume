## About
### What is the problem?
#### `rabota.by` (it's another domain of `hh.ru`) gives an opportunity to up your resumes once every 4 hours. To do this, go to the website (or mobile application) and click the appropriate button. It is inconvenient and takes a lot of time.
### Solving
#### This app just up all your resumes automatically.
### Instruments
- #### Python 3.12.2
- #### Type annotations
- #### Settings. Flexible app settings
- #### Logging. Colorized stdout logging (different colors for each level)
- #### Error logging. All exceptions will be sent to Telegram user
- #### Docker
- #### CRON
## How to use
**WARNING: You need to fill the `.env` file: uncomment and set required env variables with value `NEED TO SET`.**
- There are 2 ways to auth:
  1) Throughout the cookies (you need to fill `COOKIES_HHTOKEN`, `COOKIES_HHUID`, `COOKIES_XSRF`)
  2) Throughout the login/password (you need to fill `USERNAME`, `PASSWORD`)
- Values of variables `COOKIES_HHTOKEN`, `COOKIES_HHUID`, `COOKIES_XSRF` are set in cookies after log in. 
Example for Google Chrome:`Dev tools -> Application -> Cookies -> https://rabota.by -> type "rabota.by" in the filter -> find hhtoken, hhuid, _xsrf`
- If you'll fill `USERNAME`, `PASSWORD` variables, `COOKIES_HHTOKEN`, `COOKIES_HHUID`, `COOKIES_XSRF` variables are not required
- `USERNAME` - is an email or a phone number of your account, `PASSWORD` - password of your account. 
- ### Run locally
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install dependencies (it is recommended to use it in a virtual environment) from the `requirements.txt` file:
    ```shell
    pip install -r requirements.txt
    ```
    _***If you want to load environment variables from file automatically you may install python-dotenv:**_
    ```shell
    pip install python-dotenv
    ```
3. Run:
   ```shell
   python .
   ```
   or if you are into a parent directory:
   ```shell
   python auto-up-resume
   ```
- ### Run in the docker-compose
   #### NOTE: This method runs the app in CRON. CRON expression is declared in the Dockerfile; now it's 51 * * * * (every hour in 51 minutes).
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install docker and docker compose.
3. Run:
   ```shell
   docker compose up
   ```
## TODO
- #### Telegram bot to run remotely
