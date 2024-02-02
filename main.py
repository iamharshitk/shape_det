import cv2 as cv
import glob


folder_path="C:\\Users\\harsh\\OneDrive\\Desktop\\SR\\t2.4\\*.png"

for file in glob.glob(folder_path):

    winname="Shape Detection"
    cv.namedWindow(winname)
    img=cv.imread(file)
   
    img=cv.resize(img,(1280,720))


    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    thresh=cv.Canny(gray,10, 50,5)
  


    contours,_=cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (20, 255 ,57), 2)


    trianglel=[]
    squarel=[]
    rectanglel=[]
    rhombil=[]
    pentagonl=[]
    hexagonl=[]
    circlel=[]
    ellipsel=[]


    for i in contours:
        perimeter=0.02*cv.arcLength(i,True)
        vertices=cv.approxPolyDP(i,perimeter, True)


        n=vertices.ravel()


        if len(vertices)==3:
            trianglel.append(vertices)
        

        elif len(vertices)==4:
            (x,y,w,h)=cv.boundingRect(vertices)

            if float(w)/h>=0.92 and float(w)/h<=1.05:
                squarel.append(vertices)
            else:
                rectanglel.append(vertices)


        elif len(vertices)==5:
            pentagonl.append(vertices)

        
        elif len(vertices)==6:
            hexagonl.append(vertices)


        else:
            (x,y,w,h)=cv.boundingRect(vertices)

            if float(w)/h>=0.95 and float(w)/h<=1.05:
                circlel.append(vertices)
            else:
                ellipsel.append(vertices)
          


    main_dict={"triangle":trianglel, "Square":squarel, "quadrilateral":rectanglel, "rhombi":rhombil, "pentagon":pentagonl, "hexagon":hexagonl, "circle":circlel, "ellipse":ellipsel}

    for shape in main_dict:
        for i in main_dict[shape]:
            (x, y, w, h) = cv.boundingRect(i)
            cv.putText(img, shape, (x+w//2,y+h), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
   

    cv.imshow(winname,img)

    cv.waitKey(0)
    cv.destroyAllWindows()




