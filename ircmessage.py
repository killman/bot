
class IRCMessage():
  """Defines an IRC message."""

  def __init__(self, channel = "", msg = "", user = "", directed = False):
    #TODO Convert to setters
    if not channel.startswith("#"):
      self.channel = "#" + channel
    else:
      self.channel = channel

    self.msg = msg
    self.user = user

    # Directed defines if the message should be directed to a username when rendered or not.
    self.directed = directed

  def is_initialized(self):
    """Checks if the message is ready to be sent"""
    if self.channel == "#" or self.msg == "":
      return false
    if self.directed and self.user == "":
      return false
    return true


  def render(self):
    """Returns a user facing representation of the message"""
    if self.directed:
      return "{0}: {1}".format(self.user, self.msg)
    else:
      return self.msg