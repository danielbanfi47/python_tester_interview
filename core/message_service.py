import logging
import sys


class MessageManipulator:
    def __init__(self, message: str):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler("debug.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.message = message

    def text_lift(self, lift_point: int) -> str:
        """
        This lift method puts the first part of the self.message after the end of the self.message
        :param lift_point: the lift (break) point, 1 based index value inside the message
        :return: lifted message as string
        :exception: ValueError if the lift point is negative or the message is not string,
                    IndexError if the lift point is out of range of the message
        """
        if not isinstance(self.message, str):
            error_message = "The original message is in invalid format"
            logging.error(error_message)
            raise ValueError(error_message)

        logging.info(f"The original message is: {self.message}")

        if lift_point < 0:
            error_message = "Lift point must be greater than zero"
            logging.error(error_message)
            raise ValueError(error_message)

        if lift_point == 0 or lift_point == len(self.message):
            logging.info(f"Lift not happened")
            return self.message

        if lift_point > len(self.message):
            error_message = f"Lift point ({lift_point}) exceeds character count of '{self.message}'"
            logging.error(error_message)
            raise IndexError(error_message)

        new_message = f"{self.message[lift_point:]}{self.message[:lift_point]}"
        logging.info(f"Lifted message is: {new_message}")
        return new_message
