## Installation
1. Clone the github repo, preferably in your Downloads folder
2. Download docker desktop from:
    ```sh
    https://www.docker.com 
    ```
    depending on your system.
3. Download the image from
    ```sh
    https://drive.google.com/file/d/1At67kQ8Ns3zCRGGoyn9QlZuvJBRDnqyL/view?usp=sharing
    ```
4. Open a terminal
5. Go to the downloads folder using(if you saved the image in Downloads):
    ```sh
    cd Downloads
    ```    
6. Execute the following in the same path where you saved the image:
    ```sh
    docker load -i creative_script_image.tar
    ```  

## Execution
1. On a terminal execute:
    ```
    docker run -iv /Users/your_user/Downloads/creative_check_script:/app/ dockerfile
    ``` 
2. The script will ask you for your facebook app secret and snowflake user(okta email)
3. If the script asks you for a token, please go to:
    ``` 
    https://developers.facebook.com/tools/explorer/
    ``` 
4. The json files with the responses will be saved on the folder of the github repo you cloned.
5. If you want to re-execute the script, just repeat execution-step 1.


