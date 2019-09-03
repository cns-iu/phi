# Data Collection

Data was collected for 17 primary investigators awarded a grant as part of the Precision Health Initiative (PHI) Grand Challenge grant process.

`Data Last Updated 08/20/2019`

## Data Collection Method

Using the Web of Science's online interface [advanced search](http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?product=WOS&search_mode=AdvancedSearch), queries were created to gather publications for each PI. Over time these queries will be refined to be as accurate as possible. After refining the queries, we then merge all the publications into a single query. From there we export the results and combine them into one "ISI" file.

## Web of Science Queries Used

The queries used are saved in the [wos-extract.isi_history.wos](wos-extract.isi_history.wos) file in this directory. You can load them up via the advanced search referenced previously.

## Data Extraction Method

You can export from the results page by clicking the dropdown box arrow and selecting `Save to Other File Formats`. A popup box will appear. Select the record range (you can do 500 records at a time) and choose `Full Record and Cited References` as the Record Content. Finally make sure the File Format is selected as `Other Reference Software`. When you click Send, an ISI/RIS file is generated. Save all of those and then merge them by concatenating them and removing the header/footer of subsequent files where appropriate. Make sure the combined file has a `.isi` extension and is saved in this directory as [wos-extract.isi](wos-extract.isi).

## Data Processing Methods

### Data reformatting

Load the data file into Sci2 as ISI format, and save the processed results as a csv ([wos-extract.csv](intermediate-files/wos-extract.csv)).

Next, in Open Refine create a new project using the [wos-extract.csv](intermediate-files/wos-extract.csv) file. In the project, apply the set of processing steps found in [01-refine-isi-authors.json](intermediate-files/01-refine-isi-authors.json), and save results as, [wos-extract.isi_author.csv](intermediate-files/wos-extract.isi_author.csv).

### Author name disambiguation

Next, in Open Refine create a new project using the [wos-extract.isi_author.csv](intermediate-files/wos-extract.isi_author.csv). file. In the project, apply the set of processing steps found in [02-refine-isi-authordisambiguation.json](intermediate-files/02-refine-isi-authordisambiguation.json), and save results as, [wos-extract.isi_author-disambiguation.csv](wos-extract.isi_author-disambiguation.csv). This file is saved in the main data directory for the AGC1 visualization.

### Co-author Network Extraction

After creating the [wos-extract.isi_author-disambiguation.csv](wos-extract.isi_author-disambiguation.csv) data set, we create a final Open Refine project that uses this same file to create a merged data set that will be used to update the [wos-extract.csv](intermediate-files/wos-extract.csv) data set. Apply the refine processing steps from the [03-refine-isi-mergeAuthorNames-sciGephi.json](intermediate-files/03-refine-isi-mergeAuthorNames-sciGephi.json); (save) the results as [wos-extract.cleaned-coauthornet.csv](intermediate-files/wos-extract.cleaned-coauthornet.csv).

Next, open [wos-extract.cleaned-coauthornet.csv](intermediate-files/wos-extract.cleaned-coauthornet.csv) and [wos-extract.csv](intermediate-files/wos-extract.csv) in a data editor, like Excel. Clear the original Authors and Authors (Full Name) fields, and then use a VLOOKUP function that looks-up the replacement Author and Author (Full Name) by the Unique ID ([wos-extract.csv](intermediate-files/wos-extract.csv)) and id field ([wos-extract.cleaned-coauthornet.csv](intermediate-files/wos-extract.cleaned-coauthornet.csv)). The updated ([wos-extract.csv](intermediate-files/wos-extract.csv)) is saved as [wos-extract.cleaned-coauthornet.for-sci2.csv](intermediate-files/wos-extract.cleaned-coauthornet.for-sci2.csv)). Alternatively, you can run "python3 [update-coauthor-fields.py](intermediate-files/update-coauthor-fields.py)", which also generates the [wos-extract.cleaned-coauthornet.for-sci2.csv](intermediate-files/wos-extract.cleaned-coauthornet.for-sci2.csv)) file.

With Sci2, load [wos-extract.cleaned-coauthornet.for-sci2.csv](intermediate-files/wos-extract.cleaned-coauthornet.for-sci2.csv)) and run the workflow process outlined in the [sci2-wos-extract-cleaned-coauthornetGephi-worlflow.xml](intermediate-files/sci2-wos-extract-cleaned-coauthornetGephi-worlflow.xml). Or run "python3 [create-coauthor-network.py](intermediate-files/create-coauthor-network.py)" which also generates a file ([wos-extract.cleaned-coauthornet.for-gephi.graphml](intermediate-files/wos-extract.cleaned-coauthornet.for-gephi.graphml)) for loading into Gephi. The extracted co-author network is passed to Gephi for the final layout of the co-author network, and the addition of a boolean field, "show_label". The *show_label* field must be updated with the list of Principle Investigators listed in the file [wos-extract.isi_history.wos](wos-extract.isi_history.wos). The final layout is saved as a GEXF formatted network, and saved as [wos-extract.isi_full-layout.gexf](wos-extract.isi_full-layout.gexf).

## Data Loading

You can optionally build the database manually by running `npm run build:database`. This repository is setup to automatically process the database on every commit to master and publish it to github pages.
