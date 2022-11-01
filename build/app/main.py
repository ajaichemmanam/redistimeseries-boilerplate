# Simple example
from redistimeseries.client import Client

if __name__ == "__main__":
    print("Hello world!")

    rts = Client(host="10.8.60.5", port=56379, decode_responses=True)
    rts.create("test", labels={"Time": "Series"}, duplicate_policy="last")
    rts.add("test", 1, 1.12)
    rts.add("test", 2, 1.12)
    print(rts.get("test"))
    rts.incrby("test", 1)
    rts.range("test", "-", "+")
    rts.range("test", "-", "+", aggregation_type="avg", bucket_size_msec=10)
    rts.range("test", "-", "+", aggregation_type="sum", bucket_size_msec=10)
    print(rts.info("test").__dict__)

    # Example with rules
    rts.create("source", retention_msecs=40, duplicate_policy="last")
    rts.create("sumRule")
    rts.create("avgRule")
    rts.createrule("source", "sumRule", "sum", 20)
    rts.createrule("source", "avgRule", "avg", 15)
    rts.add("source", "*", 1)
    rts.add("source", "*", 2)
    rts.add("source", "*", 3)
    print(rts.get("sumRule"))
    print(rts.get("avgRule"))
    print(rts.info("sumRule").__dict__)
