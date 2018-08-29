# Data Collection

Data was collected for 11 primary investigators awarded a grant as part of the Precision Health Initiative (PHI) Grand Challenge grant process.

## Data Collection Method

Using the Web of Science's online interface [advanced search](http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?product=WOS&search_mode=AdvancedSearch), queries were created to gather publications for each PI. Over time these queries will be refined to be as accurate as possible. After refining the queries, we then merge all the publications into a single query. From there we export the results and combine them into one "ISI" file.

## Web of Science Queries Used

The queries used are saved in the [wos-extract.isi_history.wos](wos-extract.isi_history.wos) file in this directory. You can load them up via the advanced search referenced previously.

## Data Extraction Method

You can export from the results page by clicking the dropdown box arrow and selecting `Save to Other File Formats`. A popup box will appear. Select the record range (you can do 500 records at a time) and choose `Full Record and Cited References` as the Record Content. Finally make sure the File Format is selected as `Other Reference Software`. When you click Send, an ISI/RIS file is generated. Save all of those and then merge them by concatenating them and removing the header/footer of subsequent files where appropriate. Make sure to the combined file has a `.isi` extension and is saved in this directory as `wos-extract.isi`.


## Co-author Network Extraction

Load the ISI file into Sci2, extract a coauthor network, and layout the network with DrL/OpenOrd. Save the network file as an `.nwb` file into this directory as `wos-extract.isi_full-layout.nwb`

## Data Loading

You can optionally build the database manually by running `npm run build:database`. This repository is setup to automatically process the database on every commit to master and publish it to github pages.
