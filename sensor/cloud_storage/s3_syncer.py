import os, sys
from sensor.exception import SensorException
from sensor.logger import logging

import os
class S3Sync:


    def sync_folder_to_s3(self,folder,aws_buket_url):
        command = f"aws s3 sync {folder} {aws_buket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_buket_url):
        command = f"aws s3 sync  {aws_buket_url} {folder} "
        os.system(command)

