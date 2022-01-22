# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

def main():
    # TODO: Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,        # sets logging to output all messages, Debug is lowest level
    filename="output.log",                          # outputs logs to file
    filemode="w")                                   # writing only mode

    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")  # program may be unable to run with critical error

    # TODO: Output formatted strings to the log
    logging.info("Here's a {} variable and an int:".format("string",10))


if __name__ == "__main__":
    main()
