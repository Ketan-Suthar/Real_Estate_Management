from wtforms import *

class DatasetVO:
    datasetId = IntegerField()
    datasetFilename = StringField()
    datasetFilepath = StringField()
    datasetDescription = StringField()
    datasetActiveStatus = StringField()
