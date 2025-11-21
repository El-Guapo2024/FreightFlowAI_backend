import time

def run_worker():
    """
    Placeholder for a background worker process.
    In the future, could listen to redis queue (celery/RQ)
    to process OCR tasks async
    """

    print("Worker process started")

    while True:
        print("Worker heartbeat: waiting for tasks...")
        time.sleep(10) # simulate doing work/waiting

        