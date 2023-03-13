import numpy as np
import mediapipe as mp
from src.bpose_utils import *


img_fpaths = ["data/inputs/airbaby-roxrite.png"]
desired_width = 960
desired_height = 960
landmark_line_thinkness = 3 # default = 2

# Read Images
images = {f.split('/')[-1].split('.')[0]: cv2.imread(f) for f in img_fpaths}
print(images)

# Preview Images
#for n, img in images.items():
#    print(f"Image Name: {n}")   
#    resize_and_show(img, desired_width=desired_width, desired_height=desired_height)

# Init MediaPipe Pose 
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing_styles._THICKNESS_POSE_LANDMARKS = landmark_line_thinkness

with mp_pose.Pose(
	static_image_mode=True, 
	min_detection_confidence=0.5, 
	model_complexity=1,
	) as pose:
	for n, img in images.items():
		results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

		# Print Nose Landmark
		#image_hight, image_width, _ = img.shape
		#if not results.pose_landmarks:
		#   continue
		#print(
		#   f'Nose coordinates: ('
		#   f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
		#   f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_hight})'
		# )

		# Draw Pose Landmarks
		print(f'Pose landmarks of {n}:')
		annotated_image = img.copy()
		# Args:
		#     image: A three channel BGR image represented as numpy ndarray.
		#     landmark_list: A normalized landmark list proto message to be annotated on
		#     the image.
		#     connections: A list of landmark index tuples that specifies how landmarks to
		#     be connected in the drawing.
		#     landmark_drawing_spec: Either a DrawingSpec object or a mapping from hand
		#     landmarks to the DrawingSpecs that specifies the landmarks' drawing
		#     settings such as color, line thickness, and circle radius. If this
		#     argument is explicitly set to None, no landmarks will be drawn.
		#     connection_drawing_spec: Either a DrawingSpec object or a mapping from hand
		#     connections to the DrawingSpecs that specifies the connections' drawing
		#     settings such as color and line thickness. If this argument is explicitly
		#     set to None, no landmark connections will be drawn.
		mp_drawing.draw_landmarks(
			image=annotated_image, 
			landmark_list=results.pose_landmarks, 
			connections=mp_pose.POSE_CONNECTIONS, 
			landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
			)
		
		# Save Landmarks Image
		cv2.imwrite(f"data/outputs/{n}.png", resize_and_show(annotated_image, desired_width=desired_width, desired_height=desired_height))