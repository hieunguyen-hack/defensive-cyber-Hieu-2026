DMARC (Domain-based Message Authentication, Reporting, and Conformance) is an email security protocol that leverages
two baseline authentication checks—SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail)—to protect your domain from being spoofed by bad actors.

Setting your DMARC policy to p=reject is the ultimate enforcement phase. It tells every receiving email server in the world: "If an incoming message claiming to be from my domain fails both SPF and DKIM verification,
block it immediately at the gateway.
Do not deliver it to the inbox, and do not put it in the spam folder."

How DMARC Verification Works (The Architecture)DMARC relies on a concept called Identifier Alignment. An email passes DMARC validation only if the visible header domain (the From: address the user sees)
matches the domain validated by SPF (the technical Return-Path address) or DKIM (the cryptographic signing domain d=).
If an attacker tries to send an email with the header From: admin@yourdomain.com, the receiving server checks your domain's public DNS text records to process the evaluation.

Step-by-Step Production Implementation:

Phase 1: Monitoring Mode (p=none)This is your discovery period. It forces receiving mail systems to process checks and email you daily XML diagnostic reports without altering how the messages are delivered.  
Create a DNS record at the host location _dmarc.yourdomain.com with the type TXT:
v=DMARC1; p=none; rua=mailto:dmarc-reports@yourdomain.com; adkim=r; aspf=r;

Phase 2: Soft Enforcement (p=quarantine) with a Percentage Ramp

You can use the pct tag to apply the policy to only a fraction of failing messages while keeping an eye out for issues.
v=DMARC1; p=quarantine; pct=25; rua=mailto:dmarc-reports@yourdomain.com;

Phase 3: Absolute Lockdown (p=reject):

Once your p=quarantine at pct=100 runs perfectly for 30 consecutive days with no legitimate emails failing authentication, you are ready to enforce maximum protection.
v=DMARC1; p=reject; rua=mailto:dmarc-reports@yourdomain.com; sp=reject;

p=reject: Directs receiving servers to completely reject the email during the SMTP handshake connection phase (typically returning a 550 5.7.1 bounce error to the malicious sender).
The target recipient never sees the email.
sp=reject: Explicitly locks down all subdomains with the same rule, preventing attackers from trying to spoof addresses like support@updates.yourdomain.com
