# downloading the file
import urllib.request

def download_file():
    url = "https://bheem-models.s3.ap-south-1.amazonaws.com/netG_epoch_4_90.pth"
    filename = "./model/srgan/netG_epoch_4_90.pth"
    urllib.request.urlretrieve(url, filename)
    print(f"File downloaded successfully: {filename}")

