# TireFire
* Scalable Python tool for initial enumeration.
* TireFire is a simple enumeration platform to place your order of operations for enumeration and is easily altered to support your methodologies as they are maleated and appeneded.
* TireFire is a product of *19% security solutions.*
* ReReleased March 1 2021 with a SQLite backend for straightforward module adding.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/Tire_fire.jpg)
## Easily add modules
- Navigate to DB Browser for SQLite (Built into Kali).
- Open the TireFire.db file (File>Open Databse>Navigate to TireFire.db>Open).
- Navigate to "Browse Data" and the "Main" table.
- When adding a command, keep in mind Name, Port, and Description are for the primary display screen; Cmd_Name, Cmd_Description, Cmd_Command, Cmd_Comment, and SubDisplayOrder are for the secondary display screen.
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/2_DB.png)
## Cmd_Command Special Charachters and Syntax
- Cmd_Command has a few special charachters including &&&&, #, and {}.
- &&&& is for sending commands to multiple tabs. Example: whoami &&&& id &&&& ifconfig will open three tabs and run the desired command in each. This is useful if you initially run multiple seperate commands every time you see a specific port open. 
- "#" is for sending yourself notes to another tab. This will only work if the first charachter of the first line is #. This is useful if you don't want to run a command but you want to give yourself copy-paste notes for manual enumeration.
- {} is for grabbing a variable from TireFire. Available variables are IP, Domain_Name, Naming_Context, Web_Portlist, Big_Passwordlist, Small_Passwordlist, Big_Userlist, Small_Userlist, Big_Dirlist, Small_Dirlist.
- Use " instead of ' due to the way that the string is being passed into TireFire.
## Easy to Use
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/TireFireAction.png)
## How to build
- git clone https://github.com/CoolHandSquid/TireFire.git
- cd TireFire
- sudo /bin/bash ./Build.sh 
## Useage
* TireFire will not function well if not run as root.
* Once Build.sh has been run TireFire will have been added to your path. 
* Type "TireFire 10.10.10.5" and you will be yeeting with a cyber **cannon!**
![alt text](https://github.com/CoolHandSquid/TireFire/blob/master/Images/CoolHandSquid.jpg)
## Contact
Please contact me at CoolHandSquid32@gmail.com for suggestions and ideas!













