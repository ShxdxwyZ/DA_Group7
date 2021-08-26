# DA_Group7
[Project for module IT49450, Applied Scripting using Python]

Our project's main objective is to create an application to perform penetration testing to determine vulnerabilities. We have decided to code a web crawler for reconnaissance using Scrapy.

# Our Tasks

Make use of imported libraries/modules to:
- Perform a HTTP GET request to the given website
- Display an "OK" return status
- Display the website header
- Modify the user-agent to display "Mobile"
- Parse the web crawler using "response.css"
- Display reference webpage
- Receive and store results in a .json file

Our application must also include a "Test case" with the appropriate test function(s) to test our application.

# Usage

For best readability on the output(s) in the terminal, use the "--nolog" argument alongside the usual "scrapy runspider" command.
Also, to scrape multiple pages the '-s' argument has to be used with any user agent. We used: "USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
