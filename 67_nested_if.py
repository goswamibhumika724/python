#  write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
#     Aries: March 21–April 19
#     Taurus: April 20–May 20
#     Gemini: May 21–June 21
#     Cancer: June 22–July 22
#     Leo: July 23–August 22
#     Virgo: August 23–September 22
#     Libra: September 23–October 22
#     Scorpio: October 24–November 21
#     Sagittarius: November 22–December 21
#     Capricorn: December 22–January 19
#     Aquarius: January 20–February 18
#     Pisces: February 19–March 20
date = int(input('enter birth date'))
month = int(input('enter birth month'))
if (month==3 and date>=21) or (month==4 and date<=19):
    print('you are aries')
elif (month==4 and date>=20) or (month==5 and date<=20):
    print('you are taurus')
elif (month==5 and date>=21) or (month==6 and date<=21):
    print('you are gemini')
elif (month==6 and date>=22) or (month==7 and date<=22):
    print('you are cancer')
elif (month==7 and date>=23) or (month==8 and date<=22):
    print('you are leo')
elif (month==8 and date>=23) or (month==9 and date<=22):
    print('you are virgo')
elif (month==9 and date>=23) or (month==10 and date<=22):
    print('you are libra')
elif (month==10 and date>=24) or (month==11 and date<=21):
    print('you are scorpio')
elif (month==11 and date>=22) or (month==12 and date<=21):
    print('you are sagittarius')
elif (month==12 and date>=22) or (month==1 and date<=19):
    print('you are capricorn')
elif (month==1 and date>=20) or (month==2 and date<=18):
    print('you are aquarius')  
elif (month==2 and date>=19) or (month==3 and date<=20):
    print('you are pisces')   
                               
