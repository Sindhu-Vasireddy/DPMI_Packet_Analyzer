#!/bin/bash
# you are getting the stream variable from the submit_form.html 
stream=$1
sudo ./tophosts -s ens6 ${stream}
