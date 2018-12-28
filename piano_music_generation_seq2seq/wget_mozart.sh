DATA_DIR="data/"
cat mozart.txt | xargs wget $1 -P $DATA_DIR
