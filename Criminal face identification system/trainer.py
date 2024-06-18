import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path="C:\\Users\\askar\\Documents\\Advanced Criminal Detection\\images"

def getImgID(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        faceImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        faceNp=np.array(faceImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        Ids.append(Id)
        #cv2.imshow("training",faceNp)
        #cv2.waitKey(10)
        # extract the face from the training image sample
        #faces=detector.detectMultiScale(imageNp)
         #If a face is there then append that in the list as well as Id of it
    return Ids,faces

    
Ids,faces = getImgID(path)
#print(Ids,faces)
recognizer.train(faces, np.array(Ids))
#recognizer.write('recognizer\\training_data.yml')
recognizer.write(os.path.join('C:\\Users\\Sai Karthik Achanta\\Desktop\\Major\Advanced Criminal Detection', 'recognizer', 'training_data.yml'))
cv2.destroyAllWindows()
import cv2
import os
import numpy as np
from PIL import Image

# Create LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to the dataset
dataset_path = r"C:\\Users\\Sai Karthik Achanta\\Desktop\\Major\Advanced Criminal Detection\\recognizer"

def getImgID(path):
    # Get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
    # Create empty face list
    faces = []
    # Create empty ID list
    Ids = []

    # Now loop through all the image paths and load the Ids and the images
    for imagePath in imagePaths:
        # Loading the image and converting it to grayscale
        faceImage = Image.open(imagePath).convert('L')
        
        # Convert the PIL image into a NumPy array
        faceNp = np.array(faceImage, 'uint8')
        
        # Get the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        
        faces.append(faceNp)
        Ids.append(Id)

    return Ids, faces

# Get Ids and faces from the dataset
Ids, faces = getImgID(dataset_path)

# Train the recognizer
recognizer.train(faces, np.array(Ids))

# Create the output directory if it doesn't exist
output_directory = r"C:\\Users\\Sai Karthik Achanta\\Desktop\\Major\Advanced Criminal Detection\\recognizer"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save the trained recognizer to a YAML file
output_file = os.path.join(output_directory, 'training_data.yml')
recognizer.write(output_file)

# Release resources
cv2.destroyAllWindows()

# import cv2
# import os
# import numpy as np
# from PIL import Image

# # Create LBPH face recognizer
# recognizer = cv2.face.LBPHFaceRecognizer_create()

# # Path to the dataset
# dataset_path = r"C:\Users\askar\Documents\Advanced Criminal Detection\images"

# def getImgID(path):
#     # Get the path of all the files in the folder
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
#     # Create empty face list
#     faces = []
#     # Create empty ID list
#     Ids = []

#     # Now loop through all the image paths and load the Ids and the images
#     for imagePath in imagePaths:
#         # Loading the image and converting it to grayscale
#         faceImage = Image.open(imagePath).convert('L')
        
#         # Convert the PIL image into a NumPy array
#         faceNp = np.array(faceImage, 'uint8')
        
#         # Get the Id from the image
#         Id = int(os.path.split(imagePath)[-1].split(".")[1])
        
#         faces.append(faceNp)
#         Ids.append(Id)

#     return Ids, faces

# # Get Ids and faces from the dataset
# Ids, faces = getImgID(dataset_path)

# # Train the recognizer
# recognizer.train(faces, np.array(Ids))

# # Create the output directory if it doesn't exist
# output_directory = r"C:\Users\askar\Documents\Advanced Criminal Detection\recognizer"
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Save the trained recognizer to a YAML file
# output_file = os.path.join(output_directory, 'training_data.yml')
# recognizer.write(output_file)

# # Release resources
# cv2.destroyAllWindows()

