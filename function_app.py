import azure.functions as func
import datetime
import time
import requests
import logging

from datetime import datetime, timezone

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *",  # a cada 1 minuto
                   arg_name="myTimer",
                   run_on_startup=True,
                   use_monitor=False)

def send_timestamp(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    for _ in range(6):  # 6 * 10s = 60s
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y%m%d%H%M%S")
        logging.info(f"Generated timestamp: {timestamp}")

        url = "https://webhook.site/27db4270-e7cf-4d82-962a-6bd6308dd3c9"  # <-- coloca aqui o URL real
        payload = {"timestamp": timestamp}

        try:
            logging.info(f"Sending request to: {url}")
            response = requests.post(url, json=payload)
            logging.info(f"Sent to Actions. Status: {response.status_code}")
        except Exception as e:
            logging.error(f"Error sending to Actions: {e}")

        time.sleep(10)
