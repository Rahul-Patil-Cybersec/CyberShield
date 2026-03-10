from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import QR CODE PAYMENT SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "QR CODE PAYMENT SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is QR code used for in payment apps?",
                "option1": "Send money",
                "option2": "Increase battery",
                "option3": "Play games",
                "option4": "Delete apps",
                "answer": 1
            },

            {
                "question": "Do you need to scan QR code to receive money?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Sometimes",
                "option4": "Always",
                "answer": 2
            },

            {
                "question": "Who sends fake QR codes?",
                "option1": "Scammers",
                "option2": "Bank staff",
                "option3": "Teachers",
                "option4": "Friends",
                "answer": 1
            },

            {
                "question": "What happens if you scan fake QR code?",
                "option1": "Money can be deducted",
                "option2": "Phone gets faster",
                "option3": "Free reward",
                "option4": "Nothing happens",
                "answer": 1
            },

            {
                "question": "When should you scan QR code?",
                "option1": "Only from trusted source",
                "option2": "Any unknown person",
                "option3": "Random message",
                "option4": "Social media",
                "answer": 1
            },

            {
                "question": "Scammers pretend to be:",
                "option1": "Buyers or support agents",
                "option2": "Doctors",
                "option3": "Drivers",
                "option4": "Students",
                "answer": 1
            },

            {
                "question": "What should you check before payment?",
                "option1": "Payment details",
                "option2": "Phone color",
                "option3": "Screen brightness",
                "option4": "Volume",
                "answer": 1
            },

            {
                "question": "Which app uses QR code for payment?",
                "option1": "Google Pay",
                "option2": "Camera only",
                "option3": "Calculator",
                "option4": "Notes",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Verify QR code source",
                "option2": "Scan every QR code",
                "option3": "Trust unknown sender",
                "option4": "Ignore details",
                "answer": 1
            },

            {
                "question": "How can you avoid QR code scams?",
                "option1": "Scan trusted QR codes only",
                "option2": "Scan all QR codes",
                "option3": "Trust strangers",
                "option4": "Share bank details",
                "answer": 1
            },

        ]


        for q in questions:

            Question.objects.create(
                topic=topic,
                question=q["question"],
                option1=q["option1"],
                option2=q["option2"],
                option3=q["option3"],
                option4=q["option4"],
                correct_option=q["answer"]
            )


        self.stdout.write(
            self.style.SUCCESS("QR CODE PAYMENT SCAM Quiz Imported Successfully")
        )
