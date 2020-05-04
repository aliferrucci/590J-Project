# 590J-Project
## Description:
Our attack gains access to Windows 7 systems through access to a malicious PDF.  This access is used to implant crypto mining software that will run in the background and/or exfiltrate encrypted data from the victim machine.


## A hypothetical use case of their project:
Attackers would use this attack to take advantage of the unreliable information about COVID-19 passed around. We are targeting people who want updated information about the disease but are not technically savvy to check the authenticity of the source email and would download an informational pdf. These sorts of people will not check the background processes which will mine crypto currency and steal important files.
The target is college students who leave their computers running a lot and won’t notice a background process taking up resources.  


## What the implant does:
The implant opens a shell through Adobe Reader 8.1.2 that connects to Meterpreter on our host Kali machine. This allows us to escalate our privileges and permit us to begin running mining software in the background of the victim computer and run another script that allows us to grab files on the victim’s filesystem and exfil them back to our host machine.


## How the implant is injected into the target device:
The implant is executed by creating a spear phishing link attack: setting up a SMTP to spoof our email address to appear like the email came from a legitimate source. For example, in our hypothetical use case, the spoofed email would be the CDC sending out information about COVID-19. Within the email is a pdf file, in our case an information sheet, which has been modified using Metasploit. The pdf has a payload which will allow for remote shell access of the victim's computer. Once the victim receives the pdf and downloads it, the payload will activate and give us powershell access. From the shell we can inject our crypto currency software and exfil script.


## How the implant is hidden on the device:
The implant is initially hidden with the pdf and when opened, it opens a remote shell which the victim cannot see nor know what the remote shell is doing. The files left behind will be in folders your average user will never open or even know about.  In order to get to the startup folder you have to go through the AppData folder, which is normally hidden on Windows systems.  Most things below a hidden folder on the directory tree will never be seen by a normal user.  In addition, the exfil script has been named ‘desktop.ini’ which is the default file that exists in the startup folder.


## How the implant is controlled and how that communication is obfuscated:
After gaining initial access, the implant is crafted for each host machine to exfil data from the appropriate directory of interest.  The implant is actually controlled by the user unknowingly, as it runs on startup and will not be detected.  Every time they start up their machine, the implant is activated and begins mining and exfiling data.  Communication to the victim is hidden because we are not connecting to them or sending any signals, our exploit creates a backdoor connected to a remote server to upload their files or mine bitcoin.


## How the data exfil communication is obfuscated:
Exfill communication is encrypted before sent to our C2. This means if anything is scanning the network to see what information is being sent, they will only see encrypted junk, that has no meaning. With this, it is impossible to tell that it is your files being sent over the network.  In addition, by randomizing the type of file that gets exfiltrated each time, we can avoid pattern recognition of the same traffic going to the same place on startup each time.
In addition, we are having the victim machine mine bitcoin.  One of the goals of Crypto Currency is to be anonymous and decentralized.  Even if the mining were to be discovered it points to an anonymous wallet, not a bank account or anything registered with a central authority.




## From Start to Finish, Mapped Against the ATT&CK framework, our exploit works as follows:
 
### Initial Access: Spearphishing Attachment (T1193)
We gain initial access to the target system with a targeted email campaign.  Using the Social Engineering Toolkit through Kali and an SMTP Server we have access to on port 2525, we are able to send emails with duped FROM addresses.  This increases the trust a victim has in the email and reduces their suspicion of attachments.  Given the current environment we thought it wise to use people’s desire for information and guidance on COVID19 to our advantage and send emails from the CDC with PDF’s attached that contains information about the virus.
 
### Execution: User Execution (T1204)
The execution of the payload is reliant on the user to open the PDF that was sent to them.  Since we are targeting Windows 7 Machines, we are counting on them having older versions of Adobe Reader.  Opening the PDF 

### Persistence: Logon Scripts (T1037)
Files were uploaded to the startup directory in the windows system to achieve persistence.  The scripts in the startup directory will run automatically whenever the user logs onto the machine.  This either, depending on the victim, exfil’s files, or starts up the mining software.
 
### Privilege Escalation: Process Injection (T1055)
In the reverse shell a payload is delivered that is based on Process Injection.  It exploits a weakness that allows for Process Injection into applications that are signed with the Windows Publisher Certificate.  It will spawn a second shell that has the UAC flag turned off.
 
### Defense Evasion: Bypass User Access Control (UAC) (T1088)
This allows us to perform Administrator level tasks without the target being prompted for a password.
 
### Discovery: File and Directory Discovery (T1083)
With the reverse shell we can navigate user’s file structure to locate directory of interest for exfil.
 
### Collection: Data from local resources (T1005)
We will find a local directory that contains files of interest and customize our payload to exfil the contents of that file.
 
### Command and Control: Remote File Copy (T1105)
With our initial access we copy files onto the victim machine that will connect to our listener and upload files whenever the user logs on.  The script only uploads new documents and alternates uploading different types of documents.
 
### Exfil: Automated Exfiltration (T1020)
Files are automatically encrypted and exfiltrated from the victim machine every time they log on.
 
### Impact: Resource Hijacking (T1496)
We use the victim machines resources, specifically the CPU, to mine crypto currency and reap the rewards ourselves.
 
