#!/usr/bin/python3
""" Checks data set if UTF-8 Validation """


def validUTF8(data):
    """ Checks data set """
    num_bytes = 0

    for num in data:
        # Checks the current integer if it starts a valid UTF-8 character sequence
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                num_bytes = 0
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            #Check if curret integer starts with the pattern '10'
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

        # If all bytes are correctly processed, bytes should not remain
        return num_bytes == 0
