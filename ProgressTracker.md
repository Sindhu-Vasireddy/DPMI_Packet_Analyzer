### Improvement Tracker:

1. October Submission-2016 (briefly):
   a. Positives:
      1. We had a running code that was able to capture one measurement stream.
      2. We were able to push the data into the database.
      3. We were able to implement the basic RESTAPI but with the browser.

   b. Challenges:
      1. The steps that one had to run manually to execute the program were many.
      2. We did not have live stream capturing. We were pushing the stream into a text file and then performing our tasks on it.
      3. We had issues while storing the data into the database.
      4. We did not have Grafana.

2. March Submission-2017 (briefly):
   a. Positives:
      1. We were able to reduce the number of steps to just one step.
      2. We were able to capture a live-stream.
      3. We then were able to push the data into the database continuously.
      4. We were able to perform calculations on the data collected and display it to the customer using RESTAPI.
      5. We implemented Grafana.

   b. Challenges:
      1. We were not provided with the mp stream like the first time, so, while installing the mp locally and running it, we had many troubles.
      2. We had to stop our program first to be able to perform calculations and then run it again to display it using RESTAPI.
      3. We did not have a status option to see if tophost was running or not.
      4. We were not able to manage multiple streams.
      5. The data stored into the database did not have a correct timestamp.
      6. Calculations needed to be corrected and made more meaningful.
      7. We were still implementing RESTAPI through the browser.
      8. We had to start tophost through a web page where the user would enter a stream number and the stream would run.
      9. We couldn’t stop the tophost through the curl commands.

3. June Submission-2017:
   a. Positives:
      1. We were able to show whether tophost is running or not.
      2. We no longer need to stop the app to be able to see the calculations and status of tophost.
      3. RESTAPI implementation was using curl, instead of through the browser.
      4. Corrected the timestamp issue in the database.
      5. We could capture the running status of the top-host.
      6. We included user authentication for security.
      7. We were able to define the measurement stream that is being captured by the user.
      8. We were able to start the tophost using the curl commands itself, without the need for a web page like last time.
      9. We have also enabled the stop functionality through the curl commands.
      10. We were able to correct the calculations and were also able to add the missing details (for e.g.: the source-destination pair IPs for the max_packet & the min_packet) as asked.
      11. We have also made documentation stating the prerequisites to be installed along with the syntax for the curl commands needed to be run.

   b. Challenges:
      1. Handling of multiple measurement streams.
      2. Calculations had to be made more usable.

We are now able to handle multiple streams and have tried our best to make the code have better practical implications from a customer's perspective, as per the changes proposed by our Prof. Patrik Arlos. We thank him for all the guidance and support.
###