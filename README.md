# pyspark-demo

## Setup instructions
clone the repo
```
https://github.com/davidkgreenfield/pyspark-demo.git
```

```
pip install -r requirements.txt
```

## import into intellij
make sure the SDK interpreter is the virtualenv for the project


## run configuration
Run the main.py file.  It will fail but in the process set up a run configuration.  In that run configuration add the environment parameter "PYSPARK_SUBMIT_ARGS"

PYSPARK_SUBMIT_ARGS ->	--packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell

