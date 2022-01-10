# import json
import json
import logging
import base64
import azure.functions as func

def main(msg: func.QueueMessage) -> None:

    message = msg.get_body()

    #Get message body
    message_to_proccess = base64.b64decode(message)
    new_message_to_proccess = str(message_to_proccess)
    m2 = new_message_to_proccess.replace("b","")
    m3 = m2.replace('"',"")
    v1 = data = json.loads(m2)
    logging.info(message_to_proccess)
    logging.info(m2)
    logging.info(m3)
    logging.info(f'Data data type is: {type(data)}')
    logging.info(f'Data v1 type is: {type(v1)}')
    logging.info(f'Data m3 type is: {type(m3)}')
