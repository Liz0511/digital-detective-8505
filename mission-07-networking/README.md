# Mission 7 - How computers communicate

## 1. Task / objective
The aim of this mission was to understand basic networking terms, check a website connection and learn what happens when we open a website.

## 2. Work completed

### Task 7.1 - Network concepts

| Term | Meaning | Example |
|---|---|---|
| LAN | A network in a small area | Home Wi-Fi |
| MAN | A network covering a city or large campus | City network |
| WAN | A network covering a large geographical area | Internet |
| DNS | Finds the IP address linked to a domain name | Looking up `example.com` |
| Router | Connects networks and forwards data | Wi-Fi router |
| Protocol | Rules used by devices to communicate | HTTP and TCP |
| Packet switching | Data is divided into smaller packets | Sending data over the internet |
| Client-server | A client requests something and a server responds | Browser and website server |

### Task 7.2 - Checking network information

I can use these commands:

```bash
ping -c 4 example.com
nslookup example.com
```

`ping` checks whether a destination responds to network requests. `nslookup` checks DNS information and can show the IP address associated with a domain.

**My observation:** [Run both commands and write whether they worked. Do not paste your private IP address or Wi-Fi details.]

DNS is useful because we normally remember website names instead of IP addresses. DNS helps the browser find the address of the website.

### Task 7.3 - What happens when I open a website?

1. First, I enter a website name in the browser.
2. The browser checks where the website is located. If needed, it asks DNS for the IP address.
3. DNS returns the address of the website server.
4. My computer sends data through the local network and router.
5. The browser and server communicate using network protocols.
6. The server sends the requested website files back.
7. The browser displays the website on the screen.

## 3. Commands / tools used
- `ping -c 4 example.com` - checks network connectivity.
- `nslookup example.com` - checks DNS information.
- Web browser - used to open websites.

## 4. My understanding
I understood that the internet connects many networks together. DNS helps us find websites using their names. The router forwards data, and the browser works as a client that requests information from a server.

## 5. Difficulties faced
At first, I found DNS and packet switching a little confusing, but I understood them after learning their examples


