
1. Prototype pollution in JavaScript applications
Definition: Prototype pollution is a JavaScript vulnerability where an attacker manipulates the prototype of base objects (like Object.prototype). Because almost all objects inherit from this prototype, the injected properties are unexpectedly inherited by every object in the application, leading to logic flaws, privilege escalation, or remote code execution (RCE).
<img width="984" height="595" alt="image" src="https://github.com/user-attachments/assets/ab9dc21a-154f-48fa-982b-54386803dc10" />
<img width="1007" height="552" alt="image" src="https://github.com/user-attachments/assets/94c3238d-096a-4019-9063-34f5c3392152" />

Impact:
+)One possible impact is access control bypass. For example, if an application checks whether a user has a property such as isAdmin, and that property is polluted into the prototype, ordinary users may be treated as administrators if the code does not properly check whether the property belongs directly to the user object.

+) Another impact is denial of service. Prototype pollution can break application logic by changing common object properties or methods. This may cause errors, crashes, infinite loops, or unexpected behaviour, making the application unavailable or unreliable.

+) Prototype pollution can also lead to data leakage or security control bypass. If polluted properties affect configuration options, an attacker may be able to disable security settings, change request behaviour, bypass filters, or expose information that should remain protected.

2. secret leakage in public repositories and CI/CD pipelines:
Definition: This happens when developers accidentally commit API keys, cloud credentials, database passwords, private tokens, or signing keys into GitHub repositories or build logs.
<img width="1600" height="650" alt="image" src="https://github.com/user-attachments/assets/5a294cc2-cef6-4235-82cd-a5e39924e2ce" />

Impact:
+) Attackers may be able to access storage buckets, virtual machines, databases, logs, or internal services. Depending on the permission level of the leaked key, the attacker may be able to read sensitive data, modify resources, or create new infrastructure under the victim’s account.
+) Financial loss through cloud abuse. Attackers may use exposed cloud credentials to create expensive resources, run cryptocurrency mining workloads, send spam, or host malicious infrastructure. This can create unexpected cloud bills for the organisation, even if no customer data is stolen.
+) Production system compromise. CI/CD pipelines often have permission to build, test, and deploy applications. If attackers obtain pipeline credentials, they may be able to change environment variables, access production secrets, modify deployment scripts, or push unauthorised code into live systems.

3. Path traversal in remote support or file upload systems
Definition: A critical vulnerability that allows attackers to break out of the intended root directory, enabling them to read or write arbitrary files on the server.  Path traversal in remote support or file upload systems can be serious because it allows an attacker to escape the intended folder and interact with files outside the allowed directory. This usually happens when an application accepts a filename or file path from the user but does not properly validate it. Attackers may try to use patterns like ../ to move up the directory structure and reach sensitive files.
Impacts:
+) Unauthorised file reading: instead of only downloading files from an upload folder, the attacker may be able to read configuration files, log files, system files, or application source code. These files may contain sensitive information such as database credentials, API keys, internal paths, or security settings.
+) Remote code execution:If a path traversal vulnerability allows an attacker to upload or overwrite files in a directory where code is executed by the server, the attacker may be able to run malicious commands.

4. An unsafe webhook implementation
Definition: occurring when an endpoint accepts or sends automated data over the internet without proper authentication, integrity checks, and network isolation. Because webhooks essentially act as "reverse APIs" requiring publicly accessible endpoints, failing to secure them creates massive backdoors into your internal systems

Source: https://hookdeck.com/webhooks/guides/complete-guide-to-webhook-security#:~:text=Encrypt%20all%20data:%20TLS%20helps,enforces%20this%20strategy%20is%20Stripe.

Impacts:
+)Request Forgery (Spoofing): Attackers send fake payloads directly to your endpoint (e.g., faking a "successful payment" to unlock premium features).
+)Replay Attacks: Intercepted legitimate requests are fired repeatedly to cause duplicate actions (like shipping an order twice).
+)Server-Side Request Forgery (SSRF): Malicious payloads force your server to make requests to secure internal databases or metadata services.
+)Injection Attacks: Payloads containing arbitrary code, malicious scripts, or SQL commands exploit your parser to manipulate databases or run unauthorized system commands

5. Misconfigured CORS policy
Definition: CORS, or Cross-Origin Resource Sharing, controls which websites are allowed to make browser-based requests to an API. A weak implementation occurs when an API uses overly permissive settings, such as allowing all origins or reflecting arbitrary origins while also allowing credentials. This can be dangerous because a malicious website may be able to make authenticated requests from a victim’s browser and read sensitive API responses.
Impact:
+) sensitive data exposure. If an API allows requests from untrusted origins and also allows credentials such as cookies or authorization headers, a malicious website could make a request to the vulnerable API using the victim’s logged-in session. If the API response is readable by the malicious site, private information such as account details, email addresses, personal records, order history, or internal data may be exposed.
+) session-based account compromise. CORS misconfiguration does not usually steal the password directly, but it may allow an attacker-controlled website to perform authenticated actions through the victim’s browser. If the victim is already logged in to the vulnerable service, the malicious website may be able to abuse that active session depending on the API’s behaviour and authentication design.
Source: https://portswigger.net/web-security/cors
<img width="1746" height="804" alt="image" src="https://github.com/user-attachments/assets/51504769-fed2-4d75-9aee-a0bebd3f3bb7" />

