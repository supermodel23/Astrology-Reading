from flask import Flask, render_template

AAFinalProject = Flask(__name__)

@AAFinalProject.route('/')
def astrology():
	return sign, compat_sign

astro_dict = {"Aries":  "Adventurous and energetic, Pioneering and courageous, Enthusiastic and confident,\n Dynamic and quick-witted, Selfish and quick-tempered, Impulsive and impatient, Foolhardy and daredevil\n",
"Taurus": "Patient and reliable, Warmhearted and loving, Persistent and determined, Placid and security loving,  Jealous and possessive, Resentful and inflexible, Self-indulgent and greedy\n"	,
"Gemini": "Adaptable and versatile, Communicative and witty, Intellectual and eloquent, Youthful and lively,  Nervous and tense, Superficial and inconsistent, Cunning and inquisitive\n " ,
"Cancer":  "Emotional and loving, Intuitive and imaginative, Shrewd and cautious, Protective and sympathetic,  Changeable and moody, Overemotional and touchy, Clinging and unable to let go\n ",	
"Leo": "Generous and warmhearted, Creative and enthusiastic, Broad-minded and expansive, Faithful and loving,  Pompous and patronizing, Bossy and interfering, Dogmatic and intolerant\n",
"Virgo": "Modest and shy  Meticulous and reliable,  Practical and diligent,  Intelligent and analytical,   Fussy and a worrier,  Overcritical and harsh,  Perfectionist and conservative",
"Libra": "Diplomatic and urbane,  Romantic and charming,  Easygoing and sociable,  Idealistic and peaceable,   Indecisive and changeable,  Gullible and easily influenced, Flirtatious and self-indulgent\n ",
"Scorpio": "Determined and forceful,  Emotional and intuitive,  Powerful and passionate,  Exciting and magnetic,   Jealous and resentful,  Compulsive and obsessive,  Secretive and obstinate\n ",
"Sagittarius": "Optimistic and freedom-loving,  Jovial and good-humored,  Honest and straightforward,  Intellectual and philosophical,   Blindly optimistic and careless,  Irresponsible and superficial,  Tactless and restless\n ",
"Capricorn": "Practical and prudent,  Ambitious and disciplined,  Patient and careful,  Humorous and reserved,   Pessimistic and fatalistic,  Miserly and grudging\n ",
"Aquarius": "Friendly and humanitarian,  Honest and loyal,  Original and inventive,  Independent and intellectual,   Intractable and contrary,  Perverse and unpredictable,  Unemotional and detached\n 	",
"Pisces": "Imaginative and sensitive,  Compassionate and kind,  Selfless and unworldly,  Intuitive and sympathetic,   Escapist and idealistic,  Secretive and vague,  Weak-willed and easily led\n",
}

Compatibility_dict= {"Aries": "Aries is the passionate firebrand of the zodiac, with every second filled with excitement.Your Perfect Partner - Leo & Sagittarius. A Very Close Match - Gemini. Your Soulmate - Aries. Opposites Attract - Virgo & Scorpio. You guys have your differences - Pisces & Taurus. Going to Need Some Work - Cancer & Capricorn. Don't even bother - Libra" , 
"Taurus": "Taurus is the home maker of the zodiac,looking for secuity rather than excitement in their lovelife. Your Perfect Partner - Virgo & Capricorn. A Very Close Match - Cancer & Pisces.Your Soulmate - Taurus. Opposites Attract - Libra & Sagittarius. You guys have your differences - Aries & Gemini. Going to Need Some Work - Leo & Aquarius. Don't even bother - Scorpio" ,
"Gemini": "Geminis are lively and happy, and are the most fascinating and enjoyable lovers of the zodiac. Your Perfect Partner - Libra & Aquarius. A Very Close Match - Aries & Leo. Your Soulmate - Gemini. Opposites Attract - Scoprio & Capricorn. You guys have your differences - Taurus & Cancer. Going to Need Some Work - Virgo & Pisces. Don't even bother - Sagittarius" ,
"Cancer": "Once past the hard outer-shell, Cancerians are the most sensitive lovers of the zodiac. Your Perfect Partner - Scorpio & Pisces.  A Very Close Match - Taurus & Virgo.  Your Soulmate - Cancer. Opposites Attract - Sagittarius & Aquarius. You guys have your differences - Gemini & Leo. Going to Need Some Work - Aries & Libra. Don't even bother - Capricorn" ,
"Leo": "Leos like to be the lively centre of attention. There is never a dull moment with a Leo.  Your Perfect Partner - Aries & Sagittarius. A Very Close Match - Gemini.  Your Soulmate - Leo. Opposites Attract - You guys have your differences - Cancer & Virgo. Going to Need Some Work - Scorpio & Taurus. Don't even bother - Aquarius" ,
"Virgo": "Virgos are faithful and trustworthy in love. Deeply committed to their lover, they are more practical than romantic. Your Perfect Partner - Taurus & Capricorn. A Very Close Match - Cancer & Scorpio. Your Soulmate - Virgo. Opposites Attract - Aries & Aquarius. You guys have your differences - Leo & Libra. Going to Need Some Work - Gemini & Sagittarius. Don't even bother - Pisces" ,
"Libra": "Librans are big romantics. With great empathy for their lover, they make the most thoughtful partners. Your Perfect Partner - Gemini & Aquarius. A Very Close Match - Leo & Sagittarius. Your Soulmate - Libra. Opposites Attract - Taurus & Pisces. You guys have your differences - Virgo & Scorpio. Going to Need Some Work - Cancer & Capricorn. Don't even bother - Aries" ,
"Scorpio": "Scoprpios are the most passionate and loyal of the zodiac. They are real believers in love at first sight. Your Perfect Partner - Cancer and Pisces. A Very Close Match - Virgo and Capricorn. Your Soulmate - Scorpio. Opposites Attract - Aries and Gemini. You guys have your differences - Libra and Sagittarius. Going to Need Some Work - Leo and Aquarius. Don't even bother - Taurus" ,
"Sagittarius": "Endearingly frank and innocent, Sagittarians are pretty straightforward when it comes to love. Your Perfect Partner - Aries and Leo. A Very Close Match - Libra, Aquarius. Your Soulmate - Sagittarius. Opposites Attract - Taurus and Cancer. You guys have your differences - Scorpio and Capricorn. Going to Need Some Work - Virgo and Pisces. Don't even bother - Gemini" ,
"Capricorn": "Capricorns are wary of falling in love at first, but once they fall for their loved one, they are loyal for life. Your Perfect Partner - Taurus and Virgo. A Very Close Match - Scorpio and Pisces. Your Soulmate - Capricorn. Opposites Attract - Gemini and Leo. You guys have your differences - Sagittarius and Aquarius. Going to Need Some Work - Aries and Libra. Don't even bother - Cancer" ,
"Aquarius": "Whilst exciting and wild lovers, Aquarians aren't necessarily the most sentimental and romantic of the zodiac. Your Perfect Partner - Gemini and Libra. A Very Close Match - Aries and Sagittarius. Your Soulmate - Aquarius. Opposites Attract - Cancer and Virgo. You guys have your differences - Capricorn and Pisces. Going to Need Some Work - Taurus and Scorpio. Don't even bother - Leo" ,
"Pisces": "Pisces are deeply romantic daydreamers. Incredibly sentimental, Pisces will shower their lovers with love. Your Perfect Partner - Cancer and Scorpio. A Very Close Match - Capricorn and Taurus. Your Soulmate - Pisces. Opposites Attract - Leo and Libra. You guys have your differences - Aries and Aquarius. Going to Need Some Work - Gemini and Sagittarius. Don't even bother - Virgo"}

goodbye_msg = "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding!\n"

def astro_reading():

	print "\n"+ "Hello! Welcome to your free astrology reading by April & Annette, by way of python.\n"
	name = raw_input('What is your name?\n')

	print "\n"+'Hello ' + name
	print "\n"+'Tell us your birthday to learn your astrological sign and personality traits\n'
	sign_reading = raw_input('Do you want to know what your astrological sign is? Type Yes or No.\n')
	sign_reading = sign_reading.lower()

	if sign_reading=='yes' or sign_reading=='YES' or sign_reading=='y':
	 	print "\n Awesome, let's get started! We need to know your birthday. \n" 
	 	month = raw_input('Tell us your birth month. Make sure to type the full month i.e. December NOT Dec\n')
	 	month = month.lower()


		try:
			if int(month) > 0:
	 			print 'We need full month name, not the month number. Thank you.'
	 			month = raw_input('Tell us your birth month. Make sure to type the full month i.e. December NOT Dec\n')
	 			month = month.lower()
		except:
		 	pass


	 	day = raw_input('Tell us the day of the month your were born \n')
	 	day = int(day)
	 	print "\n"
	 	print month, day
	 	

		if month == "march" and day >= 21 or month == "april" and day <=20:
			sign = "Aries"
			print "You're an Aries!\n"
			print astro_dict ["Aries"] 
		if month == "april" and day >= 21 or month == "may" and day <=21:
			sign = "Taurus"
			print "You're an Taurus! \n"
			print astro_dict ["Taurus"]
		if month == "may" and day >= 21 or month == "june" and day <=21:
			sign = "Gemini"
			print "You're a Gemini!\n "
			print astro_dict ["Gemini"]
		if month == "june" and day >= 22 or month == "july" and day <=22:
			sign = "Cancer"
			print "You're a Cancer! \n"
			print astro_dict ["Cancer"]
		if month == "july" and day >= 23 or month == "august" and day <=21:
			sign = "Leo"
			print "You're a Leo\n! "
			print astro_dict ["Leo"]
		if month == "august" and day >= 22 or month == "september" and day <=23:
			sign = "Virgo"
			print "You're a Virgo!\n"
			print astro_dict ["Virgo"]
		if month == "september" and day >= 24 or month == "october" and day <=23:
			sign = "Libra"
			print "You're a Libra!\n"
			print astro_dict ["Libra"]
		if month == "october" and day >= 24 or month == "november" and day <=22:
			sign = "Scorpio"
			print "You're a Scorpio!\n"
			print astro_dict ["Scorpio"]
		if month == "november" and day >= 23 or month == "december" and day <=22:
			sign = "Sagittarius"
			print "You're a Sagittarius!\n"
			print astro_dict ["Sagittarius"]
		if month == "december" and day >= 23 or month == "january" and day <=20:
			sign = "Capricorn"
			print "You're a Capricorn!\n"
			print astro_dict ["Capricorn"]
		if month == "january" and day >= 21 or month == "february" and day <=19:
			sign = "Aquarius"
			print "You're an Aquarius!\n"
			print astro_dict ["Aquarius"]
		if month == "february" and day >= 20 or month == "march" and day <=20:
			sign = "Pisces"
			print "You're a Pisces!\n"
			print astro_dict ["Pisces"]
			

			print "\n We aren't done yet."
	else:
		print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding!"

		

	Compatibility = raw_input('Do you want to know what sign you are or are not compatible with? Type Yes or No.\n')
	if Compatibility =='Yes' or Compatibility=='yes' or Compatibility=='YES' or Compatibility=='Y':
		if sign == "Aries":
			compat_sign = Compatibility_dict ["Aries"]
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Taurus":
			compat_sign = Compatibility_dict ["Taurus"]
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"  
		if sign == "Gemini":
			compat_sign =Compatibility_dict ["Gemini"]  
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Cancer":
			compat_sign = Compatibility_dict ["Cancer"]  
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Leo":
			compat_sign = Compatibility_dict ["Leo"] 
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Virgo":
			compat_sign = Compatibility_dict ["Virgo"]  
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Libra":
			compat_sign = Compatibility_dict ["Libra"]  
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Scorpio":
			compat_sign = Compatibility_dict ["Scorpio"]  					
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Sagittarius":
			compat_sign = Compatibility_dict ["Sagittarius"] 
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Capricorn":
			compat_sign = Compatibility_dict ["Capricorn"]  
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Aquarius":
			compat_sign = Compatibility_dict ["Aquarius"]  	 		
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
		if sign == "Pisces":
			compat_sign = Compatibility_dict ["Pisces"] 
			#print "\nThank you for your time. We hope you had fun! Go to www.hackbrightacademy.com to learn more about coding! And good luck looking for your best mate.\n"
			
	
		return  compat_sign, sign

	else:
		print goodbye_msg
	

@AAFinalProject.route('/')
def astro_web():
	return sign, compat_sign

print astro_reading()
print goodbye_msg

if __name__ == '__main__':
	astro_web()
	astro_reading()
	AAFinalProject.run()

