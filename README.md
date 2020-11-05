# PyTallyODBCtoSQL
Python code to connect with Tally and extract reports. 

Tally.ERP9 by Tally Solutions is one to be biggest Accounting software provider in India and SAARC countries. Aimed at simplicity and ease of use, this software has become defacto - go to tool for many small and medium organizations and their auditors.

However, the software contains a big gap which is interoperability and extraction of data from tally databases directly. Tally.ERP stores data in a properietary XML tags, which are not easy to use for the end users. As a result there are numerous TDL (Tally definition language) tools and BI tools which help serve this need.

A simple Google Search (https://www.google.com/search?q=tally+bi+tools) will fetch you the likes of Tallingence, ElegantJ, Dataception, Easy Reports and many others. There's a cost attached to it, and when you need to extract simple data like list of Vendors along with PAN, Mobile and Address, it becomes manual task very quickly. No one would want to invest considerable amount in such BI tools for simple data extraction.

That's where this python code attempt comes in to picture. It's aimed at helping Accountants and Auditors alike to easily extract data from Tally without much techincal knowledge.

Tally.ERP9's current versions support SQL queries (https://help.tallysolutions.com/article/Tally.ERP9/Data_Management/DM_SQL_Query.htm). User has to go to Calculator in the software and enter the SQL text directly. The Software understand the SQL script and displays the rows directly in the window itself (in tabular format).

Shortcoming of this approach:-
1) User may not be knowing how to use SQL queries. Many users today don't even know that this feature exists.
2) The results are in the software window only. To extract it in excel, user has to perform further actions. 

With these few lines of python codes, users can simplify the same. There are two parts to this repository.
IT > containing code and SQL queries, which IT can use and modify according to user needs.
User > containing a simple GUI, which can read the default queries and custom queries as the IT deploys, extract the data directly to Excel Files which users can view at a click of a button.

