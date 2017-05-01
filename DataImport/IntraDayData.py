import pandas as pd


class IntraDayData:
    def __init__(self, raw_data):
        self.prev_settlement = raw_data.preClose

