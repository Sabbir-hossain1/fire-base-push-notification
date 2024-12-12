import firebase_admin
from firebase_admin import credentials, messaging
from django.http import JsonResponse

cred = credentials.Certificate(
    "softmaxapp-2560a-firebase-adminsdk-8duk9-dee33ba598.json"
)
firebase_admin.initialize_app(cred)


def send_fcm_message(request):
    try:
        # Single message example

        # # registration_token = "f-1-oaG8Swu2RecTBX6RyU:APA91bHukGflzjpNZZW_KQ34v-71q_ILgztwCO9ALODkzaaPLjYGka3D5MUaJLtfP5AyLt-mUswgyjyQBNdDwqA0nUuoNC5EosvMCHpa5u-NrGJiBnng9Ao"
        # registration_token = "e5CR1OkrR72pkSqI4sYaqF:APA91bGqxIaxad2LOTcnlnWg8gsGlRr65EX5u9XaiFsKFQZY_z4qvgQOaQ8u2E7e8of3E3tg9AksmIFgBdQBe8vlos-GHmHHgiEgA4Z-h9Ul9tpM98im3w4"
        # # registration_token = "f4kM91qbTT-cpsJIDbSlQT:APA91bHiHEp4tP55n8N-sgyAcMW-svUxbNCIf9tFOwfa7KARsJ-_D6z8tSwQYCIDfd3jXrnjBKdWaBPTgL8ua2Wih8ULfROZu1vylwhZT86BGeSwiuWrVw8"
        # message = messaging.Message(
        #     data={
        #         "score": "850",
        #         "time": "2:45",
        #     },
        #     token=registration_token,
        # )

        # # Send the message
        # response = messaging.send(message)

        # multiple message
        registration_tokens = [
            "cV8f5KUURz2QMdMuMelIPF:APA91bGPjUQ3OfVVb-donP3U-B3mEVyWaBlalXll_bGKmQzycItGOyTYM7cJmnc6cgk4gBvH0YD5fuq6thWr28X8w-PI_UCbLc0MiSsdBDOq8dOKmGp6mx0"
            "f71jgOrVTcSVxuHFgC5Jiv:APA91bGgh_OeBXmj80OTmLHHIAedivys_hKToH9n4523lKuu4TJmHYvfzNSQaI0Bdttk_lP3ZLR_yo2i6M8w4C2gUOH1dLwWmdYLdJ7CcF5EK3EGJ-MvX78",
        ]

        message = messaging.MulticastMessage(
            data={"score": "850", "time": "2:45"},
            tokens=registration_tokens,
        )
        multiple_response = messaging.send_multicast(message)
        print("{0} messages were sent successfully".format(multiple_response.success_count))
        return JsonResponse(
            {
                "success": True,
                # "single esponse": response,
                "batch_response": multiple_response,
            },
            status=200,
        )

    except Exception as e:
        # Handle errors gracefully
        return JsonResponse({"success": False, "error": str(e)}, status=500)
