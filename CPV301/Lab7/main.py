import cv2
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk
import PIL.Image as Image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image

def open_image():
    global photo
    filepath = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image = cv2.imread(filepath)
    image = detect_face(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)

    image_label.configure(image=photo)
    image_label.image = photo

root = Tk()
root.state('zoomed')  # This will make the window fullscreen

# Create a frame for the button
button_frame = Frame(root)
button_frame.pack(side=TOP, fill=X)

button_img = Button(button_frame,
                    text="Open Image",
                    fg="red",
                    command=open_image)
button_img.pack()

# Create a frame for the image
image_frame = Frame(root)
image_frame.pack(fill=BOTH, expand=YES)

# Create a blank image of the same size as the screen
blank_image = Image.new('RGB', (root.winfo_screenwidth(), root.winfo_screenheight()), 'white')
photo = ImageTk.PhotoImage(blank_image)

# Create a label for the image and place it in the image frame
image_label = Label(image_frame, image=photo)
image_label.pack(fill=BOTH, expand=YES)

root.mainloop()
