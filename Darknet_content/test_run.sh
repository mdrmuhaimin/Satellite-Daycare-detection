for f in data/daycare/test/*; do
  ./darknet detect cfg/yolov3-daycare.cfg yolov3-daycare_10000.weights $f -out predictions/$f
done
