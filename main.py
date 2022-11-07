import openai
import requests

print("This is using Open ai to generate images , Please read the pricing as it is affected to ur api key account ")
print("For more information go to https://github.com/ofcoursenp/openai-imagecreation")

apikey = input("Enter ur api key : ")
openai.api_key = apikey
prompt = str(input('Enter what do u want the image to generate : '))
print("What size do u want \n1: 1024x1024 \n2: 512x512 \n3: 256x256")
sizeinput = int(input("Enter 1 for number 1 and 2 for number 2 and 3 for number 3 : "))
if sizeinput == 1:
    size = '1024x1024'
elif sizeinput == 2:
    size = '512x512'
elif sizeinput == 3:
    size = '256x256'

if sizeinput < 1 and sizeinput > 3:
    print("Wrong number quiting the program...")
    quit()


var = openai.Image.create(
    prompt=prompt,
    n=1,
    size=size
)

vard = var['data'][0]
url = vard['url']

namefile = prompt[0:8] + '.png'
print(namefile)

r = requests.get(url)
with open(namefile,"wb") as f:
    f.write(r.content)



print(f"Go to {namefile} file for ur creation")

