from django.db import models

class Account(models.Model):
	crm_code = models.CharField("Codice NWG", max_length=255)
	#name = models.CharField(max_length=255)
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	birth_date = models.DateField()  
	birth_city = models.ForeignKey('City')
	nationality = models.CharField(max_length=255)    
	phone = models.CharField(max_length=255)
	other_phone = models.CharField(max_length=255, null=True, blank=True) 
	email = models.CharField(max_length=255)
	sex = models.CharField(max_length=1)
	crm_vat_registration_number = models.CharField(max_length=255, null=True, blank=True)
	crm_social_security_number = models.CharField(max_length=255, null=True, blank=True)
	legal_form = models.CharField(max_length=255)
	#pricebook_id = models.IntegerField(max_length=19)
	bank_branch = models.ForeignKey('Bank_branch')
	checking_account = models.CharField(max_length=255)
	checking_account_control = models.CharField("CIN", max_length=255, null=True, blank=True) #CIN
	iban = models.CharField(max_length=255)
	legal_rep_firstname = models.CharField(max_length=255, null=True, blank=True)
	legal_rep_lastname = models.CharField(max_length=255, null=True, blank=True)
	#customer_firstname = models.CharField(max_length=255)
	#customer_lastname = models.CharField(max_length=255)
	identity_doc_number = models.CharField(max_length=25)
	identity_doc_date = models.DateField()
	identity_doc_city = models.ForeignKey('City', related_name='identity_doc_city', null=True, blank=True)
	headquarter_address = models.CharField(max_length=255, null=True, blank=True)
	headquarter_number = models.CharField(max_length=20, null=True, blank=True)
	headquarter_postcode = models.CharField(max_length=10, null=True, blank=True)
	company_type = models.CharField(max_length=40, null=True, blank=True)
	def __str__(self):
		return self.crm_code

class Bank_branch(models.Model):
	bank = models.ForeignKey('Bank', verbose_name="Banca")
	bank_branch = models.CharField("Filiale", max_length=255)
	bank_brach_code = models.CharField("CAB", max_length=255) #CAB
	def __str__(self):
		return self.bank_branch	

class Bank(models.Model):
	bank = models.CharField(max_length=255)
	bank_code = models.CharField("ABI", max_length=255) #ABI
	def __str__(self):
		return self.bank

class City(models.Model):
	city = models.CharField(max_length=255)
	municipality = models.CharField(max_length=255)
	district = models.CharField(max_length=255, null=True, blank=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.city