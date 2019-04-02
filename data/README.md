## Instructions to read and use data

Depending on the framework used for object detection it will require the box annotated in a certain way.

Use the notebook **'Data Annotations.ipynb'** to modify from the default way of annotation to the one you require.

The default way is a text file with **"filename,x-min,x-max,y-min,y-max,class"** on each line. Class is 1 for Daycare and 0 for NonDaycare.

The notebook reads from the original annotation csv that has the box information and saves to a file specified in "save_to_file".

Both Daycare and NonDaycare images were shared via GDrive.
