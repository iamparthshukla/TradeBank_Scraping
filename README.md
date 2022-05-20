# TradeBank_Scraping

The repository consists of two scripts: ExportScript.py, for scraping the export data, and ImportScript.py for scraping the import data.

This project is an end-to-end solution on the selenium-scraped websites to the report-generation Excel format conversion.

<br>
The two steps required in this conversion are:
<br>
1. Running ImportScript.py/ExportScript.py <br> 2. Running Convert-Excel.py

## Running ImportScript.py/ExportScript.py

Please make sure your dependencies are updated as per the script requirements. The pre-existing drivers in the script support the M1 Mac configuration. 
<br><br>For your respective platform, please download the suitable drivers from https://chromedriver.chromium.org/downloads in correlation with your respective Chrome version. For other browsers, please follow the selenium documentation. Chrome is recommended for this particular script because the tests have only been run on Chrome Version 100.0.4896.127 (Official Build) (arm64).
<br><br> The .xlsx documents in the script are usable for current purposes.

## Running Convert-Excel.py

Make sure you insert the file name in the start of the file produced in step 1. This script allows you convert this excel in the report-accepted format.
