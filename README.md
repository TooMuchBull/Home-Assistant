# Home-Assistant

Some random scripts that I use in Home Assistant.  Some use the python script integration and others are done in yaml.

add_plex_media_players.py

Automatically adds new plex entities to media_player.plex_clients group

check_unavailable_zigbee_devices.py

Checks if any zigbee devices have been unavailable for 24 hours, paired with automation to send notification of any devices in the list to my phone.

enable_timer_motion_automations.py

"Resets" the automations in my home that can be manually disabled via buttons once per day



script.verify_scene_applied 

Requires configuration.yaml changes as well as an input boolean (for me input_boolean.scene_match)

configuration.yaml additions:

input_text:
  verify_scene_entity_id:
    name: "Verify Scene Entity ID"

input_number:
  verify_scene_retry_counter:
    name: "Verify Scene Retry Counter"
    min: 0
    max: 10
    step: 1
