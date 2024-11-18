## About
### Problem
#### `rabota.by` (it's another domain of `hh.ru`) gives an opportunity to up your resumes once every 4 hours.
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
## How to
**WARNING: You need to fill the `.env` file: uncomment and set required env variables with value `NEED TO SET`.**
- Values of variables `COOKIES_HHTOKEN`, `COOKIES_HHUID`, `COOKIES_XSRF` are set in cookies after log in. 
Example for Google Chrome:`Dev tools -> Application -> Cookies -> https://rabota.by -> type "rabota.by" in the filter -> find hhtoken, hhuid, _xsrf` 
- ### Run locally
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install dependencies (it is recommended to use it in a virtual environment) from the `requirements.local.txt` file:
    ```shell
    pip install -r requirements.local.txt
    ```
3. Run:
   ```shell
   python .
   ```
   or if you are into a parent directory:
   ```shell
   python auto-up-resume
   ```
### Production run (Docker)
#### NOTE: This method runs the app in CRON. CRON expression is declared in the Dockerfile; now it's 51 * * * * (every hour in 51 minutes).
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install docker.
3. Build a docker image:
   ```shell
   docker build . --tag=auto-up-resume
   ```
4. Run a docker container:
   ```shell
   docker run --name auto-up-resume auto-up-resume
   ```
## TODO
- #### docker compose
- #### Telegram bot to run remotely