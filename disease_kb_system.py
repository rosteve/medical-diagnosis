from pyknow import *

################################################################################################################################################
#  INSTALLATION 

# For this project to run, you need to have a python package known as 'Pyknow'

# First ensure you have Python installed and also pip installed https://pip.pypa.io/en/stable/installing/)

# once you have pip installed, you can install pyknow as below:

# steps to installing pyknow:
# 1. Download or git clone pyknow git repository from this link -> https://github.com/buguroo/pyknow 
# 2. Once downloaded/cloned .. navigate on the terminal/command line to inside pyknow folder then run the command below: 
#                       pip install .


#    Running 'pip install .' will install this package

# To run my project, navigate inside the unzipped folder and run this command below:
#>               python disease_kb_system.py

# If using python3 run the program throught this command: python3 disease_kb_system.py


# This will run the system and respond to each question by typing 'yes' or 'no'
# The expert system will fire the rule that has the exact symptoms or the closes rule if not perfectly matching.

################################################################################################################################################



class findDisease(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Community health diagnosis Knowledge Based System ".center(100, "*"))
		print("Hey there! I am Dr. Stephine, I am here to help you make your health better.")
		print("Please help me know by answering some questions about the conditions you're experiencing")
		print("Do you feel any of the symptoms listed below:")
		print("(Answer by typing in full either yes or no)")
		print("_".center(100, "*"))
		print("")
		yield Fact(action="findDisease")

################################################################################################################################################
#  We give rules a Salience of 1 so that they are executed first before the other rules with a default salience zero are executed.
#  These rules pick the fact through user input using the function "input()" then rules that contain the knowledge get compared on
#  and the most satisfying rule becomes the most probable disease the patient is suffering from.
################################################################################################################################################

	@Rule(Fact(action='findDisease'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache=input("headache: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(back_pain=input("back pain: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(chest_pain=input("chest pain: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(cough=input("cough: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(fainting=input("fainting: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(fatigue=input("fatigue: ")))
	 
	@Rule(Fact(action='findDisease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sunken_eyes=input("sunken eyes: ")))
	
	@Rule(Fact(action='findDisease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(low_body_temp=input("low body temperature: ")))
	
	@Rule(Fact(action='findDisease'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(restlessness=input("restlessness: ")))
	
	@Rule(Fact(action='findDisease'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(sore_throat=input("sore throat: ")))
	
	@Rule(Fact(action='findDisease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fever=input("fever: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(nausea=input("Nausea: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(blurred_vision=input("blurred_vision: ")))

	@Rule(Fact(action='findDisease'), NOT(Fact(diffulty_breathing=W())),salience = 1)
	def symptom_13(self):
		self.declare(Fact(diffulty_breathing=input("difficulty in breathing: ")))
		
##################################################################################################
#
# Knowledge base, I use the rules below to determine the disease the patient is suffering from. 
#
##################################################################################################


	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def tb(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def asthma(self):
		self.declare(Fact(disease="Asthma"))

	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="yes"))
	def corona(self):
		self.declare(Fact(disease="Corona Virus"))

	@Rule(Fact(action='findDisease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def sinusitis(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def epilepsy(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def heartDisease(self):
		self.declare(Fact(disease="Heart Disease"))
	
	@Rule(Fact(action='findDisease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"),Fact(diffulty_breathing="no"))
	def arthritis(self):
		self.declare(Fact(disease="Arthritis"))



    # Giving it a negative salience so that it will be executed after all the previous rules have been executed.
	@Rule(Fact(action='findDisease'),Fact(disease=MATCH.disease),salience = -998)
	def foundExactDisease(self, disease):
		print("_".center(100, "*"))
		print("")
		id_disease = disease
		treatments = getDiseaseTreatments(id_disease)
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

	@Rule(Fact(action='findDisease'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)
	def notExactDisease(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("_".center(100, "*"))
		print("\nDid not find any disease that matches your exact symptoms provided")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		max_count = 0
		max_disease = ""
		for key,val in symptomMap.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		getClosestDisease(max_disease)


# Variables initialization.
allDiseases = []
symptomMap = {}
diseaseTreatmentMap = {}


# Defining the functions to be used.
def fetchAndReadData():
	global allDiseases,symptoms,symptomMap,diseaseDescriptionMap,diseaseTreatmentMap
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	allDiseases = diseases_t.split("\n")
	diseases.close()
	for disease in allDiseases:
		disease_s_file = open("symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		symptomMap[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		diseaseTreatmentMap[disease] = disease_s_data
		disease_s_file.close()
	

def getDisease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptomMap[str(symptom_list)]

def getDiseaseTreatments(disease):
	return diseaseTreatmentMap[disease]

def getClosestDisease(disease):
		print("")
		id_disease = disease
		treatments = getDiseaseTreatments(id_disease)
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

if __name__ == "__main__":
	fetchAndReadData()
	engine = findDisease()
	while(1):
		engine.reset()
		engine.run()
		print("_".center(100, "*"))
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()