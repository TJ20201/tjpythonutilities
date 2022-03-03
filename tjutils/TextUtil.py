import requests

class TextUtil():
	def __init__(self):
		pass

	def generalValues():
		return {
					"alphabet": 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
					"version_general": "1.0.0",
					"version_encrypt": "1.0.0"
				}

	# Used for in-code anti list overflowing. 
	def antiOverflow(index, l):
		if index < len(l):
			return index-len(l)
		else:
			return index

	# General encryption and decryption functions.
	def valuesForCrypt():
		return {
					"chars":    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓',
					"encchars": 'GHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓ABCDEF',
					# Previous versions
					"0.0.0": "66faaf98a5fc2ee74a37e626a243b1a5dc7cd8ef"
				}
	def encrypt(text):
		alphabet = TextUtil.generalValues()["alphabet"]
		chars = TextUtil.valuesForCrypt()["chars"]
		encchars = TextUtil.valuesForCrypt()["encchars"]
		text2 = ''
		for char in text:
			cindex = chars.find(char)
			nchar = encchars[TextUtil.antiOverflow(cindex, encchars)]
			if nchar in alphabet:
				nchar = nchar.swapcase()
			text2 = text2 + nchar
		encrypted = text2[::-1]
		ret = f'!SYSARG!enc:/{TextUtil.generalValues()["version_encrypt"]}/:!' + encrypted
		return ret
	def decrypt(text):
		alphabet = TextUtil.generalValues()["alphabet"]
		chars = TextUtil.valuesForCrypt()["chars"]
		encchars = TextUtil.valuesForCrypt()["encchars"]
		if text.startswith('!SYSARG!enc:/'):
			version = text.split("/")[1]
			text = text[16+len(str(version)):]
			if version != TextUtil.generalValues()["version_encrypt"]:
				return TextUtil.decrypt_old(text, version, TextUtil.valuesForCrypt()[version])
			text2 = ''
			for char in text:
				cindex = encchars.find(char)
				nchar = chars[TextUtil.antiOverflow(cindex, chars)]
				if nchar in alphabet:
					nchar = nchar.swapcase()
				text2 = text2 + nchar
			decrypted = text2[::-1]
			return decrypted
		else:
			print('Error: Text ' + '\'' + text + '\' is not encrypted!' )

	# Handle Older Versions (0.0.0 handled separately)
	def decrypt_old(text, version, altVersion):
		rq = requests.get(f"https://raw.githubusercontent.com/TJ20201/tjpythonutilities/{altVersion}/tjutil-meta/TextUtil.json")
		if str(rq) == "<Response [404]>":
			# Backup list
			chars =    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓'
			encchars = 'GHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓ABCDEF'
		text2 = ''
		r2 = requests.get(f"https://raw.githubusercontent.com/TJ20201/tjpythonutilities/{altVersion}/tjutils/TextUtil.py")
		if version == "0.0.0":
			alphabet = TextUtil.generalValues()["alphabet"]
			text2 = ''
			for char in text:
				cindex = encchars.find(char)
				nchar = chars[TextUtil.antiOverflow(cindex, chars)]
				if nchar in alphabet:
					nchar = nchar.swapcase()
				text2 = text2 + nchar
			decrypted = text2[::-1]
			return decrypted
