import requests

'''

https://discord.com/api/v9/interactions

{
   "type":2,
   "application_id":"936929561302675456",
   "guild_id":"1072796769794142238",
   "channel_id":"1072796769794142241",
   "session_id":"2f10612da06594a69ac7cad15f9079df",
   "data":{
      "version":"994261739745050686",
      "id":"938956540159881230",
      "name":"imagine",
      "type":1,
      "options":[
         {
            "type":3,
            "name":"prompt",
            "value":"sea,boys,girls"
         }
      ],
      "application_command":{
         "id":"938956540159881230",
         "application_id":"936929561302675456",
         "version":"994261739745050686",
         "default_permission":true,
         "default_member_permissions":null,
         "type":1,
         "nsfw":false,
         "name":"imagine",
         "description":"There are endless possibilities...",
         "dm_permission":true,
         "options":[
            {
               "type":3,
               "name":"prompt",
               "description":"The prompt to imagine",
               "required":true
            }
         ]
      },
      "attachments":[

      ]
   },
   "nonce":"1072868148404813824"
}
'''

SERVER_ID = ""
CHANNEL_ID = ""
USER_TOKEN = "USER_TOKEN"

def PassPromptToSelfBot(prompt: str):
    payload = {"type": 2,
               "application_id": "936929561302675456",
               "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID,
               "session_id": "0a010c9eaf31b12c8b2345c0d38bbb7c",
               "data": {"version": "994261739745050686",
                        "id": "938956540159881230",
                        "name": "imagine",
                        "type": 1,
                        "options": [{"type": 3, "name": "prompt", "value": prompt}],
                        "application_command": {"id": "938956540159881230",
                                                "application_id": "936929561302675456",
                                                "version": "994261739745050686",
                                                "default_permission": True,
                                                "default_member_permissions": None,
                                                "type": 1,
                                                "name": "imagine",
                                                "description": "There are endless possibilities...",
                                                "dm_permission": True,
                                                "options": [{"type": 3, "name": "prompt",
                                                             "description": "The prompt to imagine",
                                                             "required": True}]},
                        "attachments": []}
               }

    header = {
        'authorization': USER_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response


def Upscale(index: int, messageId: str, messageHash: str):
    payload = {"type": 3,
               "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID,
               "message_flags": 0,
               "message_id": messageId,
               "application_id": "936929561302675456",
               "session_id": "45bc04dd4da37141a5f73dfbfaf5bdcf",
               "data": {"component_type": 2,
                        "custom_id": "MJ::JOB::upsample::{}::{}".format(index, messageHash)}
               }
    header = {
        'authorization': USER_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response


def MaxUpscale(messageId: str, messageHash: str):
    payload = {"type": 3,
               "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID,
               "message_flags": 0,
               "message_id": messageId,
               "application_id": "936929561302675456",
               "session_id": "1f3dbdf09efdf93d81a3a6420882c92c", "data":
                   {"component_type": 2, "custom_id": "MJ::JOB::upsample_max::1::{}::SOLO".format(messageHash)}}
    header = {
        'authorization': USER_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response


def Variation(index: int, messageId: str, messageHash: str):
    payload = {"type": 3, "guild_id": SERVER_ID,
               "channel_id": CHANNEL_ID,
               "message_flags": 0,
               "message_id": messageId,
               "application_id": "936929561302675456",
               "session_id": "1f3dbdf09efdf93d81a3a6420882c92c",
               "data": {"component_type": 2, "custom_id": "MJ::JOB::variation::{}::{}".format(index, messageHash)}}
    header = {
        'authorization': USER_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response

