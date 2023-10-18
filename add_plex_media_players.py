# Get existing group members
group_entity_id = "media_player.plex_clients"
group_members = hass.states.get(group_entity_id).attributes["entity_id"]

# Get all Plex media players
plex_media_players = [x for x in hass.states.all() if x.entity_id.startswith("media_player.plex_")]

# Add Plex media players to the group if not already present
for plex_media_player in plex_media_players:
    if plex_media_player.entity_id not in group_members:
        group_members.append(plex_media_player.entity_id)

# Update the group
hass.services.call("group", "set", {
    "object_id": group_entity_id.split(".")[1],
    "entities": group_members,
    "control": "hidden",
})
