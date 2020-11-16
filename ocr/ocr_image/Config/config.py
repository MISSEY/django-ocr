from django.conf import settings
import os
image_data ={
    "save_path":os.path.join(settings.BASE_DIR,'Outputs')
}
log_dir = "./ocr/ocr_image/Logs"
image_file = "./test_images/test33.jpg"
log_type = 'DEBUG'  # DEBUG or INFO