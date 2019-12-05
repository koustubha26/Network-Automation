# Network-Automation

The primary aim of the project is to developed a Python script to automate Telnet & IP address assignment to
all interfaces. I simulated the network design in GNS3. It involves connecting hosts on a cloud to each of the routers that they want to access. In the network, it is shown as a straight through cable connecting network cloud to router interfaces. Instead of configuring each individual router with the necessary commands, it is better to configure all routers at once taking advantage of IP addresses of connecting interfaces. 

The "Initial-config-files" repo contains files assign telnet and enable passwords, assign IP addresses to the interfaces that connect host network to each of the routers. The "IP-Address-Assignment" repo has files that contain IP address configuration for the interfaces of each of the routers.

I validated the script by varying number of routers in a network & examining changes in running configurations of routers. I started off by taking 2 routers and tried the automating process of Telnet and IP address assignment. Then, I changed to 4 router scenario by making necessary changes to the code. I incremented the router count to 10 and simulated the design for all the 3 cases on GNS3. Then, I generalized the scenario to N-router case and proved the efficacy of my algorithm. The sample scenario diagram simulated in GNS3 for 4 router case is uploaded in the repository.
