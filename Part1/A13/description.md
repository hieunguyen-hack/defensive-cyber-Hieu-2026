
1.Bitwarden:

Bitwarden is an online password manager that securely stores and synchronizes encrypted credentials across devices.
1st step: Encryption happens on your device
You create a master password
Bitwarden uses it to generate an encryption key
Your data (passwords, notes, etc.) is encrypted locally using:
AES-256 encryption
2nd step: Encrypted data is stored in the cloud
The encrypted vault is uploaded to Bitwarden servers
Server only stores ciphertext (unreadable data) -> ensure secure

3rd step: Synchronization across devices
When you log in on another device:
It downloads the encrypted vault
Uses your master password to decrypt locally

4th step: Autofill & usage
When you open a website:
Bitwarden decrypts relevant credentials locally
Autofills them into the login form

<img width="1162" height="646" alt="image" src="https://github.com/user-attachments/assets/50b27dd0-c8c1-4493-830b-bf3ed7c7f5d2" />


2. GitGuardian:

GitGuardian is a security tool that detects and prevents sensitive data leaks (secrets) in code repositories.
How it works:
Developer pushes code to GitHub (or GitLab, etc.)
GitGuardian scans the repository
If it detects a secret:
Sends alert
Suggests remediation (e.g., revoke key)

A developer accidentally uploads:
AWS_SECRET_KEY=abcd1234...
GitGuardian:
Detects it instantly
Alerts you
Tells you to revoke the key
<img width="1899" height="951" alt="image" src="https://github.com/user-attachments/assets/981a7263-4b0c-4381-b891-1e12ab17af45" />

3. Web Application Firewalls (WAF):

Web application firewalls (WAFs) are a critical security defense for websites, mobile applications, and APIs. They monitor, filter, and block data packets to and from web applications, protecting them from threats. WAFs are designed (trained) to detect and protect against dangerous security flaws that are most common within web traffic.

How does it works:
A WAF works by inspecting HTTP requests and applying predefined rules to identify malicious traffic:
GET requests: These requests retrieve data from the server.
POST requests: These requests send data to the server to change its state.
PUT requests: These requests send data to the server to update or create.
DELETE requests: These are requests to delete data.

<img width="1459" height="660" alt="image" src="https://github.com/user-attachments/assets/c29e8be5-698f-4143-a705-b574de577720" />

4. Snyk: an AI tool and also has the similar name as the company

Snyk is an online security tool that finds and fixes vulnerabilities in your code, dependencies, and containers.
Snyk scans your project to detect:
🐞 Vulnerable open-source libraries (most common issue)
💻 Code vulnerabilities (e.g., insecure functions)
🐳 Container security issues (Docker images)
☁️ Infrastructure misconfigurations (cloud settings)

How it works
You connect your repo (GitHub, GitLab, etc.)
Snyk scans your project online
It identifies known vulnerabilities using its database
It suggests:
Fixes
Safer versions of dependencies


5. Canarytokens:

Canarytokens is a free tool that helps you discover you've been breached by having attackers announce themselves.
You place a fake or hidden piece of data somewhere.

When a token is triggered, you typically get:
🌍 IP address of the attacker
📍 Approximate location (geo/IP-based)
🖥️ Device / user agent info
⏰ Time of access
📄 Which token/file/link was accessed

👉 This tells you:
“This specific resource was accessed unexpectedly.”

<img width="230" height="219" alt="image" src="https://github.com/user-attachments/assets/17d6f053-d844-40fe-8683-6f61a93e8d43" />
