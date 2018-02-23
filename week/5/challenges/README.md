Pentesting II
======

## Assignment details

This assignment has two parts. It is due by 3/1 at 11:59 PM.
To submit your homework, please post your responses as either a public note **or** as a link
to your publicly available writeup on Piazza.


**There will be a late penalty of 5% off per day late!**

### Part 1

*Note:* We're currently experiencing some problems with the VPN and we're working to resolve them ASAP.
If you are accessing these challenges from within the campus network, please private message us to let us know
about this and we will help get you connected to the challenges ASAP. Otherwise, continue working on part 2,
and let us know if you have any questions. Thanks for your patience with this.


Mark has now implemented some of the precautions described in your previous assignment, such as:

    - Closed port 1337
    - Changed his password
    - Upgraded his firewall, IDS and IPS
    - Increased his password size

With all these upgrades, Mark boasts that his company's security posture is now more stronger than ever and that his site is totally impenetrable.
In fact, Mark recently told us that he is constantly logging into the Briong "hidden" admin panel to check if his site has been compromised, and so
far, he claims that it hasn't.

Your task is to show Mark that he still has work to do! Find Mark's password, locate the flag and (try to) crack the easter egg!

Note: If you're connecting to the server on UMD campus, we suggest using our class VPN in order to complete this assignment. Kali Linux already ships with the OpenVPN client, however if you do not already have it, simply run:

    $ apt-get install -y openvpn

Once that is complete, download the OpenVPN profile (`client.ovpn.zip`) within Kali and run:

    $ unzip client.ovpn.zip

Enter the password provided in class...

    $ openvpn <path to client.ovpn file>

This will start a VPN tunnel to our class server where you will be able to run the exploits in our contained environment.
Once connected to the VPN, you will only be able to access the class server and will not be able to access the outside internet.
To make sure you are connected to our VPN, open a new terminal window and type:

    $ curl briong.com

Which will make a request to http://briong.com to verify that your web traffic is being routed through our VPN properly. Similarly, you may open
the Firefox web browser within Kali Linux and navigate to the briong website.

Let us know if you are having trouble connecting to the VPN.

### Part 2

Mark has decided to offer a new service to his customers that allows for them to detect if their servers are up or down at any given time.
In fact, Mark claims that his new solution is inherently secure because it uses the Linux `ping` command to do the uptime checking instead of using a web-based OSINT solution.

However, there are rumors that Mark's new service is vulnerable to a [Command Injection](https://www.owasp.org/index.php/Command_Injection) attack.
Can you prove to Mark that his new uptime system isn't as secure as he claims? If you can, go and get the flag!

main server:    `nc briong.com 45`

backup server:  `nc irc.csec.umiacs.umd.edu 45`

For full credit, write up (step-by-step) how you got the flag and what Mark should do to protect from this vulnerability.

You will earn full credit for answering these questions:
1. The right flag
2. Showing what input you used to obtain the flag.
3. Describing your thought process.
4. Any suggested precautions Mark could implement to prevent this vulnerability (hint: can you find the script that Mark uses to check if a customer's server is up?)

### Format

All two parts should be written in the same blog post, clearly separated.
Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

Part 1 is worth 50 points, part 2 is worth 50.

### Tips

Look through the slides from lecture 4 and 5 for guidance. Let us know if you have any questions.

Good luck!
