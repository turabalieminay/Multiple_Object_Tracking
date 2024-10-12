import cv2 
from random import randint 


def createTracker(i):
    
    trackers = ["BOOSTING", "MIL", "KCF", "CSRT", "TLD", "MEDIANFLOW", "MOSSE"]
    
    tracker_algorithm = trackers[i]
    
    if tracker_algorithm == "BOOSTING":
        tracker = cv2.legacy.TrackerBoosting_create()
         
    elif tracker_algorithm == "MIL":
        tracker = cv2.legacy.TrackerMIL_create()
    
    elif tracker_algorithm == "KCF":
        tracker = cv2.legacy.TrackerKCF_create()    

    elif tracker_algorithm == "CSRT":
        tracker = cv2.legacy.TrackerCSRT_create()

    elif tracker_algorithm == "TLD":
        tracker = cv2.legacy.TrackerTLD_create()

    elif tracker_algorithm == "MEDİANFLOW":
        tracker = cv2.legacy.TrackerMedianFlow_create()    

    elif tracker_algorithm == "MOSSE":
        tracker = cv2.legacy.TrackerMOSSE_create()     
        
    else:
        print("[ERROR].. number out of index !")    
        
    return tracker


cap = cv2.VideoCapture("test.mp4")
ret , frame = cap.read()

if ret ==  False:
    print("Something went wrong when loading")
    
elif ret == None:
    print("Wrong Path")


boxes = [] 
colors = []


while True:
    box = cv2.selectROI("MultiTracker", frame)
    boxes.append(box)
    color_generator = (randint(0, 255),randint(0, 255),randint(0, 255)) 
    colors.append(color_generator)
    
    print("[INFO].. Press Q to start tracking")   
    print("[INFO].. Press any key to select the next object")
        
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

    
print("Boxes: ",boxes)
print("Coloes: ",colors)    

#trackers = ["BOOSTING", "MIL", "KCF", "CSRT", "TLD", "MEDIANFLOW", "MOSSE"]
tracker_index = 3
multi_tracker = cv2.legacy.MultiTracker_create()

for box in boxes:
    multi_tracker.add(createTracker(tracker_index), frame, box)


while True:
    
    ret, frame = cap.read()
    if ret ==  False:
        print("Something went wrong when loading")
        
    elif ret == None:
        print("Wrong Path")
        
    ret, multiBoxes = multi_tracker.update(frame)

    for i,bbox in enumerate(multiBoxes):
        (x,y,w,h) = [int(j) for j in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h) , colors[i], 2)

    cv2.imshow("Multi Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cap.destroyAllWindows()    
        


























