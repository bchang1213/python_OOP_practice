
# Blueprints the patients.
class Patient(object):
	numb_of_patients = 0
	def __init__(self,name,allergies):
		self.name = name
		self.allergies = allergies
		self.id = Patient.numb_of_patients
		self.bed_number = 0

		Patient.numb_of_patients += 1
		self.patientinfo()

# This is a method to display the information of a patient for
# everytime that a patient is initialized.
	def patientinfo(self):
		print "\n" + ("#" * 20)
		print "Patient info"
		for attr,val in self.__dict__.iteritems():
			print "{}: {}".format(attr, val)
		print "#" * 20


class Hospital(object):
	def __init__(self, name, capacity):
		self.patientlist = []
		self.name = name
		self.capacity = capacity - len(self.patientlist)
		self.hospitalinfo()

	def hospitalinfo(self):
		print "#" * 20
		print "Hospital info"
		for attr,val in self.__dict__.iteritems():
			print "{}: {}".format(attr, val)
		print "#" * 20
		print "\n"

	def admit(self, patient):
		if self.capacity > 0:
			self.patientlist.append(patient)
			patient.bed_number += self.capacity
			self.capacity -= 1
			print "Admission for",patient.name,"is complete."
			self.hospitalinfo()
		else:
			print "We're sorry, the hospital is full."
		return self

	def lookup(self):
		print "\n" + ("#" * 20)
		print "Patient List"
		print "#" * 20

		for x in self.patientlist:
			print "#" * 20
			for key,value in x.__dict__.iteritems():
				print key,value
		print "\n" + ("#" * 20)

	def discharge(self, patient):
		print "\n" + ("#" * 20)
		print "Discharged - New Patient List"
		print "#" * 20

		for x in self.patientlist:
			print "#" * 20
			for key,value in x.__dict__.iteritems():
				if key == "name" and value == patient:
					x.bed_number = 0
					self.patientlist.remove(x)
					print "Patient",x.name,"has been removed and his bed number is",x.bed_number,"."
			else:
				"Please look up and enter patient's exact name."


patient = Patient("Brian","pollen")
patient2 = Patient("Kyle", "weeds")
patient3 = Patient("Jorge", "cats")

hospital = Hospital("Sacred Heart", 3)

hospital.admit(patient).admit(patient2).admit(patient3)

hospital.discharge("Jorge")

hospital.lookup()