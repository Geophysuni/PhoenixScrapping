# phoenixScrapp 
This is a simple library that helps you easily scrapp data to a structured dataframe with just a few steps. The library is developed by [Phoenix Revival](https://phoenix-revival.eu/).
## Dependencies
To run the code you need os, pandas and numpy libraries, that normally are distributed with all python IDE
## How to use

You can run test.py file to see how code is working or just foolow these simple steps.

1. Dowload html pages to your local directory (you can use any tool to save hwole site or do it manually)

2. Create an object of `pScrapp` class with path to source directory

3. Find a unique indicator, that can be used to separate valuable files with needed information from others. In the test case such indicator is a `"Change model"` phrase that exists on pages with prices and doesn`t exist on a main page

4. Find an html tag or other part of code, that goes before information that has to be scrapped.
![ ](/img/1.jpg)
Run `.scrapp` function with name of feature, target phrase that comes before valuable data and symbol following after it.

5. The object of `pScrapp` class will create a DataFrame atribute called `data` with column named by fature and values of scrapped data opposite to each file.

6. Running `.scrapp` function with new tag and other parameters will add new column and new found data.

After all needed data are collected you may save or process them with your own algorithms.