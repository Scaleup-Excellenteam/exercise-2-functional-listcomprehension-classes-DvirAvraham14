class PostOffice(object):
    """A Post Office class. Allows users to message each other.
    Args:
        usernames (list): Users for which we should create PO Boxes.
    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_headline, message_body, urgent=False):
        """Send a message to a recipient.
        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_headline (str): The headline of the message.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            # >>> po_box = PostOffice(['a', 'b'])
            # >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            # >>> len(po_box.boxes['b'])
            1
            # >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'headline': message_headline,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """ Read N top messages from the inbox of the user.
            and mark them as read.
            Args:
                username (str): The user's username.
                n (int): The number of messages to read.

            Returns: n top messages from the inbox of the user.

            Raises:
                    KeyError: If the user does not exist.
        """
        user_box = self.boxes[username]
        user_box = user_box if n is None else user_box[:n]
        for index, message in enumerate(user_box):
            user_box[index]['read'] = True
        return user_box

    def search_inbox(self, username, keyword):
        """Search for messages in the inbox of the user.
            Args:
                username (str): The user's username.
                keyword (str): The keyword to search for.

            Returns: A list of messages that contain the keyword.

            Raises:
                    KeyError: If the user does not exist.
        """
        user_box = self.boxes[username]
        return [message for message in user_box if keyword in message['body']
                or keyword in message['sender']]

# test PostOffice class

po_box = PostOffice(['a', 'b', 'c'])
po_box.send_message('a', 'b', 'title', 'Hello!', urgent=True)
po_box.send_message('a', 'b', 'title', 'Two!', urgent=True)
po_box.send_message('a', 'b', 'title', 'You!', urgent=True)
po_box.send_message('b', 'a', 'title', 'Me!')

print('Test read_inbox')
for message in po_box.read_inbox('b'):
    print(message)

print('Test search_inbox')
for message in po_box.search_inbox('b', 'Hello'):
    print(message)
