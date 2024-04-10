import os

def send_video_description(bot, chat_id, feature):
    
    if feature == 'jump_to_pallet':
        description_text = ""
        
    elif feature == 'texture_slizing':
        description_text = ""

    elif feature == 'invisible_stun':
        description_text = "123123"

    elif feature == 'texture_abuse':
        description_text = "123123"

    elif feature == 'crouch_tech':
        description_text = "123123"

    elif feature == 'snowball_protection':
        description_text = "123123"

    elif feature == 'for_the_people':
        description_text = "123123"

    elif feature == 'bloodlust_reset':
        description_text = "123123"

    elif feature == 'agility_bite':
        description_text = "123123"
    
    elif feature == 'cabinet_stand':
        description_text = "123123"

    elif feature == 'back_flip':
        description_text = "123123"

    elif feature == 'ability_block':
        description_text = "123123"

    elif feature == 'solo_escape':
        description_text = "123123"

    elif feature == 'timing_adrenaline':
        description_text = "123123"

    elif feature == 'corrupt_evade':
        description_text = "123123"

    elif feature == 'terror_running':
        description_text = "123123"

    elif feature == 'cabinet_stand':
        description_text = "123123"

    elif feature == 'proper_reset':
        description_text = "123123"

    elif feature == 'high_ground_abuse':
        description_text = "123123"

    elif feature == 'ability_reset':
        description_text = "123123"

    elif feature == 'koli_timing':
        description_text = "123123"

    elif feature == 'clown_abuse':
        description_text = "123123"

    elif feature == 'high_ground':
        description_text = "123123"
 
    else:
        description_text = "Описание для этой фишки пока не реализовано."

    bot.send_message(chat_id, description_text,parse_mode='HTML')

def find_video_path(video_filename):
    videos_directory = 'video/'
    video_path = os.path.join(videos_directory, video_filename)
    if os.path.exists(video_path):
        return video_path
    return None
