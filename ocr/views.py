from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import os
import cv2
#from .ocr_image import app
import shutil

def index(request):
    return render(request, 'ocr/detail.html')


def load_image(filename):
    img = cv2.imread(str(os.path.join(settings.BASE_DIR,'images')) + filename)
    return img

def delete_image(filename):
    os.remove(str(os.path.join(settings.BASE_DIR,'images')) + filename)

def upload_image(request):
    # question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        image = request.FILES['myfile']
        fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR,'images'))
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        img = load_image(uploaded_file_url)
        model = os.path.join(settings.BASE_DIR, 'model')
        #uuid = app.main(img)
        uuid = None
        delete_image(uploaded_file_url)
        if(uuid is  None):
            uuid = "Please upload image again for OCR"
        return render(request, 'ocr/upload.html', {
            'message': uuid,
        })
#
#
def make_archive(uuid,path):
    shutil.make_archive(uuid, 'zip', path)
    try:
        dest = shutil.move(os.path.join(settings.BASE_DIR,str(uuid)+'.zip'), os.path.join(settings.BASE_DIR,'zips'))
    except(shutil.Error):
        os.remove(str(os.path.join(settings.BASE_DIR,str(uuid)+'.zip')))
        dest = os.path.join(os.path.join(settings.BASE_DIR,'zips'),str(uuid)+'.zip')
    return dest
def get_crop_and_ocr(request):
    if(request.method == 'POST'):
        uuid = request.POST['uuid']
        path = os.path.join(settings.BASE_DIR, 'Outputs'+'/'+uuid)
        try :
            zip_file = make_archive(uuid,path)
            message = "Download file"
            response = HttpResponse(open(zip_file, 'rb'), content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="%s"' % str(uuid)+'.zip'
            return response
        except FileNotFoundError :
            message = "File Not Exist, Please do OCR again"
            return HttpResponse(message)














