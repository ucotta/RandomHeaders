# RandomHeaders

Python Module that generates fake user agents with a locally saved DB.  All the other Fake User Agent programs that I've seen scrape from a website that frequently goes down.

This is useful for webscraping, and testing programs that identify devices based on the user agent.

## Getting Started

```
>>> import RandomHeaders
>>> header = RandomHeaders.LoadHeader()
>>> print header

{'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML'}
```

### Language and encoding

Optionally you can supply a list of languages and RandomHeaders will return a headers with the language and a default enconding.
 
```
>>> import RandomHeaders
>>> header = RandomHeaders.LoadHeader(lang=("en-US", "fr-FR", "es-ES"))
>>> print header

{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10', 'Accept-Language': 'ca-ES,es;q=0.9', 'Accept-Encoding': 'gzip, deflate, br'}
```
