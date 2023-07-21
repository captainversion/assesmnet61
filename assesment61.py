

import json
d = {"states:Capitals":[{"Arunachal Pradesh": "Itanagar"},
               {"Assam": "Dispur"},
               {"Nagland": "Kohima"},
               {"Manipur": "Imphal"},
               {"Megalaya": "Shillong"},
               {"Tripura": "Agartala"},
               {"Mizoram": "Aizawal"}]}


			   
with open("OneDrive/pyhton screen shot/indian.json","w") as file:
	json.dump(d,file)


