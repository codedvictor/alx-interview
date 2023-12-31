#!/usr/bin/python3

"""
method that determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    check to unlock all boxes
    """
    if not boxes or not boxes[0]:
        return False

    numb = len(boxes)
    checked = [False] * numb
    checked[0] = True
    queue = [0]

    while queue:
        present_box = queue.pop(0)

        for key in boxes[present_box]:
            if 0 <= key < numb and not checked[key]:
                checked[key] = True
                queue.append(key)

    return all(checked)
