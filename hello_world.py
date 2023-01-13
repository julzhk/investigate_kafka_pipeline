import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

der_topic = app.topic('der_item')


@app.agent(der_topic)
async def process(der_items):
    async for der in der_items:
        print(der)
        #  check in der warehouse
        #  save it to a database
#       der check?

