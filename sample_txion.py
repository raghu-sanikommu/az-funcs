sample_txion = {
  "segments": [
    {
        "start": 0,
        "end": 3.5,
        "text": "Thank you for calling Martha's Flores, Thomas Sisy.",
        "id": 0
    },
    {
        "start": 3.5,
        "end": 7.5,
        "text": "Hello, I'd like to order flowers and I think you have what I'm looking for.",
        "id": 1
    },
    {
        "start": 7.5,
        "end": 11,
        "text": "I'd be happy to take care of your order. May I have your name please?",
        "id": 2
    },
    {
        "start": 11,
        "end": 12.5,
        "text": "Randall Thomas.",
        "id": 3
    },
    {
        "start": 12.5,
        "end": 15.5,
        "text": "Randall Thomas, can you spell that for me?",
        "id": 4
    },
    {
        "start": 15.5,
        "end": 22.5,
        "text": "Randall, AN, B-A-L-L, Thomas, TH-O, M-A-S.",
        "id": 5
    },
    {
        "start": 22.5,
        "end": 27.5,
        "text": "Thank you for that information Randall. May I have your home or office number area code first?",
        "id": 6
    },
    {
        "start": 27.5,
        "end": 34,
        "text": "Ericko 409, then 5865088.",
        "id": 7
    },
    {
        "start": 34,
        "end": 41,
        "text": "That's 409 866 5088. Do you have a fax number or email address?",
        "id": 8
    },
    {
        "start": 41,
        "end": 47,
        "text": "Email is www.randall.com",
        "id": 9
    },
    {
        "start": 47,
        "end": 52,
        "text": "Randall.Thomasatchimel.com may have your shipping address.",
        "id": 10
    },
    {
        "start": 52,
        "end": 53,
        "text": "6800.",
        "id": 11
    },
    {
        "start": 53,
        "end": 54,
        "text": "Okay.",
        "id": 12
    },
    {
        "start": 54,
        "end": 60.5,
        "text": "Glad is Avenue, Belmont, Texas, Zip Code, 7706.",
        "id": 13
    },
    {
        "start": 60.5,
        "end": 70.5,
        "text": "Thank you for the information. What products were you interested in purchasing?",
        "id": 14
    },
    {
        "start": 70.5,
        "end": 73.5,
        "text": "Red roses, probably a dozen.",
        "id": 15
    },
    {
        "start": 73.5,
        "end": 76.5,
        "text": "One dozen of red roses? Do you want long stems?",
        "id": 16
    },
    {
        "start": 76.5,
        "end": 77.5,
        "text": "Sure.",
        "id": 17
    },
    {
        "start": 77.5,
        "end": 81.5,
        "text": "All right Randall, let me process your order. One moment please.",
        "id": 18
    },
    {
        "start": 82.5,
        "end": 83.5,
        "text": "Okay.",
        "id": 19
    },
    {
        "start": 85,
        "end": 88.5,
        "text": "Randall, you're ordering one dozen long-stent red roses.",
        "id": 20
    },
    {
        "start": 88.5,
        "end": 91,
        "text": "The total amount of your order is $40.",
        "id": 21
    },
    {
        "start": 91,
        "end": 94,
        "text": "And it will be shipped to your address within 24 hours.",
        "id": 22
    },
    {
        "start": 94,
        "end": 97,
        "text": "I was thinking to deliver my roses again.",
        "id": 23
    },
    {
        "start": 97,
        "end": 99,
        "text": "Within 24 hours.",
        "id": 24
    },
    {
        "start": 99,
        "end": 100,
        "text": "Okay, no problem.",
        "id": 25
    },
    {
        "start": 100,
        "end": 102,
        "text": "Is there anything else I can help you with?",
        "id": 26
    },
    {
        "start": 102,
        "end": 104,
        "text": "That's all for now, thanks.",
        "id": 27
    },
    {
        "start": 104,
        "end": 109,
        "text": "No problem, Randall. Thank you for calling Martha's Flores. Have a nice day.",
        "id": 28
    },
    {
        "start": 111.5,
        "end": 114,
        "text": "You too",
        "id": 29
    }
]
}


sample_json_to_llm = [
    {
      "text": "Thank you for calling Martha's Flores, Thomas Sisy.",
      "id": 0
    },
    {
      "text": "Hello, I'd like to order flowers and I think you have what I'm looking for.",
      "id": 1
    },
    {
        "text": "I'd be happy to take care of your order. May I have your name please?",
        "id": 2
    },
    {
        "text": "Randall Thomas.",
        "id": 3
    },
    {
        "text": "Randall Thomas, can you spell that for me?",
        "id": 4
    },
    {
        "text": "Randall, AN, B-A-L-L, Thomas, TH-O, M-A-S.",
        "id": 5
    },
    {
        "text": "Thank you for that information Randall. May I have your home or office number area code first?",
        "id": 6
    },
    {
        "text": "Ericko 409, then 5865088.",
        "id": 7
    },
    {
        "text": "That's 409 866 5088. Do you have a fax number or email address?",
        "id": 8
    },
    {
        "text": "Email is www.randall.com",
        "id": 9
    },
    {
        "text": "Randall.Thomasatchimel.com may have your shipping address.",
        "id": 10
    },
    {
        "text": "6800.",
        "id": 11
    },
    {
        "text": "Okay.",
        "id": 12
    },
    {
        "text": "Glad is Avenue, Belmont, Texas, Zip Code, 7706.",
        "id": 13
    },
    {
        "text": "Thank you for the information. What products were you interested in purchasing?",
        "id": 14
    },
    {
        "text": "Red roses, probably a dozen.",
        "id": 15
    },
    {
        "text": "One dozen of red roses? Do you want long stems?",
        "id": 16
    },
    {
        "text": "Sure.",
        "id": 17
    },
    {
        "text": "All right Randall, let me process your order. One moment please.",
        "id": 18
    },
    {
        "text": "Okay.",
        "id": 19
    },
    {
        "text": "Randall, you're ordering one dozen long-stent red roses.",
        "id": 20
    },
    {
        "text": "The total amount of your order is $40.",
        "id": 21
    },
    {
        "text": "And it will be shipped to your address within 24 hours.",
        "id": 22
    },
    {
        "text": "I was thinking to deliver my roses again.",
        "id": 23
    },
    {
        "text": "Within 24 hours.",
        "id": 24
    },
    {
        "text": "Okay, no problem.",
        "id": 25
    },
    {
        "text": "Is there anything else I can help you with?",
        "id": 26
    },
    {
        "text": "That's all for now, thanks.",
        "id": 27
    },
    {
        "text": "No problem, Randall. Thank you for calling Martha's Flores. Have a nice day.",
        "id": 28
    },
    {
        "text": "You too.",
        "id": 29
    }
]


sample_sentences_to_llm = [
    "Thank you for calling Martha's Flores, Thomas Sisy.",
    "Hello, I'd like to order flowers and I think you have what I'm looking for.",
    "I'd be happy to take care of your order. May I have your name please?",
    "Randall Thomas.",
    "Randall Thomas, can you spell that for me?",
    "Randall, AN, B-A-L-L, Thomas, TH-O, M-A-S.",
    "Thank you for that information Randall. May I have your home or office number area code first?",
    "Ericko 409, then 5865088.",
    "That's 409 866 5088. Do you have a fax number or email address?",
    "Email is www.randall.com",
    "Randall.Thomasatchimel.com may have your shipping address.",
    "6800.",
    "Okay.",
    "Glad is Avenue, Belmont, Texas, Zip Code, 7706.",
    "Thank you for the information. What products were you interested in purchasing?",
    "Red roses, probably a dozen.",
    "One dozen of red roses? Do you want long stems?",
    "Sure.",
    "All right Randall, let me process your order. One moment please.",
    "Okay.",
    "Randall, you're ordering one dozen long-stent red roses.",
    "The total amount of your order is $40.",
    "And it will be shipped to your address within 24 hours.",
    "I was thinking to deliver my roses again.",
    "Within 24 hours.",
    "Okay, no problem.",
    "Is there anything else I can help you with?",
    "That's all for now, thanks.",
    "No problem, Randall. Thank you for calling Martha's Flores. Have a nice day.",
    "You too."
]


prompt_for_json = """
From above array of objects containing "sentence" and "id" parameters where:
- "sentence" defines the sentence spoke by either a customer care agent or a customer
- "id" defines the index of object in the array
Analyze the following parameters:

  1. Identify by whom each sentence is spoke by, and push the role and the "id" of that sentence in the array separated by _ (underscore) into an array according to below criteria and put it in the json under the key 'segments':
    a. If its agent, push '<id>_AGNT'
    b. If its customer, push '<id>_CUST'
    c. If you can't identify, push '<id>_NA'
    d. Make sure, you push the role for every sentence in the given array of sentences
  2. Identify overall sentiment in the conversation whether its 'positive' or 'negative' and push it into the json under the key 'overall_sentiment'
  3. Identify the crisp and short version of issue description and push it into the json under the key 'issue_description'
  4. Identify the crisp and short version of resolution provided and push it into the json under the key 'resolution_provided'
  3. Output only the json and nothing else

  Example:
  Input: ['Hello, welcome to Airtel Care, How may I help you?', 'Hi, I am unable to connect to my internet', 'Sorry for the inconvenience, let me look into it, please wait', 'Thanks for waiting, it seems your recharge has finished, please recharge to continue using internet', 'Thank You, will do that', 'You too, have a nice day']
  Output: { 'segments': ['AGNT', 'CUST', 'AGNT', 'AGNT', 'CUST', 'AGNT'], 'overall_senitiment': 'positive', 'issue_description': 'Unable to connect to internet', 'resolution_provided': 'Recharge to continue using internet' }
"""


prompt_for_sentence = f"""
You are a powerful analyzing tool that can analyze conversation between a customer care agent and customer.


{"sentences"}


From above array of "sentence" strings where "sentence" defines the sentence spoke by either a customer care agent or a customer,
Analyze the following parameters:

  1. Identify by whom each sentence is spoke by, and push the role and the "id" of that sentence in the array separated by _ (underscore) into an array according to below criteria and put it in the json under the key 'segments':
    a. "id" is the index of "sentence" in the array
    b. If its agent, push '<id>_AGNT'
    c. If its customer, push '<id>_CUST'
    d. If you can't identify, push '<id>_NA'
    e. Make sure, you push the role for every sentence in the given array of sentences
  2. Identify overall sentiment in the conversation whether its 'positive' or 'negative' and push it into the json under the key 'overall_sentiment'
  3. Identify the crisp and short version of issue description and push it into the json under the key 'issue_description'
  4. Identify the crisp and short version of resolution provided and push it into the json under the key 'resolution_provided'
  3. Output only the json and nothing else

  Example:
  Input: ['Hello, welcome to Airtel Care, How may I help you?', 'Hi, I am unable to connect to my internet', 'Sorry for the inconvenience, let me look into it, please wait', 'Thanks for waiting, it seems your recharge has finished, please recharge to continue using internet', 'Thank You, will do that', 'You too, have a nice day']
  Output: {{ 'segments': ['0_AGNT', '1_CUST', '2_AGNT', '3_AGNT', '4_CUST', '5_AGNT'], 'overall_senitiment': 'positive', 'issue_description': 'Unable to connect to internet', 'resolution_provided': 'Recharge to continue using internet' }}
"""

sample_txion_long = [
    {
        "id": 0,
        "text": "Thank you for calling Questron, this is Candice, how may I help you?"
    },
    {
        "id": 1,
        "text": "I still have not received my order."
    },
    {
        "id": 2,
        "text": "You said I would receive it on the 20th, it's on the 22nd, still nothing."
    },
    {
        "id": 3,
        "text": "I don't know what's going on, but if it's not too much of a bother to you, I would really"
    },
    {
        "id": 4,
        "text": "really now love to get what I paid for."
    },
    {
        "id": 5,
        "text": "You know what I mean?"
    },
    {
        "id": 6,
        "text": "Oh, if it's beyond the promised delivery date, we definitely need to look into that."
    },
    {
        "id": 7,
        "text": "May I have your order number and your full name so I can check for you?"
    },
    {
        "id": 8,
        "text": "That's exactly what I'm thinking, like, I don't understand, what's taking so long?"
    },
    {
        "id": 9,
        "text": "Anyway, the order number is 498-4977 and my name is Tabitha Ratched."
    },
    {
        "id": 10,
        "text": "Thank you, Tabitha."
    },
    {
        "id": 11,
        "text": "I will now go ahead and pull up your order and hopefully I can give you an immediate"
    },
    {
        "id": 12,
        "text": "answer."
    },
    {
        "id": 13,
        "text": "One moment, please."
    },
    {
        "id": 14,
        "text": "Go ahead, thank you."
    },
    {
        "id": 15,
        "text": "Okay, like what she said, the estimated delivery date is on the 20th."
    },
    {
        "id": 16,
        "text": "It's not 22nd, so it's two days late."
    },
    {
        "id": 17,
        "text": "Normally, when a parcel is late like this, we send an email informing you of the delay,"
    },
    {
        "id": 18,
        "text": "so let me visit the FedEx website and track it."
    },
    {
        "id": 19,
        "text": "Thank you, Candice."
    },
    {
        "id": 20,
        "text": "That would be appreciated."
    },
    {
        "id": 21,
        "text": "I actually haven't tried tracking it on the FedEx website since you already gave me the"
    },
    {
        "id": 22,
        "text": "delivery date through email, so yes, please go ahead."
    },
    {
        "id": 23,
        "text": "Okay, according to the FedEx note here, your parcel was delivered on the 20th at 10am."
    },
    {
        "id": 24,
        "text": "It said that it was left on the front porch."
    },
    {
        "id": 25,
        "text": "Have you tried checking your front porch?"
    },
    {
        "id": 26,
        "text": "What?"
    },
    {
        "id": 27,
        "text": "What?"
    },
    {
        "id": 28,
        "text": "What?"
    },
    {
        "id": 29,
        "text": "You're kidding, right?"
    },
    {
        "id": 30,
        "text": "Okay, okay."
    },
    {
        "id": 31,
        "text": "First of all, my apartment has no front porch."
    },
    {
        "id": 32,
        "text": "Second, the only way to deliver parcels in a residence is by leaving them to the concierge."
    },
    {
        "id": 33,
        "text": "Third, I was at home the whole day on the 20th and no one, literally no one, knocked"
    },
    {
        "id": 34,
        "text": "on my door or called my number to notify me of a parcel."
    },
    {
        "id": 35,
        "text": "So whatever this FedEx guy is saying, he's lying, okay?"
    },
    {
        "id": 36,
        "text": "He's lying."
    },
    {
        "id": 37,
        "text": "That's definitely odd."
    },
    {
        "id": 38,
        "text": "Have you tried checking with your building's concierge to see if they have kept a package"
    },
    {
        "id": 39,
        "text": "for you?"
    },
    {
        "id": 40,
        "text": "I just checked this morning and the answer is no, otherwise I wouldn't be calling you."
    },
    {
        "id": 41,
        "text": "Yeah."
    },
    {
        "id": 42,
        "text": "Your neighbors also wouldn't happen to receive it, right?"
    },
    {
        "id": 43,
        "text": "Since as you said, all parcels go to the concierge."
    },
    {
        "id": 44,
        "text": "Correct."
    },
    {
        "id": 45,
        "text": "And if the note says he left it on my doorstep, again, that's impossible."
    },
    {
        "id": 46,
        "text": "No one can access our doorsteps here except us tenants."
    },
    {
        "id": 47,
        "text": "So there's clearly a mistake here."
    },
    {
        "id": 48,
        "text": "Yes, that makes sense."
    },
    {
        "id": 49,
        "text": "So here's what we're going to do, Tabitha."
    },
    {
        "id": 50,
        "text": "It is likely that FedEx delivered the order to the wrong address."
    },
    {
        "id": 51,
        "text": "So I will file a PDNR claim on your behalf."
    },
    {
        "id": 52,
        "text": "It means parcel delivered, not received."
    },
    {
        "id": 53,
        "text": "What this does is to let FedEx investigate to find your missing parcel."
    },
    {
        "id": 54,
        "text": "And after the investigation, we will either refund, replace, or find your missing parcel."
    },
    {
        "id": 55,
        "text": "Okay."
    },
    {
        "id": 56,
        "text": "Yeah."
    },
    {
        "id": 57,
        "text": "And for me to initiate the claim, I will send you an email right now."
    },
    {
        "id": 58,
        "text": "Please reply to that email confirming that you have not received your parcel."
    },
    {
        "id": 59,
        "text": "Your response to that email is very important because that will serve as the documentation"
    },
    {
        "id": 60,
        "text": "proving to FedEx that you are requesting for us to file a claim on your behalf."
    },
    {
        "id": 61,
        "text": "Okay."
    },
    {
        "id": 62,
        "text": "Whatever happens, I'm going to get my refund though, right?"
    },
    {
        "id": 63,
        "text": "You're right."
    },
    {
        "id": 64,
        "text": "Of course."
    },
    {
        "id": 65,
        "text": "And the sooner they find your parcel, the better."
    },
    {
        "id": 66,
        "text": "By the way, in the event that the parcel isn't recovered, would you prefer a replacement"
    },
    {
        "id": 67,
        "text": "or a refund?"
    },
    {
        "id": 68,
        "text": "I need a replacement for that."
    },
    {
        "id": 69,
        "text": "I don't want a refund."
    },
    {
        "id": 70,
        "text": "Okay."
    },
    {
        "id": 71,
        "text": "I will make note of that."
    },
    {
        "id": 72,
        "text": "And after the investigation, which usually takes five to seven business days, I will"
    },
    {
        "id": 73,
        "text": "check with the supplier for its availability."
    },
    {
        "id": 74,
        "text": "And then they can process the replacement for you."
    },
    {
        "id": 75,
        "text": "Okay."
    },
    {
        "id": 76,
        "text": "It's disappointing that this has to happen, but okay, whatever."
    },
    {
        "id": 77,
        "text": "At least I don't have to file a dispute."
    },
    {
        "id": 78,
        "text": "To be honest, I was already thinking of calling my bank this morning and filing a dispute."
    },
    {
        "id": 79,
        "text": "Yes."
    },
    {
        "id": 80,
        "text": "This is definitely not the experience that we want you to have, but we will try our best"
    },
    {
        "id": 81,
        "text": "to make this as easy as possible for you considering the situation."
    },
    {
        "id": 82,
        "text": "I will also keep this case in progress."
    },
    {
        "id": 83,
        "text": "So whatever questions you might have during the investigation, you just reply to the same"
    },
    {
        "id": 84,
        "text": "email thread and I will be there to answer your questions."
    },
    {
        "id": 85,
        "text": "So let me get this straight."
    },
    {
        "id": 86,
        "text": "Seven business days for the investigation."
    },
    {
        "id": 87,
        "text": "And if it isn't found, you're going to check with the team if it's available."
    },
    {
        "id": 88,
        "text": "And if it's available, another seven days to deliver the replacement."
    },
    {
        "id": 89,
        "text": "Yes, Tabitha, that's correct."
    },
    {
        "id": 90,
        "text": "But of course, if they find the parcel during the investigation, then you don't need to"
    },
    {
        "id": 91,
        "text": "wait that long."
    },
    {
        "id": 92,
        "text": "That's already the maximum time frame."
    },
    {
        "id": 93,
        "text": "Yeah, well, I hope they do, but I honestly don't have much hope for it."
    },
    {
        "id": 94,
        "text": "But okay, a replacement's fine, I guess."
    },
    {
        "id": 95,
        "text": "Okay, yeah."
    },
    {
        "id": 96,
        "text": "I cannot guarantee that 100% that they would find your missing parcel, but there have been"
    },
    {
        "id": 97,
        "text": "cases in the past when they did find the missing parcel."
    },
    {
        "id": 98,
        "text": "I will, of course, update you throughout the process."
    },
    {
        "id": 99,
        "text": "Okay, so I guess that's my best option."
    },
    {
        "id": 100,
        "text": "What do you need me to do?"
    },
    {
        "id": 101,
        "text": "Just reply to your email saying that I didn't receive a parcel?"
    },
    {
        "id": 102,
        "text": "That's correct."
    },
    {
        "id": 103,
        "text": "I have just sent you the email."
    },
    {
        "id": 104,
        "text": "All right, I will reply in five minutes."
    },
    {
        "id": 105,
        "text": "I'm going to have my lunch break."
    },
    {
        "id": 106,
        "text": "What's your name again?"
    },
    {
        "id": 107,
        "text": "Candice."
    },
    {
        "id": 108,
        "text": "All right, Candice, thank you so much."
    },
    {
        "id": 109,
        "text": "That's all I need for now."
    },
    {
        "id": 110,
        "text": "I have to go."
    },
    {
        "id": 111,
        "text": "Bye."
    },
    {
        "id": 112,
        "text": "Okay, enjoy your lunch, Tabitha."
    },
    {
        "id": 113,
        "text": "Thanks for calling Question."
    },
    {
        "id": 114,
        "text": "Bye."
    },
    {
        "id": 115,
        "text": ""
    }
]











