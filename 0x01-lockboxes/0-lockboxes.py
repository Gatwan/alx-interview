#!/usr/bin/python3
""" Find keys that can unlock boxes """


def canUnlockAll(boxes):
    """ Find keys """
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    bunch_keys = [0]

    while bunch_keys:
        curr_box = bunch_keys.pop()
        keys = boxes[curr_box]

        for key in keys:
            if key >= 0 and key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                bunch_keys.append(key)

    return all(unlocked_boxes)
