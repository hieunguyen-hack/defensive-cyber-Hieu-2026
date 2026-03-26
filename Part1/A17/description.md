1. Password-Based Authentication
Mechanism: User proves identity via secret string (password/PIN).
Use: Login systems, email, university portals.
Weakness: Vulnerable to brute force, phishing, and reuse attacks.

2. Multi-Factor Authentication (MFA)
Mechanism: Combines ≥2 factors (knowledge + possession/biometric).
Use: Banking, cloud services, university accounts.
Weakness: Can still be bypassed via SIM swap or MFA fatigue attacks.

3. Biometric Authentication
Mechanism: Uses physical traits (fingerprint, face, iris).
Use: Smartphones, secure facilities.
Weakness: False positives; cannot be revoked if leaked.

4. Smart Cards / Security Tokens
Mechanism: Hardware device stores keys or generates OTP codes.
Use: Enterprise login, secure buildings, VPN access.
Weakness: Loss/theft of device can compromise access.

5. Role-Based Access Control (RBAC)
Mechanism: Permissions assigned based on predefined roles.
Use: Universities (student vs staff), corporate systems.
Weakness: Poor role design can lead to excessive privileges.

6. File/Database Encryption
Mechanism: Data encrypted using algorithms (e.g., AES); requires key.
Use: Protect sensitive files, databases.
Weakness: Key management failure = total data exposure.

7. Full Disk Encryption (FDE)
Mechanism: Encrypts entire storage device at rest.
Use: Laptops, mobile devices (BitLocker, FileVault).
Weakness: Ineffective if attacker gains access while device is unlocked.

8. Firewall
Mechanism: Filters incoming/outgoing traffic via rule sets (IP, port).
Use: Network perimeter defense, enterprise security.
Weakness: Cannot stop attacks that originate inside the network.

9. VPN (Virtual Private Network)
Mechanism: Creates encrypted tunnel between user and network.
Use: Remote access to internal systems (e.g., university network).
Weakness: If credentials are stolen, attacker gains trusted access.

10. Access Control Lists (ACLs)
Mechanism: Defines permissions (read/write/execute) per user/group.
Use: File systems, network devices.
Weakness: Misconfiguration can unintentionally expose resources.

Passwords, MFA, biometrics, tokens → lock identity (authentication)
RBAC, ACLs → lock permissions (authorization)
Encryption, disk encryption → lock data
Firewall, VPN → lock network access
