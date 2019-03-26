# Simple web crawler

### Requirements

The crawler should be limited to one domain. 
Given a starting URL it should visit all pages within 
the domain, but not follow the links to external sites 
such as Google or Twitter.

The output should be a simple structured site map 
(this does not need to be a traditional XML s
itemap - just some sort of output to reflect what your 
crawler has discovered), showing links to other pages 
under the same domain, links to external URLs and 
links to static content such as images for each 
respective page.

### Build

* Clone repository:

```
git clone https://github.com/sebastianczech/crawler
```

* Install ``virtualenv`` (if needed):

```
pip install virtualenv
```

* Create virtual environment:

```
cd crawler
virtualenv -p python3 venv
```

* Activate virtual environment:

``` 
source venv/bin/activate
```

### Test

```
python -m unittest test_crawler.py
```

### Run

```
python crawler.py URL DEPTH
```

Where ``URL`` is address of HTTP resource to crawl 
and ``DEPTH`` is optional parameter to limit the depth of crawl e.g:

```
python crawler.py https://www.google.com 3
```

If ``DEPTH`` is too big, the for this simple web crawler Python
is showing stack overflow error. 