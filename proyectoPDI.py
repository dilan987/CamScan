import numpy as np
import cv2

cap= cv2.VideoCapture(0)


variable=0
while True:
    
    contadorfiltro1=False
    contadorfiltro2=False
    contadorfiltro3=False
    contadorfiltro4=False
    cerrar=False

    ret,frame=cap.read()
    
    frame =cv2.flip(frame,1)
    rol= frame[0:500,0:640]
    gray = cv2.cvtColor(rol,cv2.COLOR_BGR2GRAY)
    gray_filter =cv2.GaussianBlur(gray,(7,7),0)
    #creamos un rectagulo al rededor de (rol)
    dimension1 = (0, 100)
    dimension2 = (640,480)
    ret1 = cv2.rectangle(rol, dimension1, dimension2, (10, 50, 20), 5)
    img = rol[dimension1[1] : dimension2[1], dimension1[0] : dimension2[0]]
    pantalla = img

            # definimos los rectangulos para interacciones  
    cuadro=cv2.rectangle(rol,(0,0),(640,100),(0,0,0),thickness =2,lineType=4,shift=0)
    cuadrofiltro1=cv2.rectangle(rol,(5,15),(120,80),(0,0,0),thickness =2,lineType=4,shift=0)
    cuadrofiltro2=cv2.rectangle(rol,(125,15),(240,80),(0,0,0),thickness =2,lineType=4,shift=0)
    cuadrofiltro3=cv2.rectangle(rol,(245,15),(360,80),(0,0,0),thickness =2,lineType=4,shift=0)
    cuadrofiltro4=cv2.rectangle(rol,(365,15),(485,80),(0,0,0),thickness =2,lineType=4,shift=0)
    cuadrosalir=cv2.rectangle(rol,(490,15),(635,80),(0,0,0),thickness =2,lineType=4,shift=0)
        

    #cv2.putText(rol,"region de interes",(50,40),cv2.FONT_ITALIC,0.6,(0,0,0),1,cv2.LINE_AA)

    
    #circulos=cv2.HoughCircles(gray_filter,cv2.HOUGH_GRADIENT,1,40,param1=50,param2=50,minRadius=10,maxRadius=70)
    circulos = cv2.HoughCircles(gray_filter, cv2.HOUGH_GRADIENT, 1, 40, np.array([]), 50, 50, 10, 70)
    circulos=np.uint16(np.around(circulos))
    try:
        if(len(circulos)>0):
            
            for i in circulos[0,:]:
                cv2.circle(rol,(i[0],i[1]),i[2],(0,0,255),2)
                cv2.circle(rol,(i[0],i[1]),2,(255,0,0),2)
                if i[0] >= 5 and i[0] <=120 and i[1] >= 15  and i[1] <=80:
                    contadorfiltro1=True
                    variable=1
                    
                        
                            
                elif i[0] >= 125 and i[0] <=240 and i[1] >= 15  and i[1] <=80:
                    variable=2
                    contadorfiltro2=True
                
                elif i[0] >= 245 and i[0] <=360 and i[1] >= 15  and i[1] <=80:
                        
                    variable=3
                    contadorfiltro3=True
                elif i[0] >= 365 and i[0] <=485 and i[1] >= 15  and i[1] <=80:

                    variable=4
                    contadorfiltro4=True
                elif i[0] >= 490 and i[0] <=635 and i[1] >= 15  and i[1] <=80:
                        
                    cerrar=True
                else:
                    cv2.imshow('frame',rol)
                
            if cerrar==True:
                break
        else:
            cv2.imshow('frame',rol)
        
        if variable==1:
            filtro1=cv2.cvtColor(pantalla,cv2.COLOR_BGR2HSV)
            filtro=rol[dimension1[1] : dimension2[1], dimension1[0] : dimension2[0]]=filtro1
            cv2.imshow( 'frame',rol)
        if variable==2:
            filtro1=cv2.cvtColor(pantalla,cv2.COLOR_BGR2YCrCb)
            filtro=rol[dimension1[1] : dimension2[1], dimension1[0] : dimension2[0]]=filtro1
            cv2.imshow('frame',rol)
        if variable==3:
            filtro1=cv2.cvtColor(pantalla,cv2.COLOR_BGR2XYZ) # X es color rojo/verde Y es brillo Z es azul/amarillo
            filtro=rol[dimension1[1] : dimension2[1], dimension1[0] : dimension2[0]]=filtro1
            cv2.imshow('frame',rol)
        if variable==4:
            
            rango1 = (200,230,200)
            rango2 = (255,255,255)
            mask = cv2.inRange(pantalla, rango1, rango2)
            result = cv2.bitwise_and(pantalla, pantalla, mask=mask)
            filtro=rol[dimension1[1] : dimension2[1], dimension1[0] : dimension2[0]]=result
            cv2.imshow('frame',rol)
 
    except Exception:
        print("")

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break



cap.release()
cv2.destroyAllWindows()