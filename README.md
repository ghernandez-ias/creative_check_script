## Installation
1. Clone the github repo
2. Once you have the files you cloned from github, go to the .env file.
3. On the empty fb_app_secret variable, paste your facebook app secret key without leaving spaces and without quotes.
4. Finally, on the snowflake_user variable, paste you ias email without leaving spaces and without quotes.
5. In case you don't see the .env file, go to finder and press at the same time Shift + Command + .

## Execution
1. On Finder, go to the folder you cloned from github.
2. Go to dist folder, then go to run and look for the "run" file.
3. Double click the run file and wait until it executes.
4. In case the script asks for a token go to the Facebook api explorer, get a new one and paste it on the terminal
    ```sh
    https://developers.facebook.com/tools/explorer/
    ```
5. Enter your IDs comma or line break separated.
6. To stop typing IDs double click the enter button.
7. To check the responses, you will have a json file for every ID you entered in the path where you cloned the repo.
8. In case you want to re-execute the script, repeat step 3.

