from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionExtractSymptom(Action):
    def name(self) -> Text:
        return "action_extract_symptom" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        symptom = None

        # Extract the symptom entity from the latest message
        if entities:
            for entity in entities:
                if entity['entity'] == 'symptom':
                    symptom = entity['value']
        
        if symptom:
            response = f"I see that you mentioned {symptom} as a symptom."
            # Save the symptom to a slot
            return [SlotSet("symptom", symptom)]
        else:
            response = "Could you please specify the symptom you are experiencing?"

        dispatcher.utter_message(text=response)

        return []
