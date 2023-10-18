automations = hass.states.entity_ids('automation')
to_enable = []

for automation in automations:
    state = hass.states.get(automation)
    if state is None:
        continue
    
    name = state.attributes.get('friendly_name', '').lower()
    if name.startswith("timer") or name.startswith("motion"):
        if state.state == "off":
            to_enable.append(automation)

if to_enable:
    hass.services.call('automation', 'turn_on', {'entity_id': to_enable})
