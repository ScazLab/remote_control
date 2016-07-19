==============
Remote control
==============

A remote controller to send messages to a robot. The server has access to the robot, receives messages, pass them to a callback which execute the corresponding actions and return either success or failure which is sent back to the client. The client exposes the `send_message` command that blocks until success message is received and raise exception on failure.
