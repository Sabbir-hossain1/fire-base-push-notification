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
    
# "error": "Unexpected HTTP response with status: 404; body: <!DOCTYPE html>\n<html lang=en>\n  <meta charset=utf-8>\n  <meta name=viewport content=\"initial-scale=1, minimum-scale=1, width=device-width\">\n  <title>Error 404 (Not Found)!!1</title>\n  <style>\n    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}\n  </style>\n  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>\n  <p><b>404.</b> <ins>That\u2019s an error.</ins>\n  <p>The requested URL <code>/batch</code> was not found on this server.  <ins>That\u2019s all we know.</ins>\n"
