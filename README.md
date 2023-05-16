# service-now-close-tickets

Take a value from a list from a text file and go to a webpage, search for that value, open the form that opens up and copy paste fields from that page to another field on the same page and press a button, loop for another value in the text file. Use python  to automate this.
Wait for the page to load and wait after submitting the value to load the page. i need to find two values on the searched page and then input those values on that same page in other input form repectivly. append this function in the code.
in the above code i need to input the value in the search bar on the webpage and press enter.
Further add a function to check if the field2 searched on the web page is today then skip to the next value and create a new log file skipped.log in the folder with the skipped values and prompt the number of values skipped on the terminal.
This version of the code checks if the second value found on the page is equal to today's date, and if so, skips to the next value in the loop. It keeps track of all skipped values in a list and writes them to a log file after the loop finishes. It also prints the number of skipped values to the console. Please adjust the date format in the comparison to match the format of the dates on your web page.
