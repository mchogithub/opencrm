from django.contrib import admin
from opencrm.models import Account, Bank, Bank_branch, City

class AccountAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['crm_code']}),
		('Generalità', {'fields': ['firstname', 'lastname', 'birth_date','birth_city','nationality', 'sex']}),
		('Contatti', {'fields': ['phone', 'other_phone', 'email']}),
		('Documento d\'identità', {'fields': ['identity_doc_number','identity_doc_date'], 'classes': ['collapse']}),
		('Coordinate bancarie', {'fields': ['bank_branch', 'checking_account', 'checking_account_control','iban']}),
		('Codici', {'fields': ['crm_vat_registration_number', 'crm_social_security_number'], 'classes': ['collapse']}),
		('Società', {'fields': ['legal_rep_firstname', 'legal_rep_lastname', 'headquarter_address','headquarter_number','headquarter_postcode','company_type']}),
	]
	list_display = ('crm_code','lastname','firstname')
	list_filter = ['birth_date']
	search_fields = ['lastname']

class Bank_branchAdmin(admin.ModelAdmin):
	list_display = ('bank', 'bank_branch')

class CityAdmin(admin.ModelAdmin):
	list_display = ('city', 'municipality', 'district','country')

admin.site.register(Account, AccountAdmin)
admin.site.register(Bank_branch, Bank_branchAdmin)
admin.site.register(Bank)
admin.site.register(City, CityAdmin)