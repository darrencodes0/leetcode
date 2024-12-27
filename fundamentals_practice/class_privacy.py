class class_privacy:

  def __private_method():
    print("I am private")

  """
  Private methods use __ in front of the method signature, can only be called
  within other methods and not in the main.
  """

  def _default_method():
    print("I am default")

  """
  Default methods use _ in front of the method signature, can be called both in
  the main and other methods. This is mainly just to signify to other programmers
  to use with caution.
  """

