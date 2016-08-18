import sys
import pickle

class Margaret:

    def read_messages(messages):

        try:
            with open('messages.p', 'rb') as m:
                deserialized_messages = pickle.load(m)

        except (FileNotFoundError, EOFError):
            deserialized_messages = {}


        if "Margaret" not in deserialized_messages:
            deserialized_messages["Margaret"] = []
        deserialized_messages["Margaret"].append(messages)

        with open('messages.p', 'wb+') as m:
            pickle.dump(deserialized_messages, m)
            print(deserialized_messages)

if __name__ == "__main__":
  Margaret.read_messages(sys.argv[1])
