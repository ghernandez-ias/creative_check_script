import os
import json
import logging
import requests
import tools.logger as lg
from dotenv import set_key
from facebook.facebook import *
from snowflake_conn.snowflake import SnowflakeConn

def get_ids_user():
    logger = lg.logger(logging.DEBUG)
    inputs = []
    logger.info('Please enter your IDs:')
    while True:
        user_input = input()
        if ',' in user_input:
            sep_inputs = user_input.split(',')
            inputs = inputs + sep_inputs
        else:
            inputs.append(user_input)

        if user_input == "":
            break
    
    #Removing empty and whitespace strings from the list
    inputs = list(filter(str.strip, inputs))
    return inputs

def append_to_json(response,id):
    with open(f'{id}_response.json', 'a') as f:
        f.write('\n')
        json.dump(response,f)

def execute_process():
    logger = lg.logger(logging.DEBUG)
    snowflake_connection = SnowflakeConn()
    cursor = snowflake_connection.start_connection()
    token = os.getenv('fb_60_days_token')

    inputs = get_ids_user()
    if inputs:
        logger.info('Processing ids...')
        for input in inputs:
            logger.info(f'Processing id: {input}')

            query_string = f"""SELECT EXT_MAPPING_ID FROM {os.getenv('snowflake_table')} WHERE EXT_CAMPAIGN_ID in ({input});"""
    
            results = snowflake_connection._execute_query(query_string)
            if results:
                for id in results:
                    try:
                        step_1 = requests.get(f'https://graph.facebook.com/v15.0/{id[0]}?fields=creative&access_token={token}')
                        tmp_json = step_1.json()
                        creative_id = tmp_json['creative']['id']

                        step_2 = requests.get(f'https://graph.facebook.com/v15.0/{creative_id}?fields=asset_feed_spec{{optimization_type}}&access_token={token}')
                        append_to_json(step_2.json(), input)
                    except:
                        raise Exception('Please verify your token')
        logger.info(f'Id: {input} processed, please check the json file with the responses' )
    else:
        logger.info('No ids provided')

if __name__ == "__main__":
    logger = lg.logger(logging.DEBUG)

    is_valid = check_long_token()
    if is_valid:
        execute_process()
    else:
        logger.error('Long life token has expired, please enter a new token:')
        while is_valid == False:
            received_token = input()
            fb_60_days_token = get_60_days_token(received_token)

            set_key(".env", "fb_60_days_token", fb_60_days_token)
            os.environ["fb_60_days_token"] = fb_60_days_token
            is_valid = check_long_token()
            if is_valid == False:
                logger.error('Unvalid token, please verify that it has not expired:')
        if is_valid:
            execute_process()







    