import cv2
import dropbox
import random
import time

start_time=time.time()


def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time  
        result=False
    return img_name

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.Axgv0JZQMb3jXFkhcH6GBJ3-0YUHo8ODxQHwLFngxldQIKDVbIDLc2ZWMHHRdJ-qZH1Ajok4Sq2Isn_mMQlwyiiHh3GCVsVUm6mK770VAR3OTcoqXqJV15KlBGktp9tQ2h8-7k8'
    file=img_name
    file_from=file
    file_to="/@Class102/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=15):
            name=take_snapshot()
            upload_file(name)

main()        