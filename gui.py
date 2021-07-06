import tkinter as tk
from tkinter import *

from bs4 import BeautifulSoup
import requests


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


instructions = tk.Label(root, text="Search for BMW OR Audi.", font="Raleway")
instructions.grid(columnspan=3,column=0, row=0)

def onclick(args):
    if args == 1:
        # change this '' to any auction website you want with the specific filters through the website.
        html_text = requests.get(
            'https://auctions.asm-autos.co.uk/auction/items/?make=bmw&fuel=1&transmission=0&category=7&layout=r50&seller=0&location=0&time=all&distance=&search=&sort=10&tab=1').text
        soup = BeautifulSoup(html_text, 'lxml')
        cars = soup.find_all('div', class_='row vehicle_list')
        for index,  car in enumerate(cars):
            title_n = car.find('div', class_='list_title').text
            odometer = car.find('div', class_='col-lg-6 pt-lg-3 d-md-none d-lg-block mb-lg-2').text
            price = car.find('span', class_='list_price_2').text
            ## set this to be the specific folder you want your textfiles saved to.
            with open(f'bmw/{index}.txt', 'w') as f:
                f.write(f"Title: {title_n.strip()}")
                f.write(f"odometer: {odometer.strip()}\n")
                f.write(f"current bid: {price.strip()}")
            print(f'File saved: {index}')
    if args == 2:
        # change this '' to any auction website you want with the specific filters through the website.
        html_text = requests.get(
            'https://auctions.asm-autos.co.uk/auction/items/?make=audi&fuel=1&transmission=0&category=7&layout=r50&seller=0&location=0&time=all&distance=&search=&sort=10&tab=1').text
        soup = BeautifulSoup(html_text, 'lxml')
        cars = soup.find_all('div', class_='row vehicle_list')
        for index,  car in enumerate(cars):
            title_n = car.find('div', class_='list_title').text
            odometer = car.find('div', class_='col-lg-6 pt-lg-3 d-md-none d-lg-block mb-lg-2').text
            price = car.find('span', class_='list_price_2').text
            # set this to be the specific folder you want your textfiles saved to.
            with open(f'audi/{index}.txt', 'w') as f:
                f.write(f"Title: {title_n.strip()}")
                f.write(f"odometer: {odometer.strip()}\n")
                f.write(f"current bid: {price.strip()}")
            print(f'File saved: {index}')




search_text = tk.StringVar()
search_btn = tk.Button(root, textvariable=search_text, font="Raleway", bg="#20bebe", fg="white", command=lambda:onclick(1))
search_text.set("Search Bmw")
search_btn.grid(column=1, row=1)

search_text1 = tk.StringVar()
search_btn1 = tk.Button(root, textvariable=search_text1, font="Raleway", bg="#20bebe", fg="white", command=lambda:onclick(2))
search_text1.set("Search Audi")
search_btn1.grid(column=2, row=2)


canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)
root.mainloop()