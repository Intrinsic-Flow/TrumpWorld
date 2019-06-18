# TrumpWorld
Grakn.ai TrumpWorld example for CORE 1.5.0 and Workbase 1.2.0

## Installation

- Get GRAKN.AI CORE 1.5.0 from - https://grakn.ai/download
- Get GRAKN Workbase 1.2.0 from - https://github.com/graknlabs/workbase/releases

Once you have installed both of these download the files from this github and place in a directory.

## Setting up the Schema and loading the data ##
First you need to load the schema, secondly load the processed data. This data was created from the original data files held in the data directory by running the graqlizer.py script.

Start GRAKN Core by going to where GRAKN is installed and running:
```
./grakn server start
```
Stay in the grakn directory and run:
```
./grakn console --keyspace trumpworld --file <path to file>/schema.gql
```
Once this has completed successfully the entities data needs to be loaded, this sets up the person and organisation data.
```
./grakn console --keyspace trumpworld --file <path to file>/entities.gql
```
Lastly load the relations data, this is the mapping of the persons and organisations linked through the relations and inference
```
./grakn console --keyspace trumpworld --file <path to file>/relations.gql
```
## Workbase
If you now open workbase you will be able to select the trumpworld keyspace and view the scheme and run queries on the data, to start the following query will give you DONALD J. TRUMP and VLADIMIR PUTIN.
```
match $x isa person, has name "DONALD J. TRUMP";$y has name "VLADIMIR PUTIN";get;
```
Then all you need to do is double click the names to expand the graph. If you select 2 entities (click holding down cmd/option) and right click you will get the option to "select shortest path" which shows grakn in full effect with this example.

Enjoy!
