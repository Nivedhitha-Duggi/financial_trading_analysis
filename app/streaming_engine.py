import threading
from bintrees import FastRBTree
from pybloom_live import ScalableBloomFilter
import ccxt
import time

class StreamingEngine:
    def __init__(self, max_data_points=1000):
        self.data = FastRBTree()
        self.bloom_filter = ScalableBloomFilter()
        self.exchange = ccxt.binance()
        self.max_data_points = max_data_points
        self.data_thread = threading.Thread(target=self.continuous_data_processing, daemon=True)
        self.data_thread.start()

    def continuous_data_processing(self):
        while True:
            self.ingest_real_time_data(symbol='BTC/USDT', timeframe='1m', limit=100)
            time.sleep(300)

    def ingest_real_time_data(self, symbol, timeframe='1m', limit=100):
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        for candle in ohlcv:
            timestamp = int(candle[0])
            data_point = {
                'open': candle[1],
                'high': candle[2],
                'low': candle[3],
                'close': candle[4],
                'volume': candle[5]
            }

            # Check for duplicate data before ingestion
            if not self.check_timestamp(timestamp):
                self.data[timestamp] = data_point
                self.bloom_filter.add(str(timestamp))

        self.remove_old_data()

    def remove_old_data(self):
        if len(self.data) > self.max_data_points:
            cutoff_time = list(self.data)[0]
            del self.data[cutoff_time]
            self.bloom_filter.remove(str(cutoff_time))

    def check_timestamp(self, timestamp):
        return str(timestamp) in self.bloom_filter

