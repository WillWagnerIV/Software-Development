
limrick = "There once was a man from Crass \
            Whose balls were made of brass, \
            and in stormy weather,\
            They clanged together,\
            And sparks flew from his ass!"


pFile = open("example.txt", "wt")

pFile.write(limrick) 

pFile.close()






pFile = open("example.txt", "rt")

print(pFile.read()) 

pFile.close
