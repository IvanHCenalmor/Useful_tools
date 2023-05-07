import PySimpleGUI as sg
import cv2
import os

def image_converter(filename, desired_extension):
    img = cv2.imread(filename)
    file_name, _ = os.path.splitext(filename)
    print(file_name + desired_extension)
    cv2.imwrite(file_name + desired_extension, img)
    return file_name + desired_extension

def image_converter_from_folder(folder, desired_extension):
    for filename in os.listdir(folder):
        image_converter(os.path.join(folder, filename), desired_extension)
        
extension_choices = ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico', '.jfif'] 

# Define the window's contents
layout = [[sg.Text('Your File'), sg.InputText('Default Filename', key='-Filename-'), sg.FileBrowse()],
          [sg.Text('Your Folder'), sg.InputText('Default Folder', key='-Folder-'), sg.FolderBrowse()],   
          [sg.Text('Is a File'), sg.Checkbox('File', 1, key='-isFile-')],             
          [sg.Text('Desired extension'), sg.OptionMenu(extension_choices, s=(15,2), key='-extension-')],
          [sg.OK(), sg.Cancel()]]

# Create the window
window = sg.Window('Image converter', layout)

while True:
    # Display and interact with the Window
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Cancel":
        break
    elif event == "OK":
        if values['-isFile-']:
            if os.path.exists(values['-Filename-']):
                new_filename = image_converter(values['-Filename-'], values['-extension-'])
                sg.popup('Image {} has been converted into {}.'.format(values['-Filename-'], new_filename))
            else:
                raise ValueError('File does not exist.')
        else:
            if os.path.exists(values['-Folder-']):
                image_converter_from_folder(values['-Folder-'], values['-extension-'])
                sg.popup('All images in {} have been converted into extension {}.'.format(values['-Folder-'], values['-extension-']))
            else:
                raise ValueError('Folder does not exist.')

# Finish up by removing from the screen
window.close()