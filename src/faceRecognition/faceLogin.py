import os
import face_recognition


def load_and_encode(namefile):
  picture_of_user = face_recognition.load_image_file(namefile)
  #encode into a feature vector
  face_encoding = face_recognition.face_encodings(picture_of_user)
  if len(face_encoding) > 0:
    return face_encoding[0]
  else: 
    raise NameError('No face was found')

def detectUser(ID='obama'):
  biden_encoding = load_and_encode('Temp/%s_temp.jpg' % ID)
  for image in os.listdir('Faces'):
    biden_encodingID= load_and_encode('Faces/'+image)
    if comparePeople(biden_encoding, biden_encodingID):
      print('Face found on '+ image)
      return True
  print('Face not found')
  return False

def comparePeople(biden_encoding, biden_encodingID):
  results = face_recognition.compare_faces([biden_encoding], biden_encodingID)
  return results[0]


