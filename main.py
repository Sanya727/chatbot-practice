import csv

with open('csvFiles.csv', mode='w') as csvfile:
  fieldnames=['Topic','link']
  writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({"Topic":"Disney wikipedia","link":"https://en.wikipedia.org/wiki/The_Walt_Disney_Company"})
  writer.writerow({"Topic":"Disney history","link":"https://d23.com/disney-history/"})
  writer.writerow({"Topic":"List of disney movies","link":"https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films"})
  