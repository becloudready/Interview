# SFTP setup in aws ec2 (ubuntu)

sudo apt update && sudo apt install openssh-server 
sudo adduser --shell /bin/false sftpuser 
sudo mkdir -p /var/sftp/files 
sudo chown sftpuser:sftpuser /var/sftp/files 
sudo chown root:root /var/sftp 
sudo chmod 755 /var/sftp 
sudo vim /etc/ssh/sshd_config 

	Match User sftpuser
	ForceCommand internal-sftp
	PasswordAuthentication yes
	ChrootDirectory /var/sftp
	PermitTunnel no
	AllowAgentForwarding no
	AllowTcpForwarding no
	X11Forwarding no
	
sudo sshd -t 
sudo systemctl restart ssh 
