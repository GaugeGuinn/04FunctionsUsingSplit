def meal_time(time):
  hour, minutes = time.split(":")
  hour = int(hour)
  if hour >= 7 and hour < 8:
    return "breakfast"
  elif hour >= 12 and hour < 13:
    return "lunch"
  elif hour >= 18 and hour < 19:
    return "dinner"
  else:
    return "nothing at this time"

print("12:30 =>", meal_time("12:30"))
print("8:45 =>", meal_time("8:45"))
print("18:30 =>", meal_time("18:30"))
print("22:00 =>", meal_time("22:00"))
print("00:00 =>", meal_time("00:00"))


def get_filename_extension(file):
  filename, fileExtension = file.split(".")
  return fileExtension

print("--------------------")
print("hello.json =>", get_filename_extension("hello.json"))
print("code.zip =>", get_filename_extension("code.zip"))
print("HelloWorld.csv =>", get_filename_extension("HelloWorld.csv"))

def is_image_file(file):
 filename, extension = file.split(".")
 if extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif" or extension == "tiff":
    return True
 else:
    return False

print("--------------------")
print("hello.jpg =>", is_image_file("hello.jpg"))
print("helloWorld.jpeg =>", is_image_file("helloWorld.jpeg"))
print("hi.csv =>", is_image_file("hi.csv"))
print("woah.gif =>", is_image_file("woah.gif"))
print("picture.json =>", is_image_file("picture.json"))