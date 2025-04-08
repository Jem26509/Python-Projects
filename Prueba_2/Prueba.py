
import cv2
import numpy as np
import mediapipe as mp


from mediapipe import solutions



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Reading an image in default mode
#image = cv2.imread("Image.png")


webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  
  if not webcam.isOpened():
      print("Cannot open camera")
      exit()
  while True:
      # Capture frame-by-frame
      ret, image = webcam.read()
  
      # if image is read correctly ret is True
      if not ret:
          print("Can't receive frame (stream end?). Exiting ...")
          break

      # Our operations on the frame come here
      image.flags.writeable = False
      gray = cv2.flip(image, 1)
      #gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

      results = face_mesh.process(gray)
      # Draw the face mesh annotations on the image.
      gray.flags.writeable = True
      
      if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
          mp_drawing.draw_landmarks(
              image=gray,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_TESSELATION,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_tesselation_style())
          """mp_drawing.draw_landmarks(
              image=gray,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_CONTOURS,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_contours_style())"""
          """mp_drawing.draw_landmarks(
              image=gray,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_IRISES,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_iris_connections_style())"""
          
          #Coordenadas de la cara (arriba y abajo)
          top = (face_landmarks.landmark[10].x, face_landmarks.landmark[10].y)
          bottom = (face_landmarks.landmark[152].x, face_landmarks.landmark[152].y)

          #Obtener coordenadas del 'cuadrado' de la cara para poder mostrarlo en la pantalla despues
          face_left_x = face_landmarks.landmark[234].x
          face_right_x = face_landmarks.landmark[454].x
          face_top_y = face_landmarks.landmark[10].y
          face_bottom_y = face_landmarks.landmark[152].y

          #Dejar algo de espacio alrededor
          face_left_x = face_left_x - .1
          face_right_x = face_right_x + .1
          face_top_y = face_top_y - .1
          face_bottom_y = face_bottom_y + .1

          webcam_width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
          webcam_height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)

          cv2.line(
              gray, 
              (int(top[0] * webcam_width), int(top[1] * webcam_height)),
              (int(bottom[0] * webcam_width), int(bottom[1] * webcam_height)),
              (0, 255, 0), 3
          )

          #cv2.circle(gray, (int(top[0] * webcam_width), int(top[1] * webcam_height)), 8, (0,0,255), -1)
          #cv2.circle(gray, (int(bottom[0] * webcam_width), int(bottom[1] * webcam_height)), 8, (0,0,255), -1)          
        
      # Display the resulting frame
      cv2.imshow('Prueba Jem', gray)

      if cv2.waitKey(1) == ord('q'):
          break

# When everything done, release the capture
webcam.release()
cv2.destroyAllWindows()    




