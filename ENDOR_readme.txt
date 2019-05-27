1.Add a weekly low, high, median, average for every record.
	Due to the fact, the dataset is constantly updated and needs to be handled accordingly.
	The data ingestion will be from the raw data that updates every X interval of time.
	We will add a timestamp to the ETH_USD_agg file, this way we can manage the data consuming above the aggregation.
	The timestamp info can be managed in a side table or in other logic processes.



2.Think of bad data that might break the ETL pipeline and add relevant defense mechanisms against it.
	I added is_number function, the function prevent the pipline from braek


3.Think of bad data that can’t be fixed and build a monitoring ecosystem around it.
	I built a function that writes to log all the bad records.
	Also in the main function, I added an option to remove these rows from the target files.
	The calculations don't affect the bad rows.


4.Think of a change of granularity and implement the corresponding calculations (instead of daily data, you will receive hourly data)
	In my solution, I added a week number to the data frame as granularity key to every seven days.	
	The granularity key unite group under the key instead of week number the granularity key will be the date.

5.Think of a deployment pipeline. How would you update your ETL pipeline?
	In case we are changing the structure of the data, we will need to make sure carefully the processes above it will work with the changes or adjust them to the changes.
	Before we will deploy to production we will need to do a set of chacks in dev/test environment. 
	I didn't work with this approach but I heard about it, CI/CD.
	  version-control
	  	1. commit the code with git

	  CI
		2.1 build
		2.2 unit tests
		2.3 integration test

	  CD
		3.1 review
		3.2 staging
		3.3 production

	