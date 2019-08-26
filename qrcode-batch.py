import qrcode
import os 

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    
)

file = open('D:\\qrcode\\qrcode.csv')
readlines = file.readlines()
i=0
for readline in readlines:
    
    qr.add_data(readline.strip())
    qr.make(fit=True)
    img = qr.make_image()
    filename='D:\\qrcode\\'+readline.strip()+'.png'
    readline=''
    img.save(filename)
    qr.clear()
    i=i+1
    print('done '+str(i))
print('sucess '+str(i))

file.close()