entities = hass.states.entity_ids()
zigbee_groups = [entity for entity in entities if entity.startswith("light.") and "zha_group" in entity]

non_group_lights = [
    entity
    for entity in entities
    if entity.startswith("light.")
    and "zha_group" not in entity
    and "group" not in entity
    and "all_lights" not in entity
]

all_lights = zigbee_groups + non_group_lights

hass.services.call(
    "group",
    "set",
    {
        "object_id": "all_lights",
        "name": "All Lights",
        "entities": all_lights,
        "icon": "mdi:lightbulb-group",
    },
)
