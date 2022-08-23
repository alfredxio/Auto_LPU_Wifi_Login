import asyncio
from asyncio.windows_events import NULL
from pyppeteer import launch
import tkinter as tk
from tkinter import *
import os
import platform
import os.path
import time



#/////////////////////////////////////////////////////////////////////////
#code to connect wifi

def createNewConnection(name, SSID, key):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+key+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    if platform.system() == "Windows":
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
    elif platform.system() == "Linux":
        command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
    os.system(command)
    if platform.system() == "Windows":
        os.remove(name+".xml")

def connect(name, SSID):
    if platform.system() == "Windows":
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli con up "+SSID
    os.system(command)

def displayAvailableNetworks():
    if platform.system() == "Windows":
        command = "netsh wlan show networks interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli dev wifi list"
    os.system(command)





#/////////////////////////////////////////////////////////////////////////
#code to initialise connect wifi and login page

browser = None

async def exit_site():
    browser.close()
    values.config(text='Successfully Disconnected.')




def run_site():
   
#/////////////////////////////////////////////////////////////////////////
#code to saved data
   
    file_exists = os.path.exists('data.txt')
    if(file_exists):
        with open('data.txt', 'r') as infile:
            data = infile.read()
        li = data.splitlines()
        
        ui_var.set(li[0])
        pass_var.set(li[1])

    else:
        file1 = open("data.txt","w")
        L = [ui_var.get()+"\n",pass_var.get()]
        file1.writelines(L)
        file1.close()   


    qw=ui_var.get()
    aw=pass_var.get() 
    ssid=v.get()
    


    try:
        displayAvailableNetworks()
        
        
        name = ssid
        key = "123456789a"
        createNewConnection(name, name, key)
        connect(name, name)
        print("If you aren't connected to this network, try connecting with correct credentials")
        
        
    except KeyboardInterrupt as e:

        print("\nExiting...")

    #asyncio.get_event_loop().run_until_complete(site(qw,aw))

    asyncio.run(site(qw,aw))




#/////////////////////////////////////////////////////////////////////////
#code to login page

async def site(user_id,pass2):

    browser = await launch(headless=False)
    page = await browser.newPage()
    time.sleep(2)
    await page.goto('http://10.10.0.1/24online/')

    await page.waitForNavigation({'waitUntil': 'networkidle0'})


    await page.click('[id=agreepolicy]')
    await page.type('[name=username]', user_id)
    await page.type('[name=password]', pass2)

    await page.keyboard.press('Enter')


    await page.waitForNavigation({'waitUntil': 'networkidle0'})
    values.config(text='Successfully Connected.')

    #await page.screenshot({'path': 'site.png'})





    

#/////////////////////////////////////////////////////////////////////////
#code to window



root = tk.Tk()
root.title("LPU WI-FI LOGIN")
root.geometry('400x400')

ui_var=tk.StringVar()
pass_var=tk.StringVar()
v = tk.StringVar()


lblfrstrow = tk.Label(root, text ="Enter User-Id:", )
lblfrstrow.place(x = 100, y = 20)
user_id = tk.Entry(root,textvariable = ui_var, width = 35)
user_id.place(x = 200, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Enter Pass:")
lblsecrow.place(x = 100, y = 50)
pass2 = tk.Entry(root,textvariable = pass_var, width = 35)
pass2.place(x = 200, y = 50, width = 100)


tk.Radiobutton(root, 
               text="LPU Wireless",
               padx = 20, 
               variable=v, 
               value="LPU Wireless").place(x = 130, y = 80)

tk.Radiobutton(root, 
               text="LPU Hostels",
               padx = 20, 
               variable=v, 
               value="LPU Hostels").place(x = 130, y = 110)

tk.Radiobutton(root, 
               text="Block 38",
               padx = 20, 
               variable=v, 
               value="Block 38").place(x = 130, y = 140)


store = tk.Label(root, text="Created by Alfred.io")
store.place(x = 0, y = 240, width = 400)

submitbtn = tk.Button(root, text ="CONNECT", bg ='blue', command = lambda:run_site()) 
submitbtn.place(x = 150, y = 160, width = 100)

submitbtn = tk.Button(root, text ="DISCONNECT", bg ='blue', command = lambda:exit_site()) 
submitbtn.place(x = 150, y = 190, width = 100)



values = tk.Label(root, text="")
values.place(x = 0, y = 260, width = 400)




root.mainloop()






