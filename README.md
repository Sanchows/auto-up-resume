### How to
#### Run locally
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install dependencies (it is recommended to use it in a virtual environment) from the `requirements.local.txt` file:
    ```shell
    pip install -r requirements.local.txt
    ```
3. Open `.env` file. Uncomment and set env variables with value `NEED TO SET`
4. Run:
   ```shell
   python .
   ```
   or if you are into a parent directory:
   ```shell
   python auto-up-resume
   ```
#### Production run (Docker)
1. Clone the repository and follow to the folder:
    ```shell
    git clone https://github.com/Sanchows/auto-up-resume.git
    cd auto-up-resume
    ```
2. Install docker.
3. Open `.env` file. Uncomment and set env variables with value `NEED TO SET`
4. Build a docker image:
   ```shell
   docker build . --tag=auto-up-resume
   ```
5. Run a docker container:
   ```shell
   docker run --name auto-up-resume auto-up-resume
   ```
