# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Coroutine, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser
from rasa_sdk.types import DomainDict

class ActionExtractSymptom(Action):
    def name(self) -> Text:
        return "action_extract_symptom" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        symptom = None
        print('entities: ', entities)
        if entities:
            for entity in entities:
                if entity['entity'] == 'symptom':
                    symptom = entity['value']
        
        if symptom:
            response = f"I see that you mentioned {symptom} as a symptom."
        else:
            response = "Could you please specify the symptom you are experiencing?"

        dispatcher.utter_message(text=response)

        return []
   