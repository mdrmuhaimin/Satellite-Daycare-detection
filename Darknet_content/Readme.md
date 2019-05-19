# Satellite-Daycare-detection
Experimentation of building detection in Satellite image, by detecting day care from Brazil Satellite Data

### YOLO Option

Preq: Install Darknet from here: https://pjreddie.com/darknet/install/

1. Copy images with the folder name 'Daycares' inside the data folder
2. Run prepare.sh
3. Creat test.txt inside Darknet_content/data/daycare/
4. Change config inside the net block of Darknet_content/cfg/yolov3-daycare.cfg (At the top)
5. Run copy_darknet_content.sh
6. Navigate inside darknet folder and run get_weight.sh
7. run train.sh
