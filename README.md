# Home-Assistant

Some random scripts that I use in Home Assistant.  Some use the pyscript integration and others are done in yaml.

script.verify_scene_applied requires configuration.yaml changes as well as an input boolean (for me input_boolean.scene_match)

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
