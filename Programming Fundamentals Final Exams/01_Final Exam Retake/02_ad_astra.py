import re

pattern = r'(\||#)(?P<item>[a-zA-Z ]+)\1(?P<date>\d{2}\/[0-9]{2}\/\d{2})\1(?P<calories>\d{0,4})'

