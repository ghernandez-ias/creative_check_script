## Installation
1. Clone the github repo
2. Once you have the files you cloned from github, go to the .env file.
3. On the empty fb_app_secret variable, paste your facebook app secret key without leaving spaces and without quotes.
4. Finally, on the snowflake_user variable, paste you ias email without leaving spaces and without quotes.

## Execution
1. On Finder, go to the folder you cloned from github
2. Right click over the folder, go down to services and click on the "New terminal at folder" option.
3. Once you opened the terminal paste the following on it:
    ```
    ./executable.sh
    ```
4. If you get a permission denied error, execute this(you will only need to do this once):
    ```
    chmod +x executable.sh
    ```
5. In case the script asks for a token go to the Facebook api explorer, get a new one and paste it on the terminal
    ```sh
    https://developers.facebook.com/tools/explorer/
    ```
6. Enter your IDs comma or line break separated
7. To stop typing IDs double click the enter button.
8. To check the responses, you will have a json file for every ID you entered in the path where you cloned the repo.
9. In case you want to re-execute the script, repeat step 3.

