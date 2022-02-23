class TextUtil():
	def __init__(self):
		pass

	def generalValues():
		return {
					"alphabet": 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
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
					"encchars": 'GHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`!\"£$%^&*()_+{}~:/@<>?[];\',./#\\|=-▲▼↑↓ABCDEF'
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
		ret = '!SYSARG!enc:/:!' + encrypted
		return ret
	def decrypt(text):
		alphabet = TextUtil.generalValues()["alphabet"]
		chars = TextUtil.valuesForCrypt()["chars"]
		encchars = TextUtil.valuesForCrypt()["encchars"]
		if text.startswith('!SYSARG!enc:/:!'):
			text = text.replace('!SYSARG!enc:/:!', '')
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