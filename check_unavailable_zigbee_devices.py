threshold_hours = 24

disabled_devices = []

for entity_id in hass.states.entity_ids():
    state = hass.states.get(entity_id)
    if state.state == "unavailable" and ("light" in entity_id or "sensor" in entity_id):
        last_changed = state.last_changed
        time_diff = hass.datetime() - last_changed
        time_diff_hours = time_diff.total_seconds() / 3600
        if time_diff_hours >= threshold_hours:
            disabled_devices.append(entity_id)

disabled_devices_str = ', '.join(disabled_devices)
hass.states.set("sensor.disabled_zigbee_devices", disabled_devices_str)
