def choose_image():
    global picture, picture_string, l_picture
    image = fd.askopenfilename()
    image_string = image
    image = Image.open(image)
    image = app_lg.resize((130,130))
    image = ImageTk.PhotoImage(image)
    l_image = Label(frame_details, image=image, bg=co1, fg=co4)
    l_image.place(x=390, y=10)