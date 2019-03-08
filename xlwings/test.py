''' Excel parser and editor script.
  Find target cells. Change background to red if data is between -12 and 0.
  Change background to blue if data is between 0 and 7.
  Only run on windows.
'''

import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('Book1.xlsx')

start=["D{}:D{}", "E{}:E{}", "F{}:F{}", "G{}:G{}", "L{}:L{}", "M{}:M{}", "N{}:N{}", "O{}:O{}"]



i=2
for j in range(len(wb.sheets)):
	for k in range(12):
		for l in range(len(start)):
			#print(start[l].format(i+k,j+l))
			#print wb.sheets[j].range(start[l].format(i+k,i+k)).value
			if wb.sheets[j].range(start[l].format(i+k,i+k)).value >= -12 and wb.sheets[j].range(start[l].format(i+k,i+k)).value <0:
				wb.sheets[j].range(start[l].format(i+k,i+k)).color = (255, 150+wb.sheets[j].range(start[l].format(i+k,i+k)).value*12, 150+wb.sheets[j].range(start[l].format(i+k,i+k)).value*12)
			if wb.sheets[j].range(start[l].format(i+k,i+k)).value >= 0 and wb.sheets[j].range(start[l].format(i+k,i+k)).value <7:
				wb.sheets[j].range(start[l].format(i+k,i+k)).color = (150-wb.sheets[j].range(start[l].format(i+k,i+k)).value*24, 150-wb.sheets[j].range(start[l].format(i+k,i+k)).value*24, 255)
			if wb.sheets[j].range(start[l].format(i+k,i+k)).value < -12:
				wb.sheets[j].range(start[l].format(i+k,i+k)).color = (165,165,165)
				wb.sheets[j].range(start[l].format(i+k,i+k)).api.Font.ColorIndex = 3
			if wb.sheets[j].range(start[l].format(i+k,i+k)).value >= 7:
				wb.sheets[j].range(start[l].format(i+k,i+k)).color = (0, 0, 255)
		
		

wb.save()
app.quit()

