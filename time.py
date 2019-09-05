secs_str = input("Input seconds: ") # do not change this line
secs_int=int(secs_str)
hours=int(secs_int/3600)
minutes=int(((secs_int/3600)-hours)*60)
seconds=round((((secs_int/3600)-hours)*60-minutes)*60)


# hours =
# minutes =
# seconds =
print(hours,":",minutes,":",seconds) # do not change this line
