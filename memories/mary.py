import sys
import pickle

class Mary:

    def read_messages(messages):

        try:
            with open('messages.p', 'rb') as m:
                deserialized_messages = pickle.load(m)

        except (FileNotFoundError, EOFError):
            deserialized_messages = {
                "Margaret": [],
                "Mary": []
            }
        deserialized_messages["Mary"].append(messages)

        with open('messages.p', 'wb+') as m:
            pickle.dump(deserialized_messages, m)
            print(deserialized_messages)

if __name__ == "__main__":
  Mary.read_messages(sys.argv[1])
