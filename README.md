# to run the web service
in bash run:
$ FLASK_APP=my-flask-app.py flask run --host=0.0.0.0

then wait for the initialization to end (stdout has a banner that will tell you when it is done)

then in bash run:
$ curl -X GET http://104.198.177.183:5000/?content=Trump%20is%20a%20piece%20of%20shit
(as an example)
where 104.198.177.183 is your external ip.
as of 2019jul10 you can find your external ip by running
$ curl -s http://whatismyip.akamai.com/
or just look in the google cloud compute engine dashboard and check the line of the vm you are using


OLD
----------------------------------------------------------------------
This is what the directory actually looks like (using `tree -a -L 3`):
```
.
├── input
│   ├── fasttext-crawl-300d-2m
│   │   └── crawl-300d-2M.vec
│   ├── glove840b300dtxt
│   │   └── glove.840B.300d.txt
│   ├── jigsawunintendedbias
│   │   ├── crawl-300d-2M--100L.vec
│   │   ├── glove.840B.300d--100L.txt
│   │   └── train_1000L.csv
│   └── jigsaw-unintended-bias-in-toxicity-classification
│       ├── sample_submission.csv
│       ├── test.csv
│       └── train.csv
├── logs
│   └── 2019Jun24T171417Z-0500-nvidia-smi.log
├── notebooks
│   ├── .git
│   │   ├── branches
│   │   ├── COMMIT_EDITMSG
│   │   ├── config
│   │   ├── description
│   │   ├── HEAD
│   │   ├── hooks
│   │   ├── index
│   │   ├── info
│   │   ├── logs
│   │   ├── objects
│   │   └── refs
│   ├── .gitignore
│   ├── .ipynb_checkpoints
│   │   ├── Simple LSTM - 1000voices V4 2019Jun24T104123Z-0500_tmp-name-change-checkpoint.ipynb
│   │   ├── Simple LSTM - 1000voices V4-checkpoint.ipynb
│   │   └── Simple LSTM - 1000voices V4-Original-checkpoint.ipynb
│   ├── README.md
│   ├── Simple LSTM - 1000voices V4.ipynb
│   ├── Simple LSTM - 1000voices V4-Original.ipynb
│   └── submission.csv
└── old-zip-files
    ├── fasttext-crawl-300d-2m.zip
    ├── glove840b300dtxt.zip
    ├── jigsawunintendedbias.zip
    ├── sample_submission.csv.zip
    ├── test.csv.zip
    └── train.csv.zip
```
