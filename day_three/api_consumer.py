# -*- coding: utf-8 -*-
# #I will build a tool that would convert currency based on the current market values.
import urllib
import json


def exchange_value_compute(currency,amount):
	"""
	Converts Euros into the following global currencies
	---------------------------------------------------
	USD ,IDR ,BGN ,ILS ,GBP ,DKK ,CAD ,JPY ,HUF ,RON ,
	MYR ,SEK ,SGD ,HKD ,AUD ,CHF ,KRW ,CNY ,TRY ,HRK ,
	NZD ,THB ,NOK ,RUB ,INR ,MXN ,CZK ,BRL ,PLN ,PHP ,
	ZAR ,
	---------------------------------------------------
	"""
	my_request = urllib.urlopen("http://api.fixer.io/latest")
	rates_request = json.loads(my_request.read())
	for values in rates_request["rates"]:
		if currency in values:
			current_value = amount * rates_request["rates"][currency]
	return "%s Euros is currently equal to %s %s."%(amount,current_value,currency)