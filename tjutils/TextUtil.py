class TextUtil():
	def __init__(self):
		pass

	def generalValues(self):
		return {
					"alphabet": 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
				}

	# Used for in-code anti list overflowing. 
	def antiOverflow(self, index, l):
		if index < len(l):
			return index-len(l)
		else:
			return index

	# General encryption and decryption functions.
	def valuesForCrypt(self):
		return {
					"chars":    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓',
					"encchars": 'GHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓ABCDEF'
				}
	def encrypt(self, text):
		alphabet = TextUtil.generalValues(self)["alphabet"]
		chars = TextUtil.valuesForCrypt(self)["chars"]
		encchars = TextUtil.valuesForCrypt(self)["encchars"]
		text2 = ''
		for char in text:
			cindex = chars.find(char)
			nchar = encchars[TextUtil.antiOverflow(self, index=cindex, l=encchars)]
			if nchar in alphabet:
				nchar = nchar.swapcase()
			text2 = text2 + nchar
		encrypted = text2[::-1]
		ret = '!SYSARG!enc:/:!' + encrypted
		return ret
	def decrypt(self, text):
		alphabet = TextUtil.generalValues(self)["alphabet"]
		chars = TextUtil.valuesForCrypt(self)["chars"]
		encchars = TextUtil.valuesForCrypt(self)["encchars"]
		if text.startswith('!SYSARG!enc:/:!'):
			text = text.replace('!SYSARG!enc:/:!', '')
			text2 = ''
			for char in text:
				cindex = encchars.find(char)
				nchar = chars[TextUtil.antiOverflow(self, index=cindex, l=chars)]
				if nchar in alphabet:
					nchar = nchar.swapcase()
				text2 = text2 + nchar
			decrypted = text2[::-1]
			return decrypted
		else:
			print('Error: Text ' + '\'' + text + '\' is not encrypted!' )
