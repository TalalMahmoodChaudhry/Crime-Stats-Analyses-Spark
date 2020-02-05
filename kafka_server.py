import producer_server
from kafka import KafkaProducer


def run_kafka_server():
	# TODO get the json file path
    input_file = "./police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="com.udacity.crime.police-event",
        bootstrap_servers="localhost:3000",
        client_id="com.udacity.crime.producer"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()