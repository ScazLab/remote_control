==============
Remote control
==============

A remote controller to send messages to a robot. The server has access to the robot, receives messages, pass them to a callback which execute the corresponding actions and return either success or failure which is sent back to the client. The client exposes the `send_message` command that blocks until success message is received and raise exception on failure.

Examples of client and server behaviour can be found in the `test_client.py` and `test_server.py` scripts under the `sample` directory.

Both the client and server can be used either in a `with` block:

  .. code:: python

      with Client() as c:
          status = c.send_message("Hi!")

or explicitely:

  .. code:: python

      c = Client()
      c.start()
      status = c.send_message("Hi!")
      c.close()
