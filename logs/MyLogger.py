import logging

logging.basicConfig(
    filename='.\logs\\flaskapp.log',
    filemode = "w",
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)